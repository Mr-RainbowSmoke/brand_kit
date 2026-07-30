# RainbowSmoke Color Palette Guide

## Metadata

```json
{
  "brand": "RAINBOWSMOKE",
  "category": "Color System",
  "purpose": "AI-readable and human-readable instructions for the RainbowSmoke brand color palettes",
  "last_updated": "2026-07-29",
  "master_source": {
    "type": "adobe-cclibs",
    "file": "RAINBOWSMOKE.cclibs",
    "sha256": "67b45ed492de2d94a8e1ba632799175c6171cb66c8fd2f2ab18c863039ef9f14",
    "confirmed": "2026-07-29"
  },
  "palettes": [
    {"name": "pride", "colors": 6, "file": "pride.md", "role": "primary"},
    {"name": "demiboy", "colors": 4, "file": "demiboy.md", "role": "identity representation"},
    {"name": "demisexual", "colors": 4, "file": "demisexual.md", "role": "identity representation"},
    {"name": "royalty", "colors": 5, "file": "royalty.md", "role": "secondary — blue-forward/premium"},
    {"name": "Cotton Candy", "colors": 5, "file": "cotton-candy.md", "role": "secondary — soft/celebratory"}
  ]
}
```

## Overview
This document provides AI-readable and human-readable instructions for the RainbowSmoke brand color palettes. `RAINBOWSMOKE.cclibs` (Adobe CC Library) is the confirmed master source of truth for all hex values — this file and its sibling palette files are kept in sync with it. See `../brand.manifest.json` and `../governance/SOURCE_CONFIDENCE.md` for full provenance.

---

## Color Palettes

### Pride (Traditional Rainbow)
**File:** `pride.md`
**Colors:** 6
**Usage:** Primary brand palette, celebrations, diversity, full spectrum representation

```json
{
  "color1": "#FF0000",  // Red - Life, energy, passion
  "color2": "#FF8E00",  // Orange - Healing, warmth, community
  "color3": "#FFED00",  // Yellow - Sunlight, joy, optimism
  "color4": "#008026",  // Green - Nature, growth, harmony
  "color5": "#004CFF",  // Blue - Serenity, peace, trust
  "color6": "#400098"   // Purple - Spirit, creativity, royalty
}
```

**Color Roles:**
- `color1` (Red): Call-to-action buttons, alerts, high-energy elements
- `color2` (Orange): Secondary CTAs, warm accents, community features
- `color3` (Yellow): Highlights, warnings, attention-grabbing elements
- `color4` (Green): Success states, positive feedback, natural elements
- `color5` (Blue): Links, informational elements, trust indicators — the brand deliberately skews blue-forward (~40% blue, ~10% purple across compositions)
- `color6` (Purple): Premium features, creative content, spiritual elements — capped as an accent, not dominant

---

### Demiboy
**File:** `demiboy.md`
**Colors:** 4
**Usage:** Inclusive representation, neutral to cool tones, subtle gradient effects

```json
{
  "color1": "#7F7F7F",  // Grey - Partial connection, neutrality
  "color2": "#C4C4C4",  // Light Grey - Transition, ambiguity
  "color3": "#9DD7EA",  // Light Blue - Masculinity (partial), tranquility
  "color4": "#FFFFFF"   // White - Clarity, openness, full spectrum
}
```

**Color Roles:**
- `color1` (Grey): Base backgrounds, neutral UI elements, dividers
- `color2` (Light Grey): Secondary backgrounds, subtle highlights
- `color3` (Light Blue): Primary accents, links, interactive elements
- `color4` (White): Text on dark backgrounds, clean spaces, cards

**Accessibility Notes:**
- Grey tones require careful contrast checking
- Use `color3` (Light Blue) for important interactive elements
- Pair `color1`/`color2` with dark text for readability

---

### Demisexual
**File:** `demisexual.md`
**Colors:** 4
**Usage:** High contrast design, formal contexts, accessibility-first applications

```json
{
  "color1": "#000000",  // Black - Asexuality, foundation, strength
  "color2": "#FFFFFF",  // White - Allosexuality, clarity, completeness
  "color3": "#6E0070",  // Purple - Community, connection, bonds
  "color4": "#D2D2D2"   // Grey - Grey-sexuality, middle ground
}
```

**Color Roles:**
- `color1` (Black): Text, strong borders, high-impact elements
- `color2` (White): Backgrounds, negative space, breathing room
- `color3` (Purple): Brand accents, active states, emphasis
- `color4` (Grey): Secondary text, disabled states, subtle elements

**Accessibility Notes:**
- Excellent contrast ratios (Black/White)
- Purple passes WCAG AA on white backgrounds
- Ideal for accessibility-focused designs

---

### Royalty (Secondary)
**File:** `royalty.md`
**Colors:** 5
**Usage:** Premium/campaign moments, blue-forward emphasis pieces, dark-mode UI accents

```json
{
  "color1": "#0903A6",
  "color2": "#0F1AF2",
  "color3": "#1B3BF2",
  "color4": "#798BF2",
  "color5": "#F2F2F2"
}
```

A near-monochromatic blue palette. Use to reinforce the brand's blue-forward Pride positioning without touching the full spectrum.

---

### Cotton Candy (Secondary)
**File:** `cotton-candy.md`
**Colors:** 5
**Usage:** Lighter/softer contexts — community spotlights, merch, seasonal or celebratory content

```json
{
  "color1": "#FCA8D8",
  "color2": "#A1A8E5",
  "color3": "#B2B3ED",
  "color4": "#ABCDF3",
  "color5": "#D2DFF2"
}
```

A deliberate soft-pastel contrast to the brand's usual bold/dark treatment.

---

## Implementation Guidelines

