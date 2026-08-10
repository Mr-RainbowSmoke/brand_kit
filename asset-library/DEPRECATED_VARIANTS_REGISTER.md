# Deprecated Variants Register

This register tracks duplicate and legacy file variants marked Deprecated or Archived.

## Policy
- Deprecated files remain in place for traceability until archival criteria are met.
- Deprecated files are not approved for new work.
- Archived files live in assets/archive/ and are eligible for permanent deletion after 12 months from archive date with maintainer sign-off.
- See governance/DECISION_LOG.md (Decision: Asset archival timing policy).

## Deprecated Variant Patterns
- *_png.png
- *_svg.svg
- *_2.png
- *_2.svg

## Archived Variant Inventory

All 23 deprecated variants were archived 2026-08-10 to assets/archive/.

### Profile (archived 2026-08-10)
- RAINBOWSMOKE_Profile_00_10_3_decorative_clean_png.png
- RAINBOWSMOKE_Profile_00_10_3_rigsolid_clean_png.png
- RAINBOWSMOKE_Profile_Light_00_11_0_2.png
- RAINBOWSMOKE_Profile_Light_00_11_0_png.png
- RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2_2.png
- RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2_png.png

### Glyph RS (archived 2026-08-10)
- RAINBOWSMOKE_Glyph_RS_128_00_11_0_2.svg
- RAINBOWSMOKE_Glyph_RS_256_00_11_0_2.svg

### Overlay Micro (archived 2026-08-10)
- RAINBOWSMOKE_Overlay_Micro_64_00_10_2_2.svg
- RAINBOWSMOKE_Overlay_Micro_64_00_10_2_png.png
- RAINBOWSMOKE_Overlay_Micro_64_00_10_2_svg.svg
- RAINBOWSMOKE_Overlay_Micro_128_00_10_2_2.png
- RAINBOWSMOKE_Overlay_Micro_128_00_10_2_2.svg
- RAINBOWSMOKE_Overlay_Micro_128_00_10_2_png.png
- RAINBOWSMOKE_Overlay_Micro_128_00_10_2_svg.svg
- RAINBOWSMOKE_Overlay_Micro_256_00_10_2_2.png
- RAINBOWSMOKE_Overlay_Micro_256_00_10_2_2.svg
- RAINBOWSMOKE_Overlay_Micro_256_00_10_2_png.png
- RAINBOWSMOKE_Overlay_Micro_256_00_10_2_svg.svg
- RAINBOWSMOKE_Overlay_Micro_512_00_10_2_2.png
- RAINBOWSMOKE_Overlay_Micro_512_00_10_2_2.svg
- RAINBOWSMOKE_Overlay_Micro_512_00_10_2_png.png
- RAINBOWSMOKE_Overlay_Micro_512_00_10_2_svg.svg

## Deletion Eligibility
Archived 2026-08-10. Eligible for permanent deletion after 2027-08-10 with explicit maintainer sign-off.

## Canonical Mapping Reference
See ASSET_INDEX.md for active canonical file mapping.

## Validation Command
Run before release packaging:

```bash
python3 ../scripts/check_release_manifests.py
```
