# Buttons

## Purpose
Define branded button behavior for web and campaign surfaces.

## Variants
- Primary: high emphasis actions
- Secondary: supporting actions
- Ghost: low emphasis actions on dark surfaces
- Destructive: high-risk actions

## Typography
- Label family: Le Havre Rounded or Transat
- Label weight: 700 for primary and destructive, 400-700 for secondary and ghost
- Use sentence case unless campaign art direction requires all caps

## Color Guidance
- Primary actions should favor trusted high-contrast pairings from the approved palette system.
- Avoid low-contrast text/background combinations.
- Do not use color-only differences between critical action states.

## States
- Default
- Hover
- Focus (visible outline required)
- Active
- Disabled
- Loading

## Accessibility Baseline
- Focus state must be obvious and persistent under keyboard navigation.
- Disabled state must still preserve label readability.
- Minimum contrast must meet AA.

## State Matrix

| Variant | Required states |
|---|---|
| Primary | default, hover, focus, active, disabled, loading |
| Secondary | default, hover, focus, active, disabled |
| Ghost | default, hover, focus, active, disabled |
| Destructive | default, hover, focus, active, disabled |

## Starter CSS Skeleton
```css
.btn { font-family: var(--font-ui); border-radius: 999px; }
.btn:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
.btn[disabled] { opacity: 0.6; cursor: not-allowed; }
.btn--loading { pointer-events: none; }
```