### For AI/Code Generation:
```typescript
// Import pattern
import { pride, demiboy, demisexual, royalty, cottonCandy } from './rainbowsmoke/colors';

// Access individual colors
const primaryRed = pride.color1;
const accentBlue = demiboy.color3;
const brandPurple = demisexual.color3;

// Generate gradients
const prideGradient = `linear-gradient(to right, ${pride.color1}, ${pride.color2}, ${pride.color3}, ${pride.color4}, ${pride.color5}, ${pride.color6})`;
```

### Color Selection Logic:
- **High Energy/CTA:** Use Pride `color1` (Red) or `color2` (Orange)
- **Trust/Information:** Use Pride `color5` (Blue) or Demiboy `color3` (Light Blue)
- **Success/Positive:** Use Pride `color4` (Green)
- **Neutral/Subtle:** Use Demiboy `color1`/`color2` (Greys)
- **Brand/Premium:** Use Demisexual `color3` (Purple) or the Royalty palette
- **High Contrast:** Use Demisexual palette
- **Soft/Celebratory:** Use Cotton Candy palette

### Gradient Combinations:
```css
/* Pride Spectrum */
background: linear-gradient(90deg, #FF0000, #FF8E00, #FFED00, #008026, #004CFF, #400098);

/* Demiboy Soft Gradient */
background: linear-gradient(135deg, #7F7F7F, #C4C4C4, #9DD7EA, #FFFFFF);

/* Demisexual Bold Gradient */
background: linear-gradient(180deg, #000000, #FFFFFF, #6E0070, #D2D2D2);

/* Royalty Gradient */
background: linear-gradient(90deg, #0903A6, #0F1AF2, #1B3BF2, #798BF2, #F2F2F2);

/* Cotton Candy Gradient */
background: linear-gradient(90deg, #FCA8D8, #A1A8E5, #B2B3ED, #ABCDF3, #D2DFF2);
```

### Accessibility Requirements:
- **Text on Pride Colors:** Use white text on all colors except `color3` (Yellow)
- **Text on Demiboy Colors:** Use dark text (#333) on all colors except `color1`/`color3` where white also works
- **Text on Demisexual Colors:**
  - White text on `color1` (Black), `color3` (Purple)
  - Black text on `color2` (White), `color4` (Grey)

### Color Blindness Considerations:
- **Pride:** May be difficult for red-green colorblind users; use with labels
- **Demiboy:** Safe for most color vision deficiencies
- **Demisexual:** Excellent for all color vision types (high contrast)

---

## Semantic Color Mapping

### Status Colors:
```json
{
  "success": "#008026",     // Pride color4 (Green)
  "warning": "#FFED00",     // Pride color3 (Yellow)
  "error": "#FF0000",       // Pride color1 (Red)
  "info": "#004CFF",        // Pride color5 (Blue)
  "neutral": "#D2D2D2"      // Demisexual color4 (Grey)
}
```

### UI Element Mapping:
```json
{
  "primary": "#004CFF",     // Pride Blue
  "secondary": "#400098",   // Pride Purple
  "accent": "#9DD7EA",      // Demiboy Light Blue
  "background": "#FFFFFF",  // White
  "surface": "#C4C4C4",     // Demiboy Light Grey
  "border": "#7F7F7F",      // Demiboy Grey
  "text": "#000000",        // Demisexual Black
  "textSecondary": "#D2D2D2" // Grey
}
```

---

## Data Format

All color files follow this structure:
```
paletteName: {
  "color1": "#HEXCODE",
  "color2": "#HEXCODE",
  ...
}
```

**Properties:**
- Keys are sequential: `color1`, `color2`, `color3`, etc.
- Values are uppercase hex codes with `#` prefix
- 6-character hex format (no alpha channel)
- Order represents visual sequence (left to right, top to bottom in flag), matching the order in `RAINBOWSMOKE.cclibs`

---

## Brand Usage Rules

1. **Primary Palette:** Use Pride for celebrations, events, and high-visibility campaigns
2. **Identity Palettes:** Use Demiboy/Demisexual for specific community representation
3. **Secondary Palettes:** Use Royalty for premium/blue-forward moments, Cotton Candy for soft/celebratory contexts
4. **Never modify hex values** - use as-is for brand consistency; `RAINBOWSMOKE.cclibs` governs
5. **Combine palettes thoughtfully** - consider color theory and cultural meaning
6. **Test accessibility** - always check contrast ratios for text readability

---

## Quick Reference

| Palette | Colors | Primary Use | Contrast |
|---------|--------|-------------|----------|
| Pride | 6 | Full spectrum, celebrations | Medium |
| Demiboy | 4 | Subtle, cool tones | Low-Medium |
| Demisexual | 4 | High contrast, formal | High |
| Royalty | 5 | Premium, blue-forward, dark-mode | Medium |
| Cotton Candy | 5 | Soft, celebratory, seasonal | Low |

---

## Known-Resolved History

Prior to 2026-07-29 this file (and its Notion/SharePoint mirrors) documented an older, unrelated hex set (Pride `#FF0018/#FFA52C/#FFFF41/#008018/#0000F9/#86007D`; Demiboy `#7F7F7F/#C4C4C4/#FFFFFF/#9AD9EB`; Demisexual `#000000/#808080/#FFFFFF/#800080`). Those values were superseded once `RAINBOWSMOKE.cclibs` was confirmed by the brand owner as the master source of truth (2026-01-17). This file, `pride.md`, `demiboy.md`, and `demisexual.md` have been updated to match. See `../brand-voice-guidelines.md` for the full discovery/reconciliation trail.

---

*Last Updated: July 29, 2026*
*Brand: RainbowSmoke*
*Color System Version: 2.0 (`.cclibs`-aligned)*