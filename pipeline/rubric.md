# Rubric

How a factor earns its row on the scorecard. Applied by the research routine when it proposes a change and checked by QA before merge.

## Labels

**Tier** (ranking weight, or for conversion levers, measured effect on conversion)

| Tier | Meaning | Minimum evidence to hold it |
|---|---|---|
| Required | Nothing ranks without it: indexable, mobile usable, verified GBP, HTTPS | Grade A, or B plus A |
| Core | Measured large effect, repeatedly | Grade B, or two independent grade C tests that agree |
| Supporting | Measured moderate effect | Grade B or C |
| Minor | Measurable but small, or effect shrinking year over year | Grade B or C |
| Myth | Tested and showed no benefit, or Google denied it and no test contradicts the denial | A test showing no effect, or grade A denial with no contradicting grade B or C |
| Dead | Feature or signal no longer exists (GBP Q&A, GBP messaging, meta keywords) | Grade A removal notice or the feature verifiably gone |

**Evidence grade**

| Grade | Source type | Examples |
|---|---|---|
| A | Google itself, or a government regulator | Search Central docs and blog, Search Status Dashboard, spam policies, GBP policies, Search Liaison statements, FTC rules (filed in `sources/google/`, the primary-source tier) |
| B | Large-scale study or practitioner survey with method disclosed | Whitespark Local Search Ranking Factors, Semrush and Ahrefs studies, BrightLocal consumer surveys, Seer AIO CTR studies |
| C | Practitioner test with data on real sites | Sterling Sky tests, Kyle Roof on-page tests, HeyTony field results with numbers, RSL/A's own measurements on a named client site (see below) |
| D | Opinion, anecdote, single case without data | Most creator commentary, forum posts |

### RSL/A field data

RSL/A's own measurements file in `sources/rsla/`, a fourth tier alongside `google`, `experts` and `creators`, added 2026-09-10. It exists because conversion and trust levers cannot be settled from published research: a bought study measures its own sample, not a client's visitors. Before this tier the only place for an RSL/A number was `playbook/`, where nothing carries an evidence grade, and the review widget measurements of 2026-09-06 went there for that reason.

An entry grades **C** when it names the client site, the date measured, the tool, and the numbers on both sides of a change. It grades **D** when any of those is missing. Never A or B: one agency measuring its own work is a practitioner test, not a study.

Rule 3 on independence applies unchanged. Two measurements on the same client site are one test, not two. Two different clients are independent.

Routines never write to this tier. The cloud runs cannot see client analytics, so `sources/rsla/` is edited only in a local session, the same way `playbook/` is.

Entry format, which replaces the Quote line because there is no external document to quote:

```
## YYYY-MM-DD | Short claim in plain words
- Source: RSL/A measurement, <client site or page URL>, measured YYYY-MM-DD, <tool>
- Measured: the numbers on both sides, each with its unit and its window
- Means: one or two plain sentences on what changes for a page, a profile, or a client.
- Factor: factor-id | Evidence: C|D | Lever: ranking|conversion|trust | Scope: organic|local|ai | Stage: build|audit|both
```

A measurement supports the claim it actually measures. Page weight and contrast numbers are evidence about cost and compliance, not about conversion, in the same way a standards body is grade A only for what the standard requires.

Standards bodies (W3C WCAG, IETF) are grade A for what a standard requires, and say nothing about ranking or conversion effect. Cite them only on rows whose lever is trust or whose tier is Required for compliance, never as evidence that a factor moves rankings (QA note, 2026-09-06, `text-contrast`).

**Scope:** `organic` (web results), `local` (map pack and GBP), `ai` (AI Overviews, AI Mode, assistants). A factor can carry more than one.

**Lever:** `ranking`, `conversion`, `trust`. A factor with no ranking weight but measured conversion weight is a conversion lever, not a Myth. Hero carousels are the canonical example: no ranking effect, measured conversion damage.

**Stage:** `build` when the factor is decided while a site is planned or built (architecture, URL structure, platform, page inventory), `audit` when it is diagnosed on a live site (indexing, cannibalization, internal links, decay), `both` when it applies either way. Stage does not change tier; it tells `playbook/new-site.md` and `playbook/existing-site-audit.md` which rows to walk.

## Promotion and demotion rules

1. A tier moves only when the evidence grade supporting the new tier is met. Opinion never moves a tier.
2. Google statements (grade A) set Required and Dead. They do not by themselves set Core, because Google confirms existence of a signal, not its weight.
3. Two grade C tests must be independent: different authors, different sites, different years count as independent.
4. A demotion needs the same evidence as a promotion. A factor is not demoted because it stopped being discussed.
5. A row whose only evidence is grade D is parked at Minor, the lowest tier the table carries, and listed under `## Rows resting on opinion` at the bottom of `scorecard.md`. That is a research target, not a verdict. Myth and Dead rows keep their tier when demoting would assert the opposite claim; they get a backlog line instead (QA decision, 2026-09-06).
6. When A and B or C conflict, the factor keeps its tier and a dispute opens in `factors/disputes.md`.

## Staleness

Every row carries `last verified`. A row older than 6 months is flagged `stale` in the changelog and the research routine re-verifies it on its next run. Stale rows are not trusted in playbook edits until re-verified.

## Weighting for "most and least important"

The scorecard is ordered within each category by tier, then evidence grade. A ranked cross-category list is derived, not stored: Required first, then Core sorted by evidence grade and by how recently verified. Do not invent numeric weights; the survey-derived ranks (Whitespark publishes 1 to 187 for local) are recorded in the entry and cited, never averaged with other sources.

## What is not a factor

A tool, a vendor, a tactic without a measurable claim, or a prediction. Those go in `playbook/` or nowhere.
