#!/usr/bin/env python3
"""Lint markdown style with lightweight, dependency-free checks.

Checks:
1. No trailing whitespace.
2. No multiple consecutive blank lines.
3. Heading level does not jump by more than one.
4. Exactly one H1 per file.

Exit code is non-zero when violations are found.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADING_RE = re.compile(r"^(#{1,6})\s+")
IGNORED_FILES = {
    "fonts/gsl6svi.md",
    "fonts/ojc8wen.md",
}


def iter_markdown_files() -> list[Path]:
    files = [
        path
        for path in ROOT.rglob("*.md")
        if ".github" not in path.parts
        and path.relative_to(ROOT).as_posix() not in IGNORED_FILES
    ]
    return sorted(files)


def lint_file(md_path: Path) -> list[str]:
    errors: list[str] = []
    lines = md_path.read_text(encoding="utf-8").splitlines()

    in_fence = False
    blank_run = 0
    previous_heading_level = 0
    h1_count = 0

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()

        if stripped.startswith("```"):
            in_fence = not in_fence

        if in_fence:
            continue

        if line != line.rstrip():
            errors.append(
                f"{md_path.relative_to(ROOT)}:{line_num}: trailing whitespace"
            )

        if stripped == "":
            blank_run += 1
            if blank_run > 1:
                errors.append(
                    f"{md_path.relative_to(ROOT)}:{line_num}: multiple consecutive blank lines"
                )
        else:
            blank_run = 0

        match = HEADING_RE.match(line)
        if not match:
            continue

        level = len(match.group(1))
        if level == 1:
            h1_count += 1

        if previous_heading_level and level > previous_heading_level + 1:
            errors.append(
                f"{md_path.relative_to(ROOT)}:{line_num}: heading jump from H{previous_heading_level} to H{level}"
            )

        previous_heading_level = level

    if h1_count != 1:
        errors.append(
            f"{md_path.relative_to(ROOT)}: expected exactly one H1, found {h1_count}"
        )

    return errors


def main() -> int:
    all_errors: list[str] = []
    for md_file in iter_markdown_files():
        all_errors.extend(lint_file(md_file))

    if all_errors:
        print("Errors:")
        for error in all_errors:
            print(f"- {error}")
        print("\nMarkdown style lint failed.")
        return 1

    print("Markdown style lint passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
