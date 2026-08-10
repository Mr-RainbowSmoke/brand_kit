# Navigation

## Purpose
Define navigation patterns that stay branded while remaining easy to scan and operate.

## Patterns
- Top navigation (desktop persistent)
- Mobile menu (hamburger / drawer)
- Section tabs (within-page)
- Breadcrumbs (deep hierarchy)

## Typography Baseline
- Primary nav labels: Le Havre Rounded or Transat, 14–16px, regular or medium weight
- Avoid decorative display fonts (Omnes Narrow, Rig Solid, Elliott's) in persistent navigation
- Active and current-page labels may use bold weight for emphasis

## Color Guidance for States

| State | Text | Background / indicator |
|---|---|---|
| Default | Body color or white on dark nav | Transparent |
| Hover | Royalty blue (#0F1AF2) or underline | Subtle tint optional |
| Active / current | Royalty blue or white with blue underline | Accent underline (2–3px) |
| Focus | Same as hover + visible outline | 2px outline, offset 2px |
| Mobile open | Full-width, clear background | Dark overlay behind drawer |

## Interaction Baseline
- Active/current section must be visually distinct from other links
- Focus state must differ from hover (not same treatment)
- Hover and active transitions should be fast: 100–150ms max

## Do / Don't

| Do | Don't |
|---|---|
| Keep nav labels short (1–3 words) | Use long descriptive phrases as nav labels |
| Use a visible active indicator (underline or color) | Rely on bold weight alone to show active state |
| Provide a clear close affordance on mobile menus | Leave the mobile menu dismissible only by clicking outside |
| Match terminology with the verbal system | Invent nav labels inconsistent with brand copy conventions |
| Ensure visible focus for keyboard users | Hide or suppress focus ring on nav links |

## Accessibility Baseline
- Keyboard navigation must be supported across all patterns
- Current page or section must be programmatically indicated (aria-current)
- Mobile menu must be keyboard operable and clearly dismissible

## Navigation QA Checklist
- [ ] Active section is visually distinct (color + indicator, not weight alone)
- [ ] Focus styles are visible for all nav links
- [ ] Mobile menu is keyboard operable and has a clear close affordance
- [ ] Labels are concise and consistent with terminology rules
- [ ] No decorative display fonts in persistent nav
- [ ] Hover and active states use different visual treatments

## Starter Structure
1. Brand zone: mark + home path (left or center)
2. Primary links (3–6 items max for desktop top nav)
3. Utility actions (search, account, CTA — right side)
4. Mobile collapse/expand with drawer or overlay

## Starter Navigation Template
1. Desktop: brand mark left, primary links center or left, utility actions right
2. Active state: 2–3px Royalty blue underline on current link
3. Mobile: hamburger icon opens full-width drawer, close button top-right
4. Focus style: 2px Royalty blue outline, 2px offset, on every focusable nav element
