# RAINBOWSMOKE Brand Guide Hub

Docs-first brand system for RAINBOWSMOKE. This repository now serves as the central hub for both internal creators and external partners.

## Get Started

### I am a designer
1. Understand the brand foundation: [foundation/BRAND_OVERVIEW.md](foundation/BRAND_OVERVIEW.md)
2. Apply the visual system: [visual-system/README.md](visual-system/README.md) — colors, typography, logo rules
3. Use component specs: [components/README.md](components/README.md) — buttons, forms, cards, states
4. Pick up a channel playbook: [applications/README.md](applications/README.md) — web, social, email, video
5. Pull approved assets: [asset-library/ASSET_INDEX.md](asset-library/ASSET_INDEX.md)

### I am a content writer
1. Read brand voice and values: [verbal-system/VOICE_AND_TONE.md](verbal-system/VOICE_AND_TONE.md)
2. Follow terminology and style conventions: [verbal-system/TERMINOLOGY_STYLE.md](verbal-system/TERMINOLOGY_STYLE.md)
3. Use real copy examples by channel: [verbal-system/COPY_EXAMPLES.md](verbal-system/COPY_EXAMPLES.md)
4. Check channel tone for your surface: [applications/README.md](applications/README.md)
5. Review inclusive language: [accessibility/ACCESSIBILITY_BASELINE.md](accessibility/ACCESSIBILITY_BASELINE.md)

### I am a partner or media contact
1. Review approved usage rules: [visual-system/LOGO_AND_ASSET_USAGE.md](visual-system/LOGO_AND_ASSET_USAGE.md)
2. Download release-ready assets: [asset-library/PRESS_KIT_MANIFEST.md](asset-library/PRESS_KIT_MANIFEST.md) or [asset-library/MEDIA_KIT_MANIFEST.md](asset-library/MEDIA_KIT_MANIFEST.md)
3. Check asset status: [asset-library/ASSET_INDEX.md](asset-library/ASSET_INDEX.md)
4. Understand accessibility expectations: [accessibility/ACCESSIBILITY_BASELINE.md](accessibility/ACCESSIBILITY_BASELINE.md)
5. Follow the canonical brand foundation: [foundation/BRAND_OVERVIEW.md](foundation/BRAND_OVERVIEW.md)

## Hub Sections

- Foundation: [foundation/README.md](foundation/README.md)
- Visual System: [visual-system/README.md](visual-system/README.md)
- Verbal System: [verbal-system/README.md](verbal-system/README.md)
- Accessibility: [accessibility/ACCESSIBILITY_BASELINE.md](accessibility/ACCESSIBILITY_BASELINE.md)
- Components: [components/README.md](components/README.md)
- Applications: [applications/README.md](applications/README.md)
- Asset Library: [asset-library/ASSET_INDEX.md](asset-library/ASSET_INDEX.md)
- Governance: [governance/SOURCE_OF_TRUTH.md](governance/SOURCE_OF_TRUTH.md), [governance/CHANGELOG.md](governance/CHANGELOG.md), [governance/DECISION_LOG.md](governance/DECISION_LOG.md), [governance/RELEASE_NOTES.md](governance/RELEASE_NOTES.md), [governance/CONTRIBUTOR_ANNOUNCEMENT.md](governance/CONTRIBUTOR_ANNOUNCEMENT.md), [governance/PUBLICATION_MODEL_RECOMMENDATION.md](governance/PUBLICATION_MODEL_RECOMMENDATION.md), [governance/DATA_GAPS.md](governance/DATA_GAPS.md), [governance/OPEN_QUESTIONS.md](governance/OPEN_QUESTIONS.md), [governance/SOURCE_CONFIDENCE.md](governance/SOURCE_CONFIDENCE.md)

## Canonical Brand Sources (Current)

- Brand narrative source: [foundation/BRAND_OVERVIEW.md](foundation/BRAND_OVERVIEW.md)
- Voice and tone source: [verbal-system/VOICE_AND_TONE.md](verbal-system/VOICE_AND_TONE.md)
- Color source: [colors/COLOR_GUIDE.md](colors/COLOR_GUIDE.md)
- Typography source: [fonts/FONTS_GUIDE.md](fonts/FONTS_GUIDE.md)
- Asset metadata source: [brand.manifest.json](brand.manifest.json)
- Binary assets: [assets/](assets/)

## Implementation Status

### Complete
- Hub architecture: foundation, visual, verbal, accessibility, components, applications, asset library, governance.
- Canonical source-of-truth mapping and ownership across all domains.
- Automated quality suite: manifest, link, parity, and style validators — required PR gate on main.
- Asset indexing and release manifests for social, media, creator, and press kits.
- Deprecated variant register and archival timing policy.
- Governance: decision log, changelog, open questions, source confidence, branch protection runbook.

### In progress
- Expanding component and application docs from scaffolds to full specifications.
- Accessibility contrast matrix against approved palette combinations.
- v1.0 hub launch notes and usability walkthrough.

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

