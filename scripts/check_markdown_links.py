#!/usr/bin/env python3
"""Validate local markdown links.

Checks:
1. Local markdown links point to existing files.
2. Internal heading fragments resolve to existing headings.

External links (http/https/mailto/tel/data) are ignored.
Exit code is non-zero when violations are found.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")

EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:")


def github_slug(text: str) -> str:
    value = text.strip().lower()
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"[^a-z0-9\-\s]", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-")


def extract_headings(md_path: Path) -> set[str]:
    anchors: set[str] = set()
    text = md_path.read_text(encoding="utf-8")
    in_fence = False

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        match = HEADING_RE.match(line)
        if not match:
            continue

        heading = match.group(2).strip()
        if not heading:
            continue

        anchors.add(github_slug(heading))

    return anchors


def iter_markdown_files() -> list[Path]:
    return sorted(ROOT.rglob("*.md"))


def validate_links_in_file(md_path: Path, heading_cache: dict[Path, set[str]]) -> list[str]:
    errors: list[str] = []
    in_fence = False

    for line_num, line in enumerate(md_path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        for raw_target in LINK_RE.findall(line):
            target = raw_target.strip().strip("<>")
            target = unquote(target)

            if not target or target.startswith(EXTERNAL_PREFIXES):
                continue

            if target.startswith("#"):
                fragment = target[1:]
                anchors = heading_cache.setdefault(md_path, extract_headings(md_path))
                if fragment not in anchors:
                    errors.append(
                        f"{md_path.relative_to(ROOT)}:{line_num}: missing heading fragment '#{fragment}' in same file"
                    )
                continue

            path_part, fragment = (target.split("#", 1) + [""])[:2]
            if "?" in path_part:
                path_part = path_part.split("?", 1)[0]

            resolved = (md_path.parent / path_part).resolve()
            if not resolved.exists():
                errors.append(
                    f"{md_path.relative_to(ROOT)}:{line_num}: missing target '{target}'"
                )
                continue

            if fragment and resolved.suffix.lower() == ".md":
                anchors = heading_cache.setdefault(resolved, extract_headings(resolved))
                if fragment not in anchors:
                    rel_resolved = resolved.relative_to(ROOT)
                    errors.append(
                        f"{md_path.relative_to(ROOT)}:{line_num}: missing heading fragment '#{fragment}' in {rel_resolved}"
                    )

    return errors


def main() -> int:
    errors: list[str] = []
    heading_cache: dict[Path, set[str]] = {}

    markdown_files = iter_markdown_files()
    if not markdown_files:
        print("No markdown files found.")
        return 0

    for md_path in markdown_files:
        errors.extend(validate_links_in_file(md_path, heading_cache))

    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")
        print("\nMarkdown link validation failed.")
        return 1

    print("Markdown link validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
