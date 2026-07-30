#!/usr/bin/env python3
"""Validate parity between canonical docs and brand manifest.

Checks:
1. colors/COLOR_GUIDE.md metadata source SHA matches brand.manifest.json.
2. colors/COLOR_GUIDE.md metadata brand name matches manifest brand name.
3. Palette hex values in COLOR_GUIDE match manifest theme values.
4. fonts/FONTS_GUIDE.md metadata brand name matches manifest brand name.
5. fonts/FONTS_GUIDE.md Typekit project IDs match declared integration links.
6. Manifest typography includes required core families used by canonical docs.
7. foundation/BRAND_OVERVIEW.md core identity signals align to manifest essence.
8. verbal-system/VOICE_AND_TONE.md covers manifest voice traits and avoid terms.
9. verbal-system/TERMINOLOGY_STYLE.md includes baseline canonical terminology alignment.

Exit code is non-zero when violations are found.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "brand.manifest.json"
COLOR_GUIDE = ROOT / "colors" / "COLOR_GUIDE.md"
FONTS_GUIDE = ROOT / "fonts" / "FONTS_GUIDE.md"
BRAND_OVERVIEW = ROOT / "foundation" / "BRAND_OVERVIEW.md"
VOICE_AND_TONE = ROOT / "verbal-system" / "VOICE_AND_TONE.md"
TERMINOLOGY_STYLE = ROOT / "verbal-system" / "TERMINOLOGY_STYLE.md"

HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}")
FENCE_RE = re.compile(r"```json\n(.*?)\n```", re.DOTALL)

PALETTE_MAP = {
    "pride": "pride",
    "demiboy": "demiboy",
    "demisexual": "demisexual",
    "royalty": "royalty",
    "cotton candy": "Cotton Candy",
}

REQUIRED_FONT_FAMILY_FRAGMENTS = [
    "transat",
    "le havre rounded",
    "omnes",
    "chennai",
    "rig solid",
    "elliotts",
    "sketchnote text",
]

IDENTITY_SIGNAL_ALIASES = {
    "identity in motion": {
        "identity in motion",
    },
    "spectrum first color": {
        "spectrum first color",
        "spectrum forward color",
    },
    "digital native presence": {
        "digital native presence",
        "digital native aesthetic",
    },
    "high contrast dark mode friendly": {
        "high contrast dark mode friendly",
        "high contrast dark friendly presentation",
        "high contrast and dark friendly presentation",
    },
}

VOICE_TRAIT_ALIASES = {
    "confident": {
        "confident",
        "bold",
        "bold and expressive",
    },
    "warm": {
        "warm",
        "energetic and warm",
        "warm and direct",
    },
    "bold": {
        "bold",
        "bold and expressive",
    },
    "playful": {
        "playful",
        "personality",
        "energetic",
    },
}

VOICE_AVOID_ALIASES = {
    "generic corporate": {
        "generic corporate",
        "overly corporate",
        "stiff corporate language",
        "sterile",
    },
    "flat minimalism without signal": {
        "flat",
        "generic",
        "flat or generic",
    },
}


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def extract_metadata_json(markdown_text: str) -> dict:
    match = FENCE_RE.search(markdown_text)
    if not match:
        raise ValueError("Unable to locate metadata JSON block in COLOR_GUIDE.md")
    return json.loads(match.group(1))


def normalize_text(value: str) -> str:
    normalized = value.lower().strip()
    normalized = normalized.replace("-", " ")
    normalized = normalized.replace(",", " ")
    normalized = normalized.replace(":", " ")
    normalized = normalized.replace("_", " ")
    normalized = normalized.replace("/", " ")
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized


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


def extract_core_identity_signals(markdown_text: str) -> list[str]:
    lines = markdown_text.splitlines()
    in_section = False
    signals: list[str] = []

    for line in lines:
        if line.startswith("## "):
            if line.strip() == "## Core Identity Signals":
                in_section = True
                continue
            if in_section:
                break

        if in_section and line.startswith("- "):
            signals.append(line[2:].strip())

    return signals


def extract_manifest_font_families(manifest: dict) -> set[str]:
    families = {
        normalize_text(str(item.get("family", "")))
        for item in manifest.get("typography", {}).get("fonts", [])
    }
    return {family for family in families if family}


def validate_typography_parity(
    manifest: dict, fonts_guide_text: str, errors: list[str]
) -> None:
    metadata = extract_metadata_json(fonts_guide_text)

    manifest_brand_name = str(manifest["brand"]["name"])
    guide_brand_name = str(metadata.get("brand", ""))
    if guide_brand_name.upper() != manifest_brand_name.upper():
        errors.append(
            "Brand name mismatch: "
            f"FONTS_GUIDE has '{guide_brand_name}' but manifest has '{manifest_brand_name}'"
        )

    projects = metadata.get("adobe_fonts_projects", [])
    links = metadata.get("integration", {}).get("typekit_links", [])

    declared_project_ids = {
        str(project.get("project_id", "")).strip()
        for project in projects
        if str(project.get("project_id", "")).strip()
    }
    linked_project_ids = {
        link.rsplit("/", 1)[-1].replace(".css", "").strip()
        for link in links
        if isinstance(link, str) and link.strip()
    }

    if declared_project_ids != linked_project_ids:
        errors.append(
            "Typekit project mismatch: "
            f"declared={sorted(declared_project_ids)} links={sorted(linked_project_ids)}"
        )

    manifest_families = extract_manifest_font_families(manifest)
    for family_fragment in REQUIRED_FONT_FAMILY_FRAGMENTS:
        if not any(family_fragment in family for family in manifest_families):
            errors.append(
                "Missing required typography family fragment in manifest: "
                f"'{family_fragment}'"
            )


def validate_identity_parity(manifest: dict, brand_overview_text: str, errors: list[str]) -> None:
    doc_signals = {
        normalize_text(signal) for signal in extract_core_identity_signals(brand_overview_text)
    }
    manifest_signals = [
        normalize_text(signal)
        for signal in manifest.get("identity", {}).get("essence", [])
    ]

    for manifest_signal in manifest_signals:
        allowed_doc_signals = IDENTITY_SIGNAL_ALIASES.get(
            manifest_signal, {manifest_signal}
        )
        if not any(candidate in doc_signals for candidate in allowed_doc_signals):
            errors.append(
                "Missing identity signal parity in BRAND_OVERVIEW: "
                f"manifest='{manifest_signal}'"
            )


def validate_verbal_parity(
    manifest: dict, voice_and_tone_text: str, terminology_text: str, errors: list[str]
) -> None:
    voice_doc_normalized = normalize_text(voice_and_tone_text)
    terminology_normalized = normalize_text(terminology_text)

    voice_section = manifest.get("identity", {}).get("voice", {})
    traits = [normalize_text(str(item)) for item in voice_section.get("traits", [])]
    avoid_terms = [normalize_text(str(item)) for item in voice_section.get("avoid", [])]

    for trait in traits:
        allowed_phrases = VOICE_TRAIT_ALIASES.get(trait, {trait})
        if not any(phrase in voice_doc_normalized for phrase in allowed_phrases):
            errors.append(
                "Missing voice trait parity in VOICE_AND_TONE: "
                f"manifest trait='{trait}'"
            )

    for avoid in avoid_terms:
        allowed_phrases = VOICE_AVOID_ALIASES.get(avoid, {avoid})
        if not any(phrase in voice_doc_normalized for phrase in allowed_phrases):
            errors.append(
                "Missing voice avoid-term parity in VOICE_AND_TONE: "
                f"manifest avoid='{avoid}'"
            )

    manifest_brand_name = normalize_text(str(manifest.get("brand", {}).get("name", "")))
    if manifest_brand_name and manifest_brand_name not in terminology_normalized:
        errors.append(
            "Missing terminology parity in TERMINOLOGY_STYLE: "
            f"brand name '{manifest_brand_name}' not found"
        )

    rs_terminology_markers = {
        "approved short icon reference rs",
        "use rs for approved monogram icon context",
    }
    if not any(marker in terminology_normalized for marker in rs_terminology_markers):
        errors.append(
            "Missing terminology parity in TERMINOLOGY_STYLE: "
            "approved short icon reference for RS not found"
        )


def main() -> int:
    errors: list[str] = []

    manifest = load_manifest()
    color_guide_text = COLOR_GUIDE.read_text(encoding="utf-8")
    fonts_guide_text = FONTS_GUIDE.read_text(encoding="utf-8")
    brand_overview_text = BRAND_OVERVIEW.read_text(encoding="utf-8")
    voice_and_tone_text = VOICE_AND_TONE.read_text(encoding="utf-8")
    terminology_text = TERMINOLOGY_STYLE.read_text(encoding="utf-8")
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

    validate_typography_parity(manifest, fonts_guide_text, errors)
    validate_identity_parity(manifest, brand_overview_text, errors)
    validate_verbal_parity(manifest, voice_and_tone_text, terminology_text, errors)

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
