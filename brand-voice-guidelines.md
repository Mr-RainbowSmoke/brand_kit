# RAINBOWSMOKE (Mr. RainbowSmoke LLC) Brand Guidelines

## Generation Metadata
- Created: July 28, 2026
- Version: 4 (July 29, 2026 — owner uploaded a fresh `.cclibs` export; re-verified against repo, no content changes)
- Replaces: v3 (July 28, 2026, same-day)
- Sources: Project brand files, Notion workspace, SharePoint/OneDrive, Dropbox (RAINBOWSMOKE.cclibs Adobe CC Library + live production website export), Canva
- Documents/assets processed: 14 documents + 1 Adobe CC Library (135 assets: 6 color themes, 40 font variants, ~40 image/icon/logo assets, 1 gradient)
- Discovery report used: Yes (expanded with the .cclibs library and reconnected Dropbox)
- Overall confidence: **High** — visual identity (color/type/logo) is fully reconciled by owner decision; brand voice remains the thinner section, drawn mostly from the live website and one archived template

**v4 change log (re-verification, 2026-07-29):**
- Owner uploaded a new `RAINBOWSMOKE.cclibs` export (sha256 `67b45ed4…`, previously `9cf14206…`).
- Full diff against the repo: extracted the manifest, then compared every color theme's swatches, all 44 font entries (name/family/style/typekit ID), and all 44 image assets by per-file SHA-256 of the actual embedded bytes (not just manifest metadata, which omits sha256 for some aliased components).
- **Result: zero content differences.** Same 6 themes with identical hex values, same 44 fonts, same 44 images byte-for-byte, same gradient. The only thing that changed was the outer zip container's hash — consistent with Adobe re-exporting the library rather than any edit.
- `brand.manifest.json`'s `brand.source` block updated to record the new sha256/export date; prior sha256 kept as `priorSha256` for traceability. No color/font/asset files needed changes.

**v3 change log (owner-confirmed decision):**
- `.cclibs` is confirmed as the **master source of truth** — its hex values now supersede `COLOR_GUIDE.md` for Pride, Demiboy, and Demisexual.
- This creates a **known, accepted gap**: the currently-shipped Logo Package v1.0.0-beta and the live website were built against the old `COLOR_GUIDE.md` hex values. They are not being retroactively recolored automatically — see Data Gaps.

**v2 change log (owner-confirmed decisions):**
- Adopted **royalty** and **Cotton Candy** as official secondary palettes (from `.cclibs`)
- Adopted all 15 additional font weights and 5 new typefaces found in `.cclibs` as approved

---

## Executive Summary

