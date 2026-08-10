# States

## Purpose
Normalize interactive and feedback states across components.

## Shared State Model
- Default
- Hover
- Focus
- Active
- Disabled
- Loading
- Success
- Warning
- Error

## State-to-Color Mapping

| State | Border / outline | Icon | Background tint | Notes |
|---|---|---|---|---|
| Default | Mid-gray (#C4C4C4) | — | None | Baseline; no indicator |
| Hover | Royalty blue (#0F1AF2) tint | — | Optional subtle blue | 100–150ms transition |
| Focus | Royalty blue (#0F1AF2) 2px | — | None | Outline offset 2px; required for keyboard |
| Active | Royalty dark blue (#0903A6) | — | Subtle press tint | Triggered on mousedown / keydown |
| Disabled | Light gray (#D2D2D2) | — | Gray tint | Opacity 0.5–0.6; still legible |
| Loading | Royalty blue (#0F1AF2) | Spinner | Optional tint | No pointer events |
| Success | Pride green (#008026) | ✓ | Light green tint (optional) | Text message required |
| Warning | Pride orange (#FF8E00) | ⚠ | Light amber tint (optional) | Specific risk or next action required |
| Error | Pride red (#FF0000) | ✗ | Light red tint (optional) | Error text message required |

## Messaging Rules
- Success and error must include text labels or messages — icon alone is insufficient
- Warning states must name the specific risk or required next action
- Loading states should indicate progress where possible (spinner + percentage or label)

## Visual Rules
- Focus must be visually distinct from hover — not the same treatment
- Disabled must remain legible: reduce opacity, do not remove or hide the element
- State transitions: 100–150ms; avoid jarring or flash-heavy changes

## Do / Don't

| Do | Don't |
|---|---|
| Use distinct visual treatments for focus vs hover | Make focus and hover look identical |
| Include a text message with every error and success state | Use color as the only indicator of state |
| Keep disabled elements visually accessible (opacity, not hidden) | Hide or collapse disabled controls |
| Use consistent state tokens across button, form, and card | Apply ad-hoc per-component state colors |

## Accessibility Baseline
- Keyboard users must receive equivalent state feedback to mouse users
- Motion used in state transitions must stay subtle and non-distracting
- Never remove the focus ring; customize it rather than hiding it

## States QA Checklist
- [ ] Default, hover, focus, and active states are visually distinct from each other
- [ ] Success / warning / error states include icon plus text, not color alone
- [ ] Loading state prevents duplicate interactions (pointer-events: none)
- [ ] Disabled elements retain readable labels and meet 3:1 contrast
- [ ] State transitions do not flash or strobe

## Starter State Template
1. Define state token names and map to palette values above
2. Apply tokens consistently across button, form, and card interactions
3. Wire success, warning, and error tokens to message pattern (icon + text)
4. Validate focus treatment differs from hover at component review
