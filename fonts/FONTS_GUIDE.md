# RainbowSmoke Font System Guide

## Metadata

```json
{
  "brand": "RainbowSmoke",
  "category": "Typography",
  "purpose": "AI-readable and human-readable instructions for the RainbowSmoke brand typography system",
  "last_updated": "2026-08-10",
  "adobe_fonts_projects": [
    {
      "project_id": "ojc8wen",
      "font_families": 29,
      "variations": 44
    },
    {
      "project_id": "gsl6svi",
      "font_families": 5,
      "variations": "variable (see fonts/gsl6svi.md for per-family weight axis ranges)"
    }
  ],
  "integration": {
    "typekit_links": [
      "https://use.typekit.net/ojc8wen.css",
      "https://use.typekit.net/gsl6svi.css"
    ]
  }
}
```

## Overview
This document provides AI-readable and human-readable instructions for the RainbowSmoke brand typography system. All fonts are hosted via Adobe Fonts (Typekit) across two projects.

## Scope Boundary (Canonical Ownership)
- This file is the technical and inventory reference for font families, Typekit projects, and implementation metadata.
- Policy ownership for typography usage, channel scale, and pairing decisions lives in ../visual-system/TYPOGRAPHY_SYSTEM.md.
- If guidance conflicts, follow ../visual-system/TYPOGRAPHY_SYSTEM.md.

**Adobe Fonts Projects (verified against live Typekit CSS 2026-08-10):**
- **Project ID 1:** `ojc8wen` (29 font families, 44 variations) — hosts Le Havre Rounded, Transat, Chennai, Sketchnote Text/Square, Omnes Narrow/Narrow Thin/Pro, Olivita, Backstroke, Perec Scripte Deco, Rig Solid (13 variants), and Elliott's (5 live variants). Absorbed the Rig Solid/Le Havre Rounded/Transat/Elliott's/Perec Scripte Deco roster from `gsl6svi` on 2026-01-07.
- **Project ID 2:** `gsl6svi` (5 variable font families) — repurposed 2026-01-07 to host Xanti Typewriter Variable, Aglet Mono Variable, BioRhyme Variable, Grandstander Variable, and Scatterplot VF. Previously hosted the roster now in `ojc8wen`; before that it replaced the retired `xlr7mdi` project.
- **Retired (no longer served by either project):** `kegger-collegiate`, `kegger-us`, `elliotts-blue-eyeshadow` — see fonts/ojc8wen.md's Retired Families section. Do not use in new work.

**Integration:**
```html
<link rel="stylesheet" href="https://use.typekit.net/ojc8wen.css">
<link rel="stylesheet" href="https://use.typekit.net/gsl6svi.css">
```

---

## Typography Hierarchy

### Tier 1: Primary Fonts (Use Most Often)

#### Transat
**Family:** `transat`
**Fallback:** `sans-serif`
**Available Weights:** Regular (400), Bold (700)
**Available Styles:** Normal, Italic
**Role:** Primary body text, UI labels, forms, paragraphs
**Personality:** Clean, modern, confident, geometric
**Usage Rule:** Default for all body text. If it's longer than one sentence, use Transat.

```css
/* Transat Implementation */
body {
  font-family: "transat", sans-serif;
  font-weight: 400;
}

.body-bold {
  font-family: "transat", sans-serif;
  font-weight: 700;
}

.body-italic {
  font-family: "transat", sans-serif;
  font-weight: 400;
  font-style: italic;
}
```

**AI Instructions:**
- Use for: Body copy, descriptions, captions, UI text, form labels
- Line height: 1.5-1.7 for readability
- Pairs best with: Le Havre Rounded, Omnes Narrow
- Never use: For display headlines or decorative purposes

---

#### Le Havre Rounded
**Family:** `le-havre-rounded`
**Fallback:** `sans-serif`
**Available Weights:** Regular (400), Bold (700)
**Available Styles:** Normal, Italic
**Role:** Secondary body, subheadings, UI elements, cards, navigation
**Personality:** Friendly, human, approachable, rounded, soft
**Usage Rule:** Supports Transat; never replaces it. Use for friendlier tone.

