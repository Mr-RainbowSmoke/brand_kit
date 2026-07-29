# Brand Typography System

## Metadata

```json
{
  "brand": "RAINBOWSMOKE",
  "category": "Typography",
  "purpose": "Define brand typography hierarchy and usage rules to ensure consistency and prevent font sprawl",
  "last_updated": "2026-01-05"
}
```

## Overview
This document defines RAINBOWSMOKE's typography system. It clarifies which fonts to use for body text, headlines, display moments and accents. The goal is to prevent font sprawl and ensure brand consistency.

## Core Brand Voice (Primary Fonts)

### Transat (Primary Body Font)

```json
{
  "name": "Transat",
  "role": "primary_body",
  "usage": ["body_copy", "paragraphs", "ui_labels", "forms"],
  "weights": [
    {"name": "Regular", "value": 400},
    {"name": "Bold", "value": 700}
  ],
  "personality": ["clean", "modern", "confident"],
  "rule": "If it's longer than one sentence, it's Transat.",
  "typekit_family": "transat"
}
```

### Le Havre Rounded (Secondary Body / Alt UI)

```json
{
  "name": "Le Havre Rounded",
  "role": "secondary_body",
  "usage": ["subheadings", "cards", "navigation", "callouts"],
  "weights": [
    {"name": "Regular", "value": 400},
    {"name": "Bold", "value": 700}
  ],
  "personality": ["friendly", "human", "playful"],
  "rule": "Le Havre Rounded supports Transat — it never replaces it.",
  "typekit_family": "le-havre-rounded"
}
```

## Headline & Impact Fonts

### Omnes Narrow (Black)

```json
{
  "name": "Omnes Narrow",
  "role": "primary_headline",
  "usage": ["page_titles", "section_headers", "hero_text"],
  "weights": [
    {"name": "Black", "value": 900}
  ],
  "personality": ["bold", "modern", "unmistakable"],
  "rule": "One Omnes headline per section. Let it breathe.",
  "typekit_family": "omnes-narrow"
}
```

### Chennai (Bold)

```json
{
  "name": "Chennai",
  "role": "editorial_headline",
  "usage": ["editorial_headers", "long_reads", "feature_sections"],
  "weights": [
    {"name": "Bold", "value": 700}
  ],
  "personality": ["smart", "contemporary", "balanced"],
  "rule": "Use Chennai when Omnes feels too aggressive.",
  "typekit_family": "chennai"
}
```

## Display & Statement Fonts

### Rig Solid (Selected Variants)

```json
{
  "name": "Rig Solid",
  "role": "display",
  "allowed_variants": ["Bold Fill", "Bold Inline", "Medium Outline"],
  "usage": ["hero_banners", "splash_pages", "posters"],
  "personality": ["loud", "graphic", "confident"],
  "rule": "Never mix more than one Rig Solid variant on a single page.",
  "typekit_family": "rig-solid"
}
```

### Elliott's Collection

```json
{
  "name": "Elliott's Collection",
  "role": "statement",
  "allowed_variants": ["Blue Eyeshadow", "Jigsaw Dropshadow"],
  "usage": ["one_off_moments", "art_drops", "social_headers"],
  "rule": "If you use Elliott's, everything else goes quiet.",
  "restrictions": "Maximum one instance per design"
}
```

## Accent & Expressive Fonts

### Sketchnote Text

```json
{
  "name": "Sketchnote Text",
  "role": "accent",
  "usage": ["quotes", "captions", "playful_microcopy"],
  "weights": [
    {"name": "Regular", "value": 400},
    {"name": "Bold", "value": 700}
  ],
  "personality": ["human", "expressive", "informal"],
  "typekit_family": "sketchnote-text"
}
```

### Olivita (Italic)

```json
{
  "name": "Olivita",
  "role": "expressive",
  "usage": ["pull_quotes", "poetic_lines", "emphasis"],
  "weights": [
    {"name": "Regular Italic", "value": 400, "style": "italic"}
  ],
  "personality": ["smooth", "expressive", "intimate"],
  "typekit_family": "olivita"
}
```

## Restricted Fonts (Use Sparingly)

```json
{
  "restricted_fonts": [
    {
      "name": "Kegger Collegiate",
      "restriction": "sports_or_retro_only"
    },
    {
      "name": "Kegger US",
      "restriction": "sports_or_retro_only"
    },
    {
      "name": "Backstroke",
      "restriction": "athletic_graphics_only"
    },
    {
      "name": "Perec Scripte Deco",
      "restriction": "logo_lockups_or_special_marks_only"
    },
    {
      "name": "Sketchnote Square",
      "restriction": "decorative_headings_not_body_text"
    }
  ],
  "rule": "If a font draws attention to itself, it must earn that attention."
}
```

## Approved Font Pairings

### Default UI Stack

```json
{
  "name": "Default UI Stack",
  "use_case": "standard_ui",
  "pairings": {
    "headings": "Omnes Narrow Black",
    "body": "Transat Regular",
    "ui_labels": "Le Havre Rounded"
  }
}
```

### Editorial / Blog

```json
{
  "name": "Editorial / Blog",
  "use_case": "content_publishing",
  "pairings": {
    "headings": "Chennai Bold",
    "body": "Transat Regular",
    "quotes": "Olivita Italic"
  }
}
```

### Hero / Campaign

```json
{
  "name": "Hero / Campaign",
  "use_case": "marketing_landing_pages",
  "pairings": {
    "hero_text": "Rig Solid Bold Fill",
    "supporting_text": "Le Havre Rounded",
    "fine_print": "Transat"
  }
}
```

## Web Implementation (Canonical)

### Adobe Typekit Links

```html
<link rel="stylesheet" href="https://use.typekit.net/ojc8wen.css">
<link rel="stylesheet" href="https://use.typekit.net/gsl6svi.css">
```

### CSS Custom Properties

```css
:root {
  --font-body: "transat", sans-serif;
  --font-ui: "le-havre-rounded", sans-serif;
  --font-headline: "omnes-narrow", sans-serif;
  --font-editorial: "chennai", sans-serif;
  --font-display: "rig-solid-bold-fill", sans-serif;
}
```

### Font Stack Reference

```json
{
  "css_variables": {
    "--font-body": {
      "family": "transat",
      "fallback": "sans-serif",
      "purpose": "Primary body text and paragraphs"
    },
    "--font-ui": {
      "family": "le-havre-rounded",
      "fallback": "sans-serif",
      "purpose": "UI elements and secondary text"
    },
    "--font-headline": {
      "family": "omnes-narrow",
      "fallback": "sans-serif",
      "purpose": "Primary headlines and section titles"
    },
    "--font-editorial": {
      "family": "chennai",
      "fallback": "sans-serif",
      "purpose": "Editorial content headlines"
    },
    "--font-display": {
      "family": "rig-solid-bold-fill",
      "fallback": "sans-serif",
      "purpose": "Display and hero text"
    }
  }
}
```
