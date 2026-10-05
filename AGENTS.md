# AGENTS.md - seo-intel

## What This Is

RSL/A's single SEO knowledge base: what ranks, what converts, what is required, what is a myth, and the evidence behind each call. Four source tiers (Google, industry experts, content creators, RSL/A's own client measurements) feed one cross-source scorecard. Two cloud routines refresh it on the 1st and 15th; the curated `playbook/` sits above the evidence. Part of `~/Developer/my-business/`; the GitHub remote is `rahullalia/seo-intel` (private).

## Contents

- `factors/` - the deliverable: `scorecard.md` (one row per factor), `scorecard.yaml` (same data for skills), `disputes.md` (where sources disagree)
- `sources/google|experts|creators|rsla/` - dated evidence entries, one file per category, newest first. `sources/creators/hey-tony/` holds the HeyTony Insiders and Rank Week raw material that used to live in `my-business/learning/`. `sources/rsla/` holds RSL/A's own client measurements, grade C at best, written only in a local session. `sources/creators/edward-sturm/` holds the hand-made digest of Edward Sturm's Compact Keywords method, built from his free material only (the paid course is not bought)
- `playbook/` - curated method: `new-site.md` (the build order), `existing-site-audit.md` (the audit order), `local/` (the local SEO / GBP playbook), `core-updates.md`, `ai-search.md`, `tooling.md`
- `pipeline/` - the routine contracts: `sources.yaml` (registry), `rubric.md`, `style.md`, `lint-prose.py`, `research-prompt.md`, `qa-prompt.md`
- `changelog.md` - one entry per run, newest first
- `docs/brief.md` (design spec) and `docs/plan.md` (build plan and status)
- `log.md` - session record and next steps, newest first (the pipeline's own record is `changelog.md`)

## Rules

- **No claim without a primary link and a date.** A sentence that cannot cite its source is deleted, never reworded.
- **Dash-clean.** No em or en dashes anywhere in `factors/`, `sources/*/**.md`, `playbook/`, `changelog.md`, `docs/`. Run `python3 pipeline/lint-prose.py` before every commit; it must exit 0.
- **Scorecard tiers follow `pipeline/rubric.md`.** Core or Required needs grade B evidence or two independent grade C tests. Myth needs a test that showed no effect.
- **Routines edit `sources/`, `factors/`, `changelog.md` only, and never `sources/rsla/`.** `playbook/` and `sources/rsla/` are edited by humans (or Claude in a local session) folding in verified evidence; the cloud runs cannot see client analytics.
- **Do not rename HeyTony build artifacts** under `sources/creators/hey-tony/insiders/`: `transcripts/NNN_*.txt` and `build/` filenames are pipeline contracts. Its own `CLAUDE.md` has the details.
- **Videos are gitignored** and exist only on Rahul's Mac.
- Skills read from here, so moving or renaming any of these files breaks a skill. `heyTony` checks `factors/scorecard.md` before stating a ranking fact, routes to every file in `playbook/`, and points at `sources/creators/hey-tony/insiders/` and `sources/creators/edward-sturm/compact-keywords.md`. `seoForge` checks the scorecard and reads `playbook/core-updates.md` and `playbook/ai-search.md`. `blogEngine` cites `sources/rsla/content.md` and the Edward Sturm digest in its intent gate.

## Parent

Workspace conventions: `~/Developer/CLAUDE.md`. Business hub: `~/Developer/my-business/CLAUDE.md`.
