# Video And Stream Playbook

## Goal
Ensure overlays, intros, and stream visuals remain recognizable and legible in motion.

## Required Asset Variants

| Asset | Dimensions | Format | Use case |
|---|---|---|---|
| Stream overlay frame | 1920 × 1080 px | PNG (transparent) | Persistent on-stream branding |
| Lower third | 1920 × 1080 px | PNG / animated | Speaker name + context |
| Intro slate | 1920 × 1080 px | MP4 / GIF | Pre-stream or scene intro |
| Outro slate | 1920 × 1080 px | MP4 / GIF | End-of-stream or CTA screen |
| Alert box graphic | 300 × 168 px | PNG (transparent) | Sub/follow/donation alerts |
| Webcam overlay frame | 280 × 158 px (16:9 cam) | PNG (transparent) | Face cam border and label |

## Safe Zones
- Overlay content zone: 1720 × 880 px centered (100px margin all sides)
- Lower third placement: bottom 25% of frame; keep left-aligned for readability
- Webcam zone: top-left or bottom-left corner, not obscuring content
- Alert box: top-right quadrant, clear of stream controls

## Typography Baseline
- Prioritize legibility at live viewing distances (min 28px equivalent at 1080p)
- Keep decorative display type (Rig Solid, Elliott's) to title cards or intro slates only
- Lower-third primary line: Le Havre Rounded Bold or Transat Bold, 28–36px
- Lower-third secondary line: Transat Regular, 20–24px

## Color Baseline
- Use approved high-contrast pairings for overlays on variable footage
- Preferred overlay tint: dark semi-transparent (rgba black 60–75%) behind text
- Brand-blue presence (Royalty #0F1AF2) visible in accent lines or name badges
- Avoid full Pride rainbow as overlay background — use as accent stripe or motif only

## Motion Baseline
- Transitions: 200–400ms easing; avoid hard cuts on brand elements
- Avoid high-frequency flashing or strobing effects
- Alert animations: short (under 3 seconds), non-looping unless intentional
- Provide reduced-motion alternatives for digital product usage

## Copy Tone Variant
- Live and community-first: warm, direct, energy-aware
- Lower-third labels are minimal: name, role or context, and one optional tag
- Alert copy is celebratory but brief: acknowledge the action, not a paragraph

## Do / Don't

| Do | Don't |
|---|---|
| Keep lower-third text inside the safe zone | Place lower thirds over the stream's active content area |
| Use a dark scrim behind overlay text on variable footage | Place white text directly on bright or low-contrast backgrounds |
| Keep alert animations under 3 seconds | Loop alert animations indefinitely |
| Use canonical SVG mark assets at correct resolution | Rasterize SVGs at low resolution for stream graphics |
| Test overlays at 1080p and 720p before going live | Only preview at full resolution |

## Accessibility Baseline
- Ensure sufficient contrast on dynamic backgrounds (scrim is the primary control)
- Keep lower-third text in readable size bands (min 28px equivalent at 1080p)
- Avoid flash-heavy scene transitions

## Stream Overlay Checklist
- [ ] All assets at 1920×1080 with correct format (PNG transparent for overlays)
- [ ] Lower-third text inside safe zone, readable at 720p
- [ ] Overlay marks use canonical SVG/PNG assets
- [ ] Motion effects are smooth, under 3 seconds, non-distracting
- [ ] Scene transitions avoid flash-heavy behavior
- [ ] Dark scrim applied behind any text over variable footage

## Lower Third Template
1. Primary line: creator or segment name (Le Havre Rounded Bold, 28–36px)
2. Secondary line: short context or role (Transat Regular, 20–24px)
3. Optional tag: live status, event name, or campaign marker (badge style)
