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

## Messaging Rules
- Success and error must include text labels or messages.
- Warning states should be specific about risk or next action.
- Loading states should indicate progress where possible.

## Visual Rules
- Preserve consistent state transitions across button, form, and card interactions.
- Focus state must be visually distinct from hover.
- Disabled must remain legible, not hidden.

## Accessibility Baseline
- Keyboard users must receive equivalent feedback.
- Motion used in state transitions should remain subtle and non-distracting.
