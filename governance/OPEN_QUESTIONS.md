# Open Questions

This document contains current decision items for future planning.

## Active Questions

1. Public publishing model
- Should the hub remain docs-first private with exported kits, or also publish a public docs site directly from this repo?

2. Legacy file retention strategy
- Should long integrated legacy docs remain intact as reference artifacts, or be replaced with concise pointers after full migration?

3. Asset archival timing
- When should deprecated variants move from tracked to archived status, and what retention period is required?

4. Additional CI guardrails
- Which additional checks should become required on PRs (markdown links, docs consistency, manifest-doc parity)?

## Recently Resolved

1. Canonical typography ownership
- Resolved: visual-system/TYPOGRAPHY_SYSTEM.md is policy owner.

2. Release manifest enforcement
- Resolved: CI PR gate runs manifest validator on pull requests to main.
