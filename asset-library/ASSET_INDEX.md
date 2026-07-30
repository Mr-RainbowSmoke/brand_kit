# Asset Index

This file tracks asset purpose, canonical status, and duplication risk.

## Canonical Asset Policy
- Canonical formats:
  - SVG for scalable marks and overlays
  - PNG for raster-safe distribution
  - GIF for approved motion loops
- Do not delete variants until canonical mapping is complete.

## Current Inventory Summary
- Directory: ../assets/
- Notable families:
  - Profile assets
  - Glyph RS assets
  - Overlay Micro assets
  - Motion loop asset

## Known Risks
1. Duplicate or near-duplicate variants with suffix patterns like _2, _png, _svg.
2. Unclear canonical pick per size/format for some families.

## Mapping Template
Use this table when canonical mapping begins.

| Family | Candidate Files | Canonical File | Purpose | Status |
|---|---|---|---|---|
| Profile | RAINBOWSMOKE_Profile_00_10_3_decorative_clean.png; RAINBOWSMOKE_Profile_00_10_3_decorative_clean_png.png | RAINBOWSMOKE_Profile_00_10_3_decorative_clean.png | Social/profile | Provisional Canonical |
| Profile | RAINBOWSMOKE_Profile_00_10_3_rigsolid_clean.png; RAINBOWSMOKE_Profile_00_10_3_rigsolid_clean_png.png | RAINBOWSMOKE_Profile_00_10_3_rigsolid_clean.png | Social/profile alt | Provisional Canonical |
| Profile | RAINBOWSMOKE_Profile_Light_00_11_0.png; RAINBOWSMOKE_Profile_Light_00_11_0_2.png; RAINBOWSMOKE_Profile_Light_00_11_0_png.png | RAINBOWSMOKE_Profile_Light_00_11_0.png | Light profile variant | Provisional Canonical |
| Profile | RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2.png; RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2_2.png; RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2_png.png | RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2.png | Dark transparent overlay profile | Provisional Canonical |
| Glyph RS | RAINBOWSMOKE_Glyph_RS_64_00_11_0.svg; RAINBOWSMOKE_Glyph_RS_64_00_11_0.png | RAINBOWSMOKE_Glyph_RS_64_00_11_0.svg | Mark/icon 64 | Provisional Canonical |
| Glyph RS | RAINBOWSMOKE_Glyph_RS_128_00_11_0.svg; RAINBOWSMOKE_Glyph_RS_128_00_11_0.png; RAINBOWSMOKE_Glyph_RS_128_00_11_0_2.svg | RAINBOWSMOKE_Glyph_RS_128_00_11_0.svg | Mark/icon 128 | Provisional Canonical |
| Glyph RS | RAINBOWSMOKE_Glyph_RS_256_00_11_0.svg; RAINBOWSMOKE_Glyph_RS_256_00_11_0.png; RAINBOWSMOKE_Glyph_RS_256_00_11_0_2.svg | RAINBOWSMOKE_Glyph_RS_256_00_11_0.svg | Mark/icon 256 | Provisional Canonical |
| Glyph RS | RAINBOWSMOKE_Glyph_RS_512_00_11_0.svg; RAINBOWSMOKE_Glyph_RS_512_00_11_0.png | RAINBOWSMOKE_Glyph_RS_512_00_11_0.svg | Mark/icon 512 | Provisional Canonical |
| Overlay Micro | RAINBOWSMOKE_Overlay_Micro_64_00_10_2.svg; RAINBOWSMOKE_Overlay_Micro_64_00_10_2.png; RAINBOWSMOKE_Overlay_Micro_64_00_10_2_2.svg; RAINBOWSMOKE_Overlay_Micro_64_00_10_2_png.png; RAINBOWSMOKE_Overlay_Micro_64_00_10_2_svg.svg | RAINBOWSMOKE_Overlay_Micro_64_00_10_2.svg | Overlay/watermark 64 | Provisional Canonical |
| Overlay Micro | RAINBOWSMOKE_Overlay_Micro_128_00_10_2.svg; RAINBOWSMOKE_Overlay_Micro_128_00_10_2.png; RAINBOWSMOKE_Overlay_Micro_128_00_10_2_2.svg; RAINBOWSMOKE_Overlay_Micro_128_00_10_2_2.png; RAINBOWSMOKE_Overlay_Micro_128_00_10_2_png.png; RAINBOWSMOKE_Overlay_Micro_128_00_10_2_svg.svg | RAINBOWSMOKE_Overlay_Micro_128_00_10_2.svg | Overlay/watermark 128 | Provisional Canonical |
| Overlay Micro | RAINBOWSMOKE_Overlay_Micro_256_00_10_2.svg; RAINBOWSMOKE_Overlay_Micro_256_00_10_2.png; RAINBOWSMOKE_Overlay_Micro_256_00_10_2_2.svg; RAINBOWSMOKE_Overlay_Micro_256_00_10_2_2.png; RAINBOWSMOKE_Overlay_Micro_256_00_10_2_png.png; RAINBOWSMOKE_Overlay_Micro_256_00_10_2_svg.svg | RAINBOWSMOKE_Overlay_Micro_256_00_10_2.svg | Overlay/watermark 256 | Provisional Canonical |
| Overlay Micro | RAINBOWSMOKE_Overlay_Micro_512_00_10_2.svg; RAINBOWSMOKE_Overlay_Micro_512_00_10_2.png; RAINBOWSMOKE_Overlay_Micro_512_00_10_2_2.svg; RAINBOWSMOKE_Overlay_Micro_512_00_10_2_2.png; RAINBOWSMOKE_Overlay_Micro_512_00_10_2_png.png; RAINBOWSMOKE_Overlay_Micro_512_00_10_2_svg.svg | RAINBOWSMOKE_Overlay_Micro_512_00_10_2.svg | Overlay/watermark 512 | Provisional Canonical |
| Smoke Loop | RAINBOWSMOKE_Micro_Smoke_Loop_00_11_0.gif | RAINBOWSMOKE_Micro_Smoke_Loop_00_11_0.gif | Motion | Canonical |

## Next Implementation Tasks
1. Validate provisional canonical picks with owner review.
2. Add active/deprecated status for every canonical decision.
3. Add pack manifests for social kit, media kit, creator kit, and press kit.
