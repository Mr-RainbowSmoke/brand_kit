# Cards

## Purpose
Define content card layout for web, social previews, and community highlights.

## Card Variants

| Variant | Use case |
|---|---|
| Standard | General content: articles, updates, announcements |
| Media | Image or video lead — community highlights, stream recaps |
| Social Preview | Auto-generated OG card for links shared externally |
| Community Highlight | Featured creator or partner spotlight |

## Card Anatomy
- Optional media area
- Eyebrow or label (Le Havre Rounded, small)
- Title (Omnes Narrow Black for standard; Chennai Bold for editorial density)
- Supporting body (Transat Regular)
- Optional action row (one primary action max)

## Typography
- Title: Omnes Narrow Black for standard density; Chennai Bold for editorial
- Body: Transat Regular
- Eyebrow/meta: Le Havre Rounded or Transat, reduced size

## Color Guidance
- Background: white or F2F2F2 (Royalty light) for light surfaces; near-black for dark surfaces
- Title on light background: ensure 4.5:1 contrast minimum
- Media overlay text: white on a dark scrim (semi-transparent black overlay); maintain AA contrast
- Action row: use palette-approved button variant, not custom card-only color

## Spacing Rules
- Keep clear visual hierarchy between eyebrow, title, and body
- Preserve breathing room (min 16px) around media and action areas
- Do not use more than two display fonts per card

## States
- Default: standard shadow or border treatment
- Hover (interactive cards): subtle elevation lift, no color-only indicator
- Focus (interactive cards): visible outline, same pattern as buttons
- Disabled: reduced opacity, no action row

## Do / Don't

| Do | Don't |
|---|---|
| Use one headline font per card | Mix Omnes Narrow and Rig Solid on the same card |
| Keep overlay text legible with a scrim | Place white text directly on light-toned images |
| Limit action row to one primary action | Stack multiple CTAs inside a card |
| Use consistent card sizing within a grid | Mix card sizes arbitrarily in the same row |

## Accessibility Baseline
- Interactive cards must expose visible focus styling (matches button focus rules)
- Text overlays on media must maintain AA contrast via scrim, not rely on image contrast
- Do not use color alone to distinguish card categories — use label text

## Cards QA Checklist
- [ ] Correct variant used for context (standard vs media vs social preview vs highlight)
- [ ] Title/body hierarchy remains readable at target breakpoint
- [ ] Media overlay text passes AA contrast check with scrim applied
- [ ] Interactive cards expose visible focus styling
- [ ] Action row has at most one primary action
- [ ] No more than two display font families per card

## Starter Card Template
1. Optional media area (16:9 or 1:1 ratio) with dark scrim for overlay safety
2. Eyebrow label (Le Havre Rounded, 12–14px)
3. Title (Omnes Narrow Black or Chennai Bold, sized to context)
4. Supporting body (Transat Regular, 16px min)
5. Optional action row: one primary button
