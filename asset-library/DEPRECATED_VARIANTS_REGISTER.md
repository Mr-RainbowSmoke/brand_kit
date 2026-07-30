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

## Migration Map (Deprecated -> Canonical)

| Deprecated file | Canonical target |
|---|---|
| RAINBOWSMOKE_Profile_00_10_3_decorative_clean_png.png | RAINBOWSMOKE_Profile_00_10_3_decorative_clean.png |
| RAINBOWSMOKE_Profile_00_10_3_rigsolid_clean_png.png | RAINBOWSMOKE_Profile_00_10_3_rigsolid_clean.png |
| RAINBOWSMOKE_Profile_Light_00_11_0_2.png | RAINBOWSMOKE_Profile_Light_00_11_0.png |
| RAINBOWSMOKE_Profile_Light_00_11_0_png.png | RAINBOWSMOKE_Profile_Light_00_11_0.png |
| RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2_2.png | RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2.png |
| RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2_png.png | RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2.png |
| RAINBOWSMOKE_Glyph_RS_128_00_11_0_2.svg | RAINBOWSMOKE_Glyph_RS_128_00_11_0.svg |
| RAINBOWSMOKE_Glyph_RS_256_00_11_0_2.svg | RAINBOWSMOKE_Glyph_RS_256_00_11_0.svg |
| RAINBOWSMOKE_Overlay_Micro_64_00_10_2_2.svg | RAINBOWSMOKE_Overlay_Micro_64_00_10_2.svg |
| RAINBOWSMOKE_Overlay_Micro_64_00_10_2_png.png | RAINBOWSMOKE_Overlay_Micro_64_00_10_2.png |
| RAINBOWSMOKE_Overlay_Micro_64_00_10_2_svg.svg | RAINBOWSMOKE_Overlay_Micro_64_00_10_2.svg |
| RAINBOWSMOKE_Overlay_Micro_128_00_10_2_2.png | RAINBOWSMOKE_Overlay_Micro_128_00_10_2.png |
| RAINBOWSMOKE_Overlay_Micro_128_00_10_2_2.svg | RAINBOWSMOKE_Overlay_Micro_128_00_10_2.svg |
| RAINBOWSMOKE_Overlay_Micro_128_00_10_2_png.png | RAINBOWSMOKE_Overlay_Micro_128_00_10_2.png |
| RAINBOWSMOKE_Overlay_Micro_128_00_10_2_svg.svg | RAINBOWSMOKE_Overlay_Micro_128_00_10_2.svg |
| RAINBOWSMOKE_Overlay_Micro_256_00_10_2_2.png | RAINBOWSMOKE_Overlay_Micro_256_00_10_2.png |
| RAINBOWSMOKE_Overlay_Micro_256_00_10_2_2.svg | RAINBOWSMOKE_Overlay_Micro_256_00_10_2.svg |
| RAINBOWSMOKE_Overlay_Micro_256_00_10_2_png.png | RAINBOWSMOKE_Overlay_Micro_256_00_10_2.png |
| RAINBOWSMOKE_Overlay_Micro_256_00_10_2_svg.svg | RAINBOWSMOKE_Overlay_Micro_256_00_10_2.svg |
| RAINBOWSMOKE_Overlay_Micro_512_00_10_2_2.png | RAINBOWSMOKE_Overlay_Micro_512_00_10_2.png |
| RAINBOWSMOKE_Overlay_Micro_512_00_10_2_2.svg | RAINBOWSMOKE_Overlay_Micro_512_00_10_2.svg |
| RAINBOWSMOKE_Overlay_Micro_512_00_10_2_png.png | RAINBOWSMOKE_Overlay_Micro_512_00_10_2.png |
| RAINBOWSMOKE_Overlay_Micro_512_00_10_2_svg.svg | RAINBOWSMOKE_Overlay_Micro_512_00_10_2.svg |

## Validation Command
Run before release packaging:

```bash
python3 ../scripts/check_release_manifests.py
```

## Next Actions
1. Keep migration map updated as new duplicates are discovered.
2. Keep release manifest checks passing before each distribution.
3. Perform owner-approved archival labeling pass.
