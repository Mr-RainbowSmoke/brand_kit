# Data Gaps

This document tracks known brand-system gaps that require follow-up decisions or execution.

## Open Gaps

1. GitHub mirror synchronization
- Status: Open
- Description: External mirror references may still contain older values or outdated docs.
- Impact: Potential drift between canonical hub and external copies.
- Next action: Perform controlled mirror sync from canonical hub sources.

2. Legacy shipped asset color alignment
- Status: Open
- Description: Previously shipped assets and website builds may still reflect older palette snapshots.
- Impact: Cross-channel color inconsistency risk.
- Next action: Decide reissue strategy and phase plan for updates.

3. Deep legacy narrative consolidation
- Status: In progress
- Description: Legacy integrated docs still contain mixed archival and canonical-ready content.
- Impact: Reader confusion about authoritative source.
- Next action: Continue migration into canonical domain docs and mark legacy files as reference-only.

4. Automated docs consistency checks
- Status: Partially complete
- Description: Release manifest checks exist, but docs/metadata cross-checking is not fully automated.
- Impact: Possible silent drift in non-manifest documentation.
- Next action: Add lightweight docs integrity checks in CI.

## Closed Gaps

1. Release manifest drift
- Status: Closed
- Resolution: Automated validator and PR gate now enforce manifest integrity.
