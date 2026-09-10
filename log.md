# log.md - seo-intel

Session record, newest first. The pipeline's own run record is `changelog.md`; build status is `docs/plan.md`.

## 2026-09-10 12:53 PT

**Off-cycle research run, merged as PR #2.** Rahul asked to pull any new data ahead of the September 15 cloud run. Window was four days, 2026-09-06 to 2026-09-10. Three tier researchers ran in parallel on sonnet per `pipeline/research-prompt.md`; the QA pass ran in the same session before the commit, so the deletions and the quote correction are in the one commit rather than a separate `qa:` commit.

- Nothing in the window met the entry test. No core update ran, and the feeds carried only paid media news and undated relative timestamps. All 6 entries came from `pipeline/backlog.md`.
- Three rows left `## Rows resting on opinion`: `gbp-messaging` onto Google's own removal notice at grade A, `static-html-rendering` and `hidden-accordion-content` onto Cyrus Shepard's Content Visibility score at grade B. Grade D rows fell from 41 to 38. One dispute closed.
- Two of the eight written entries were deleted as duplicate URLs already on `main`, and one patent quote was a splice of two near identical sentences and was corrected against the printed text. Full record in the PR comment and `changelog.md`.
- A page summarizer misreported both the title and the E-E-A-T sentence of Google's rater guidelines PDF. Reading the extracted text directly showed the entry was correct. Verify a summarizer before deleting an entry on its word.
- `git push` failed with "Repository not found" because the osxkeychain credential for github.com is stale. `gh` is authenticated and works, so the push went through `http.extraheader` with a basic `x-access-token` header built from `gh auth token`. `gh auth setup-git` would fix it permanently and was not run without Rahul's say-so.

**Next steps**

1. Seven of the nine website-design rows are still grade D. This run searched Baymard and Nielsen Norman for primary CTA count, real against stock photography and body font size and found only aggregator reprints with no primary page, including one fabricated Nielsen Norman statistic. `baymard.com/learn/button-design` carries no date and no matching sentence. These rows need a local session with a paid Baymard or NN/g source, not another web search.
2. `query-fan-out-targeting` has a candidate test at last: Semrush's "We Tested Query Fan-Out Optimization" reports citations rising from two to five. It is an experts tier source, so the September 15 experts run should fetch it. The id has no scorecard row until it does.
3. `bing-indexing` is confirmed absent from the Zyppy article and needs a different source. `citation-count-25-40` is confirmed unreachable from Whitespark, whose live 2026 survey prints no citation count anywhere, so the row's id names a figure no source states.
4. After the September 15 runs, `git pull` here, read the new changelog entry, and check claude.ai/settings/usage for the real token cost; replace the duration-only figures in `docs/brief.md` if the cost matters.
5. New HeyTony Insiders calls are still folded in by hand via `sources/creators/hey-tony/insiders/update-hey-tony.md` (needs the logged-in browser session).
6. Optional, Rahul's call: move the 3.2 GB Rank Week videos out of the working tree to `~/Movies/rank-week-2026/` with a pointer file.
7. Client findings that hold beyond one client go in as dated entries here, never as loose notes.

## 2026-09-06 04:57 PT

**Verification session for Select Landscape, no new evidence filed.** Three questions checked against primary sources, findings recorded here so the next session does not redo them.

- GHL review widget on a client site: the loader only resizes the frame by postMessage; the widget document on reputationhub.site is a plain indexable page with server-rendered reviews and hidden Review microdata inside GHL's document. Google calls iframe attribution best effort (SEO office hours, Dec 2023) and self-serving review markup ineligible for stars (review snippet guidelines, 2026-07-24). Measured on the frame alone: 10 requests, 304 KB on the wire, 1.0 MB of JavaScript decoded, a Cloudflare Insights beacon, 10 real axe contrast failures, an AI Summary that volunteers negative feedback, and the 1-star review shown. Verdict: no widget; Google reviews pasted verbatim and linked to the listing.
- CSLB licence number on a Google Business Profile: required, not optional. B&P 7030.5 plus 16 CCR 861 ("any electronic transmission, and any form of directory"), and CSLB's Advertising Guidelines (Sept 2018) name websites and Internet posts. It goes in the description as the number, not as a "we are licensed" claim.
- Photo geotagging stays Myth. Corrected `playbook/local/gbp-playbook.md` line 82: the upload dialog offers Logo, Cover and plain Add photos; Google auto-sorts the rest by image content and nothing can be retagged.

**Next steps**

1. Filed 2026-09-06 on Rahul's approval: 4 entries (`sources/google/technical.md` x3, `sources/experts/technical.md` x1), rows `iframe-content-attribution` (Minor, A) and `self-serving-review-markup` (Myth, A), one step each in `playbook/new-site.md` and `playbook/existing-site-audit.md`, changelog entry.

## 2026-09-06 02:50 PT

**Built the repo from zero in one session and proved the pipeline end to end.** Rahul asked for SEO docs that update themselves (Google, SERP, AEO, GEO) with a scale for what matters most, least, what is required and what is a myth, in one local folder. Decisions and reasons are in `docs/brief.md`. Scope grew mid-session by Rahul's request: programmatic SEO as a ninth category, a Stage label so the scorecard serves both a new build and an audit of an existing site, and a tooling map (`playbook/tooling.md`).

- Scaffold, rubric, style gate with a deterministic linter, source registry, routine prompts. Moved `my-business/learning/` to `sources/creators/hey-tony/` (videos gitignored) and `my-business/local-seo-playbook/` to `playbook/local/`; seoForge's two references to `playbook/`. Every skill, client and memory pointer repointed and verified.
- Bootstrap with 11 subagents: 116 scorecard rows, 142 verified entries, 15 disputes open and 5 closed, 51 rows parked at Minor on opinion-only evidence, backlog of about 35 unresolved citations. QA deleted 3 fabricated quotes and 4 duplicates and corrected 35 tiers.
- Cloud routines created (research 6am PT and QA 9am PT on the 1st and 15th, Opus 5, Todoist only). Probe found: Agent tool present, no gh CLI, egress proxy blocked until Rahul set the environment to Full. First manual run: 27 entries, 7 tier changes, PR #1 verified 27 of 27 and merged.
- Repo settings: head branches delete on merge (the cloud proxy 403s on branch deletes). Routines banned from push notifications.
- Cleanup: `skills/skills/heyTony-workspace/` moved to `skills/skills/heyTony/evals/workspace-2026-08-27/`.

**Next steps**

1. After the September 15 runs, `git pull` here, read the new changelog entry, and check claude.ai/settings/usage for the real token cost; replace the duration-only figures in `docs/brief.md` if the cost matters.
2. Every website-design row rests on HeyTony alone. When time allows, a local session should hunt external conversion studies (Baymard, Nielsen Norman) for those rows; the routines only chase items in `pipeline/backlog.md`.
3. New HeyTony Insiders calls are still folded in by hand via `sources/creators/hey-tony/insiders/update-hey-tony.md` (needs the logged-in browser session).
4. Optional, Rahul's call: move the 3.2 GB Rank Week videos out of the working tree to `~/Movies/rank-week-2026/` with a pointer file.
5. Client findings that hold beyond one client go in as dated entries here, never as loose notes.
