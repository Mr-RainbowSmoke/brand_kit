# Release Notes

## 2026-08-10 - v1.0 Brand Guide Hub Launch

### Summary
The RAINBOWSMOKE Brand Guide Hub has reached v1.0 — a comprehensive, docs-first brand system covering identity, visual, verbal, accessibility, component, and channel guidance for both internal creators and external partners.

### What This Hub Covers

**Brand Foundation**
- Brand overview, narrative, and positioning in [foundation/BRAND_OVERVIEW.md](../foundation/BRAND_OVERVIEW.md)

**Visual System**
- Color system with palette, usage bands, and accessibility pairings in [visual-system/COLOR_SYSTEM.md](../visual-system/COLOR_SYSTEM.md)
- Typography system with roles, scale, pairings, and web implementation in [visual-system/TYPOGRAPHY_SYSTEM.md](../visual-system/TYPOGRAPHY_SYSTEM.md)
- Logo and asset usage policy in [visual-system/LOGO_AND_ASSET_USAGE.md](../visual-system/LOGO_AND_ASSET_USAGE.md)

**Verbal System**
- Voice and tone with tone-by-context matrix in [verbal-system/VOICE_AND_TONE.md](../verbal-system/VOICE_AND_TONE.md)
- Terminology and style conventions in [verbal-system/TERMINOLOGY_STYLE.md](../verbal-system/TERMINOLOGY_STYLE.md)
- Copy examples by channel in [verbal-system/COPY_EXAMPLES.md](../verbal-system/COPY_EXAMPLES.md)

**Accessibility**
- WCAG AA baseline, approved contrast pairings, forbidden pairings, inclusive language rules in [accessibility/ACCESSIBILITY_BASELINE.md](../accessibility/ACCESSIBILITY_BASELINE.md)

**Components**
- Buttons, forms, cards, navigation, states, and feedback patterns with color guidance, do/don't tables, and QA checklists in [components/](../components/)

**Application Playbooks**
- Web, social, email, video/stream, mobile, print, and merch — each with required asset variants, layout/safe-zone specs, copy tone, do/don't tables, and starter templates in [applications/](../applications/)

**Asset Library**
- Asset index, release manifests (social, media, creator, press), and deprecated variants register in [asset-library/](../asset-library/)

**Governance**
- Canonical source-of-truth mapping, decision log, changelog, open questions, source confidence, and publication model in [governance/](../governance/)

**Quality Gates**
- Automated PR gate via consolidated quality-suite workflow requiring manifest, link, parity, and style checks

### Known Limitations (v1.0)
1. Tone-matrix confidence is Medium for some channels — a dedicated content review cycle is planned to upgrade to High.
2. Accessibility contrast matrix covers approved pairings but min font-size and motion timing tables are not yet complete.
3. GitHub mirror synchronization has not been performed — external mirrors may lag canonical hub values.
4. Legacy shipped assets (website builds, older packages) may still reflect pre-hub palette snapshots.

### Next-Iteration Backlog
1. Tone matrix content review cycle to upgrade confidence ratings.
2. Min font-size and spacing tables per channel (accessibility/ACCESSIBILITY_BASELINE.md).
3. Motion timing guidance and reduced-motion reference examples.
4. GitHub mirror sync from canonical hub sources.
5. Legacy shipped asset reissue strategy and phase plan.
6. Usability walkthroughs for designer, writer, and partner audiences.

### Contributor Impact
- The hub is now the authoritative source for all brand decisions.
- Legacy files (brand_page.md, brand-voice-guidelines.md) are retained as reference-only stubs with pointers to canonical sources.
- All PRs to main require quality suite to pass.

---

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
