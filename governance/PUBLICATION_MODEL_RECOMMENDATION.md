# Publication Model Recommendation

Date: 2026-07-29
Status: Accepted
Owner: Governance maintainers

## Decision Summary
Recommended model: Keep this repository docs-first as the private operational source of truth, and publish curated external outputs as versioned export kits.

## Why This Model
1. Governance stability
- Private docs-first operations preserve review quality and reduce accidental policy drift.
- CI policy already aligns to this model through a single required check and manual diagnostics.

2. Audience separation
- Internal maintainers need full context, migration notes, and operating runbooks.
- External partners need only approved usage guidance and release-safe assets.

3. Operational safety
- Export kits can be frozen, signed off, and distributed with explicit version tags.
- Public-site publishing from the same working repo increases risk of exposing in-progress guidance.

4. Migration fit
- Current roadmap still includes legacy retention, archival timing, and confidence upgrades.
- A private-first model avoids forcing public-surface completeness before governance hardening is finished.

## Implementation Policy
1. Keep this repository as the canonical authoring and governance hub.
2. Treat public-facing distribution as release artifacts, not as live docs from the working branch.
3. Continue publishing channel-specific kits from asset-library manifests.
4. Re-evaluate public-site publishing after all active governance questions are closed.

## Trigger Criteria For Re-Evaluation
A public docs site can be reconsidered when all criteria are true:
- Legacy retention strategy is finalized and implemented.
- Asset archival policy and retention window are approved.
- Tone-matrix confidence is upgraded to High through dedicated review.
- Additional CI guardrails are finalized and stable for two release cycles.

## Success Metrics
- Zero policy drift findings between canonical docs and export kits per release cycle.
- Zero broken-link regressions in published kit documentation.
- 100% release runs include quality-suite success and artifact traceability.

## Rollback / Alternative Path
If collaborators require a public docs site earlier, use a staged model:
- Publish a read-only snapshot branch or generated static export from approved tags only.
- Exclude governance internals and migration notes from public output.
- Keep main as private operational source of truth.
