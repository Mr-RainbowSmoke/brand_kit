# Adobe Fonts Project - Font Family Compilation

## Metadata

```json
{
  "project_id": "gsl6svi",
  "project_type": "Adobe Fonts (Typekit)",
  "brand": "RainbowSmoke",
  "total_families": 5,
  "total_variations": "variable (see per-family weight axis ranges below)",
  "typekit_url": "https://use.typekit.net/gsl6svi.css",
  "last_updated": "2026-08-10"
}
```

**Project ID**: gsl6svi

## Repurposed Project (read this first)

As of 2026-01-07, `gsl6svi` no longer hosts Le Havre Rounded, Transat, Rig Solid, Elliott's, or Perec Scripte Deco. Those families were consolidated into `ojc8wen` (see `ojc8wen.md`) — `gsl6svi` was repurposed to host 5 brand-new **variable** font families instead. This mirrors the earlier `xlr7mdi` → `gsl6svi` migration (see `xlr7mdi.md.deprecated`); this is the second reassignment of this project ID.

These 5 families correspond directly to 8 font elements added to `RAINBOWSMOKE.cclibs` on 2026-01-07 (Xanti Typewriter VF ExtraBold/Italic, Aglet Mono VF Regular/Italic, BioRhyme ExtraBold, Grandstander Thin/Thin Italic, Scatterplot VF Light) and are already itemized in `../brand.manifest.json`'s `typography.fonts` array with matching `typekitFontId` values.

**None of these 5 fonts have an assigned brand role yet.** See `../governance/OPEN_QUESTIONS.md`. Treat them as available-but-undecided, the same way `pride_extended` is documented in `../colors/pride.md` as adopted-into-the-library but not yet adopted-into-use.

## Font Families Overview

This Adobe Fonts project includes **5 variable font families**. Each is a single variable-font file whose weight axis spans a range (not discrete static cuts) — implementers should use `font-variation-settings` or a specific numeric `font-weight` within the declared range rather than assuming fixed steps like 400/700.

---

## 1. Xanti Typewriter Variable
**Family Name**: `xanti-typewriter-variable`
**Foundry**: CAST — Gianluca Sandrone
**Weight axis**: 25–800
**Styles**: Normal, Italic

- CSS: `font-family: "xanti-typewriter-variable", sans-serif; font-weight: 25 800; font-style: normal;`
- CSS (italic): `font-family: "xanti-typewriter-variable", sans-serif; font-weight: 25 800; font-style: italic;`

**Usage Class**: `.tk-xanti-typewriter-variable`

`.cclibs` reference points: "Xanti Typewriter VF ExtraBold" and "Xanti Typewriter VF ExtraBold Italic" (activated instances near the top of the weight range).

---

## 2. Aglet Mono Variable
**Family Name**: `aglet-mono-variable`
**Foundry**: XYZ Type — Jesse Ragan
**Weight axis**: 200–900
**Styles**: Normal, Italic

- CSS: `font-family: "aglet-mono-variable", sans-serif; font-weight: 200 900; font-style: normal;`
- CSS (italic): `font-family: "aglet-mono-variable", sans-serif; font-weight: 200 900; font-style: italic;`

**Usage Class**: `.tk-aglet-mono-variable`

`.cclibs` reference points: "Aglet Mono VF Regular" and "Aglet Mono VF Italic".

---

## 3. BioRhyme Variable
**Family Name**: `biorhyme-variable`
**Foundry**: Google
**Weight axis**: 200–800
**Styles**: Normal only

- CSS: `font-family: "biorhyme-variable", sans-serif; font-weight: 200 800; font-style: normal;`

**Usage Class**: `.tk-biorhyme-variable`

`.cclibs` reference point: "BioRhyme ExtraBold" (activated instance near the top of the weight range).

---

## 4. Grandstander Variable
**Family Name**: `grandstander-variable`
**Foundry**: Google
**Weight axis**: 100–900
**Styles**: Normal, Italic

- CSS: `font-family: "grandstander-variable", sans-serif; font-weight: 100 900; font-style: normal;`
- CSS (italic): `font-family: "grandstander-variable", sans-serif; font-weight: 100 900; font-style: italic;`

**Usage Class**: `.tk-grandstander-variable`

`.cclibs` reference points: "Grandstander Thin" and "Grandstander Thin Italic" (activated instances near the bottom of the weight range).

---

## 5. Scatterplot VF
**Family Name**: `scatterplot-vf`
**Foundry**: CAST — Giulio Galli
**Weight axis**: 300–900
**Styles**: Normal only

