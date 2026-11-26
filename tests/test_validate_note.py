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
title: A paper
authors: [A. Researcher]
venue: arXiv
year: 2026
---
[Zotero](zotero://select/library/items/ABC12345) · [论文原文](https://arxiv.org/abs/2606.00001v1)
## Mechanism
$$
L = x^2
$$
> [!example]- Code
> ```python
> print('$$')
> # {{ these braces are code, not Liquid }}
> ```
My original thought.
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

    def test_valid_minimal_note_with_body_links_and_folded_code_is_unchanged(self):
        self.assertEqual(self.check_note(GOOD), [])
        self.assertEqual(self.note.read_text(), GOOD)

    def test_hidden_markers_are_rejected_without_changing_enclosed_text(self):
        for marker in ("<!-- paper-reading:ai:start -->", "%%zt-managed%%", "%%/zt-managed%%"):
            with self.subTest(marker=marker):
                self.assertTrue(any("comments" in e or "markers" in e for e in self.check_note(GOOD + "\n" + marker)))

    def test_heading_and_chapter_format(self):
        for heading in ("# 1. Method", "# 第一部分：理解论文", "## 第一部分：理解论文", "## Part I: Understanding", "## 1. Method", "### 2.1 Setup"):
            self.assertTrue(any("unnumbered" in e for e in self.check_note(GOOD + "\n" + heading)))
        self.assertTrue(any("Use ch" in e for e in self.check_note(GOOD + "\n原文 §III-B。")))
        self.assertTrue(any("page numbers" in e for e in self.check_note(GOOD + "\nch III-B，原文第 3 页。")))
        self.assertEqual(self.check_note(GOOD + "\nch III-B; Eq. (21)."), [])

    def test_display_math_is_compact_next_to_prose(self):
        compact = "\nA probability model gives\n$$\np(x)=1\n$$\nwhich defines the distribution.\n"
        self.assertEqual(self.check_note(GOOD + compact), [])
        for old,new in [("gives\n$$","gives\n\n$$"),("$$\nwhich","$$\n\nwhich")]:
            self.assertTrue(any("empty lines" in e for e in self.check_note(GOOD + compact.replace(old,new))))

    def test_note_title_does_not_become_an_extra_heading(self):
        for title in ("# A paper", "## paper"):
            with self.subTest(title=title):
                self.assertTrue(any("repeat the note name" in e for e in self.check_note(GOOD + "\n" + title)))

    def test_english_source_label_passes(self):
        self.assertEqual(self.check_note(GOOD.replace("[论文原文]", "[Paper]")), [])

    def test_native_and_workflow_properties_are_rejected(self):
        for key in ("zotero-key", "citekey", "type", "parent-note", "reading_status", "source"):
            with self.subTest(key=key):
                errors = self.check_note(GOOD.replace("title: A paper", "title: A paper\n" + key + ": value"))
                self.assertTrue(any("Unexpected property" in e for e in errors))

    def test_single_source_links_are_required(self):
        for old, new in [("[Zotero]", "[Other]"), ("[论文原文]", "[Other]"),
                         ("https://arxiv.org/abs/2606.00001v1)", "https://arxiv.org/abs/2606.00001v1) https://arxiv.org/abs/2606.00001v1")]:
            with self.subTest(old=old):
                self.assertTrue(self.check_note(GOOD.replace(old,new)))

    def test_title_is_required_without_ownership_metadata(self):
        self.assertTrue(any("title property" in e for e in self.check_note(GOOD.replace("title: A paper", ""))))

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

    def test_side_by_side_image_table_with_escaped_width_pipes(self):
        image = self.vault / "images" / "fig-09.png"
        image.parent.mkdir()
        image.write_bytes(b"fixture")
        table = "\n| ![[images/fig-09.png\\|300]] | ![[images/fig-09.png\\|300]] |\n| :---: | :---: |\n| Figure 9: Steps. | Figure 10: Order. |\n"
        self.assertEqual(self.check_note(GOOD + table), [])

    def test_detail_note_uses_body_return_link_without_identity_properties(self):
        self.note = self.note.with_name("附加笔记.md")
        self.assertEqual(self.check_note('---\ntitle: Proof\n---\n[[Papers/paper|返回主笔记]]\n'), [])

    def test_incomplete_scaffold_and_template_values_are_rejected(self):
        for value in ["精读内容尚未生成。", "{{ zt.title }}"]:
            with self.subTest(value=value):
                self.assertTrue(any("scaffold" in e for e in self.check_note(GOOD + "\n" + value)))


class MethodFolderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.vault = Path(self.temp.name)
        self.folder = self.vault / "Papers" / "METHOD"
        self.folder.mkdir(parents=True)
        self.main = self.folder / "METHOD.md"
        self.main.write_text(GOOD, encoding="utf-8")
        self.child = self.folder / "附加笔记.md"
        self.child_text = """---
title: Complete details
---
[[Papers/METHOD/METHOD|返回主笔记]]
# 完整证明与细节
A substantive explanation.
## 我的思考
"""
        self.child.write_text(self.child_text, encoding="utf-8")

    def validate(self, path):
        return MODULE.validate(path, self.vault, self.folder)

    def test_method_named_main_and_sibling_child_pass(self):
        self.assertEqual(self.validate(self.main), [])
        self.assertEqual(self.validate(self.child), [])

    def test_method_content_is_not_split_by_default(self):
        for name in ("方法理解.md", "实验分析.md", "理论推导.md", "代码解读.md"):
            with self.subTest(name=name):
                other = self.folder / name
                other.write_text(self.child_text, encoding="utf-8")
                self.assertTrue(any("Default layout" in e for e in self.validate(other)))
                self.assertEqual(MODULE.validate(other, self.vault, self.folder, allow_extra_notes=True), [])

    def test_detail_note_requires_visible_return_link(self):
        self.child.write_text(self.child_text.replace("|返回主笔记", "|Other"), encoding="utf-8")
        self.assertTrue(any("visible" in e for e in self.validate(self.child)))

    def test_wrong_main_name_is_rejected(self):
        other = self.folder / "citekey.md"
        other.write_text(GOOD, encoding="utf-8")
        self.assertTrue(any("filename" in e for e in self.validate(other)))

    def test_child_must_target_existing_same_folder_main(self):
        for parent in ["Papers/OTHER/OTHER", "Papers/METHOD/missing", "Papers/METHOD/附加笔记"]:
            with self.subTest(parent=parent):
                self.child.write_text(self.child_text.replace("Papers/METHOD/METHOD", parent), encoding="utf-8")
                self.assertTrue(self.validate(self.child))
        self.child.write_text(self.child_text, encoding="utf-8")
        self.main.unlink()
        self.assertTrue(any("existing main" in e for e in self.validate(self.child)))

    def test_topic_subfolders_and_duplicate_identity_are_rejected(self):
        nested = self.folder / "details" / "方法理解.md"
        nested.parent.mkdir()
        nested.write_text(self.child_text, encoding="utf-8")
        self.assertTrue(any("directly" in e for e in self.validate(nested)))
        self.child.write_text(self.child_text.replace("title: Complete details", "title: Complete details\nzotero-key: ABC12345"), encoding="utf-8")
        self.assertTrue(any("Unexpected property" in e for e in self.validate(self.child)))

    def test_english_details_and_return_link(self):
        english = self.folder / "Details.md"
        english.write_text(self.child_text.replace("返回主笔记", "Return to main note"), encoding="utf-8")
        self.assertEqual(self.validate(english), [])

    def test_child_rejects_hidden_markers(self):
        self.child.write_text(self.child_text + "\n%%zt-managed%%\ntext\n%%/zt-managed%%", encoding="utf-8")
        self.assertTrue(any("managed markers" in e for e in self.validate(self.child)))



if __name__ == "__main__":
    unittest.main()
