# Release Notes

## 2026-07-29 - CI Governance Migration Complete

### Summary
The repository CI policy has been consolidated so pull requests to main are now gated by a single required check: Validate quality suite.

### What Changed
- Added consolidated workflow: .github/workflows/quality-suite.yml.
- Demoted standalone workflows to manual-only workflow_dispatch runs:
  - .github/workflows/release-manifest-check.yml
  - .github/workflows/docs-link-check.yml
  - .github/workflows/docs-manifest-parity-check.yml
  - .github/workflows/markdown-style-check.yml
- Added a Quality Suite status badge and CI policy snapshot table to README.
- Added branch-protection runbook: governance/BRANCH_PROTECTION_RUNBOOK.md.

### Operational Status
- Branch protection on main now requires only Validate quality suite.
- Standalone manual workflows were smoke-tested and completed successfully.

### Contributor Impact
- For pull requests: only one required status check should appear.
- For diagnostics: individual checks can still be run manually from Actions.

### No Breaking Changes
No changes to brand assets, policy semantics, or canonical source ownership were introduced by this CI migration.
