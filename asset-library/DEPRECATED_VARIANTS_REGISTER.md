# Deprecated Variants Register

This register tracks duplicate and legacy file variants marked Deprecated.

## Policy
- Deprecated files remain in place for traceability.
- Deprecated files are not approved for new work.
- Cleanup actions must be non-destructive and auditable.

## Deprecated Variant Patterns
- *_png.png
- *_svg.svg
- *_2.png
- *_2.svg

## Current Deprecated Variant Inventory (Pattern-Based)

### Profile
- RAINBOWSMOKE_Profile_00_10_3_decorative_clean_png.png
- RAINBOWSMOKE_Profile_00_10_3_rigsolid_clean_png.png
- RAINBOWSMOKE_Profile_Light_00_11_0_2.png
- RAINBOWSMOKE_Profile_Light_00_11_0_png.png
- RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2_2.png
- RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2_png.png

### Glyph RS
- RAINBOWSMOKE_Glyph_RS_128_00_11_0_2.svg
- RAINBOWSMOKE_Glyph_RS_256_00_11_0_2.svg

### Overlay Micro
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

## Canonical Mapping Reference
See ASSET_INDEX.md for active canonical file mapping.

## Next Actions
1. Add migration note per deprecated file to canonical target.
2. Add release-bundle lint rule to block deprecated variants in manifests.
3. Perform owner-approved archival labeling pass.
