# Logo And Asset Usage

## Canonical Sources
- Binary assets: ../assets/
- Metadata: ../brand.manifest.json
- Legacy integrated references: ../brand_page.md

## Baseline Rules
- Preserve aspect ratio and clear space.
- Do not redraw, stretch, skew, or recolor protected assets.
- Prefer SVG for scalable contexts where supported.
- Use dark-compatible presentation where specified by asset design.

## Core Asset Families
- Profile assets
- Glyph RS assets
- Overlay Micro assets
- Smoke loop motion asset

## Family Usage Baseline
- Profile assets: primary use in social profile and avatar contexts at canonical sizes.
- Glyph RS assets: icon and stamp contexts where full wordmark is not practical.
- Overlay Micro assets: stream and creator overlay layers where subtle branding is required.
- Smoke loop motion asset: motion backgrounds and stingers only; do not flatten into static mark substitutions.

## Presentation Constraints
- Default to dark backgrounds for major logo and smoke assets unless a documented exception exists.
- Maintain minimum padding around marks in composited assets.

## Current Risk
Multiple near-duplicate files exist for several families. Canonical mapping is required before cleanup.

## Next Implementation Tasks
1. Define canonical file picks per family and size.
2. Tag files as active or deprecated in asset index.
3. Add logo lockup and background contrast matrix with do/don't examples.
