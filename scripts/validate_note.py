#!/usr/bin/env python3
"""Read-only, dependency-free checks for this skill's Markdown note contract.

This is not a full YAML/Markdown/LaTeX parser, a renderer or a scientific audit.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def scalar(frontmatter: str, key: str) -> str:
    match = re.search(r"^" + re.escape(key) + r":\s*(.*?)\s*$", frontmatter, re.M)
    if not match:
        return ""
    value = match.group(1).strip()
    # Only the small scalar fields used by these checks; not a YAML parser.
    if value.startswith(('"', "'")) and value.endswith(value[0]):
        return value[1:-1]
    return value.split(" #", 1)[0].strip()


def prose_lines(body: str) -> tuple[list[tuple[int, str]], list[str]]:
    """Exclude fenced code, including fences inside Obsidian callouts."""
    output: list[tuple[int, str]] = []
    errors: list[str] = []
    fence: tuple[str, int, int] | None = None
    for number, line in enumerate(body.splitlines(), 1):
        line = re.sub(r"^(?:[ \t]*>[ \t]?)+", "", line)
        found = re.match(r"^[ \t]{0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if found and found[1][0] == fence[0] and len(found[1]) >= fence[1] and not found[2].strip():
                fence = None
            continue
        if found:
            fence = (found[1][0], len(found[1]), number)
            continue
        line = re.sub(r"(`+).*?\1", "", line)
        output.append((number, line))
    if fence:
        errors.append(f"Unclosed code fence starting at body line {fence[2]}")
    return output, errors


def embedded_target_exists(target: str, note: Path, vault: Path) -> bool:
    target = target.replace("\\|", "|")
    target = target.split("|", 1)[0].split("#", 1)[0].strip().replace("\\", "/")
    if not target:  # A block/heading embed from this same note.
        return True
    path = Path(target)
    if path.is_absolute():
        return False
    candidates = [note.parent / path, vault / path]
    if not path.suffix:
        candidates += [candidate.with_suffix(".md") for candidate in list(candidates)]
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved.is_relative_to(vault) and resolved.is_file():
            return True
    # Obsidian can resolve a unique basename anywhere in the vault.
    if len(path.parts) == 1:
        names = {path.name}
        if not path.suffix:
            names.add(path.name + ".md")
        matches = [p for name in names for p in vault.rglob(name)
                   if p.is_file() and p.resolve().is_relative_to(vault)]
        return len(matches) == 1
    return False


def is_detail_note(note: Path, body: str) -> bool:
    return note.name in ("附加笔记.md", "Details.md") or bool(re.search(
        r"(?<!!)\[\[[^]\n]+\|(?:返回主笔记|Return to main note)\]\]", body))


def validate_layout(note: Path, frontmatter: str, folder: Path, vault: Path | None,
                    allow_extra_notes: bool = False, body: str = "") -> list[str]:
    """Check filenames and visible return links without adding identity properties."""
    errors: list[str] = []
    folder = folder.resolve()
    if vault is None or not folder.is_dir() or not folder.is_relative_to(vault):
        return ["--paper-folder requires --vault and an existing folder inside it"]
    if note.parent != folder:
        errors.append("Reading notes must sit directly in --paper-folder, without topic subfolders")
    if not is_detail_note(note, body):
        if note.name != folder.name + ".md":
            errors.append("Main note filename must match the method folder name")
        return errors
    if not allow_extra_notes and note.name not in ("附加笔记.md", "Details.md"):
        errors.append("Default layout permits only 附加笔记.md or Details.md beside the main note")
    parents = re.findall(r"(?<!!)\[\[([^]\n]+)\|(?:返回主笔记|Return to main note)\]\]", body)
    if len(parents) != 1:
        return errors + ["Detail note requires one visible vault-relative 返回主笔记 / Return to main note wikilink"]
    target = parents[0].split("#", 1)[0].strip().replace("\\", "/")
    if not target or Path(target).is_absolute():
        return errors + ["Detail return link must use a vault-relative path"]
    if not target.endswith(".md"):
        target += ".md"
    parent_path = (vault / target).resolve()
    if parent_path.parent != folder or parent_path.name != folder.name + ".md":
        return errors + ["Detail return link must target the method-named main note in the same folder"]
    if parent_path == note or not parent_path.is_file():
        return errors + ["Detail return link does not resolve to an existing main note"]
    return errors


def validate(note: Path, vault: Path | None = None, paper_folder: Path | None = None,
             allow_extra_notes: bool = False) -> list[str]:
    errors: list[str] = []
    note = note.resolve()
    if not note.is_file():
        return [f"Note not found: {note}"]
    try:
        text = note.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        return [f"Cannot read UTF-8 note: {exc}"]
    if vault:
        vault = vault.resolve()
        if not vault.is_dir() or not note.is_relative_to(vault):
            return ["--vault must be an existing directory containing the note"]

    front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
    if not front:
        errors.append("Missing or unclosed YAML frontmatter")
        frontmatter, body = "", text
    else:
        frontmatter, body = front[1], text[front.end():]
    allowed = {"title", "authors", "venue", "code", "year"}
    keys = re.findall(r"^([^ \t:#][^:\n]*):", frontmatter, re.M)
    for key in keys:
        if key not in allowed:
            errors.append(f"Unexpected property: {key}; keep only title, authors, venue, code and year")
    if len(keys) != len(set(keys)):
        errors.append("Duplicate frontmatter property")
    if scalar(frontmatter, "title").lower() in ("", "null", "~"):
        errors.append("Note requires a real title property")
    detail = is_detail_note(note, body)
    if paper_folder is not None:
        errors.extend(validate_layout(note, frontmatter, paper_folder, vault, allow_extra_notes, body))

    lines, fence_errors = prose_lines(body)
    errors.extend(fence_errors)
    # Preserve original positions while blanking code examples that quote markers.
    retained = {n for n, _ in lines}
    structural_body = "\n".join(line if n in retained else " " * len(line)
                                 for n, line in enumerate(body.splitlines(), 1))
    if re.search(r"<!--|-->", structural_body):
        errors.append("HTML comments must not appear in delivered notes")
    if re.search(r"%%/?zt-managed%%", structural_body):
        errors.append("ZotLit managed markers must not appear in delivered notes")
    title_labels = {note.stem.casefold(), scalar(frontmatter, "title").casefold()}
    for number, line in lines:
        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if heading and heading[1].strip().casefold() in title_labels:
            errors.append(f"Do not repeat the note name or title as a body heading at line {number}")
        if "§" in line:
            errors.append(f"Use ch for original chapter references at body line {number}")
        if re.match(r"^#{2,6}\s+(?:\d+(?:\.\d+)*[.)、]?\s+|第[一二三四五六七八九十\d]+部分|Part\s+[IVX\d]+\b)", line, re.I):
            errors.append(f"Use direct unnumbered content headings at body line {number}")
        if re.search(r"\bch\s+[IVX\d][^\n]*(?:第\s*\d+\s*页|\b(?:pp?\.|pages?)\s*\d+)", line, re.I):
            errors.append(f"Do not append page numbers to chapter references at body line {number}")

    if not detail:
        zotero_links = re.findall(r"(?<!!)\[Zotero\]\((zotero://[^)\s]+)\)", structural_body)
        article_links = re.findall(r"(?<!!)\[(?:论文原文|Paper)\]\((https?://[^)\s]+)\)", structural_body)
        if len(zotero_links) != 1 or len(re.findall(r"zotero://", structural_body)) != 1:
            errors.append("Main note requires exactly one body [Zotero](zotero://...) link")
        if len(article_links) != 1:
            errors.append("Main note requires exactly one body [论文原文](https://...) or [Paper](https://...) link")
        elif structural_body.count(article_links[0]) != 1:
            errors.append("Article URL must appear only once in the body")
    elif re.search(r"zotero://|\[(?:论文原文|Paper)\]\(", structural_body):
        errors.append("Detail note must inherit source links from the main note instead of duplicating them")

    display_open = None
    for number, line in lines:
        delimiters = len(re.findall(r"(?<!\\)\$\$", line))
        if delimiters % 2:
            display_open = None if display_open is not None else number
        if re.search(r"{{.*?}}|{%.*?%}|\\FILL\{|精读内容尚未生成|Reading not generated yet", line):
            errors.append(f"Unresolved template/scaffold at body line {number}")
        if vault:
            for target in re.findall(r"!\[\[([^\]\n]+)\]\]", line):
                if not embedded_target_exists(target, note, vault):
                    errors.append(f"Missing, ambiguous or nonportable embed at body line {number}: {target}")
    clean_lines = [re.sub(r"^(?:[ \t]*>[ \t]?)+", "", x) for x in body.splitlines()]
    def paragraph_line(value: str) -> bool:
        value = value.strip()
        return bool(value) and not re.match(r"^(?:#|\||`|~|>|\$\$|[-*+]\s|\d+[.)]\s)", value)
    math_open = False
    for number, line in lines:
        if line.strip() == "$$":
            index = number - 1
            if not math_open and index > 0 and not clean_lines[index - 1].strip():
                before = index - 1
                while before >= 0 and not clean_lines[before].strip():
                    before -= 1
                if before >= 0 and paragraph_line(clean_lines[before]):
                    errors.append(f"Remove empty lines between prose and display math at body line {number}")
            elif math_open and index + 1 < len(clean_lines) and not clean_lines[index + 1].strip():
                after = index + 1
                while after < len(clean_lines) and not clean_lines[after].strip():
                    after += 1
                if after < len(clean_lines) and paragraph_line(clean_lines[after]):
                    errors.append(f"Remove empty lines between display math and prose at body line {number}")
            math_open = not math_open
    if display_open is not None:
        errors.append(f"Unclosed display-math delimiter starting at body line {display_open}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("note", type=Path, help="Generated literature/detail Markdown note")
    parser.add_argument("--vault", type=Path, help="Check local wikilink embeds relative to this vault")
    parser.add_argument("--paper-folder", type=Path, help="Enforce method folder/main filename and sibling-child layout")
    parser.add_argument("--allow-extra-notes", action="store_true", help="Allow additional sibling topic notes when the user explicitly requested a different split")
    args = parser.parse_args()
    errors = validate(args.note, args.vault, args.paper_folder, args.allow_extra_notes)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: structural checks only; verify YAML, sources, coverage and rendering separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
