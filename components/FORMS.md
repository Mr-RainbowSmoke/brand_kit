# Forms

## Purpose
Define form control behavior and styling guardrails.

## Controls
- Text input
- Text area
- Select
- Checkbox
- Radio
- Toggle

## Typography
- Label family: Transat, 14–16px, medium weight
- Helper and validation text: Transat or Le Havre Rounded, 12–14px
- Avoid decorative display fonts in form controls

## Spacing Rules
- Label-to-input gap: 4–6px
- Input-to-helper-text gap: 4px
- Field-to-field gap: 16–24px
- Input height: min 44px (touch-safe)

## Validation States and Color Guidance

| State | Border | Icon | Text color | Notes |
|---|---|---|---|---|
| Default | Mid-gray (#C4C4C4) | None | Body color | No indicator needed |
| Focus | Royalty blue (#0F1AF2) | None | Body color | 2px outline, no fill change |
| Success | #008026 Pride green | ✓ icon | #008026 or body | Icon required alongside color |
| Error | #FF0000 Pride red | ✗ icon | #FF0000 or body | Error text is mandatory |
| Disabled | Light gray (#D2D2D2) | None | Muted body | Reduce opacity, not hidden |

## Error Pattern
- Error state requires icon plus message text — never color alone
- Error message text appears below the field, same size as helper text
- Required field indicator: asterisk (*) with an explanatory note at form top

## Do / Don't

| Do | Don't |
|---|---|
| Show visible labels above every field | Use placeholder text as a substitute for a label |
| Include error message text below the field | Use red border color as the only error indicator |
| Keep min touch target height at 44px | Make inputs shorter than 40px for mobile |
| State which fields are required at the top | Mark every field required with no explanation |
| Preserve logical tab order | Hide or disable focus outlines |

## Accessibility Baseline
- Labels must be visible and programmatically associated with controls
- Focus indicator must be visible on every control (matches button focus pattern)
- Required fields must be explained — don't rely solely on the asterisk
- Error messages must be reachable by screen reader (aria-describedby)

## Validation Checklist
- [ ] Every field has a visible label (not placeholder-only)
- [ ] Required fields are explicitly marked and explained at form top
- [ ] Error state includes icon plus text message, not color alone
- [ ] Success state is clearly distinguishable from default
- [ ] Keyboard tab order is logical and predictable
- [ ] All inputs meet 44px min height for touch comfort

## Starter Field Template
1. Label (Transat, 14–16px)
2. Control (min 44px height, 2px focus outline on focus)
3. Helper text (optional, 12–14px, below control)
4. Validation message: icon + text on error or success