```css
/* Le Havre Rounded Implementation */
h3, h4, h5 {
  font-family: "le-havre-rounded", sans-serif;
  font-weight: 700;
}

.card-title {
  font-family: "le-havre-rounded", sans-serif;
  font-weight: 700;
}

nav a {
  font-family: "le-havre-rounded", sans-serif;
  font-weight: 400;
}
```

**AI Instructions:**
- Use for: Subheadings (h3-h5), card titles, navigation, callouts, buttons
- Creates contrast with Transat's geometric style
- Softens the overall design
- Excellent for accessibility (rounded shapes reduce visual tension)

---

### Tier 2: Headline & Impact Fonts

#### Omnes Narrow (Black)
**Family:** `omnes-narrow`
**Fallback:** `sans-serif`
**Available Weights:** Extra Light (200), Regular (400), Bold (700), Black (900)
**Available Styles:** Italic for weights 200, 400, 700; Normal for 900
**Role:** Page titles, section headers, hero text, main headlines
**Personality:** Bold, modern, condensed, unmistakable, authoritative
**Usage Rule:** One Omnes headline per section. Let it breathe with whitespace.

```css
/* Omnes Narrow Implementation */
h1 {
  font-family: "omnes-narrow", sans-serif;
  font-weight: 900;
  font-size: 3rem;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

.hero-title {
  font-family: "omnes-narrow", sans-serif;
  font-weight: 900;
  text-transform: uppercase;
}
```

**AI Instructions:**
- Use for: H1 tags, page titles, hero sections, primary headings
- Best at large sizes (32px+)
- Use weight 900 (Black) for maximum impact
- Condensed nature allows for longer headlines
- Never stack multiple Omnes headlines close together

---

#### Chennai (Bold)
**Family:** `chennai`
**Fallback:** `sans-serif`
**Available Weights:** Regular (400), Bold (700)
**Available Styles:** Normal, Italic
**Role:** Editorial headers, long-form content, feature sections, article titles
**Personality:** Smart, contemporary, balanced, readable, editorial
**Usage Rule:** Use when Omnes feels too aggressive. Better for content-heavy pages.

```css
/* Chennai Implementation */
.article-title {
  font-family: "chennai", sans-serif;
  font-weight: 700;
  font-size: 2.5rem;
  line-height: 1.2;
}

.section-header {
  font-family: "chennai", sans-serif;
  font-weight: 700;
  font-size: 1.75rem;
}
```

**AI Instructions:**
- Use for: H2 tags, article titles, editorial content, feature headers
- More versatile than Omnes (works at smaller sizes)
- Excellent for content-focused pages (blogs, articles, documentation)
- Pairs beautifully with Transat body text

---

### Tier 3: Display & Statement Fonts (Use Sparingly)

#### Rig Solid (Selected Variants)
**Families:** Multiple (`rig-solid-bold-fill`, `rig-solid-bold-inline`, `rig-solid-medium-outline`, etc.)
**Fallback:** `sans-serif`
**Available Variants:** 13 (Bold Fill, Bold Inline, Bold Halftone, Medium Outline, etc.) — hosted in `ojc8wen` as of 2026-01-07 (previously `gsl6svi`)
**Available Weights:** Light (300), Medium (500), Bold (700), Zero (100)
**Role:** Hero banners, splash pages, posters, campaign graphics
**Personality:** Loud, graphic, confident, eye-catching, impactful
**Usage Rule:** Never mix more than one Rig Solid variant on a single page.

**Approved Variants:**
- `rig-solid-bold-fill` - Primary display use
- `rig-solid-bold-inline` - Outlined bold look
- `rig-solid-medium-outline` - Lighter display option

```css
/* Rig Solid Implementation */
.hero-display {
  font-family: "rig-solid-bold-fill", sans-serif;
  font-weight: 700;
  font-size: 5rem;
  line-height: 0.9;
  text-transform: uppercase;
}

.campaign-header {
  font-family: "rig-solid-bold-inline", sans-serif;
  font-weight: 700;
  font-size: 4rem;
}
```

**AI Instructions:**
- Use for: Major campaigns, hero sections, event graphics, posters
- Extremely bold - requires ample whitespace
- Only use ONE variant per page
- Best at very large sizes (64px+)
- Never use for body text or small text
- High visual impact - use strategically

