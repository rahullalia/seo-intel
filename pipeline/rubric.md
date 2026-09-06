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
| A | Google itself | Search Central docs and blog, Search Status Dashboard, spam policies, GBP policies, Search Liaison statements |
| B | Large-scale study or practitioner survey with method disclosed | Whitespark Local Search Ranking Factors, Semrush and Ahrefs studies, BrightLocal consumer surveys, Seer AIO CTR studies |
| C | Practitioner test with data on real sites | Sterling Sky tests, Kyle Roof on-page tests, HeyTony field results with numbers |
| D | Opinion, anecdote, single case without data | Most creator commentary, forum posts |

**Scope:** `organic` (web results), `local` (map pack and GBP), `ai` (AI Overviews, AI Mode, assistants). A factor can carry more than one.

**Lever:** `ranking`, `conversion`, `trust`. A factor with no ranking weight but measured conversion weight is a conversion lever, not a Myth. Hero carousels are the canonical example: no ranking effect, measured conversion damage.

## Promotion and demotion rules

1. A tier moves only when the evidence grade supporting the new tier is met. Opinion never moves a tier.
2. Google statements (grade A) set Required and Dead. They do not by themselves set Core, because Google confirms existence of a signal, not its weight.
3. Two grade C tests must be independent: different authors, different sites, different years count as independent.
4. A demotion needs the same evidence as a promotion. A factor is not demoted because it stopped being discussed.
5. When A and B or C conflict, the factor keeps its tier and a dispute opens in `factors/disputes.md`.

## Staleness

Every row carries `last verified`. A row older than 6 months is flagged `stale` in the changelog and the research routine re-verifies it on its next run. Stale rows are not trusted in playbook edits until re-verified.

## Weighting for "most and least important"

The scorecard is ordered within each category by tier, then evidence grade. A ranked cross-category list is derived, not stored: Required first, then Core sorted by evidence grade and by how recently verified. Do not invent numeric weights; the survey-derived ranks (Whitespark publishes 1 to 187 for local) are recorded in the entry and cited, never averaged with other sources.

## What is not a factor

A tool, a vendor, a tactic without a measurable claim, or a prediction. Those go in `playbook/` or nowhere.
