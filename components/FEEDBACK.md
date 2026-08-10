# Feedback Patterns

## Purpose
Define alerts, badges, notices, and status messaging patterns.

## Pattern Types
- Informational alerts
- Success messages
- Warning notices
- Error notices
- Badges and chips

## Color and Icon Per Type

| Type | Icon | Color | Background tint | Notes |
|---|---|---|---|---|
| Informational | ℹ | Royalty blue (#0F1AF2) | Light blue tint | Neutral context, no urgency |
| Success | ✓ | Pride green (#008026) | Light green tint | Confirm completion or positive outcome |
| Warning | ⚠ | Pride orange (#FF8E00) | Light amber tint | Specific risk; include a next action |
| Error | ✗ | Pride red (#FF0000) | Light red tint | Explain the problem and next step |
| Badge / chip | — | Context-dependent | Brand palette swatch | Use for labels, counts, or status tags |

## Message Rules
- State labels must be explicit: "Success", "Warning", "Error" — not just an icon
- Use concise, action-oriented copy: explain what happened and what to do next
- Do not rely on color alone to indicate meaning
- Badges and chips must have legible text at their displayed size

## Copy Patterns

| Type | Pattern |
|---|---|
| Informational | [Fact or context]. [Optional suggested action.] |
| Success | [What succeeded]. [Optional next step.] |
| Warning | [Specific risk]. [Required action or workaround.] |
| Error | [What went wrong]. [How to fix it or who to contact.] |

## Typography Baseline
- Alert title: Le Havre Rounded Bold or Transat Bold, 14–16px
- Alert body: Transat Regular, 14px
- Badge / chip label: Transat or Le Havre Rounded, 11–13px

## Do / Don't

| Do | Don't |
|---|---|
| Pair icon + label + body copy for every state | Use only a color border and no text to signal error |
| Write error messages that explain cause and fix | Write "An error occurred" with no next step |
| Keep badge text short (1–3 words or a count) | Use a full sentence inside a badge |
| Use consistent icon set across all feedback types | Mix icon styles between alert and form error patterns |

## Accessibility Baseline
- Ensure sufficient contrast for icon and text against background tint (AA min)
- Include icon alongside state color — do not rely on color alone
- Alerts that appear dynamically should be announced to screen readers (role="alert" for errors)

## Feedback QA Checklist
- [ ] Each alert type (info/success/warning/error) has a distinct icon, label, and copy
- [ ] State meaning is conveyed by icon plus text, not color only
- [ ] Error and warning messages include a next action or recovery path
- [ ] Message hierarchy remains readable at mobile and desktop sizes
- [ ] Dynamic alerts are accessible to screen readers

## Starter Feedback Template
1. State marker: icon (left-aligned) + bold label
2. Message body: one concise sentence explaining what happened
3. Next action (optional): inline link or button — retry, dismiss, or learn-more path
