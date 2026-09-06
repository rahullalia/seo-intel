# log.md - hey-tony-insiders

Capture + synthesis of **HeyTony Insiders** (htinsiders.com), Matt Diamante's paid SEO
coaching membership. This is the ongoing continuation of **Rank Week 2026** (see
`../rankWeek2026/`). Goal: learn the full method and ship a working `/heyTony` skill.

## 2026-08-21 21:12 PT - Page Types Master + email tips (all page types, pure Matt canon)

Rahul asked for everything Matt teaches about building each page type (service/money pages, homepage, about, contact, pricing, FAQ, blog, portfolio, testimonials, legal, landing, cross-page elements): structure, layout, design, visuals, length, keyword density, other considerations, plus his email tips. Built two reference docs:

- `page-types/` folder (index `README.md`): one file per page type (`00-rules-for-every-page.md`, `01-homepage.md` ... `14-cross-page-elements.md`, plus `15-what-the-emails-add.md`, `16-source-index-124-calls.md`), the single-file build `page-types/page-types-master.md` (88.5k words): Part A universal per-page spec + governing rules + numbers table + disagreements; Part B one chapter per page type (19 chapters, identical sub-headings so page types compare side by side; every bullet cited to call / course lesson / playbook section / book chapter / email date); Part C email summary + source index of all 124 calls. Service-page file is complete on its own and routes to `../service-page-master.md` for the verbatim prompts.
- `page-types/heytony-email-tips.md` (6.1k words): every tip, prompt, checklist and template from the 190 matt@heytony.ca emails (lalia@rsla.io, Jun 2025 to Aug 2026), dated index included. Emails are ~30% tips, ~70% promos; the page-relevant gold is the internal Content Checklist, the keyword-placement rule, the Rank Week audit/rewrite/internal-link prompts, the Topic Gap Analysis prompt, and the Update & Boost method.

Sources read in full: all 124 transcripts (1.21M words), 74 curriculum lessons, `hey-tony-playbook.md`, *Get Found* (pdftotext of `../rank-week-2026/resources/downloads/getFoundBookV2.pdf`, 55k words), 190 emails. Pipeline: 12 transcript + curriculum + playbook + book digest agents (one page-type digest each, saved in the session scratchpad), split by page-type heading, 7 reducer agents (one chapter group each; last four re-run on Sonnet with word caps after Mac-sleep interruptions killed the first runs), scripted assembly (`assemble.py`) and QA (dash sweep, heading numbering). The digests are kept in `page-types/research/` (transcript digests A to L, curriculum, playbook, book, email batches) for provenance.

Gotchas: long background agents die when the Mac sleeps (caffeinate -dims helped once the lid stayed open); agents told to write after every section survive interruptions. Known source tensions are recorded in each chapter's "Where the sources are thin or disagree" (accordion FAQs, schema, word-count floors, homepage title order, location-page uniqueness standard).

## 2026-07-22 - Service-page master doc (pure Matt canon)

Rahul deferred the fresh design pass (webDesignMaster Phase 1 was underway; he redirected away from designing for now) and asked instead for ONE master document compiling everything Matt/HeyTony teaches about a service page: elements, visuals, kinds of visuals, metrics, FAQs, SEO-first. Distinct from `servicePageDesignGuide.md` in that it is PURE course canon (no external 2026 research), organized around his list.

Pulled the last unread Matt sections for completeness: Part III money-page audit (5-step pageaudit.com workflow, competitor-benchmark, common flagged fixes, the full threshold table), Part II two-prompt rewrite, Part VI tool + verbatim prompt library. Output: `servicePageMaster.md` (10 sections incl. the exact rewrite/tags/internal-link prompts, the tool list, and the SEO threshold table).

Consolidated to ONE file per Rahul: folded the 2026 external research into `servicePageMaster.md` as section 11 (clearly separated from the Matt canon in sections 1 to 10), then deleted `servicePageDesignGuide.md` and the rejected `rslaWebsite/docs/seo/servicePageDesignSystem.md`. `servicePageMaster.md` is now the single service-page reference. The rsla.io-specific application section (finish-the-migration, current-site FAQ/image notes) was dropped as stale given the planned fresh redesign; re-add an rsla.io section when that design happens.
## 2026-07-21 - Data acquisition

