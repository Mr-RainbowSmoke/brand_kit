#!/usr/bin/env python3
"""Validate parity between canonical docs and brand manifest.

Checks:
1. colors/COLOR_GUIDE.md metadata source SHA matches brand.manifest.json.
2. colors/COLOR_GUIDE.md metadata brand name matches manifest brand name.
3. Palette hex values in COLOR_GUIDE match manifest theme values.

Exit code is non-zero when violations are found.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "brand.manifest.json"
COLOR_GUIDE = ROOT / "colors" / "COLOR_GUIDE.md"

HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}")
FENCE_RE = re.compile(r"```json\n(.*?)\n```", re.DOTALL)

PALETTE_MAP = {
    "pride": "pride",
    "demiboy": "demiboy",
    "demisexual": "demisexual",
    "royalty": "royalty",
    "cotton candy": "Cotton Candy",
}


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def extract_metadata_json(markdown_text: str) -> dict:
    match = FENCE_RE.search(markdown_text)
    if not match:
        raise ValueError("Unable to locate metadata JSON block in COLOR_GUIDE.md")
    return json.loads(match.group(1))


def extract_palette_hexes(markdown_text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    pattern = re.compile(r"^###\s+(.+?)\n(.*?)(?=^###\s+|\Z)", re.MULTILINE | re.DOTALL)

    for raw_name, body in pattern.findall(markdown_text):
        section_name = raw_name.strip().lower()
        if "(" in section_name:
            section_name = section_name.split("(", 1)[0].strip()

        if section_name not in PALETTE_MAP:
            continue

        block_match = FENCE_RE.search(body)
        if not block_match:
            continue

        hexes = [value.upper() for value in HEX_RE.findall(block_match.group(1))]
        sections[section_name] = hexes

    return sections


def extract_manifest_palette_hexes(manifest: dict) -> dict[str, list[str]]:
    themes = manifest["color"]["themes"]
    result: dict[str, list[str]] = {}
    for theme in themes:
        name = str(theme["name"]).lower()
        result[name] = [str(swatch["hex"]).upper() for swatch in theme["swatches"]]
    return result


def main() -> int:
    errors: list[str] = []

    manifest = load_manifest()
    color_guide_text = COLOR_GUIDE.read_text(encoding="utf-8")
    metadata = extract_metadata_json(color_guide_text)

    manifest_brand_name = str(manifest["brand"]["name"])
    guide_brand_name = str(metadata.get("brand", ""))
    if guide_brand_name.upper() != manifest_brand_name.upper():
        errors.append(
            f"Brand name mismatch: COLOR_GUIDE has '{guide_brand_name}' but manifest has '{manifest_brand_name}'"
        )

    manifest_sha = str(manifest["brand"]["source"]["sha256"])
    guide_sha = str(metadata.get("master_source", {}).get("sha256", ""))
    if guide_sha != manifest_sha:
        errors.append(
            f"Master source sha mismatch: COLOR_GUIDE has '{guide_sha}' but manifest has '{manifest_sha}'"
        )

    manifest_palettes = extract_manifest_palette_hexes(manifest)
    guide_palettes = extract_palette_hexes(color_guide_text)

    for guide_name, manifest_name in PALETTE_MAP.items():
        if guide_name not in guide_palettes:
            errors.append(f"Missing palette section in COLOR_GUIDE: {guide_name}")
            continue

        manifest_key = manifest_name.lower()
        if manifest_key not in manifest_palettes:
            errors.append(f"Missing theme in manifest: {manifest_name}")
            continue

        guide_hexes = guide_palettes[guide_name]
        manifest_hexes = manifest_palettes[manifest_key]

        if guide_hexes != manifest_hexes:
            errors.append(
                "Palette mismatch for "
                f"{guide_name}: COLOR_GUIDE={guide_hexes} manifest={manifest_hexes}"
            )

    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")
        print("\nDocs-manifest parity validation failed.")
        return 1

    print("Docs-manifest parity validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
