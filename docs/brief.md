# seo-intel design brief

Approved by Rahul on 2026-09-06 in the session that built the repo. This is the spec the build follows.

## Purpose

A single, self-updating SEO knowledge base for RSL/A: what ranks, what converts, what is mandatory, what is a myth, each row traceable to dated evidence from Google, industry experts, and content creators. It replaces the scattered state where the HeyTony material lived in `learning/`, the local SEO playbook lived in its own folder, and the seoForge references went stale.

## Decisions

1. **One private repo, `rahullalia/seo-intel`, cloned to `~/Developer/my-business/seo-intel/`.** That clone is the single local folder.
2. **Folders for sources, not branches.** Branches cannot be read side by side. The three tiers are top-level folders under `sources/`. Branches are reserved for the pipeline: `intel/YYYY-MM-DD` per run, landing through a pull request.
3. **Eight categories, identical in every tier:** website-design, technical, content, local-gbp, citations, backlinks, ai-search, signals.
4. **The scorecard is the deliverable.** Labels: Tier (Required, Core, Supporting, Minor, Myth, Dead), Evidence (A Google, B study or survey, C practitioner test, D opinion), Scope (organic, local, ai), Lever (ranking, conversion, trust). Rules in `pipeline/rubric.md`. Core needs grade B or two independent grade C tests. Myth needs a test that showed no effect. Rows older than 6 months are flagged stale.
5. **The lever column exists because design has no ranking weight and real conversion weight.** Without it every design factor reads as Myth.
6. **Copy first, then design** is Matt Diamante's rule and the repo's position: layout carries the message. The website-design category exists mainly to catch design decisions that damage ranking (carousels, hidden content, duplicated mobile blocks, image headings, redesigns that change URLs), with everything else scored on the conversion lever.
7. **Writing quality is a gate.** `pipeline/style.md` says every sentence carries a fact, a number, a date, a source, or a decision. `pipeline/lint-prose.py` flags banned vocabulary, dashes, emojis and vague attributions deterministically. QA reads for what the linter cannot see. A claim without a primary link is deleted, not reworded.
8. **Two cloud routines, 1st and 15th.** Research at 6am PT on Opus 5 dispatches three Sonnet 5 researchers (one per tier) if the Agent tool is available in cloud sessions, else runs the tiers in sequence. QA at 9am PT on Opus 5 verifies links and quotes, applies the rubric, runs lint, and merges when clean.
9. **Notification is exception-only.** GitHub already emails the PR on open and merge, and `changelog.md` is the durable record. A Todoist task fires only when QA refuses to merge, or when no PR was produced.
10. **Feeds before search.** Registry sources with RSS are read first. Web search covers only what feeds miss.
11. **HeyTony stays hand-fed.** New Insiders calls need the logged-in membership session. The existing runbook in `sources/creators/hey-tony/insiders/update-hey-tony.md` keeps that job.
12. **Local storage.** `learning/` moved to `sources/creators/hey-tony/` (Insiders and Rank Week), videos gitignored and local only. `local-seo-playbook/` moved to `playbook/local/`. seoForge's two reference documents moved to `playbook/`. Skills point into the repo.
13. **Bootstrap runs locally once**, in a Claude Code session with the supervisor here, three researcher subagents, and a QA pass, seeded from the playbook, the seoForge references, and the six heyTony reference parts, plus a fresh research pass. Then the routines take over.

## Layout

```
seo-intel/
  README.md  CLAUDE.md  AGENTS.md  changelog.md
  factors/     scorecard.md  scorecard.yaml  disputes.md
  sources/     google/  experts/  creators/   (8 category files each)
               creators/hey-tony/insiders/  creators/hey-tony/rank-week-2026/
  playbook/    local/  core-updates.md  ai-search.md
  pipeline/    sources.yaml  rubric.md  style.md  lint-prose.py  research-prompt.md  qa-prompt.md
  docs/        brief.md  plan.md
```

## Cost

Routines draw down the Claude subscription like interactive sessions. Estimate per run: three Sonnet researcher sessions at about 4M cumulative tokens each (90 percent cache reads), one Opus supervisor at 3M, one Opus QA at 3.3M. About 18M cumulative tokens, 1.8M fresh, roughly 20 dollars API-equivalent per run, 40 per month, landing in two of four weeks. The first real run replaces this estimate with measured usage from the run log.

## Open until the probe runs

Whether cloud routine sessions expose the Agent tool. A one-off probe routine settles it before the research routine is created. If absent, the research routine runs tiers sequentially with the same caps; a three-routine split is the fallback if that proves too slow.
