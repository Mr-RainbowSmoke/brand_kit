# Email Playbook

## Goal
Keep outbound communication clear, branded, and consistent across newsletter and campaign formats.

## Required Asset Variants

| Asset | Dimensions | Use case |
|---|---|---|
| Email header / banner | 600 × 200 px (2×: 1200×400) | Top of every branded email |
| Hero image | 600 × 338 px (16:9) | Campaign lead image |
| Profile mark (light) | 120 × 120 px | Footer brand lockup |
| Social icon set | 24 × 24 px each | Footer social links |

## Layout Baseline
- Max content width: 600px (standard email client safe zone)
- Single-column layout for core messages; two-column max for list-style sections
- Padding: 24px horizontal on all content blocks
- Branded header first; CTA above the fold where possible

## Structure Baseline
- Branded header (logo mark + optional header banner)
- Clear lead section: one sentence that frames the value
- Body: 2–3 short blocks with consistent heading hierarchy
- Single primary CTA (button, not text link only)
- Footer: brand mark, social icons, unsubscribe link

## Typography Baseline
- Body clarity over stylistic novelty — use web-safe equivalents of brand fonts where email clients restrict
- Minimum body size: 16px; minimum footer/legal: 12px
- Limit decorative display type to header imagery, not live text

## Color Baseline
- Use tested high-contrast pairings (see [accessibility/ACCESSIBILITY_BASELINE.md](../accessibility/ACCESSIBILITY_BASELINE.md))
- CTA button: Royalty blue (#0903A6 or #0F1AF2) with white label
- Reserve high-intensity accents (Pride rainbow) for graphic elements, not live text backgrounds

## Copy Tone Variant
- Purpose-driven and concise — no filler or padding sentences
- Lead with the reader's benefit, not RAINBOWSMOKE's achievement
- CTAs use active verbs: Join, Watch, Get, Explore — not Click here
- Subject line: specific, specific, specific — max 50 characters for mobile preview

## Do / Don't

| Do | Don't |
|---|---|
| Write a preheader that supports the subject line | Leave the preheader blank or duplicate the subject line |
| Use one primary CTA per email | Stack multiple competing CTA buttons |
| Test rendering in major clients before send | Rely solely on desktop preview |
| Keep link text descriptive ("Read the full guide") | Use "Click here" or bare URLs as link text |
| Include plain-text version | Send HTML-only with no plain-text fallback |

## Accessibility Baseline
- Link text must be descriptive (never "click here")
- CTA button labels must be specific and action-oriented
- Maintain AA contrast on all text elements
- Images must have alt text; decorative images use alt=""

## Email QA Checklist
- [ ] Subject line is specific and ≤50 characters
- [ ] Preheader supports the primary message
- [ ] Branded header uses canonical mark asset
- [ ] One clear primary CTA is present
- [ ] Typography remains readable across major email clients
- [ ] Canonical assets only (no deprecated duplicates)
- [ ] Links are descriptive and action-oriented
- [ ] All images have alt text
- [ ] Plain-text version is present

## Starter Message Template
1. Header: branded banner (600×200px) + logo mark
2. Lead: one sentence framing the reader's value
3. Body block 1: core message with heading
4. Body block 2 (optional): supporting detail or creator highlight
5. CTA: Royalty blue button, one primary action
6. Footer: mark, social icons, unsubscribe
