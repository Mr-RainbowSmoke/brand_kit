# Contributor Announcement Pack

Use these templates to communicate the completed CI governance migration.

## PR Comment Template

### CI Policy Update: Quality Suite Is Now the Primary Required Check

We completed the CI governance migration for this repo.

What changed:
- Pull requests to main are now gated by one required check: Validate quality suite.
- Standalone validator workflows remain available as manual diagnostics.

Primary required workflow:
- .github/workflows/quality-suite.yml

Manual-only workflows:
- .github/workflows/release-manifest-check.yml
- .github/workflows/docs-link-check.yml
- .github/workflows/docs-manifest-parity-check.yml
- .github/workflows/markdown-style-check.yml

Operational notes:
- Branch protection has been updated to require only Validate quality suite.
- Standalone manual workflows were smoke-tested successfully.
- Release details are documented in governance/RELEASE_NOTES.md.

## Team Chat Template

CI update completed for brand_kit:
- Required PR gate is now Validate quality suite.
- Individual validator workflows are manual-only for diagnostics.
- Branch protection is aligned to this policy.
- Standalone workflow smoke tests all passed.

Details:
- governance/RELEASE_NOTES.md
- governance/BRANCH_PROTECTION_RUNBOOK.md

## Short Email Template

Subject: brand_kit CI policy update complete

Team,

The CI policy migration is now complete in brand_kit.

Effective immediately:
- Required PR check on main: Validate quality suite.
- Standalone checks are manual-only diagnostics.

Branch protection has been updated and manual workflow smoke tests passed.

Reference docs:
- governance/RELEASE_NOTES.md
- governance/BRANCH_PROTECTION_RUNBOOK.md

Thanks.
