# Branch Protection Runbook

This runbook defines the required branch-protection policy for main.

## Goal
Set main so the consolidated quality suite is the primary required PR check, while standalone workflows remain manual-only diagnostics.

## Target Repository
- Owner: Mr-RainbowSmoke
- Repo: brand_kit
- Branch: main

## Required Status Check Policy

### Required check
- Validate quality suite (from .github/workflows/quality-suite.yml)

### Not required (manual-only workflows)
- Release Manifest Check
- Docs Link Check
- Docs Manifest Parity Check
- Markdown Style Check

## GitHub UI Steps
1. Open repository settings.
2. Navigate to Branches.
3. Edit the branch protection rule for main (or create one).
4. Enable Require status checks to pass before merging.
5. In required checks, keep only Validate quality suite.
6. Remove standalone checks from required list.
7. Save changes.

## Verification Checklist
- [ ] quality-suite.yml runs on pull requests to main.
- [ ] quality-suite job name appears as Validate quality suite.
- [ ] standalone workflows are visible and runnable via workflow_dispatch.
- [ ] pull requests are blocked when the quality suite fails required checks.

## Optional GitHub CLI Approach
If GitHub CLI is authenticated with repo admin scope, branch protection can be managed by API calls. This is optional and environment-dependent.

## Rollback Plan
If consolidation causes operational issues:
1. Re-add standalone workflows as required checks in branch protection.
2. Optionally restore pull_request triggers in standalone workflow files.
3. Document rollback in governance/CHANGELOG.md and governance/DECISION_LOG.md.
