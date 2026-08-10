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

---

## External Mirror Sync — Credential Setup

The workflow `.github/workflows/sync-external-mirrors.yml` requires one GitHub Actions secret:

| Secret name | Value |
|---|---|
| `RCLONE_CONFIG` | Full `rclone.conf` file, base64-encoded |

### Step 1 — Install rclone locally
```bash
# macOS
brew install rclone

# Windows (WSL or PowerShell)
curl https://rclone.org/install.sh | sudo bash
```

### Step 2 — Configure each remote interactively

Run `rclone config` and follow the prompts for each remote. Use these remote names exactly — the workflow depends on them:

#### Remote: `sharepoint`
- Choose: `Microsoft OneDrive`
- Auth type: select `Microsoft App` (service principal) or follow browser OAuth
- At the `drive_type` prompt choose: `documentLibrary`
- Navigate to the target SharePoint site and select the `Brand Guide` document library
- SharePoint site URL: `https://djfox8705live.sharepoint.com/sites/BrandGuide`

> For service principal (CI-safe) auth: create an Azure App Registration at portal.azure.com → App registrations. Grant `Files.ReadWrite.All` and `Sites.ReadWrite.All` API permissions (application type, admin consent required). Use the client ID, client secret, and tenant ID when rclone prompts.

#### Remote: `gdrive`
- Choose: `Google Drive`
- Auth: create a service account at console.cloud.google.com → IAM → Service Accounts
- Download the JSON key, then during rclone config choose `service account credentials JSON file` and paste the path
- Share the target Google Drive folder with the service account email address

#### Remote: `dropbox`
- Choose: `Dropbox`
- Follow the browser OAuth flow — rclone will open a browser window for authorization
- Dropbox app registration: apps.dropbox.com → Create app → Full Dropbox access

### Step 3 — Encode and store the config as a GitHub secret
```bash
# After completing rclone config for all three remotes:
cat ~/.config/rclone/rclone.conf | base64 -w 0
```
Copy the output and add it as a repository secret named `RCLONE_CONFIG` at:
`https://github.com/Mr-RainbowSmoke/brand_kit/settings/secrets/actions`

### Step 4 — Verify before first run
```bash
# Test each remote before pushing to CI
rclone lsd sharepoint:
rclone lsd gdrive:
rclone lsd dropbox:
```

### Rotation
When credentials expire or are rotated:
1. Run `rclone config` to update the affected remote
2. Re-encode the config and update the `RCLONE_CONFIG` secret
3. Trigger a manual workflow_dispatch run to verify sync still works
