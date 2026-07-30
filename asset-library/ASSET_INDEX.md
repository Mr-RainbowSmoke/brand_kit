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

## Lifecycle Status Rules
- Active: approved for new work and distribution.
- Deprecated: retained for traceability only; do not use in new work.
- Archived: historical reference only.

## Current Lifecycle Decisions

| Canonical File | Lifecycle | Notes |
|---|---|---|
| RAINBOWSMOKE_Profile_00_10_3_decorative_clean.png | Active | Primary profile mark. |
| RAINBOWSMOKE_Profile_00_10_3_rigsolid_clean.png | Active | Alternate profile mark. |
| RAINBOWSMOKE_Profile_Light_00_11_0.png | Active | Light-context profile variant. |
| RAINBOWSMOKE_Profile_Overlay_Dark_Transparent_00_10_2.png | Active | Overlay profile variant. |
| RAINBOWSMOKE_Glyph_RS_64_00_11_0.svg | Active | Canonical scalable glyph 64. |
| RAINBOWSMOKE_Glyph_RS_128_00_11_0.svg | Active | Canonical scalable glyph 128. |
| RAINBOWSMOKE_Glyph_RS_256_00_11_0.svg | Active | Canonical scalable glyph 256. |
| RAINBOWSMOKE_Glyph_RS_512_00_11_0.svg | Active | Canonical scalable glyph 512. |
| RAINBOWSMOKE_Overlay_Micro_64_00_10_2.svg | Active | Canonical scalable overlay 64. |
| RAINBOWSMOKE_Overlay_Micro_128_00_10_2.svg | Active | Canonical scalable overlay 128. |
| RAINBOWSMOKE_Overlay_Micro_256_00_10_2.svg | Active | Canonical scalable overlay 256. |
| RAINBOWSMOKE_Overlay_Micro_512_00_10_2.svg | Active | Canonical scalable overlay 512. |
| RAINBOWSMOKE_Micro_Smoke_Loop_00_11_0.gif | Active | Canonical motion asset. |

| Variant Pattern | Lifecycle | Notes |
|---|---|---|
| *_png.png | Deprecated | Duplicate naming variant of canonical PNG. |
| *_svg.svg | Deprecated | Duplicate naming variant of canonical SVG. |
| *_2.png | Deprecated | Duplicate variant pending archival pass. |
| *_2.svg | Deprecated | Duplicate variant pending archival pass. |

## Kit Manifests
- [SOCIAL_KIT_MANIFEST.md](SOCIAL_KIT_MANIFEST.md)
- [MEDIA_KIT_MANIFEST.md](MEDIA_KIT_MANIFEST.md)
- [CREATOR_KIT_MANIFEST.md](CREATOR_KIT_MANIFEST.md)
- [PRESS_KIT_MANIFEST.md](PRESS_KIT_MANIFEST.md)

## Deprecated Register
- [DEPRECATED_VARIANTS_REGISTER.md](DEPRECATED_VARIANTS_REGISTER.md)

## Next Implementation Tasks
1. Validate lifecycle decisions with owner review.
2. Perform non-destructive archival labeling pass for deprecated duplicates.
3. Add release-bundle lint/check rule to block deprecated variants.
