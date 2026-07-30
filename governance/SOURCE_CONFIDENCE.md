# Source Confidence

This document records confidence in major brand domains and their evidentiary basis.

## Confidence Matrix

| Domain | Confidence | Basis |
|---|---|---|
| Color system | High | Canonical palette docs + manifest alignment + cclibs provenance decisions |
| Typography system | High | Canonical policy + inventory documentation + integration references |
| Logo and asset usage | High | Canonical asset mapping + lifecycle policy + manifest checks |
| Voice and values | High | Canonical verbal policy and examples consolidated from legacy sources |
| Tone by context | Medium | Strong internal guidance, but still evolving with channel execution feedback |
| External mirror parity | Medium | Canonical hub is stable; external mirrors may require explicit sync passes |

## Notes
- Confidence should be revised whenever major policy or source changes occur.
- Use this file with DATA_GAPS and OPEN_QUESTIONS during release planning.

## Provenance Signals
- cclibs export provenance is treated as the strongest visual-source signal for palette and asset identity.
- Live site and shipped packages are useful operational evidence but may lag canonical policy updates.
- Archived template sources can inform tone hypotheses but should not override active canonical docs.
