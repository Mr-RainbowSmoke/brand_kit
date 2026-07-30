# Source Of Truth Map

This file defines canonical ownership per domain to prevent drift.

## Canonical Domains
1. Brand identity narrative
- Canonical source: ../foundation/BRAND_OVERVIEW.md
- Upstream integrated reference: ../brand_page.md
- Supporting source: ../foundation/README.md

2. Verbal system
- Canonical source: ../verbal-system/VOICE_AND_TONE.md
- Upstream integrated reference: ../brand-voice-guidelines.md
- Supporting source: ../verbal-system/README.md
- Related canonical docs:
	- ../verbal-system/TERMINOLOGY_STYLE.md
	- ../verbal-system/COPY_EXAMPLES.md

3. Color system
- Canonical source: ../visual-system/COLOR_SYSTEM.md
- Upstream integrated reference: ../colors/COLOR_GUIDE.md
- Palette files: ../colors/*.md

4. Typography
- Canonical source: ../visual-system/TYPOGRAPHY_SYSTEM.md
- Upstream integrated reference: ../fonts/FONTS_GUIDE.md
- Secondary reference: ../typography/BrandTypography.md

5. Asset metadata
- Canonical source: ../brand.manifest.json

6. Asset binaries
- Canonical source: ../assets/

6a. Asset release manifests
- Canonical sources:
	- ../asset-library/SOCIAL_KIT_MANIFEST.md
	- ../asset-library/MEDIA_KIT_MANIFEST.md
	- ../asset-library/CREATOR_KIT_MANIFEST.md
	- ../asset-library/PRESS_KIT_MANIFEST.md

6b. Deprecated asset tracking
- Canonical source:
	- ../asset-library/DEPRECATED_VARIANTS_REGISTER.md

6c. Asset release validation tooling
- Canonical sources:
	- ../scripts/check_release_manifests.py
	- ../scripts/README.md
	- ../.github/workflows/release-manifest-check.yml

6d. Documentation integrity tooling
- Canonical sources:
	- ../scripts/check_markdown_links.py
	- ../.github/workflows/docs-link-check.yml

6e. Documentation quality and parity tooling
- Canonical sources:
	- ../scripts/check_markdown_style.py
	- ../.github/workflows/markdown-style-check.yml
	- ../scripts/check_docs_manifest_parity.py
	- ../.github/workflows/docs-manifest-parity-check.yml
	- ../.github/workflows/quality-suite.yml
- CI policy:
	- quality-suite.yml is the primary required PR check.
	- standalone workflows are manual-only diagnostic checks.

11. Governance status tracking
- Canonical sources:
	- ../governance/DATA_GAPS.md
	- ../governance/OPEN_QUESTIONS.md
	- ../governance/SOURCE_CONFIDENCE.md
	- ../governance/LEGACY_ARCHIVE_MAP.md
	- ../governance/BRANCH_PROTECTION_RUNBOOK.md

7. Logo and asset usage policy
- Canonical source: ../visual-system/LOGO_AND_ASSET_USAGE.md

8. Hub navigation and discovery
- Canonical source: ../README.md

9. Component patterns
- Canonical sources:
	- ../components/BUTTONS.md
	- ../components/FORMS.md
	- ../components/CARDS.md
	- ../components/STATES.md
	- ../components/NAVIGATION.md
	- ../components/FEEDBACK.md

10. Application playbooks
- Canonical sources:
	- ../applications/WEB.md
	- ../applications/SOCIAL.md
	- ../applications/VIDEO_STREAM.md
	- ../applications/EMAIL.md
	- ../applications/MOBILE.md
	- ../applications/PRINT.md
	- ../applications/MERCH.md

## Governance Rules
- One canonical source per domain.
- Non-canonical duplicates must explicitly point to canonical source.
- Deprecations must be recorded in governance/DECISION_LOG.md.
- Structural changes must be reflected in governance/CHANGELOG.md.

## Next Implementation Tasks
1. Continue canonical extraction from any remaining legacy mixed-content sections.
2. Review application/component completeness warnings and remediate weak sections.
3. Decide whether optional markdown style linting should become blocking.
