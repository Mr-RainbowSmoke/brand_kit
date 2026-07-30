# Open Questions

This document contains current decision items for future planning.

## Active Questions

1. Legacy file retention strategy
- Should long integrated legacy docs remain intact as reference artifacts, or be replaced with concise pointers after full migration?

2. Asset archival timing
- When should deprecated variants move from tracked to archived status, and what retention period is required?

3. Additional CI guardrails
- Which additional checks should become required on PRs beyond current manifest, markdown-link, and docs-manifest parity checks (style linting, deeper docs consistency)?

4. Tone matrix validation depth
- Should we keep current tone-by-context guidance as-is, or run a dedicated content review cycle to upgrade confidence from Medium to High?

## Recently Resolved

1. Canonical typography ownership
- Resolved: visual-system/TYPOGRAPHY_SYSTEM.md is policy owner.

2. Release manifest enforcement
- Resolved: Required PR gate now runs via consolidated quality-suite workflow; standalone manifest workflow is manual-only.

3. Docs-manifest parity enforcement
- Resolved: Required PR gate now runs via consolidated quality-suite workflow; standalone parity workflow is manual-only.

4. Markdown style lint baseline
- Resolved: Optional non-blocking style lint runs inside quality-suite for PRs and as manual standalone workflow.

5. Branch protection required-check policy
- Resolved: main now requires only Validate quality suite; standalone checks are manual-only.

6. Standalone workflow operability after demotion
- Resolved: Manual workflow_dispatch smoke tests passed for all standalone validator workflows.

7. Public publishing model
- Resolved: Keep the hub docs-first private for operations and publish external guidance as versioned export kits.
- Source: governance/PUBLICATION_MODEL_RECOMMENDATION.md
