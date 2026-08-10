# Print Playbook

## Goal
Keep printed materials visually consistent with digital identity while preserving legibility.

## Use Cases
- Posters (A2, A1, or custom event sizes)
- One-pagers / fact sheets (A4 / US Letter)
- Event collateral (programs, badges, signage)
- Partner handouts (folded brochures, tear-off cards)

## Required Asset Variants

| Asset | Format | Notes |
|---|---|---|
| Primary mark (vector) | EPS or PDF | Required for print; never rasterize from PNG |
| RS glyph (vector) | EPS or SVG exported to PDF | For smaller placements and spot-color use |
| Color palette swatches | CMYK values (see below) | Required for print color matching |

## CMYK Color Reference

| Color | Hex | CMYK (approx.) | Notes |
|---|---|---|---|
| Pride red | #FF0000 | 0, 100, 100, 0 | Verify with vendor — may need spot color |
| Pride orange | #FF8E00 | 0, 44, 100, 0 | |
| Pride yellow | #FFED00 | 0, 7, 100, 0 | |
| Pride green | #008026 | 100, 0, 70, 50 | |
| Pride blue | #004CFF | 100, 70, 0, 0 | |
| Pride violet | #400098 | 75, 100, 0, 40 | |
| Royalty dark | #0903A6 | 100, 97, 0, 35 | Primary print CTA |
| Black | #000000 | 0, 0, 0, 100 | Rich black for large fills: 60C 40M 40Y 100K |

## Color Baseline
- Use approved palette CMYK values from the table above for print output
- Verify print-safe rendering with vendor before full production run
- Keep key text/background combinations high contrast; refer to approved pairings in [accessibility/ACCESSIBILITY_BASELINE.md](../accessibility/ACCESSIBILITY_BASELINE.md)

## Layout Baseline
- Bleed: 3mm on all sides (standard vendor requirement)
- Safe margin (inside bleed): min 5mm from trim edge for live content
- Logo clear space: minimum cap-height of the mark on all sides
- Body text minimum: 8pt for small print; 10–12pt for comfortable reading
- Resolution: 300 DPI minimum for all raster elements

## Typography Baseline
- Preserve hierarchy; avoid crowding multiple display fonts on one piece
- Body content: Transat or Le Havre Rounded at comfortable reading sizes
- Headlines: Omnes Narrow Black or Chennai Bold — one per piece
- Decorative display (Rig Solid, Elliott's): title cards or poster art only

## Do / Don't

| Do | Don't |
|---|---|
| Use vector mark files (EPS/PDF) for all print output | Export the logo from a low-res PNG for print |
| Set bleed to 3mm and keep live content inside safe margin | Extend critical content to the edge with no bleed |
| Validate CMYK output with vendor before large print run | Trust screen RGB values for print color accuracy |
| One dominant headline font per piece | Mix three or more display fonts on a single layout |
| Include the brand URL or handle in footer | Omit brand contact path on partner-facing materials |

## Production Baseline
- File format for vendor handoff: print-ready PDF/X-1a or PDF/X-4
- Embed all fonts or outline text before export
- Validate logo clear space before final export

## Print Production Checklist
- [ ] Vector mark files used (no rasterized logos)
- [ ] Bleed set to 3mm, live content inside 5mm safe margin
- [ ] Typography hierarchy readable at target print size
- [ ] CMYK values verified against reference table
- [ ] 300 DPI minimum for all raster elements
- [ ] Fonts embedded or outlined in final PDF
- [ ] Output in vendor-required format (PDF/X-1a or PDF/X-4)

## Starter Layout Template
1. Header band: brand mark (vector) plus headline (Omnes Narrow Black)
2. Core message: concise value statement (Transat Regular, min 10pt) and 2–3 supporting points
3. Proof or highlight strip: creator or community visual element
4. Action footer: CTA phrase, brand URL or handle, and QR code (optional)