- CSS: `font-family: "scatterplot-vf", sans-serif; font-weight: 300 900; font-style: normal;`

**Usage Class**: `.tk-scatterplot-vf`

`.cclibs` reference point: "Scatterplot VF Light" (activated instance near the bottom of the weight range).

---

## Quick Reference Table

| Font Family | Foundry / Designer | Weight Axis | Styles | `.cclibs` Activated Instance(s) |
|---|---|---|---|---|
| Xanti Typewriter Variable | CAST / Gianluca Sandrone | 25–800 | Normal, Italic | ExtraBold, ExtraBold Italic |
| Aglet Mono Variable | XYZ Type / Jesse Ragan | 200–900 | Normal, Italic | Regular, Italic |
| BioRhyme Variable | Google | 200–800 | Normal | ExtraBold |
| Grandstander Variable | Google | 100–900 | Normal, Italic | Thin, Thin Italic |
| Scatterplot VF | CAST / Giulio Galli | 300–900 | Normal | Light |

---

## CSS Usage Examples

```css
/* Xanti Typewriter Variable */
.mono-typewriter {
  font-family: "xanti-typewriter-variable", sans-serif;
  font-weight: 700;
}

/* Aglet Mono Variable */
.mono-code {
  font-family: "aglet-mono-variable", sans-serif;
  font-weight: 400;
}

/* BioRhyme Variable */
.serif-display {
  font-family: "biorhyme-variable", sans-serif;
  font-weight: 800;
}

/* Grandstander Variable */
.rounded-playful {
  font-family: "grandstander-variable", sans-serif;
  font-weight: 100;
}

/* Scatterplot VF */
.experimental-display {
  font-family: "scatterplot-vf", sans-serif;
  font-weight: 300;
}
```

### Using Typekit Classes

```html
<div class="tk-xanti-typewriter-variable">Typewriter mono</div>
<div class="tk-aglet-mono-variable">Code / mono UI</div>
<div class="tk-biorhyme-variable">Serif display</div>
<div class="tk-grandstander-variable">Playful rounded</div>
<div class="tk-scatterplot-vf">Experimental display</div>
```

---

## HTML Integration

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adobe Fonts Project - gsl6svi</title>

    <!-- Adobe Fonts Stylesheet -->
    <link rel="stylesheet" href="https://use.typekit.net/gsl6svi.css">

    <style>
        .mono-code {
            font-family: "aglet-mono-variable", sans-serif;
            font-weight: 400;
        }

        .serif-display {
            font-family: "biorhyme-variable", sans-serif;
            font-weight: 800;
        }
    </style>
</head>
<body>
    <p class="mono-code">Monospace code sample.</p>
    <div class="serif-display">SERIF DISPLAY</div>
</body>
</html>
```

---

## Complete Font Family List (Copy-Paste Ready)

```css
font-family: "xanti-typewriter-variable", sans-serif;
font-family: "aglet-mono-variable", sans-serif;
font-family: "biorhyme-variable", sans-serif;
font-family: "grandstander-variable", sans-serif;
font-family: "scatterplot-vf", sans-serif;
```

---

## Notes

- **Total Font Families**: 5, all variable-weight fonts
- **Last Updated**: August 10, 2026
- **License**: Subject to Adobe Typekit Terms of Use
- **Project ID**: gsl6svi
- **Fallback**: All fonts specify `sans-serif` as fallback
- **Migration note**: This project ID previously hosted Le Havre Rounded, Transat, Rig Solid (13 variants), Elliott's (6 variants), and Perec Scripte Deco — as of 2026-01-07 those live in `ojc8wen` instead (see `ojc8wen.md`). `gsl6svi` was itself the successor to the retired `xlr7mdi` project (see `xlr7mdi.md.deprecated`) before this second reassignment.
- **Role status**: None of these 5 families has an assigned brand role in `../visual-system/TYPOGRAPHY_SYSTEM.md` yet. See `../governance/OPEN_QUESTIONS.md`.

## Recommended Usage

Pending formal role assignment. Provisional read based on each font's character, for design exploration only — not yet policy:

- **Xanti Typewriter Variable**: Monospace/typewriter aesthetic — technical or retro-typewriter display moments
- **Aglet Mono Variable**: Clean monospace — code samples, technical UI, data displays
- **BioRhyme Variable**: Slab-serif character — editorial display, print-forward moments
- **Grandstander Variable**: Rounded and playful — friendly display, casual campaigns
- **Scatterplot VF**: Experimental/variable-forward — art direction, one-off statement pieces
