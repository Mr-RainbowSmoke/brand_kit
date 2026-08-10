# Open Questions

This document contains current decision items for future planning.

## Active Questions

1. Brand role assignment for the 5 new gsl6svi fonts
- Question: `gsl6svi` (Adobe Fonts) was repurposed on 2026-01-07 to host 5 new variable font families — Xanti Typewriter Variable, Aglet Mono Variable, BioRhyme Variable, Grandstander Variable, Scatterplot VF — confirmed present in `RAINBOWSMOKE.cclibs` and documented in fonts/gsl6svi.md and fonts/FONTS_GUIDE.md (Tier 6). None has been assigned a role (body/headline/display/accent) in visual-system/TYPOGRAPHY_SYSTEM.md.
- Needed: Brand owner decision on whether/how to fold these into the typography hierarchy, or to leave them unassigned.
- Discovered: 2026-08-10, during `.cclibs` + live Typekit kit reconciliation.

## Recently Resolved

1. Canonical typography ownership
- Resolved: visual-system/TYPOGRAPHY_SYSTEM.md is policy owner.

2. Release manifest enforcement
- Resolved: Required PR gate now runs via consolidated quality-suite workflow; standalone manifest workflow is manual-only.

3. Docs-manifest parity enforcement
- Resolved: Required PR gate now runs via consolidated quality-suite workflow; standalone parity workflow is manual-only.

4. Markdown style lint baseline
- Resolved: Optional non-blocking style lint runs inside quality-suite for PRs and as manual standalone workflow.

5. Branch protection required-check policy
- Resolved: main now requires only Validate quality suite; standalone checks are manual-only.

6. Standalone workflow operability after demotion
- Resolved: Manual workflow_dispatch smoke tests passed for all standalone validator workflows.

7. Public publishing model
- Resolved: Keep the hub docs-first private for operations and publish external guidance as versioned export kits.
- Source: governance/PUBLICATION_MODEL_RECOMMENDATION.md

8. Legacy file retention strategy
- Resolved: Retain permanently as pointer stubs or scope-bounded companions. No legacy file is ever policy authority.

9. Asset archival timing
- Resolved: Deprecated → Archived after 2 clean release cycles; assets/archive/ folder; eligible for permanent deletion after 12 months with maintainer sign-off.

10. Additional CI guardrails
- Resolved: Current quality suite (manifest, link, parity, style) is sufficient. No additional required checks needed at this time.

11. Tone matrix validation depth
- Resolved: Tone matrix reviewed 2026-08-10. All 5 required contexts have formality, energy, and channel notes. Confidence upgraded to High in SOURCE_CONFIDENCE.md.
