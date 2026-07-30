# Release Checks

## Manifest Validator

Use this check before publishing Social, Media, Creator, or Press kits.

### What it validates
- Referenced asset files exist in ../assets/
- Deprecated variants are not referenced in release manifests
- Manifests include at least one asset reference

### Run
From repository root:

```bash
python3 scripts/check_release_manifests.py
```

### Exit behavior
- Exit code 0: pass
- Exit code non-zero: fail, fix manifest references before release

## CI Integration
- Workflow file: ../.github/workflows/release-manifest-check.yml
- Trigger: manual workflow dispatch
- Behavior: standalone on-demand manifest check

## Markdown Docs Integrity Validator

Use this check to validate local markdown links and heading fragments.

### What it validates
- Local markdown links resolve to existing files
- Internal heading fragments resolve to existing headings
- External links are ignored by this local check

### Run
From repository root:

```bash
python3 scripts/check_markdown_links.py
```

### CI Integration
- Workflow file: ../.github/workflows/docs-link-check.yml
- Trigger: manual workflow dispatch
- Behavior: standalone on-demand docs-link check

## Markdown Style Lint (Optional)

Use this check to flag style drift in markdown docs.

### What it validates
- No trailing whitespace
- No repeated blank-line runs
- No heading depth jumps (for example H2 to H4)
- Exactly one H1 per markdown file

### Run
From repository root:

```bash
python3 scripts/check_markdown_style.py
```

### CI Integration
- Workflow file: ../.github/workflows/markdown-style-check.yml
- Trigger: manual workflow dispatch
- Behavior: informational only (optional, non-blocking)

## Docs Manifest Parity Validator

Use this check to keep canonical docs aligned with manifest metadata.

### What it validates
- Color guide master-source SHA matches manifest SHA
- Color guide brand name matches manifest brand name
- Key palette hex sequences in COLOR_GUIDE match manifest themes
- Fonts guide brand metadata matches manifest brand metadata
- Fonts guide Typekit project IDs match declared integration links
- Manifest includes required core typography family groups referenced by canonical docs
- Foundation core identity signals remain aligned with manifest identity essence
- Voice-and-tone coverage remains aligned with manifest voice traits and avoid terms
- Terminology baseline remains aligned with canonical brand-name and RS reference usage
- Tone matrix includes required channel contexts (Social, Website, Campaign, Support, Media/Partner)
- Copy examples include required channel contexts with at least one example bullet per context
- Application playbooks emit optional completeness warnings for missing baseline sections/checklists/templates
- Component docs emit optional completeness warnings for missing baseline sections/checklists/templates

### Run
From repository root:

```bash
python3 scripts/check_docs_manifest_parity.py
```

### CI Integration
- Workflow file: ../.github/workflows/docs-manifest-parity-check.yml
- Trigger: manual workflow dispatch
- Behavior: standalone on-demand parity check

## Consolidated Quality Suite

Runs all validators in one CI workflow and publishes a summary report artifact.

### Included checks
- Release manifest validator (required)
- Markdown link validator (required)
- Docs-manifest parity validator (required)
- Markdown style lint (optional/informational)

### CI Integration
- Workflow file: ../.github/workflows/quality-suite.yml
- Trigger: pull requests to main and manual workflow dispatch
- Behavior: primary PR gate; fails only when required checks fail; uploads quality-suite-report artifact on every run
