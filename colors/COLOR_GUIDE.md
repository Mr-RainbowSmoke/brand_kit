# RainbowSmoke Color Palette Guide

## Metadata

```json
{
  "brand": "RainbowSmoke",
  "category": "Color System",
  "purpose": "AI-readable and human-readable instructions for the RainbowSmoke brand color palettes representing pride flags",
  "last_updated": "2026-01-05",
  "palettes": [
    {"name": "pride", "colors": 6, "file": "pride.md"},
    {"name": "demiboy", "colors": 4, "file": "demiboy.md"},
    {"name": "demisexual", "colors": 4, "file": "demisexual.md"}
  ]
}
```

## Overview
This document provides AI-readable and human-readable instructions for the RainbowSmoke brand color palettes. Each palette represents a specific pride flag with carefully selected colors for inclusive design.

---

## Color Palettes

### Pride (Traditional Rainbow)
**File:** `pride`  
**Colors:** 6  
**Usage:** Primary brand palette, celebration, diversity, full spectrum representation

```json
{
  "color1": "#FF0018",  // Red - Life, energy, passion
  "color2": "#FFA52C",  // Orange - Healing, warmth, community
  "color3": "#FFFF41",  // Yellow - Sunlight, joy, optimism
  "color4": "#008018",  // Green - Nature, growth, harmony
  "color5": "#0000F9",  // Blue - Serenity, peace, trust
  "color6": "#86007D"   // Purple - Spirit, creativity, royalty
}
```

**Color Roles:**
- `color1` (Red): Call-to-action buttons, alerts, high-energy elements
- `color2` (Orange): Secondary CTAs, warm accents, community features
- `color3` (Yellow): Highlights, warnings, attention-grabbing elements
- `color4` (Green): Success states, positive feedback, natural elements
- `color5` (Blue): Links, informational elements, trust indicators
- `color6` (Purple): Premium features, creative content, spiritual elements

---

### Demiboy
**File:** `demiboy`  
**Colors:** 4  
**Usage:** Inclusive representation, neutral to cool tones, subtle gradient effects

```json
{
  "color1": "#7F7F7F",  // Grey - Partial connection, neutrality
  "color2": "#C4C4C4",  // Light Grey - Transition, ambiguity
  "color3": "#FFFFFF",  // White - Clarity, openness, full spectrum
  "color4": "#9AD9EB"   // Light Blue - Masculinity (partial), tranquility
}
```

**Color Roles:**
- `color1` (Grey): Base backgrounds, neutral UI elements, dividers
- `color2` (Light Grey): Secondary backgrounds, subtle highlights
- `color3` (White): Text on dark backgrounds, clean spaces, cards
- `color4` (Light Blue): Primary accents, links, interactive elements

**Accessibility Notes:**
- Grey tones require careful contrast checking
- Use `color4` (Light Blue) for important interactive elements
- Pair `color1`/`color2` with dark text for readability

---

### Demisexual
**File:** `demisexual`  
**Colors:** 4  
**Usage:** High contrast design, formal contexts, accessibility-first applications

```json
{
  "color1": "#000000",  // Black - Asexuality, foundation, strength
  "color2": "#808080",  // Grey - Grey-sexuality, middle ground
  "color3": "#FFFFFF",  // White - Allosexuality, clarity, completeness
  "color4": "#800080"   // Purple - Community, connection, bonds
}
```

**Color Roles:**
- `color1` (Black): Text, strong borders, high-impact elements
- `color2` (Grey): Secondary text, disabled states, subtle elements
- `color3` (White): Backgrounds, negative space, breathing room
- `color4` (Purple): Brand accents, active states, emphasis

**Accessibility Notes:**
- Excellent contrast ratios (Black/White)
- Purple passes WCAG AA on white backgrounds
- Ideal for accessibility-focused designs

---

## Implementation Guidelines

### For AI/Code Generation:
```typescript
// Import pattern
import { pride, demiboy, demisexual } from './rainbowsmoke/colors';

// Access individual colors
const primaryRed = pride.color1;
const accentBlue = demiboy.color4;
const brandPurple = demisexual.color4;

// Generate gradients
const prideGradient = `linear-gradient(to right, ${pride.color1}, ${pride.color2}, ${pride.color3}, ${pride.color4}, ${pride.color5}, ${pride.color6})`;
```

### Color Selection Logic:
- **High Energy/CTA:** Use Pride `color1` (Red) or `color2` (Orange)
- **Trust/Information:** Use Pride `color5` (Blue) or Demiboy `color4` (Light Blue)
- **Success/Positive:** Use Pride `color4` (Green)
- **Neutral/Subtle:** Use Demiboy `color1`/`color2` (Greys)
- **Brand/Premium:** Use Demisexual `color4` (Purple)
- **High Contrast:** Use Demisexual palette

### Gradient Combinations:
```css
/* Pride Spectrum */
background: linear-gradient(90deg, #FF0018, #FFA52C, #FFFF41, #008018, #0000F9, #86007D);

/* Demiboy Soft Gradient */
background: linear-gradient(135deg, #7F7F7F, #C4C4C4, #FFFFFF, #9AD9EB);

/* Demisexual Bold Gradient */
background: linear-gradient(180deg, #000000, #808080, #FFFFFF, #800080);
```

### Accessibility Requirements:
- **Text on Pride Colors:** Use white text on all colors except `color3` (Yellow)
- **Text on Demiboy Colors:** Use dark text (#333) on all colors
- **Text on Demisexual Colors:** 
  - White text on `color1` (Black), `color2` (Grey), `color4` (Purple)
  - Black text on `color3` (White)

### Color Blindness Considerations:
- **Pride:** May be difficult for red-green colorblind users; use with labels
- **Demiboy:** Safe for most color vision deficiencies
- **Demisexual:** Excellent for all color vision types (high contrast)

---

## Semantic Color Mapping

### Status Colors:
```json
{
  "success": "#008018",     // Pride color4 (Green)
  "warning": "#FFFF41",     // Pride color3 (Yellow)
  "error": "#FF0018",       // Pride color1 (Red)
  "info": "#0000F9",        // Pride color5 (Blue)
  "neutral": "#808080"      // Demisexual color2 (Grey)
}
```

### UI Element Mapping:
```json
{
  "primary": "#0000F9",     // Pride Blue
  "secondary": "#86007D",   // Pride Purple
  "accent": "#9AD9EB",      // Demiboy Light Blue
  "background": "#FFFFFF",  // White
  "surface": "#C4C4C4",     // Demiboy Light Grey
  "border": "#7F7F7F",      // Demiboy Grey
  "text": "#000000",        // Demisexual Black
  "textSecondary": "#808080" // Grey
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
- Order represents visual sequence (left to right, top to bottom in flag)

---

## Brand Usage Rules

1. **Primary Palette:** Use Pride for celebrations, events, and high-visibility campaigns
2. **Secondary Palettes:** Use Demiboy/Demisexual for specific community representation
3. **Never modify hex values** - use as-is for brand consistency
4. **Combine palettes thoughtfully** - consider color theory and cultural meaning
5. **Test accessibility** - always check contrast ratios for text readability

---

## Quick Reference

| Palette | Colors | Primary Use | Contrast |
|---------|--------|-------------|----------|
| Pride | 6 | Full spectrum, celebrations | Medium |
| Demiboy | 4 | Subtle, cool tones | Low-Medium |
| Demisexual | 4 | High contrast, formal | High |

---

*Last Updated: January 4, 2026*  
*Brand: RainbowSmoke*  
*Color System Version: 1.0*
