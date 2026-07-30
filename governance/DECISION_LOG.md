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
