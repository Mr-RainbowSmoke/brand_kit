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

## States QA Checklist
- [ ] Default, focus, and error states are distinct across core components.
- [ ] Success/warning/error states include text, not color alone.
- [ ] Loading behavior communicates progress without disruptive motion.

## Starter State Template
1. Define state token names and visual intent.
2. Map state tokens to button/form/card interactions.
3. Add message pattern for success, warning, and error.
