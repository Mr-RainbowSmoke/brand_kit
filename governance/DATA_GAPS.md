# Data Gaps

This document tracks known brand-system gaps that require follow-up decisions or execution.

## Open Gaps

1. External mirror synchronization
- Status: Workflow ready — credentials pending
- Targets:
  - SharePoint brand guide site: https://djfox8705live.sharepoint.com/sites/BrandGuide
  - Dropbox (asset kit exports)
  - Google Drive (asset kit exports)
- Automation: .github/workflows/sync-external-mirrors.yml triggers on push to main
- Remaining action: configure RCLONE_CONFIG secret per governance/BRANCH_PROTECTION_RUNBOOK.md, then trigger first sync via workflow_dispatch

2. Legacy shipped asset color alignment
- Status: Open
- Description: Previously shipped assets and website builds may still reflect older palette snapshots.
- Impact: Cross-channel color inconsistency risk.
- Next action: Decide reissue strategy and phase plan for updates.

3. Deep legacy narrative consolidation
- Status: Closed
- Resolution: All legacy files formally classified: pointer stubs (brand_page.md, brand-voice-guidelines.md), scope-bounded companion (typography/BrandTypography.md), provenance artifact (brand.html). Retention policy ratified in DECISION_LOG.md.

4. Automated docs consistency checks
- Status: Partially complete
- Description: Release manifest checks exist, but docs/metadata cross-checking is not fully automated.
- Impact: Possible silent drift in non-manifest documentation.
- Next action: Add lightweight docs integrity checks in CI.

## Closed Gaps

1. Release manifest drift
- Status: Closed
- Resolution: Automated validator and PR gate now enforce manifest integrity.
