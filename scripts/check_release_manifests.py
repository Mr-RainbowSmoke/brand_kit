#!/usr/bin/env python3
"""Validate asset release manifests.

Checks:
1. Referenced asset paths exist.
2. Deprecated variants are not referenced.
3. Manifest structure includes at least one asset reference.

Exit code is non-zero when violations are found.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_LIBRARY = ROOT / "asset-library"
ASSETS_DIR = ROOT / "assets"

MANIFEST_FILES = [
    ASSET_LIBRARY / "SOCIAL_KIT_MANIFEST.md",
    ASSET_LIBRARY / "MEDIA_KIT_MANIFEST.md",
    ASSET_LIBRARY / "CREATOR_KIT_MANIFEST.md",
    ASSET_LIBRARY / "PRESS_KIT_MANIFEST.md",
]

DEPRECATED_REGISTER = ASSET_LIBRARY / "DEPRECATED_VARIANTS_REGISTER.md"

ASSET_PATH_RE = re.compile(r"\.\./assets/([A-Za-z0-9_.\-]+)")
DEPRECATED_PATTERN_RE = re.compile(
    r"(_png\.png|_svg\.svg|(?<!\d)_2\.png|(?<!\d)_2\.svg)$"
)
DEPRECATED_FILE_LINE_RE = re.compile(r"^-\s+([A-Za-z0-9_.\-]+)$")


def load_deprecated_filenames() -> set[str]:
    if not DEPRECATED_REGISTER.exists():
        return set()

    deprecated: set[str] = set()
    in_inventory = False

    for raw_line in DEPRECATED_REGISTER.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line == "## Current Deprecated Variant Inventory (Pattern-Based)":
            in_inventory = True
            continue
        if in_inventory and line.startswith("## "):
            break
        if in_inventory:
            match = DEPRECATED_FILE_LINE_RE.match(line)
            if match:
                deprecated.add(match.group(1))

    return deprecated


def collect_manifest_assets(manifest_path: Path) -> list[str]:
    matches = ASSET_PATH_RE.findall(manifest_path.read_text(encoding="utf-8"))
    return matches


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    deprecated_explicit = load_deprecated_filenames()

    for manifest_path in MANIFEST_FILES:
        if not manifest_path.exists():
            errors.append(f"Missing manifest: {manifest_path.name}")
            continue

        assets = collect_manifest_assets(manifest_path)
        if not assets:
            warnings.append(f"No asset references found in {manifest_path.name}")
            continue

        for filename in assets:
            asset_file = ASSETS_DIR / filename
            if not asset_file.exists():
                errors.append(
                    f"{manifest_path.name}: referenced asset does not exist -> {filename}"
                )

            if DEPRECATED_PATTERN_RE.search(filename) or filename in deprecated_explicit:
                errors.append(
                    f"{manifest_path.name}: deprecated variant referenced -> {filename}"
                )

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")
        print("\nManifest validation failed.")
        return 1

    print("Manifest validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
