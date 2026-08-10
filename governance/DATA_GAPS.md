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
- Status: Phase plan defined
- Scope: All brand touchpoints — website, social profiles, press/media kits, physical/print
- Ownership: Solo maintainer until AI agent workflow is established
- Impact: Public-facing web and social still show visibly off-brand palette values

### Phase 1 — High urgency (web and social profiles)
- Surfaces: rainbowsmokeofficial.com, Twitter/X profile, Instagram profile
- Action: Audit CSS and image assets for stale hex values; replace with canonical palette from visual-system/COLOR_SYSTEM.md
- How to verify: Inspect rendered pages against approved pairings in accessibility/ACCESSIBILITY_BASELINE.md
- Owner: Solo maintainer
- Status: Not started

### Phase 2 — Medium urgency (press and media kit reissue)
- Surfaces: Press/media kits previously distributed to partners and media contacts
- Action: Package updated kits from canonical manifests (PRESS_KIT_MANIFEST.md, MEDIA_KIT_MANIFEST.md); redistribute to known contacts
- How to verify: Run check_release_manifests.py before each kit export
- Owner: Solo maintainer via hub
- Status: Not started

### Phase 3 — Discovery (unknown touchpoints)
- Action: Audit all brand touchpoints beyond the known URLs above; add any discovered surfaces to Phase 1 or 2 as appropriate
- Trigger: Run before Phase 1 completes so newly found surfaces can be addressed in the same pass
- Owner: Solo maintainer
- Status: Not started

### Phase 4 — Low urgency (legacy PDFs and static documents)
- Surfaces: Previously distributed PDFs, one-pagers, decks
- Action: Document as non-actionable (cannot be recalled); monitor for re-use and replace on request
- Owner: Solo maintainer
- Status: Acknowledged, no immediate action required

### Phase 5 — Next production cycle (physical/merch)
- Surfaces: Apparel, stickers, badges, event items already produced or shipped
- Action: Do not attempt recall; apply canonical palette and updated asset variants at next production run
- Owner: Solo maintainer
- Status: Deferred to next production order

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
