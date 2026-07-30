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

## Open Decisions
1. Public publishing model:
- Option A: private docs + exported media kits
- Option B: public docs site from same source

2. Typography overlap resolution:
- Option A: merge BrandTypography into FONTS_GUIDE
- Option B: keep both with strict scope boundaries

3. Asset duplicate handling strategy:
- Option A: canonical map first, no deletions in v1
- Option B: selective cleanup after mapping verification
