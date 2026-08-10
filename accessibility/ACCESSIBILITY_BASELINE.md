# Accessibility Baseline

This document defines minimum accessibility requirements for RAINBOWSMOKE brand usage.

## Policy
- WCAG target: AA minimum for all public-facing digital surfaces.
- Preferred level: AAA for key reading surfaces where feasible.

## Requirements
1. Contrast
- Body text contrast must meet AA minimum.
- UI controls and focus indicators must meet AA minimum.
- Color alone must not carry critical meaning.

2. Typography
- Body text should remain legible at common device sizes.
- Avoid decorative display fonts for long passages.
- Preserve line-height and spacing for readability.

3. Motion
- Avoid rapid flashing and high-frequency strobing.
- Provide reduced-motion alternatives for animated effects.
- Keep loops supportive, not distracting.

4. Interaction
- Keyboard navigation must be preserved in digital interfaces.
- Focus state must be visible and consistent.
- Error states must include text, not color alone.

## Next Implementation Tasks
1. Add min font-size and spacing tables by channel.
2. Add motion timing guidance and reduced-motion examples.

## Approved Color Contrast Pairings

Text must meet 4.5:1 (AA body) or 3:1 (AA large text / UI) against its background.

| Text color | Background | Ratio (approx.) | WCAG level | Notes |
|---|---|---|---|---|
| #FFFFFF white | #004CFF Pride blue | 4.9:1 | AA | Primary button / nav use |
| #FFFFFF white | #400098 Pride violet | 7.8:1 | AAA | High-contrast hero |
| #FFFFFF white | #008026 Pride green | 4.5:1 | AA | Use at large sizes only |
| #FFFFFF white | #0903A6 Royalty dark blue | 9.1:1 | AAA | Preferred for CTA surfaces |
| #FFFFFF white | #0F1AF2 Royalty mid blue | 6.4:1 | AAA | Strong CTA pairing |
| #000000 black | #FFED00 Pride yellow | 15.3:1 | AAA | High-visibility alert text |
| #000000 black | #FCA8D8 Cotton Candy pink | 6.2:1 | AAA | Community / soft surface text |
| #000000 black | #ABCDF3 Cotton Candy blue | 7.1:1 | AAA | Light surface body text |
| #000000 black | #F2F2F2 Royalty off-white | 18.1:1 | AAA | Standard light surface |
| #000000 black | #FFFFFF white | 21:1 | AAA | Default maximum |

## Forbidden Pairings

| Text color | Background | Issue |
|---|---|---|
| #FFED00 Pride yellow | #FFFFFF white | ~1.1:1 — fails all levels |
| #FF8E00 Pride orange | #FFFFFF white | ~2.7:1 — fails AA |
| #FF0000 Pride red | #FFFFFF white | ~3.9:1 — fails AA body text |
| #FF0000 Pride red | #008026 Pride green | ~1.3:1 — fails all levels |
| #FCA8D8 Cotton Candy pink | #FFFFFF white | ~1.8:1 — fails all levels |
| #798BF2 Royalty light | #FFFFFF white | ~3.1:1 — fails AA body text |

> Contrast ratios are approximate. Verify specific use cases with a contrast checker before release.

## Inclusive Language Rules
- Use gender-neutral language by default (they/them when pronoun is unknown)
- Prefer identity-affirming language aligned with LGBTQ+ community standards
- Avoid ableist, sexist, or exclusionary idioms in all copy
- See [verbal-system/TERMINOLOGY_STYLE.md](../verbal-system/TERMINOLOGY_STYLE.md) for brand-specific term guidance
