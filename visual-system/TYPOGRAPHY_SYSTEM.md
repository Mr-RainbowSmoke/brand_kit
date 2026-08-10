# Typography System

This is the canonical typography policy for RAINBOWSMOKE.

## Governance Boundary
- This document owns typography policy, role hierarchy, pairing rules, channel scales, and usage decisions.
- ../fonts/FONTS_GUIDE.md owns inventory, technical metadata, and integration details.
- ../typography/BrandTypography.md is a quick reference companion and must not introduce conflicting rules.

## Role Hierarchy
### Body
- Transat
- Le Havre Rounded

### Headline
- Omnes Narrow
- Chennai

### Display and Statement
- Rig Solid variants
- Elliott's Collection variants

### Accent
- Sketchnote Text
- Olivita

## Baseline Rules
1. Use body families for long-form readability.
2. Use headline families for section hierarchy and scanability.
3. Use display families only for emphasis moments.
4. Avoid mixing multiple high-expression display families in one composition.
5. Keep functional UI text in body or headline families, never in decorative display families.

## Role-To-Weight Matrix

| Role | Family | Approved weights and styles | Notes |
|---|---|---|---|
| Body default | Transat | 400, 700, 400 italic | Default long-form and UI text baseline. |
| Body alternate | Le Havre Rounded | 400, 700, 400 italic | Friendly secondary body and UI support. |
| Primary headline | Omnes Narrow | 900 preferred, 700 secondary | Use for major hierarchy and page entry points. |
| Editorial headline | Chennai | 700 preferred, 400 secondary | Use when Omnes is too aggressive. |
| Display primary | Rig Solid family | Approved variants only | One variant per composition. |
| Statement display | Elliott's Collection | Approved variants only | One statement use per composition. |
| Accent quote | Sketchnote Text | 400, 700, 400 italic | Use sparingly for personality. |
| Accent expressive | Olivita | 400 italic preferred | Pull quotes and expressive moments only. |

## Approved Pairing Matrix

| Use case | Heading | Body | Accent | Constraints |
|---|---|---|---|---|
| Standard web UI | Omnes Narrow | Transat | Le Havre Rounded | Keep display fonts out of navigation and forms. |
| Editorial page | Chennai | Transat | Olivita | Maintain generous line height and whitespace. |
| Campaign landing | Rig Solid | Le Havre Rounded | Transat fine print | Only one Rig variant per page. |
| Social static | Omnes Narrow or Chennai | Transat | Sketchnote Text | Keep text count low and hierarchy clear. |
| Stream overlay | Omnes Narrow | Le Havre Rounded | none | Prioritize legibility over decoration. |

## Responsive Type Scale By Channel

Values below are baseline recommendations and can be tuned per layout while preserving hierarchy.

### Web

| Token | Mobile | Tablet | Desktop |
|---|---|---|---|
| Display | 40-56px | 56-72px | 72-96px |
| H1 | 32-40px | 40-48px | 48-64px |
| H2 | 24-30px | 30-36px | 36-44px |
| H3 | 20-24px | 24-28px | 28-32px |
| Body | 16-18px | 16-18px | 16-20px |
| Caption | 12-14px | 12-14px | 12-14px |

### Social and Creator Graphics

| Format | Headline | Support text | Small detail |
|---|---|---|---|
| 1080x1080 | 64-96px | 28-42px | 18-24px |
| 1080x1920 | 72-112px | 32-48px | 20-28px |
| 1920x1080 | 72-120px | 30-46px | 18-24px |

### Stream Overlays

| Element | Recommended size | Notes |
|---|---|---|
| Nameplate | 28-40px | Prefer Omnes Narrow for labels. |
| Status tag | 20-28px | Keep high contrast and short text. |
| Supporting info | 16-22px | Prefer Le Havre Rounded or Transat. |

## Accessibility And Legibility Guardrails
1. Keep body text line-height between 1.5 and 1.7.
2. Keep headline line-height between 1.1 and 1.3.
3. Avoid long all-caps paragraphs.
4. Avoid using decorative display fonts for body, controls, or legal copy.

## Integration Notes
- Adobe Typekit project details and links are documented in ../fonts/FONTS_GUIDE.md.
- Fallback behavior should remain consistent across web and static design contexts.

## Retired Fonts
Kegger Collegiate, Kegger US, and Elliott's Blue Eyeshadow were retired from Adobe Fonts on 2026-01-07 and are no longer served by either Typekit project. Do not use them in new work. For sports/athletic contexts, use Backstroke. Full detail in ../fonts/ojc8wen.md's Retired Families section.

## Pending Role Assignment
Five variable font families were added to the `gsl6svi` Adobe Fonts project on 2026-01-07 (Xanti Typewriter Variable, Aglet Mono Variable, BioRhyme Variable, Grandstander Variable, Scatterplot VF) and are documented in ../fonts/FONTS_GUIDE.md (Tier 6) and ../fonts/gsl6svi.md. None has been assigned a role in the hierarchy above yet — treat as available-but-undecided until this section is updated with a ratified placement. Open item tracked in ../governance/OPEN_QUESTIONS.md.

## Maintenance Rule
Any typography policy change must be applied here first, then reflected in supporting references.