---

#### Elliott's Collection
**Families:** Multiple (`elliotts-jigsaw-dropshadow`, `elliotts-typhoid-mary-3d-lig`, etc.)
**Fallback:** `sans-serif`
**Available Variants:** 5 (`elliotts-blue-eyeshadow` retired from Adobe Fonts 2026-01-07 — do not use; see fonts/ojc8wen.md Retired Families)
**Weight:** All at 400
**Role:** One-off moments, art drops, social headers, special features
**Personality:** Artistic, unique, expressive, vintage, playful
**Usage Rule:** If you use Elliott's, everything else goes quiet. Maximum one use per design.

**Approved Variants:**
- `elliotts-jigsaw-dropshadow` - 3D puzzle effect

**Other Variants (Use with Caution):**
- `elliotts-typhoid-mary-3d-lig` - 3D light effect
- `elliotts-typhoid-mary-3d-dar` - 3D dark effect
- `elliotts-venus-d-outlined` - Outlined display
- `elliotts-venus-dioxide` - Solid display

```css
/* Elliott's Implementation */
.special-feature {
  font-family: "elliotts-jigsaw-dropshadow", sans-serif;
  font-weight: 400;
  font-size: 4rem;
  text-align: center;
}

.social-header {
  font-family: "elliotts-jigsaw-dropshadow", sans-serif;
  font-weight: 400;
  font-size: 3rem;
}
```

