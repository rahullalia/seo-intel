# log.md - seo-intel

Session record, newest first. The pipeline's own run record is `changelog.md`; build status is `docs/plan.md`.

## 2026-10-05 14:50 PT

**The skills now read the scorecard, and Edward Sturm's Compact Keywords is on file.** Rahul asked two things: whether the skill structure over this repo was sound, and what to make of Sturm's claim that conversion pages beat blog articles.

- The structure was sound but the deliverable was orphaned: no skill read `factors/scorecard.md`. `heyTony` now checks it before stating a ranking fact and routes to every playbook file. `seoForge` checks it before repeating a number. Grade A or B rows, and Required, Myth and Dead tiers, outrank the skill text. Grade C or D rows leave the creator's method standing, labelled as method.
- Sturm's free material is digested in `sources/creators/edward-sturm/compact-keywords.md`. The course was not bought and its login gated pages were not fetched. Detail and counts are in `changelog.md` under 2026-10-05.
- `blogEngine` gained Gate 0.5: sort the keyword into learn, weigh or hire before the interview, and name the money page the post feeds. A hire keyword stops the post and goes to the service page pipeline.
- New row `purchase-intent-page-type` at Minor grade D. RSL/A's own rsla.io numbers are the first entry in `sources/rsla/content.md`.
- Gotcha recorded in memory: a Search Console page filter with a non-page dimension undercounts. Sum `dimensions=page` rows.

**Next steps**

- Rahul: decide when the 13 money pages on branch brand-visual-system ship. They are the buying pages this whole question is about, and `/services/crm` and `/bakersfield` still return 404 on the live site.
- 90 days after they ship: re-measure blog against service pages on rsla.io and file it in `sources/rsla/content.md`, which would lift the entry to grade C. Tracked as RSL-544, blocked by RSL-369.
- Pushed 2026-10-05 on Rahul's go, after `git pull --rebase`.
- Standing rule from the same message: every site RSL/A manages gets checked for missing conversion pages. The check is `heyTony` workflow B, and the cross-client sweep is tracked in Linear.

## 2026-09-10 13:40 PT

**Two fixes off the back of the morning run, merged as PR #3.** Rahul asked what to do about the seven grade D design rows and pushed back on the citation count number. He was right on both counts.

- `citation-count-25-40` stated a range no source prints. Renamed `citation-count-target`, restated to name Darren Shaw's 30 to 50 recommendation as the only published range and call the stopping point unproven. The Uberall study Shaw cites compared 3,000 locations against 3,000 and found no ceiling, so the row was asserting the opposite of its own category's only measured study. Both playbook steps and `playbook/local/citations.md` now size the build to the competitor gap, which that file already prescribed one section earlier. Two backlog lines closed.
- New fourth source tier `sources/rsla/` for RSL/A's own client measurements, grade C at best, routines barred from it in both prompts. This is the real unlock for the conversion rows: no bought study will settle `single-primary-cta` or `real-team-photos`, but a before and after on a client site is grade C under the existing rubric, and two different clients are independent. Seeded with the Select Landscape review widget measurement that had to go in `playbook/` on 2026-09-06 for lack of a tier.
- `lint-prose.py` had two bugs the new tier exposed: it did not read `sources/rsla/`, and it flagged the client name Select Landscape. Both fixed, regression checked against three lines.

**Next steps**

1. Start filing RSL/A measurements. The cheapest first test is a before and after on one client's primary CTA count, using the GA4 and form pipeline already on those sites. Two clients gets `single-primary-cta` to Core under rule 3.
2. Three rows bundle a compliance or cost claim with a conversion claim under one lever, so good evidence cannot attach: `tap-to-call`, `text-contrast`, `review-carousel-plugin`. Either split them or let a row carry two levers with separate grades. Rahul's call, not started.
3. `accessibility-baseline` and `body-font-size` are provable from published standards for roughly an hour of work, not done today.
4. `whitespace-section-rhythm` has no measurable claim and belongs in the playbook as house style rather than on the scorecard. Not moved.

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
