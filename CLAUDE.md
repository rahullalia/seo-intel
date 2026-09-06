# CLAUDE.md - seo-intel

## What This Is

RSL/A's single SEO knowledge base: what ranks, what converts, what is required, what is a myth, and the evidence behind each call. Three source tiers (Google, industry experts, content creators) feed one cross-source scorecard. Two cloud routines refresh it on the 1st and 15th; the curated `playbook/` sits above the evidence. Part of `~/Developer/my-business/`; the GitHub remote is `rahullalia/seo-intel` (private).

## Contents

- `factors/` - the deliverable: `scorecard.md` (one row per factor), `scorecard.yaml` (same data for skills), `disputes.md` (where sources disagree)
- `sources/google|experts|creators/` - dated evidence entries, one file per category, newest first. `sources/creators/hey-tony/` holds the HeyTony Insiders and Rank Week raw material that used to live in `my-business/learning/`
- `playbook/` - curated method: `local/` (the local SEO / GBP playbook), `core-updates.md`, `ai-search.md`
- `pipeline/` - the routine contracts: `sources.yaml` (registry), `rubric.md`, `style.md`, `lint-prose.py`, `research-prompt.md`, `qa-prompt.md`
- `changelog.md` - one entry per run, newest first
- `docs/brief.md` (design spec) and `docs/plan.md` (build plan and status)

## Rules

- **No claim without a primary link and a date.** A sentence that cannot cite its source is deleted, never reworded.
- **Dash-clean.** No em or en dashes anywhere in `factors/`, `sources/*/**.md`, `playbook/`, `changelog.md`, `docs/`. Run `python3 pipeline/lint-prose.py` before every commit; it must exit 0.
- **Scorecard tiers follow `pipeline/rubric.md`.** Core or Required needs grade B evidence or two independent grade C tests. Myth needs a test that showed no effect.
- **Routines edit `sources/`, `factors/`, `changelog.md` only.** `playbook/` is edited by humans (or Claude in a local session) folding in verified evidence.
- **Do not rename HeyTony build artifacts** under `sources/creators/hey-tony/insiders/`: `transcripts/NNN_*.txt` and `build/` filenames are pipeline contracts. Its own `CLAUDE.md` has the details.
- **Videos are gitignored** and exist only on Rahul's Mac.
- Skills read from here: `heyTony` points at `sources/creators/hey-tony/insiders/`, `seoForge` at `playbook/core-updates.md` and `playbook/ai-search.md`.

## Parent

Workspace conventions: `~/Developer/CLAUDE.md`. Business hub: `~/Developer/my-business/CLAUDE.md`.
