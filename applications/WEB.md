# Web Playbook

## Goal
Apply RAINBOWSMOKE branding consistently across websites and landing pages.

## Required Asset Variants

| Asset | Format | Usage |
|---|---|---|
| Primary glyph (RS mark) | SVG | Header logo, favicon companion |
| Favicon | ICO / 32x32 PNG | Browser tab |
| OG social image | 1200x630 PNG | Link previews across platforms |
| Hero banner | 1920x1080 PNG/SVG | Landing page hero |
| Profile mark (light) | PNG/SVG | Light-surface headers |

## Safe Zones and Layout Rules
- Logo clear space: minimum equal to the cap-height of the mark on all sides
- Hero text: left-aligned or centered; never right-aligned on first touch
- Hero CTA zone: keep above the fold on common 1080p viewport
- Content column: max-width 800px for reading-weight content; 1200px for full-bleed layouts
- Navigation: sticky or anchored; must stay legible on both light and dark surfaces

## Structure Baseline
- Hero with one primary headline (Omnes Narrow Black) and one supporting line
- Section rhythm uses consistent heading levels (h2 for section titles, h3 for sub-items)
- Distinct CTA zone per page — one primary action, one supporting action max

## Typography Baseline
- Body readability takes priority over display impact
- Follow [visual-system/TYPOGRAPHY_SYSTEM.md](../visual-system/TYPOGRAPHY_SYSTEM.md) for full role assignments
- Minimum body size: 16px; minimum UI label: 14px

## Color Baseline
- Use approved palette combinations only (see [visual-system/COLOR_SYSTEM.md](../visual-system/COLOR_SYSTEM.md))
- Royalty blue preferred for primary CTA backgrounds
- Cotton Candy reserved for secondary or seasonal accent surfaces
- Preserve 4.5:1 contrast on all CTA and nav text

## Copy Tone Variant
- Confident and direct — no hedging, no filler
- Lead with value; explain how not just what
- CTAs use active verbs: Join, Watch, Get, Explore — not Click here or Learn more

## Do / Don't

| Do | Don't |
|---|---|
| Use one clear primary CTA per page | Stack multiple competing CTAs in the hero |
| Keep body text in Transat at readable sizes | Use display fonts (Rig Solid, Elliott's) for body copy |
| Apply Royalty blue to key interactive actions | Use Pride rainbow as a UI color sequence on interactive elements |
| Ensure logo has clear space on all surfaces | Place the mark against a competing busy pattern |
| Validate keyboard nav and focus states before launch | Ship without visible focus indicator |

## Asset Usage
- Prefer SVG marks where possible
- Keep profile and glyph marks within approved clear-space zones
- Use only active canonical assets (see [asset-library/ASSET_INDEX.md](../asset-library/ASSET_INDEX.md))

## Accessibility Baseline
- Keyboard navigation required across all interactive elements
- Focus states required and consistent with component specs
- Contrast at AA minimum; AAA preferred for primary reading surfaces

## Build Checklist
- [ ] Typography hierarchy follows TYPOGRAPHY_SYSTEM.md
- [ ] Color pairings use approved combinations only
- [ ] Hero has one primary CTA above the fold
- [ ] Header, nav, and CTA zones are readable at mobile and desktop breakpoints
- [ ] Canonical mark assets used (no deprecated duplicates)
- [ ] Focus and keyboard traversal behavior validated
- [ ] OG image is present and correctly sized

## Starter Page Template
1. Hero: Omnes Narrow Black headline, one supporting line (Transat), one Royalty blue CTA
2. Value section: 3 short benefit blocks with Le Havre Rounded labels
3. Community section: creator-focused proof or featured content card
4. Action section: one secondary text CTA and one final primary CTA
