# Mobile Playbook

## Goal
Apply brand rules to mobile-first interfaces and app surfaces.

## Layout Baseline
- Content column: full-width with 16–24px horizontal padding
- Minimum touch target: 44 × 44px (Apple HIG / Material guidance)
- Primary actions above the fold at 375px viewport width (iPhone SE baseline)
- Keep primary actions visible without excessive scroll (max 1.5 screens to CTA)
- Use clear hierarchy in constrained viewports: one H1, one CTA zone per screen

## Typography Baseline
- Follow mobile scale in [visual-system/TYPOGRAPHY_SYSTEM.md](../visual-system/TYPOGRAPHY_SYSTEM.md)
- Minimum body size: 16px; minimum label: 14px
- Avoid decorative display fonts (Rig Solid, Elliott's) for functional UI text
- Headlines: Omnes Narrow Black at sizes that breathe in constrained viewports

## Color Baseline
- Use approved high-contrast combinations (see [accessibility/ACCESSIBILITY_BASELINE.md](../accessibility/ACCESSIBILITY_BASELINE.md))
- Avoid thin low-contrast text on bright accents (Pride yellow, Cotton Candy on white)
- Dark-mode consideration: verify Royalty blue (#0F1AF2) label contrast on dark backgrounds

## Required Asset Variants

| Asset | Dimensions | Notes |
|---|---|---|
| App icon | 1024 × 1024 px | iOS/Android submission; must include clear space |
| Splash / loading screen mark | 200 × 200 px | Centered glyph on brand color background |
| Notification icon | 96 × 96 px (Android) | Monochrome, transparent background |
| In-app header mark | SVG (flex width) | Scales to nav bar height |

## Do / Don't

| Do | Don't |
|---|---|
| Keep min touch target at 44×44px | Make tappable areas smaller for visual compactness |
| Show the primary CTA without scrolling on 375px | Bury primary actions below the fold |
| Use Royalty blue for primary interactive elements | Use Pride rainbow sequence for interactive states |
| Test at 375px (small) and 428px (large) breakpoints | Only design at 390px and assume it scales |
| Preserve OS-level focus and accessibility features | Suppress native focus or override system accessibility |

## Accessibility Baseline
- Touch targets must meet 44×44px minimum
- Focus and active states must remain visible (do not suppress OS defaults)
- Font sizes must remain user-scalable (avoid fixed px that block dynamic type)
- Contrast at AA minimum on both light and dark surfaces

## Mobile QA Checklist
- [ ] Core actions reachable without excessive scrolling on 375px viewport
- [ ] Typography follows mobile scale guidance
- [ ] All touch targets ≥44×44px
- [ ] Primary and secondary actions are visually distinct
- [ ] Canonical assets used (no deprecated variants)
- [ ] Contrast meets AA minimum on both light and dark surfaces
- [ ] Dynamic type scaling not blocked

## Starter Screen Template
1. Header zone: brand mark (SVG, flex width) and one contextual action
2. Primary content zone: headline (Omnes Narrow Black) + 1–2 support sentences
3. Action zone: one primary CTA button (Royalty blue, 44px min height) and one optional secondary text action
4. Support zone: helper copy or status message (Transat Regular, 14–16px)

## Typography Baseline
- Follow mobile scale recommendations in ../visual-system/TYPOGRAPHY_SYSTEM.md.
- Avoid decorative display type for functional UI.

## Color Baseline
- Use approved high-contrast combinations.
- Avoid thin low-contrast text on bright accents.

## Accessibility Baseline
- Touch targets should be comfortably tappable.
- Focus and active states should remain visible.

## Mobile QA Checklist
- [ ] Core actions are reachable without excessive scrolling.
- [ ] Typography follows mobile scale guidance in ../visual-system/TYPOGRAPHY_SYSTEM.md.
- [ ] Primary and secondary actions are visually distinct.
- [ ] Touch targets are comfortably tappable.
- [ ] Canonical assets are used (no deprecated variants).
- [ ] Contrast meets AA minimum.

## Starter Screen Template
1. Header zone: clear title and one contextual action.
2. Primary content zone: key creator/community value.
3. Action zone: one primary CTA and one optional secondary action.
4. Support zone: concise helper copy or status message.
