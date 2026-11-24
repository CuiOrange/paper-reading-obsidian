"""Contract-level checks using temporary vaults; no live Zotero or Obsidian writes."""
import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_note.py"
SPEC = importlib.util.spec_from_file_location("validate_note", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

GOOD = """---
type: literature-note
zotero-key: ABC12345g12345
---
# A paper
%%zt-managed%%
Imported annotation.
%%/zt-managed%%
<!-- paper-reading:ai:start -->
## Method
$$
L = x^2
$$
> [!example]- Code
> ```python
> print('$$')
> # {{ these braces are code, not Liquid }}
> ```
<!-- paper-reading:ai:end -->
<!-- paper-reading:user:start -->
My original thought.
<!-- paper-reading:user:end -->
"""


class NoteContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.vault = Path(self.temp.name)
        self.note = self.vault / "Papers" / "paper.md"
        self.note.parent.mkdir()

    def check_note(self, text):
        self.note.write_text(text, encoding="utf-8")
        return MODULE.validate(self.note, self.vault)

    def test_valid_note_with_group_identity_and_folded_code_is_unchanged(self):
        self.assertEqual(self.check_note(GOOD), [])
        self.assertEqual(self.note.read_text(), GOOD)

    def test_analysis_inside_managed_region_is_rejected(self):
        text = GOOD.replace("%%/zt-managed%%\n", "")
        text = text.replace("<!-- paper-reading:ai:end -->", "<!-- paper-reading:ai:end -->\n%%/zt-managed%%")
        self.assertTrue(any("overlap" in e for e in self.check_note(text)))

    def test_missing_identity_cannot_pass_as_completed_literature_note(self):
        self.assertTrue(any("zotero-key" in e for e in self.check_note(GOOD.replace("zotero-key: ABC12345g12345", ""))))

    def test_unclosed_callout_code_and_math_are_detected(self):
        self.assertTrue(any("code fence" in e for e in self.check_note(GOOD.replace("> ```\n", ""))))
        self.assertTrue(any("display-math" in e for e in self.check_note(GOOD.replace("L = x^2\n$$", "L = x^2"))))

    def test_portable_embeds_and_missing_assets(self):
        asset = self.vault / "assets" / "figure.png"
        asset.parent.mkdir()
        asset.write_bytes(b"fixture")
        self.assertEqual(self.check_note(GOOD + "\n![[assets/figure.png|600]]\n![[figure.png]]"), [])
        self.assertTrue(any("embed" in e for e in self.check_note(GOOD + "\n![[missing.png]]")))
        self.assertTrue(any("embed" in e for e in self.check_note(GOOD + "\n![[/etc/hosts]]")))

    def test_detail_note_uses_parent_without_duplicate_native_identity(self):
        self.assertEqual(self.check_note('---\ntype: paper-detail\nparent-note: "[[Papers/paper]]"\n---\n# Proof\n'), [])

    def test_incomplete_scaffold_and_template_values_are_rejected(self):
        for value in ["精读内容尚未生成。", "{{ zt.title }}"]:
            with self.subTest(value=value):
                self.assertTrue(any("scaffold" in e for e in self.check_note(GOOD + "\n" + value)))


if __name__ == "__main__":
    unittest.main()
