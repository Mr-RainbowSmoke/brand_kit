# RAINBOWSMOKE Brand Guide Hub

Docs-first brand system for RAINBOWSMOKE. This repository now serves as the central hub for both internal creators and external partners.

## Start Here

### If you are internal team or collaborators
1. Read the brand foundation in [foundation/README.md](foundation/README.md).
2. Follow visual rules in [visual-system/README.md](visual-system/README.md).
3. Follow voice rules in [verbal-system/README.md](verbal-system/README.md).
4. Use component and channel guides in [components/README.md](components/README.md) and [applications/README.md](applications/README.md).

### If you are external partners or media
1. Use this hub as the latest reference for approved brand usage.
2. Check asset usage and status in [asset-library/ASSET_INDEX.md](asset-library/ASSET_INDEX.md).
3. Follow accessibility and compliance notes in [accessibility/ACCESSIBILITY_BASELINE.md](accessibility/ACCESSIBILITY_BASELINE.md).

## Hub Sections

- Foundation: [foundation/README.md](foundation/README.md)
- Visual System: [visual-system/README.md](visual-system/README.md)
- Verbal System: [verbal-system/README.md](verbal-system/README.md)
- Accessibility: [accessibility/ACCESSIBILITY_BASELINE.md](accessibility/ACCESSIBILITY_BASELINE.md)
- Components: [components/README.md](components/README.md)
- Applications: [applications/README.md](applications/README.md)
- Asset Library: [asset-library/ASSET_INDEX.md](asset-library/ASSET_INDEX.md)
- Governance: [governance/SOURCE_OF_TRUTH.md](governance/SOURCE_OF_TRUTH.md), [governance/CHANGELOG.md](governance/CHANGELOG.md), [governance/DECISION_LOG.md](governance/DECISION_LOG.md), [governance/RELEASE_NOTES.md](governance/RELEASE_NOTES.md), [governance/DATA_GAPS.md](governance/DATA_GAPS.md), [governance/OPEN_QUESTIONS.md](governance/OPEN_QUESTIONS.md), [governance/SOURCE_CONFIDENCE.md](governance/SOURCE_CONFIDENCE.md)

## Canonical Brand Sources (Current)

- Brand narrative source: [foundation/BRAND_OVERVIEW.md](foundation/BRAND_OVERVIEW.md)
- Voice and tone source: [verbal-system/VOICE_AND_TONE.md](verbal-system/VOICE_AND_TONE.md)
- Color source: [colors/COLOR_GUIDE.md](colors/COLOR_GUIDE.md)
- Typography source: [fonts/FONTS_GUIDE.md](fonts/FONTS_GUIDE.md)
- Asset metadata source: [brand.manifest.json](brand.manifest.json)
- Binary assets: [assets/](assets/)

## Current Implementation Status

### Completed in this phase
- Hub structure scaffolding created.
- Governance and source-of-truth mapping created.
- Accessibility baseline document created.
- Asset indexing framework created.

### In progress
- Consolidating overlapping docs into domain-level canonical sections.
- Adding concrete application playbooks and component standards.
- Building canonical asset mapping for duplicate and near-duplicate variants.

## New Canonical Verbal Docs
- [verbal-system/VOICE_AND_TONE.md](verbal-system/VOICE_AND_TONE.md)
- [verbal-system/TERMINOLOGY_STYLE.md](verbal-system/TERMINOLOGY_STYLE.md)
- [verbal-system/COPY_EXAMPLES.md](verbal-system/COPY_EXAMPLES.md)

## Asset Release Manifests
- [asset-library/SOCIAL_KIT_MANIFEST.md](asset-library/SOCIAL_KIT_MANIFEST.md)
- [asset-library/MEDIA_KIT_MANIFEST.md](asset-library/MEDIA_KIT_MANIFEST.md)
- [asset-library/CREATOR_KIT_MANIFEST.md](asset-library/CREATOR_KIT_MANIFEST.md)
- [asset-library/PRESS_KIT_MANIFEST.md](asset-library/PRESS_KIT_MANIFEST.md)

## Release Validation
Run before publishing any kit bundle:

```bash
python3 scripts/check_release_manifests.py
```

Manual standalone workflow:
- [.github/workflows/release-manifest-check.yml](.github/workflows/release-manifest-check.yml)

## Docs Integrity Validation
Run to validate local markdown links and heading fragments:

```bash
python3 scripts/check_markdown_links.py
```

Manual standalone workflow:
- [.github/workflows/docs-link-check.yml](.github/workflows/docs-link-check.yml)

Optional style linting:

```bash
python3 scripts/check_markdown_style.py
```

Manual standalone workflow (non-blocking):
- [.github/workflows/markdown-style-check.yml](.github/workflows/markdown-style-check.yml)

## Docs-Manifest Parity Validation
Run to validate key canonical docs against manifest values:

```bash
python3 scripts/check_docs_manifest_parity.py
```

Manual standalone workflow:
- [.github/workflows/docs-manifest-parity-check.yml](.github/workflows/docs-manifest-parity-check.yml)

## Consolidated Quality Suite
Run all quality validators together:

```bash
python3 scripts/check_release_manifests.py && \
python3 scripts/check_markdown_links.py && \
python3 scripts/check_docs_manifest_parity.py && \
python3 scripts/check_markdown_style.py
```

Primary required PR check and artifact report:
- [.github/workflows/quality-suite.yml](.github/workflows/quality-suite.yml)

[![Quality Suite](https://github.com/Mr-RainbowSmoke/brand_kit/actions/workflows/quality-suite.yml/badge.svg)](https://github.com/Mr-RainbowSmoke/brand_kit/actions/workflows/quality-suite.yml)

## CI Policy Snapshot

| Check | Local command | Workflow | PR requirement | Trigger policy |
|---|---|---|---|---|
| Quality suite (consolidated) | `python3 scripts/check_release_manifests.py && python3 scripts/check_markdown_links.py && python3 scripts/check_docs_manifest_parity.py && python3 scripts/check_markdown_style.py` | [.github/workflows/quality-suite.yml](.github/workflows/quality-suite.yml) | Required | pull_request + workflow_dispatch |
| Release manifest validator | `python3 scripts/check_release_manifests.py` | [.github/workflows/release-manifest-check.yml](.github/workflows/release-manifest-check.yml) | Manual only | workflow_dispatch |
| Docs link validator | `python3 scripts/check_markdown_links.py` | [.github/workflows/docs-link-check.yml](.github/workflows/docs-link-check.yml) | Manual only | workflow_dispatch |
| Docs-manifest parity validator | `python3 scripts/check_docs_manifest_parity.py` | [.github/workflows/docs-manifest-parity-check.yml](.github/workflows/docs-manifest-parity-check.yml) | Manual only | workflow_dispatch |
| Markdown style lint | `python3 scripts/check_markdown_style.py` | [.github/workflows/markdown-style-check.yml](.github/workflows/markdown-style-check.yml) | Manual only (informational) | workflow_dispatch |

## Working Principles

1. One canonical source per domain.
2. Non-canonical docs must point to canonical sources.
3. Changes must be logged in governance records.
4. Prefer additive migration over destructive cleanup until mapping is complete.

## Legacy Reference Files

Legacy files remain available while migration is in progress:
- [brand.html](brand.html)
- [brand_page.md](brand_page.md)
- [brand-voice-guidelines.md](brand-voice-guidelines.md)
- [typography/BrandTypography.md](typography/BrandTypography.md)
- [colors/](colors/)
- [fonts/](fonts/)

