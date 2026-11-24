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


def marker_span(body: str, start: str, end: str, label: str, required: bool, errors: list[str]):
    # Structural markers must occupy their own unindented line, outside code.
    starts = list(re.finditer(r"^" + re.escape(start) + r"[ \t]*$", body, re.M))
    ends = list(re.finditer(r"^" + re.escape(end) + r"[ \t]*$", body, re.M))
    if not starts and not ends and not required:
        return None
    if len(starts) != 1 or len(ends) != 1:
        errors.append(f"{label}: expected exactly one standalone start/end pair")
        return None
    if starts[0].start() >= ends[0].start():
        errors.append(f"{label}: end marker precedes start")
        return None
    return starts[0].start(), ends[0].end()


def embedded_target_exists(target: str, note: Path, vault: Path) -> bool:
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


def validate(note: Path, vault: Path | None = None) -> list[str]:
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
    detail = scalar(frontmatter, "type") == "paper-detail"
    if detail:
        if not scalar(frontmatter, "parent-note"):
            errors.append("Detail note requires parent-note")
        if scalar(frontmatter, "zotero-key"):
            errors.append("Detail note must not duplicate the literature note's zotero-key")
    elif scalar(frontmatter, "zotero-key").lower() in ("", "null", "~"):
        errors.append("Literature note requires ZotLit-generated zotero-key")

    lines, fence_errors = prose_lines(body)
    errors.extend(fence_errors)
    # Preserve original positions while blanking code examples that quote markers.
    retained = {n for n, _ in lines}
    structural_body = "\n".join(line if n in retained else " " * len(line)
                                 for n, line in enumerate(body.splitlines(), 1))
    spans = []
    for label, start, end, required in [
        ("ZotLit managed region", "%%zt-managed%%", "%%/zt-managed%%", not detail),
        ("AI region", "<!-- paper-reading:ai:start -->", "<!-- paper-reading:ai:end -->", not detail),
        ("User region", "<!-- paper-reading:user:start -->", "<!-- paper-reading:user:end -->", not detail),
    ]:
        span = marker_span(structural_body, start, end, label, required, errors)
        if span:
            spans.append((label, span))
    for i, (label, (start, end)) in enumerate(spans):
        for other, (other_start, other_end) in spans[i + 1:]:
            if start < other_end and other_start < end:
                errors.append(f"Regions overlap: {label} and {other}")

    display_open = None
    for number, line in lines:
        delimiters = len(re.findall(r"(?<!\\)\$\$", line))
        if delimiters % 2:
            display_open = None if display_open is not None else number
        if re.search(r"{{.*?}}|{%.*?%}|\\FILL\{|精读内容尚未生成", line):
            errors.append(f"Unresolved template/scaffold at body line {number}")
        if vault:
            for target in re.findall(r"!\[\[([^\]\n]+)\]\]", line):
                if not embedded_target_exists(target, note, vault):
                    errors.append(f"Missing, ambiguous or nonportable embed at body line {number}: {target}")
    if display_open is not None:
        errors.append(f"Unclosed display-math delimiter starting at body line {display_open}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("note", type=Path, help="Generated literature/detail Markdown note")
    parser.add_argument("--vault", type=Path, help="Check local wikilink embeds relative to this vault")
    args = parser.parse_args()
    errors = validate(args.note, args.vault)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: structural checks only; verify YAML, sources, coverage and rendering separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
