# Decision Log

## 2026-07-29
### Decision: Hub model
- Decision: Use a docs-first repository as the source-of-truth.
- Rationale: Stable version control, easier review, deterministic governance.

### Decision: Audience strategy
- Decision: Build for both internal and external audiences.
- Rationale: Enables both creator operations and partner/media access.

### Decision: Depth strategy
- Decision: Build comprehensive v1 instead of a quick reference only.
- Rationale: Avoid rework and fragmentation during scale-up.

### Decision: Delivery priority
- Decision: Prioritize quality foundation over speed-only publication.
- Rationale: Reduces ambiguity and drift across future channels.

### Decision: Canonical consolidation approach
- Decision: Introduce domain-level canonical docs first, then migrate detail from legacy integrated docs.
- Rationale: Creates stable target locations before deep content refactors and reduces migration risk.

### Decision: Typography file ownership boundary
- Decision: Set visual-system/TYPOGRAPHY_SYSTEM.md as policy owner, keep fonts/FONTS_GUIDE.md for inventory and integration, and keep typography/BrandTypography.md as quick reference.
- Rationale: Eliminates overlap conflicts while preserving existing technical detail and onboarding convenience.

### Decision: Playbook implementation order
- Decision: Ship concrete component and application playbooks incrementally, starting with high-usage digital channels.
- Rationale: Delivers immediate operational value while allowing future expansion to mobile, print, and merch.

### Decision: Verbal-system canonical expansion
- Decision: Split verbal policy into core voice (VOICE_AND_TONE), terminology/style conventions, and channel copy examples.
- Rationale: Improves maintainability and allows faster channel-specific updates without destabilizing core voice policy.

### Decision: Asset lifecycle policy
- Decision: Mark canonical assets as Active and duplicate naming variants as Deprecated before any cleanup deletions.
- Rationale: Preserves safety, traceability, and continuity while reducing accidental use of ambiguous files.

### Decision: Deprecated variant register
- Decision: Maintain a dedicated non-destructive deprecated register before any archival/move actions.
- Rationale: Ensures cleanup is auditable and reversible while preserving collaborator trust in asset paths.

### Decision: Release manifest hardening gate
- Decision: Add a local validation script that blocks manifest references to deprecated or missing assets.
- Rationale: Prevents accidental distribution drift and makes release packaging deterministic.

### Decision: PR enforcement for release validation
- Decision: Run manifest validation automatically on pull requests to main.
- Rationale: Moves release safety checks from optional local practice to consistent repository policy.

### Decision: Legacy integrated files as reference-only
- Decision: Keep brand_page.md and brand-voice-guidelines.md as historical integrated references with explicit canonical pointers.
- Rationale: Preserves provenance while preventing policy drift across duplicate documentation surfaces.

### Decision: PR enforcement for markdown docs integrity
- Decision: Run local markdown link and heading-fragment validation on pull requests to main.
- Rationale: Prevents navigation drift and broken internal references across the Brand Guide Hub.

### Decision: Optional markdown style linting
- Decision: Run markdown style linting on PRs as non-blocking quality telemetry.
- Rationale: Improves authoring consistency without interrupting active migration work.

### Decision: PR enforcement for docs-manifest parity
- Decision: Run docs-to-manifest parity validation on pull requests to main.
- Rationale: Prevents silent divergence between canonical color documentation and manifest source-of-truth values.

### Decision: Expanded parity coverage scope
- Decision: Enforce parity coverage for color, typography metadata, core typography family presence, and foundation identity essence signals.
- Rationale: Keeps cross-domain canonical docs synchronized with source metadata while migration continues.

### Decision: Verbal and terminology parity enforcement
- Decision: Extend docs-manifest parity checks to include voice trait coverage, avoid-term coverage, and baseline terminology alignment.
- Rationale: Prevents drift between manifest voice intent and canonical verbal policy docs.

### Decision: Tone-matrix context parity enforcement
- Decision: Enforce required tone-matrix channel contexts in VOICE_AND_TONE (Social, Website, Campaign, Support, Media/Partner).
- Rationale: Preserves channel-policy completeness during ongoing documentation refactors.

### Decision: Copy-examples structural parity enforcement
- Decision: Enforce required channel contexts and minimum example-bullet presence in COPY_EXAMPLES.
- Rationale: Ensures practical usage examples remain complete across all required verbal channels.

### Decision: Optional application playbook completeness telemetry
- Decision: Add non-blocking completeness checks for application playbooks (required baseline headings, checklist/template presence, checklist density).
- Rationale: Surfaces documentation quality gaps early without disrupting active content migration.

### Decision: Optional component-doc completeness telemetry
- Decision: Add non-blocking completeness checks for component docs (required baseline headings, checklist/template presence, checklist density).
- Rationale: Keeps reusable UI guidance operationally complete while preserving migration velocity.

### Decision: Consolidated quality suite workflow
- Decision: Add a single CI workflow that runs all validators and publishes a report artifact/summary.
- Rationale: Improves PR review visibility by centralizing quality status while preserving detailed specialized checks.

### Decision: Consolidated suite as primary PR gate
- Decision: Keep quality-suite.yml as the required PR-triggered check and demote standalone validator workflows to manual-only.
- Rationale: Reduces PR status noise while retaining targeted workflows for on-demand diagnostics.

### Decision: Branch-protection runbook governance
- Decision: Maintain a dedicated branch-protection runbook as the operational source for required-check setup on main.
- Rationale: Keeps CI gate policy reproducible for maintainers and future repository admins.

### Decision: Publication model policy
- Decision: Keep this repository as a private docs-first operational source of truth and publish external-facing content as versioned export kits.
- Rationale: Preserves governance quality and operational safety while migration/completeness work remains in progress.

## Open Decisions
1. Typography overlap resolution:
- Option A: merge BrandTypography into FONTS_GUIDE
- Option B: keep both with strict scope boundaries

2. Asset duplicate handling strategy:
- Option A: canonical map first, no deletions in v1
- Option B: selective cleanup after mapping verification