RAINBOWSMOKE (d.b.a. Mr. RainbowSmoke LLC) is a social media/content creator network built around live streaming (YouTube, Twitch, TikTok) and creative content, positioned as "your bold rainbow brand for live entertainment and creative content." The brand identity is loud, warm, and maximalist rather than minimal: realistic billowing smoke effects, animated network nodes, and bold display typography (Rig Solid, Elliott's Collection) sit on top of a Pride-rooted, blue-forward color system (~40% blue, ~10% purple) that founder Rainbow has consistently steered toward blue while keeping full Pride-spectrum integrity. The voice — drawn from the live rainbowsmokeofficial.com site — is inclusive, community-driven, and unapologetically colorful: "we believe in the power of community and the magic that happens when people come together to share their passions," building "a space where everyone feels welcome to be their true, colorful selves."

Content should read as energetic and inviting rather than corporate; visuals should feel photographic/realistic (real smoke, real texture) rather than flat or minimal, always on dark backgrounds.

---

## We Are / We Are Not

| We Are | We Are Not |
|--------|------------|
| **Bold & maximalist** — realistic smoke, animated nodes, loud display type | **Minimal or flat** — we don't default to clean flat-design shortcuts |
| **Inclusive & authentic** — "welcome to be their true, colorful selves" | **Generic or sanitized** — no boilerplate diversity language without substance |
| **Blue-forward Pride** — blue dominates (~40%) while the full Pride spectrum stays intact | **Purple-forward or muted** — purple is capped at ~10%, an accent only |
| **Community-first** — streaming, creator network, "building meaningful connections" | **Transactional or platform-first** — the community is the point, not the tech |
| **Energetic & warm** — "vibrant," "magic," "bold" | **Flat corporate tone** — avoid stiff, formal B2B phrasing |

### Voice Attributes Detail

#### Bold & Maximalist
- **What it means:** Visuals lean into realism and drama — billowing smoke with layered colors and heavy blur, animated pulsing network nodes, thick display fonts (Rig Solid Bold Fill, Elliott's Jigsaw Dropshadow) — never restrained or minimal.
- **How it shows up:** Logo package explicitly built with "realistic smoke" over "line wisps," CSS animations for flowing smoke, dark backgrounds as the default canvas.
- **What to avoid:** Flat vector icon treatments, pastel restraint, quiet typography.
- **Evidence:** Logo Package v1.0.0-beta spec ("Realistic Smoke... heavy blur for photographic effect"); user's stated preference for "realistic, bold design aesthetics over minimal approaches."
- **Confidence:** High

#### Inclusive & Authentic
- **What it means:** Diversity and self-expression are treated as lived values, not decoration.
- **How it shows up:** Live site copy: "celebrate diversity, creativity, and authentic self-expression"; values list includes Authenticity ("being true to ourselves") and Inclusivity ("welcoming space... regardless of background").
- **What to avoid:** Generic "we support diversity" filler without the community/creator framing.
- **Evidence:** rainbowsmokeofficial.com `/about` page (live production copy, high confidence).
- **Confidence:** High

#### Blue-Forward Pride
- **What it means:** The brand deliberately skews the traditional Pride rainbow toward blue, while keeping every stripe present.
- **How it shows up:** Logo package: "~40% blues, ~10% purples... Blue-forward: Emphasizes blue spectrum while maintaining Pride rainbow integrity."
- **What to avoid:** Even color distribution across the spectrum, or purple-heavy compositions.
- **Evidence:** Logo Package v1.0.0-beta; matches Rainbow's documented preference for blue.
- **Confidence:** High

#### Community-First
- **What it means:** The product is the creator network and the people in it, not the streaming tech.
- **How it shows up:** "What We Do" site section frames YouTube/Twitch/TikTok as channels for community, not the offering itself; values include Community ("supporting each other") and Excellence ("quality in everything we create").
- **Evidence:** rainbowsmokeofficial.com `/about`.
- **Confidence:** High

---

## Brand Personality

- **Archetype:** The Ringleader — a warm, larger-than-life host who makes everyone feel like part of the show.
- **If our brand were a person:** Someone hosting a colorful, high-energy livestream who genuinely means it when they say everyone's welcome — bold on camera, sincere off it.
- **Core values expressed in voice:** Authenticity, Inclusivity, Creativity, Community, Excellence (site's own stated values list).

---

## Visual Identity

### Color System — `.cclibs` is master (v3)

**Core palettes** — canonical values now sourced from `RAINBOWSMOKE.cclibs` (Adobe CC Library, confirmed master source of truth):
- Pride: `#FF0000` `#FF8E00` `#FFED00` `#008026` `#004CFF` `#400098`
- Demiboy: `#7F7F7F` `#C4C4C4` `#9DD7EA` `#FFFFFF`
- Demisexual: `#000000` `#FFFFFF` `#6E0070` `#D2D2D2`

**⚠️ Known gap — not yet reconciled:** `COLOR_GUIDE.md` (and its SharePoint/Notion mirrors) still document the old hex set (Pride `#FF0018/#FFA52C/#FFFF41/#008018/#0000F9/#86007D`; Demiboy `#7F7F7F/#C4C4C4/#FFFFFF/#9AD9EB`; Demisexual `#000000/#808080/#FFFFFF/#800080`), and both the shipped **Logo Package v1.0.0-beta** and the **live rainbowsmokeofficial.com site** were built against those old values. Nothing has been recolored yet — see Data Gaps for recommended next steps (update `COLOR_GUIDE.md` and mirrors to match master; decide whether existing shipped assets get reissued).

**Secondary palettes — adopted from `.cclibs`:**
- **Royalty** — `#0903A6` `#0F1AF2` `#1B3BF2` `#798BF2` `#F2F2F2`. A heavily blue, near-monochromatic palette. Suggested role: premium/campaign moments, blue-forward emphasis pieces, dark-mode UI accents — reinforces the brand's blue-forward Pride positioning.
- **Cotton Candy** — `#FCA8D8` `#A1A8E5` `#B2B3ED` `#ABCDF3` `#D2DFF2`. Soft pastel palette. Suggested role: lighter/softer contexts — community spotlights, merch, seasonal or celebratory content — as a deliberate contrast to the brand's usual bold/dark treatment.
- **Pride Extended** (8-color, adds `#00C0C0` cyan and `#8E008E` magenta to the standard spectrum) — remains **not yet adopted**; it duplicates the role of the core Pride palette without a clear separate use case. Revisit if a specific need comes up.
- Plus one custom linear gradient ("pride-flag-style-animation") used for smoke/animation effects — already in active use via the logo package.
- **Royalty** — `#0903A6` `#0F1AF2` `#1B3BF2` `#798BF2` `#F2F2F2`. A heavily blue, near-monochromatic palette. Suggested role: premium/campaign moments, blue-forward emphasis pieces, dark-mode UI accents — reinforces the brand's blue-forward Pride positioning.
- **Cotton Candy** — `#FCA8D8` `#A1A8E5` `#B2B3ED` `#ABCDF3` `#D2DFF2`. Soft pastel palette. Suggested role: lighter/softer contexts — community spotlights, merch, seasonal or celebratory content — as a deliberate contrast to the brand's usual bold/dark treatment.
- **Pride Extended** (8-color, adds `#00C0C0` cyan and `#8E008E` magenta to the standard spectrum) — remains **not yet adopted**; it duplicates the role of the core Pride palette without a clear separate use case. Revisit if a specific need comes up.
- Plus one custom linear gradient ("pride-flag-style-animation") used for smoke/animation effects — already in active use via the logo package.

### Typography
Approved system (confirmed consistent across `FONTS_GUIDE.md`, `BrandTypography.md`, Notion Typography System, and in production use on rainbowsmokeofficial.com via the `gsl6svi.css` Typekit link):

| Font | Role | Weights documented |
|---|---|---|
| Transat | Primary body | 400, 700 |
| Le Havre Rounded | Secondary body / UI | 400, 700 |
| Omnes Narrow | Primary headline | 900 (Black) |
| Chennai | Editorial headline | 700 (Bold) |
| Rig Solid (Bold Fill / Bold Inline / Medium Outline) | Display | — |
| Elliott's Collection (Blue Eyeshadow / Jigsaw Dropshadow) | Statement, max 1 per design | — |
| Sketchnote Text | Accent (quotes, captions) | 400, 700 |
| Olivita | Accent (pull quotes) | 400 italic |
| Kegger Collegiate, Kegger US, Backstroke, Perec Scripte Deco, Sketchnote Square | Restricted / situational | — |

### Typography — newly adopted additions (v2)

**Extended weights for existing approved families** (adds finer control within already-approved roles; use the same role rules as the base family above):
- Transat: + Light, Light Oblique, Medium, Medium Oblique, Standard, Standard Oblique, Bold Oblique, Black, Black Oblique
- Le Havre Rounded: + Light, Thin Italic
- Chennai: + Thin, Light Oblique
- Omnes (Pro): + ExtraLight Italic

**Five newly adopted typefaces** (new roles — use deliberately, these are distinctive additions to the system):

| Font | Foundry | Suggested role |
|---|---|---|
| **Aglet Mono VF** (Regular, Italic) | XYZ Type | Code/technical contexts — dev docs, Cloudflare Workers/Wrangler snippets, terminal-style UI moments |
| **Xanti Typewriter VF ExtraBold** (+ Italic) | CAST | Retro/typewriter accent — behind-the-scenes captions, "leaked memo" style social posts, an alternative to the sports-only Kegger fonts for general retro use |
| **BioRhyme ExtraBold** | Google Fonts | Serif slab display alternative — editorial statement headlines when Chennai/Omnes feel too clean |
| **Grandstander** (Thin, Thin Italic) | Google Fonts | Playful/rounded display accent — lighter-touch social graphics, community/fan content |
| **Scatterplot VF Light** | CAST, designer Giulio Galli | Experimental/variable display accent — use sparingly for one-off creative moments, similar spirit to Elliott's Collection |

*These were unused/undocumented in the shipped Logo Package and website — treat as available starting now, not as retroactively applied to existing assets.*

### Logo & Icon System (Logo Package v1.0.0-beta, current/canonical)
- **Main Wordmark:** "RAINBOWSMOKE" in Rig Solid Bold Fill with realistic rainbow smoke + network nodes. For banners/headers/YouTube/Twitch.
- **Jigsaw Alternative:** Same wordmark in Elliott's Jigsaw Dropshadow for high-impact campaigns.
- **RS Profile Icon:** Bold "RS" monogram with smoke, sized for TikTok/YouTube/Twitch/Instagram profile pictures (512/256/128/64px).
- Always on **dark/black backgrounds**; minimum 64px height (icons) / 200px width (wordmarks); 20px minimum padding; do not recolor.
- The `.cclibs` library additionally contains: a "Light" profile variant, a dark-transparent overlay profile, micro overlay icons (64–512px, SVG+PNG), and a "Micro Smoke Loop" animation asset — these extend the documented package and appear production-ready (organized under Adobe library groups: Profiles, Icons, Backgrounds, Animations, Logos).

---

## Tone-by-Context Matrix

| Context | Formality | Energy | Notes |
|---|---|---|---|
| Social media | Low | High | Casual, fun, engaging |
| Website | Medium | Medium-High | Professional yet friendly (confirmed by live site copy) |
| Marketing / campaigns | Medium | High | Inspiring, action-oriented |
| Customer / creator support | Medium | Warm | Helpful, empathetic |
| Media kit / outreach emails | Medium-High | Medium | See SharePoint message template — leads with what's included, stays brief |

*Confidence: Medium. The tone descriptors above come from an Archived, largely-template Notion "Brand Kit" doc — the categories are plausible and consistent with the live site's actual tone, but weren't independently corroborated by additional sources.*

---

## Terminology Guide

| Term | Usage |
|---|---|
| RAINBOWSMOKE | All-caps brand/wordmark name |
| Mr. RainbowSmoke | The person/persona behind the brand; "d.b.a Mr. RainbowSmoke LLC" |
| RAINBOWSMOKE LLC | Legal entity name |
| Creator network | How the business describes itself (not "platform" or "agency") |
| RS | Approved short/monogram form, icon use only |

---

## Confidence Scores

| Section | Confidence | Basis |
|---|---|---|
| Color System | High | `.cclibs` confirmed as master (v3); royalty + Cotton Candy adopted (v2). Known gap: shipped assets not yet updated to match |
| Typography | High | 4+ corroborating sources, confirmed in production CSS; extended weights/typefaces adopted by owner decision (v2) |
| Logo/Icon System | High | Shipped v1.0.0-beta spec + matching canonical library assets |
| Brand Voice / Values | High | Live production website copy |
| Tone-by-Context | Medium | Single archived template source |
| Terminology | Medium | Consistent across sources but never formally documented as a glossary |

---

## Open Questions for Team Discussion

### Resolved in v3
6. ~~Whether `.cclibs` or `COLOR_GUIDE.md` governs core hex values~~ — **Decided:** `.cclibs` is confirmed master; its Pride/Demiboy/Demisexual hex values now govern. `COLOR_GUIDE.md` and mirrors are out of date and should be updated to match (see Data Gaps).

### Resolved in v2
1. ~~Which color hex values are canonical~~ — **Decided:** `royalty` and `Cotton Candy` adopted as new secondary palettes. `pride_extended` left unadopted (no clear use case yet — revisit if one comes up).
2. ~~Should the extra `.cclibs` font weights/typefaces be approved?~~ — **Decided:** all 15 extra weights and 5 new typefaces adopted; see Typography section above for suggested roles.

### Medium Priority
3. **Brand voice is thin.** Only the live website and one archived template speak to tone. Consider a short working session to formalize tone-by-context guidance so it isn't resting on a single source.
4. ~~Figma coverage gap~~ — **Not applicable:** confirmed there's no Figma account for this brand.
5. **Existing shipped assets are off-palette.** The Logo Package v1.0.0-beta and live website use the old hex values. Follow-up meeting scheduled Thu July 30 to decide reissue vs. phase-out.
6. **GitHub mirror (`Mr-RainbowSmoke/brand_kit`) still has the old hex values.** No connector available to update it directly — corrected file provided for manual paste into `colors/COLOR_GUIDE.md`.

---

## Data Gaps & Recommendations

- [x] Resolve the color conflict — done in v3 (`.cclibs` confirmed master for all hex values; royalty + Cotton Candy adopted in v2).
- [x] Confirm the extra `.cclibs` font weights/typefaces — done in v2 (all adopted, roles assigned).
- [x] Update `COLOR_GUIDE.md` and its SharePoint mirrors to match the new master hex values — both SharePoint copies (`brand_kit/colors/` and `rainbowsmokev1/colors/`) updated directly. No Notion mirror existed to update (only an unrelated Archived template).
- [ ] **GitHub mirror not yet updated:** `github.com/Mr-RainbowSmoke/brand_kit` (`colors/COLOR_GUIDE.md`, `fonts/FONTS_GUIDE.md`, `brand_page.md`) is a third documentation mirror, discovered via Notion's connected-source search. No GitHub connector is available, so this wasn't updated automatically — the corrected `COLOR_GUIDE.md` content has been provided as a file for manual paste. Worth noting: `brand_page.md` in that repo already references `.cclibs` as canonical, so it may be ahead of where SharePoint/Notion were.
- [x] Decide whether the Logo Package v1.0.0-beta and live website get reissued/recolored — **follow-up scheduled:** "RAINBOWSMOKE Website Redesign Follow-up," Thu July 30, 2:00–3:00 PM.
- [ ] Formalize a short brand-voice/tone document beyond the current template + website copy.
- [x] ~~Re-check Figma once a usable connector/tool is available~~ — not applicable; no Figma account exists.

---

## Appendix: Sources

| # | Source | Platform | Type | Date | Confidence |
|---|--------|----------|------|------|------------|
| 1 | COLOR_GUIDE.md, pride/demiboy/demisexual.md | Project files / SharePoint / Notion | SUPERSEDED (v3) — now out of date, needs updating to match master | Jan 5, 2026 | Low (superseded) |
| 2 | FONTS_GUIDE.md, BrandTypography.md | Project files / SharePoint / Notion | AUTHORITATIVE (documented), extended by #4 | Jan 5, 2026 | High |
| 3 | RAINBOWSMOKE_Logo_Package_v1.0.0-beta | Notion | SHIPPED — built on now-superseded colors, not yet reconciled | Jan 5–6, 2026 | Medium |
| 4 | RAINBOWSMOKE.cclibs (Adobe CC Library) | Dropbox / user upload | **MASTER / SOURCE OF TRUTH (confirmed)** | Jan 17, 2026 | High |
| 5 | rainbowsmokeofficial.com (about, index, etc.) | Dropbox (static export) | LIVE PRODUCTION — built on now-superseded colors, not yet reconciled | Jan 19, 2026 | Medium |
| 6 | RAINBOWSMOKE Brand Kit | Notion (Archive) | TEMPLATE / draft, generic colors — colors superseded by #1 | Jan 7, 2026 | Low (colors) / Medium (voice/tone) |
| 7 | RAINBOWSMOKE BRAND GUIDLINES | Notion (Retired) | RETIRED — explicitly marked non-authoritative | Dec 12, 2025 | N/A |
| 8 | CANVA_README.txt | SharePoint / Dropbox | OPERATIONAL (asset import guide) | Jan 7, 2026 | Medium |
| 9 | Message Templates (media kit outreach) | SharePoint | OPERATIONAL (voice sample) | Jan 28, 2026 | Medium |

---

*Guideline generated via `/brand-voice:discover-brand` + `/brand-voice:guideline-generation`. Not yet saved to a persistent working folder — this session is a browser-based chat, not a Claude Code project, so the file is provided as a download below rather than at `.claude/brand-voice-guidelines.md`.*