Logged into htinsiders.com (Rahul's paid annual membership) via Chrome DevTools. The platform
is built on **membership.io**; video is HLS on `cdn.membership.io`, and every file exposes a
machine transcript at `app.membership.io/file/{hash}/embed/caption?type=vtt`. Rather than pull
~85GB of video, extracted the **transcripts as text** (Rahul's call: transcripts + resources,
no video archive).

**Extraction mechanics (for future updates):**
- Enumerate a playlist: `GET htinsiders.com/api/hub/JkjwBkopdD/{playlistHash}/files?page=N&sort=position` (same-origin fetch; hub = `JkjwBkopdD`).
- Pull a transcript: `GET app.membership.io/file/{fileHash}/embed/caption?type=vtt` - **must be fetched from an `app.membership.io` top-level origin** (CORS blocks it from htinsiders.com). Cookies (`membershipio_session`, httpOnly) are carried automatically in-browser, so run the fetch loop via chrome-devtools `evaluate_script` on an `app.membership.io` tab. No cookie extraction needed.
- Call Replays playlist hash: `NjLAZpDgOq`. Video Training page loads 8 curriculum playlists.

**Captured** (all under this folder):

| Set | Count | Words | Location |
|---|---|---|---|
| Call Replays | 124 / 125 | ~1.20M | `transcripts/` (clean `.txt`), `transcriptsRaw/` (`.vtt`) |
| Video Training curriculum | 74 / 74 | ~52K | `curriculum/` |
| Tool/resource references | 5 tools | - | `resources.md` |

- 1 call replay ("Technical SEO with Denroi 29.01.2026") genuinely has no transcript on the platform - skipped.
- `inventory.json`, `curriculumInventory.json` - full manifests (title, hash, duration, AI summary).
- `summaries.md` - all 124 membership.io auto-summaries, quick-reference.
- Call replays carry **no downloadable attachments** (video + transcript only). Matt's 5 member tools are custom web apps (Railway / Zapier) - logic lives server-side; the workflows behind them are demoed in the Work Session transcripts. See `resources.md`.

## 2026-07-21 - Synthesis (done)

Map-reduce over the transcripts → master playbook `heyTonyPlaybook.md` (**53k words, 6 Parts**),
mirroring `../rankWeek2026/rankWeekPlaybook.md` but full-curriculum. Full-parallel extraction
(Rahul's call). Multi-agent workflow `build/synthesisWorkflow.js` (regenerate via the Python
planner that emits `build/build_plan.json`):
- **Extract** - 124 agents (sonnet), one per call → dense faithful digest in `build/extractions/`.
- **Reduce** - 14 agents (sonnet) → per-category syntheses in `build/syntheses/` (foundations reducers read the raw short curriculum directly).
- **Compose** - 6 agents (opus), one per theme cluster → `build/themes/`.

Run: 144 agents, 0 errors, ~16.4M subagent tokens, ~62 min. Theme 04 silently failed its Write
(agent returned OK, no file) → regenerated with one direct opus agent. Assembly gotcha: a
`\s-\s` sanitize regex ate newlines and merged ~800 bullet lines; fixed to only convert em/en
dashes (workspace rule) and leave newlines alone. Final playbook: 2137 lines, 7 H1s, 0 em/en dashes.

Parts: I Philosophy/System · II Keywords/Content · III On-Page/Money-Pages ·
IV Technical/Web-Design/Internal-Linking · V Off-Page/AI-Search · VI Tools/Local/Ecom/Mindset.

## 2026-07-21 - Skill shipped

`/heyTony` skill built and installed:
- `myBusiness/skills/skills/heyTony/SKILL.md` (operator's manual: the 5 governing rules, the
  cadence/patience number table, 6 core workflows incl. the "why doesn't it rank" diagnosis, a
  task→Part router) + `reference/heyTonyPlaybook.md` (copy of the master playbook).
- Symlinked `~/.claude/skills/heyTony` → the skill dir (single source of truth; no stray copies).
- Positioned as the strategy/decision layer; composes with `seoForge` (infra build) and
  `blogEngine` (rsla.io writing), which execute what heyTony decides.

**To update** as new daily calls drop: run `updateHeyTony.md` (the runbook) in any Claude session
with the logged-in browser. It uses `build/deltaDetect.py` to diff a fresh playlist listing against
`inventory.json` (detects new calls by hash, not by date, so skipped weeks are fine), pulls only new
transcripts, folds them into the relevant playbook Part incrementally, and re-copies the playbook
into the skill's `reference/`. Validated 2026-07-21 (0-new and 1-new cases).

## 2026-07-21 - Triggering + scheduling decisions

- **Triggering:** hardened the skill `description` by expert review (front-loaded the trigger, added
  explicit sibling-skill routing) and saved a 20-query trigger eval set at
  `skills/heyTony/evals/triggerEvals.json`. Did NOT run skill-creator's automated optimizer:
  `run_loop.py` needs a standalone `ANTHROPIC_API_KEY` (not set) for its improve step, and
  `run_eval.py`'s headless harness can't cleanly measure an already-installed skill (it looks for a
  unique `heyTony-skill-<id>` name but the model invokes the real `heyTony`, so it read 0/3 on a
  clear trigger - a measurement artifact). To run it properly later: set an API key AND temporarily
  remove the `~/.claude/skills/heyTony` symlink for a clean measurement.
- **Scheduling:** true hands-off auto-update is NOT possible here - the content lives in the
  local-only umbrella (no remote for a cloud env to clone) and the pull needs the local
  authenticated browser. Cloud routines (schedule skill) have neither; CronCreate and /loop are
  session-only. Decision: no auto-scheduler; updates run on-demand via the runbook (Rahul's call).

## 2026-07-21 - Skill validated via skill-creator eval loop

Ran skill-creator's task-eval loop (the step originally skipped): 3 realistic SEO tasks
(new-client game plan, ranking diagnosis, money-page + AI citation), each with `/heyTony`
vs a no-skill baseline (6 agents). Verdict: with-skill outputs faithfully executed Matt's
method (one-keyword-per-page, match-lowest-of-top-3, GSC exclusion-reason fixes, internal-link
case evidence, patience windows, CID link, review velocity, AEO/GEO controllable signals) and
were materially more specific/faithful than baseline. Self-sufficient for RSL/A's core (local/
SMB/B2B service SEO). Added an "Edges of the method" section to SKILL.md so it's honest about
thin areas (ecommerce-at-scale, enterprise technical, international, deep schema→seoForge).
Trigger eval set at `skills/heyTony/evals/triggerEvals.json`. Rahul reviewed: trusts the read.

## 2026-07-21 - Service-page design guide (derived deliverable)

Rahul asked for everything Matt says about web design for SEO, plus research, synthesized into "how should a service page be designed" (general + rsla.io). Extracted the playbook's design material (Part III money-page structure/CTAs/location pages, Part IV web-design principles/typography/page-builder/mobile/internal-linking, Part V AEO on-page) and ran 3 parallel agents: 2 web-research (structure+length; visuals+FAQ+schema+AEO) and 1 mapping rsla.io's actual service pages.

Key convergence: Matt's method and independent 2026 research agree on the big levers (answer-first, match-the-top-3 word count, real photos over stock, schema is not an AI-citation lever per the Ahrefs controlled study). New external facts folded in: NN/G above-fold attention data, Backlinko word-count study, and **FAQ rich results fully deprecated by Google in May 2026** (two independent research threads confirmed via Search Central).

rsla.io findings (site is a Vite+React SPA, prerendered, services in `serviceData.js`): prerender ships FAQs as visible `<dl>` so the hydrated `<details>` accordion is NOT the crawl trap; the real gaps are (1) finish the template migration (Automations/CRM/Custom-Builds still on the thin old `ServiceLayout`), (2) internal linking into service pages, (3) trim FAQs ~7 -> 3-4, (4) capture pricing intent without publishing numbers. The 2026-07-22 `docs/seo/servicePageDesignBrief.md` already nails answer-first hero + founder trust + real-artifact imagery, so the guidance is additive.

Output: `servicePageDesignGuide.md` (12 sections, general method + research + rsla.io application + a build/audit checklist). Em/en-dash-free per workspace rule.