**AI Instructions:**
- Use for: Special campaigns, social media graphics, event-specific designs
- Extremely stylized - dominates the design
- Only use once per design (one Elliott's variant total)
- All other typography should be minimal when Elliott's is present
- Not suitable for accessibility-first contexts

---

### Tier 4: Accent & Expressive Fonts

#### Sketchnote Text
**Family:** `sketchnote-text`
**Fallback:** `sans-serif`
**Available Weights:** Regular (400), Bold (700)
**Available Styles:** Normal, Italic (only for Regular)
**Role:** Pull quotes, captions, playful microcopy, annotations
**Personality:** Human, handwritten, expressive, informal, friendly
**Usage Rule:** Use for personality, not for primary content.

```css
/* Sketchnote Text Implementation */
blockquote {
  font-family: "sketchnote-text", sans-serif;
  font-weight: 400;
  font-size: 1.25rem;
  font-style: italic;
}

.annotation {
  font-family: "sketchnote-text", sans-serif;
  font-weight: 400;
  font-size: 0.875rem;
}

.playful-cta {
  font-family: "sketchnote-text", sans-serif;
  font-weight: 700;
}
```

**AI Instructions:**
- Use for: Blockquotes, captions, annotations, personality touches
- Adds human warmth to digital designs
- Works well in small doses
- Pairs well with clean fonts like Transat
- Not for body text or critical UI

---

#### Olivita (Italic)
**Family:** `olivita`
**Fallback:** `sans-serif`
**Available Weights:** Regular (400)
**Available Styles:** Normal, Italic
**Role:** Pull quotes, poetic lines, emphasis, testimonials
**Personality:** Smooth, expressive, intimate, elegant, flowing
**Usage Rule:** Use italic variant for emphasis and expression.

```css
/* Olivita Implementation */
.pull-quote {
  font-family: "olivita", sans-serif;
  font-weight: 400;
  font-style: italic;
  font-size: 1.5rem;
  line-height: 1.4;
}

.testimonial {
  font-family: "olivita", sans-serif;
  font-weight: 400;
  font-style: italic;
}
```

**AI Instructions:**
- Use for: Testimonials, pull quotes, emphasis, poetic content
- Always use italic for best effect
- Creates emotional connection
- Excellent for human stories and personal content
- Use sparingly for maximum impact

---

### Tier 5: Restricted Fonts (Situational Use Only)

#### Retired: Kegger Collegiate / Kegger US
`kegger-collegiate` and `kegger-us` were retired from Adobe Fonts on 2026-01-07 — neither family is served by `ojc8wen` or `gsl6svi` anymore, and neither has a `.cclibs` presence. **Do not use.** For sports/athletic/retro contexts, use Backstroke instead (below). See fonts/ojc8wen.md's Retired Families section for the full record.

---

#### Backstroke
**Family:** `backstroke`
**Fallback:** `sans-serif`
**Weight:** Regular (400)
**Role:** Athletic graphics, brush-style headings, energetic displays
**Usage Rule:** Athletic contexts only

```css
.athletic-header {
  font-family: "backstroke", sans-serif;
  font-weight: 400;
  text-transform: uppercase;
}
```

---

#### Perec Scripte Deco
**Family:** `perec-scripte-deco`
**Fallback:** `sans-serif`
**Weight:** Regular (400)
**Role:** Logo lockups, special marks, decorative headers
**Usage Rule:** Special occasions only - decorative script

```css
.logo-script {
  font-family: "perec-scripte-deco", sans-serif;
  font-weight: 400;
  font-size: 2rem;
}
```

---

#### Sketchnote Square
**Family:** `sketchnote-square`
**Fallback:** `sans-serif`
**Weight:** Regular (400)
**Role:** Decorative headings, playful displays (not body text)
**Usage Rule:** Display only, never for body text

```css
.decorative-heading {
  font-family: "sketchnote-square", sans-serif;
  font-weight: 400;
  font-size: 2.5rem;
}
```

---

#### Omnes Narrow Thin
**Family:** `omnes-narrow-thin`
**Fallback:** `sans-serif`
**Weight:** Extra Light (200)
**Style:** Italic only
**Role:** Ultra-light elegant text, luxury contexts
**Usage Rule:** Use sparingly for elegant, minimal designs

```css
.elegant-subheading {
  font-family: "omnes-narrow-thin", sans-serif;
  font-weight: 200;
  font-style: italic;
  font-size: 1.5rem;
  letter-spacing: 0.1em;
}
```

---

#### Omnes Pro
**Family:** `omnes-pro`
**Fallback:** `sans-serif`
**Weight:** Medium (500)
**Role:** Professional body text alternative
**Usage Rule:** Use when slightly heavier weight needed than Transat

```css
.professional-text {
  font-family: "omnes-pro", sans-serif;
  font-weight: 500;
}
```

---

### Tier 6: New / Unassigned Fonts (Pending Brand Role Decision)

Five variable font families were added to `gsl6svi` on 2026-01-07 (see fonts/gsl6svi.md for full detail) and to `RAINBOWSMOKE.cclibs`, but **no formal brand role has been assigned yet**. Treat these as available-but-undecided — same status as `pride_extended` in colors/pride.md. Do not build canonical UI patterns on them until visual-system/TYPOGRAPHY_SYSTEM.md records a decision; open item tracked in governance/OPEN_QUESTIONS.md.

- **Xanti Typewriter Variable** (`xanti-typewriter-variable`, CAST / Gianluca Sandrone) — weight 25–900, normal + italic. Typewriter/monospace character.
- **Aglet Mono Variable** (`aglet-mono-variable`, XYZ Type / Jesse Ragan) — weight 200–900, normal + italic. Clean monospace.
- **BioRhyme Variable** (`biorhyme-variable`, Google) — weight 200–800, normal only. Slab-serif display.
- **Grandstander Variable** (`grandstander-variable`, Google) — weight 100–900, normal + italic. Rounded, playful.
- **Scatterplot VF** (`scatterplot-vf`, CAST / Giulio Galli) — weight 300–900, normal only. Experimental display.

```css
/* Reference only — not yet an approved brand pairing */
font-family: "xanti-typewriter-variable", sans-serif;
font-family: "aglet-mono-variable", sans-serif;
font-family: "biorhyme-variable", sans-serif;
font-family: "grandstander-variable", sans-serif;
font-family: "scatterplot-vf", sans-serif;
```

---

## Approved Font Pairings

### Default UI Stack (Most Common)
```css
:root {
  --font-heading: "omnes-narrow", sans-serif;
  --font-body: "transat", sans-serif;
  --font-ui: "le-havre-rounded", sans-serif;
}

h1, h2 {
  font-family: var(--font-heading);
  font-weight: 900;
}

body, p {
  font-family: var(--font-body);
  font-weight: 400;
  line-height: 1.6;
}

button, nav a, .card-title {
  font-family: var(--font-ui);
  font-weight: 700;
}
```

---

### Editorial / Blog Stack
```css
:root {
  --font-editorial-heading: "chennai", sans-serif;
  --font-editorial-body: "transat", sans-serif;
  --font-editorial-quote: "olivita", sans-serif;
}

.article-title {
  font-family: var(--font-editorial-heading);
  font-weight: 700;
  font-size: 2.5rem;
}

.article-body {
  font-family: var(--font-editorial-body);
  font-weight: 400;
  font-size: 1.125rem;
  line-height: 1.7;
}

blockquote {
  font-family: var(--font-editorial-quote);
  font-weight: 400;
  font-style: italic;
  font-size: 1.5rem;
}
```

---

### Hero / Campaign Stack
```css
:root {
  --font-campaign-hero: "rig-solid-bold-fill", sans-serif;
  --font-campaign-support: "le-havre-rounded", sans-serif;
  --font-campaign-body: "transat", sans-serif;
}

.hero-text {
  font-family: var(--font-campaign-hero);
  font-weight: 700;
  font-size: 5rem;
  line-height: 0.9;
  text-transform: uppercase;
}

.hero-subheading {
  font-family: var(--font-campaign-support);
  font-weight: 400;
  font-size: 1.5rem;
}

.fine-print {
  font-family: var(--font-campaign-body);
  font-weight: 400;
  font-size: 0.875rem;
}
```

---

## AI Implementation Guidelines

### Font Selection Decision Tree

```
START: What type of content?

├─ BODY TEXT (paragraphs, descriptions)
│  └─ Use: Transat (400)
│     - Line height: 1.5-1.7
│     - Font size: 16-18px base
│
├─ PRIMARY HEADLINE (H1, hero)
│  ├─ Campaign/Event? → Rig Solid Bold Fill (700)
│  ├─ Editorial? → Chennai Bold (700)
│  └─ Default → Omnes Narrow Black (900)
│
├─ SECONDARY HEADLINE (H2-H3)
│  ├─ Formal? → Chennai Bold (700)
│  └─ Friendly → Le Havre Rounded Bold (700)
│
├─ UI ELEMENTS (buttons, nav, cards)
│  └─ Use: Le Havre Rounded (400 or 700)
│
├─ SPECIAL DISPLAY (one-off, artistic)
│  ├─ Maximum impact → Elliott's Collection
│  └─ Graphic/bold → Rig Solid variants
│
├─ QUOTES/EMPHASIS
│  ├─ Playful → Sketchnote Text (400 italic)
│  └─ Elegant → Olivita (400 italic)
│
└─ SPORTS/ATHLETIC
   └─ Use: Backstroke (Kegger Collegiate/US retired from Adobe Fonts 2026-01-07)
```

---

### Responsive Typography Scale

```css
/* Mobile First */
:root {
  --text-xs: 0.75rem;     /* 12px */
  --text-sm: 0.875rem;    /* 14px */
  --text-base: 1rem;      /* 16px */
  --text-lg: 1.125rem;    /* 18px */
  --text-xl: 1.25rem;     /* 20px */
  --text-2xl: 1.5rem;     /* 24px */
  --text-3xl: 1.875rem;   /* 30px */
  --text-4xl: 2.25rem;    /* 36px */
  --text-5xl: 3rem;       /* 48px */
  --text-6xl: 3.75rem;    /* 60px */
  --text-7xl: 4.5rem;     /* 72px */
}

/* Tablet & Desktop */
@media (min-width: 768px) {
  :root {
    --text-5xl: 4rem;     /* 64px */
    --text-6xl: 5rem;     /* 80px */
    --text-7xl: 6rem;     /* 96px */
  }
}
```

---

### Accessibility Requirements

#### Minimum Font Sizes
- **Body text:** 16px minimum (1rem)
- **Small text:** 14px minimum (0.875rem)
- **Large text:** 18px+ (1.125rem+)

#### Contrast Ratios (WCAG AA)
- **Normal text (< 18px):** 4.5:1 minimum
- **Large text (≥ 18px or ≥ 14px bold):** 3:1 minimum

#### Line Height Recommendations
- **Body text:** 1.5-1.7
- **Headlines:** 1.1-1.3
- **UI elements:** 1.2-1.4

#### Letter Spacing
- **Headlines (large):** -0.02em to -0.04em (tighter)
- **Body text:** 0 (default)
- **Uppercase text:** +0.05em to +0.1em (wider)
- **Small text:** +0.01em to +0.02em (slightly wider)

---

## Complete Font Reference

### Quick Copy-Paste Font Families

```css
/* Primary Fonts */
font-family: "transat", sans-serif;
font-family: "le-havre-rounded", sans-serif;

/* Headline Fonts */
font-family: "omnes-narrow", sans-serif;
font-family: "chennai", sans-serif;

/* Display Fonts */
font-family: "rig-solid-bold-fill", sans-serif;
font-family: "rig-solid-bold-inline", sans-serif;
font-family: "rig-solid-medium-outline", sans-serif;

/* Elliott's Collection (elliotts-blue-eyeshadow retired 2026-01-07, do not use) */
font-family: "elliotts-jigsaw-dropshadow", sans-serif;

/* Accent Fonts */
font-family: "sketchnote-text", sans-serif;
font-family: "olivita", sans-serif;

/* Restricted/Situational (kegger-collegiate, kegger-us retired 2026-01-07, do not use) */
font-family: "backstroke", sans-serif;
font-family: "perec-scripte-deco", sans-serif;
font-family: "sketchnote-square", sans-serif;
font-family: "omnes-narrow-thin", sans-serif;
font-family: "omnes-pro", sans-serif;

/* New / unassigned (gsl6svi, added 2026-01-07 — pending brand role, see Tier 6) */
font-family: "xanti-typewriter-variable", sans-serif;
font-family: "aglet-mono-variable", sans-serif;
font-family: "biorhyme-variable", sans-serif;
font-family: "grandstander-variable", sans-serif;
font-family: "scatterplot-vf", sans-serif;
```

---

### Font Weights Reference

```css
/* Standard Weights */
font-weight: 100; /* Rig Solid Zero variants; low end of Grandstander Variable's axis */
font-weight: 200; /* Extra Light (Omnes Narrow, Omnes Narrow Thin); low end of Aglet Mono / BioRhyme Variable axes */
font-weight: 300; /* Light (Rig Solid Light variants); low end of Scatterplot VF axis */
font-weight: 400; /* Regular/Normal (Most fonts) */
font-weight: 500; /* Medium (Omnes Pro, Rig Solid Medium) */
font-weight: 600; /* Semi-Bold (Not available in static-cut fonts; within all 5 new variable-font axes) */
font-weight: 700; /* Bold (Most fonts) */
font-weight: 800; /* Extra Bold; top of BioRhyme Variable's axis */
font-weight: 900; /* Black (Omnes Narrow); top of Aglet Mono / Grandstander / Scatterplot VF axes */

/* Xanti Typewriter Variable's axis (25–800) extends below 100 — see fonts/gsl6svi.md */
```

---

## Brand Rules Summary

**ALWAYS:**
- Use Transat for body text
- Pair Transat with Le Havre Rounded for UI
- Use Omnes Narrow Black for main headlines
- Test accessibility (contrast, size, readability)
- Limit to 2-3 font families per page

**NEVER:**
- Mix multiple Rig Solid variants on one page
- Use display fonts for body text
- Use more than one Elliott's font per design
- Ignore minimum font size requirements
- Create walls of text in decorative fonts
- Reference `kegger-collegiate`, `kegger-us`, or `elliotts-blue-eyeshadow` — all three are retired from Adobe Fonts and will silently fall back to the generic fallback

**IF YOU'RE UNSURE:**
- Default to Transat + Le Havre Rounded + Omnes Narrow
- This trio covers 90% of use cases
- Add accent fonts only when needed for specific effect
- Tier 6 fonts (Xanti Typewriter, Aglet Mono, BioRhyme, Grandstander, Scatterplot VF) are new and unassigned — don't build canonical patterns on them yet

---

*Last Updated: August 10, 2026*
*Brand: RainbowSmoke*
*Typography System Version: 2.0 (live-Typekit-kit-aligned)*
*Adobe Fonts Projects: ojc8wen (29 families / 44 variations), gsl6svi (5 variable families)*