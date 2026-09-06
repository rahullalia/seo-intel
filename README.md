# seo-intel

What actually moves rankings, what only moves conversions, what is mandatory, and what is a myth. Every row traceable to its evidence.

## Start here

1. `factors/scorecard.md` is the answer. One row per factor: tier, evidence grade, scope, lever, last verified, sources.
2. `factors/disputes.md` is where Google and the field disagree. Both sides, cited.
3. `sources/<tier>/<category>.md` is the evidence behind the rows. Tiers: `google` (primary), `experts` (Semrush, Ahrefs, Moz, Whitespark, Sterling Sky, Near Media and peers), `creators` (HeyTony, Edward Sturm and peers). Newest entry on top.
4. `playbook/` is what RSL/A does about it. Curated by hand from the evidence. Start at `playbook/new-site.md` for a site being built, `playbook/existing-site-audit.md` for a site that exists, `playbook/tooling.md` for which tool answers which question.

## Categories (identical in every tier, nine)

| File | Covers |
|---|---|
| `website-design.md` | Layout, hero, visuals, typography, color, spacing, mobile, page builders, as they touch ranking or conversion |
| `technical.md` | Crawling, indexing, speed, Core Web Vitals, schema, sitemaps, canonicals, redirects, hosting |
| `content.md` | Copy, on-page elements, keywords, intent, helpfulness, E-E-A-T, AI content policy |
| `local-gbp.md` | Google Business Profile fields, map pack ranking, reviews, proximity, verification, suspensions |
| `citations.md` | Directories, aggregators, NAP consistency, local citations, brand mentions |
| `backlinks.md` | Links, digital PR, press releases, anchor text, link spam policy |
| `ai-search.md` | AI Overviews, AI Mode, ChatGPT, Perplexity, Copilot, citation behavior, AEO and GEO |
| `signals.md` | Everything else measured: engagement, freshness, brand, entities, social, Reddit |
| `programmatic.md` | Programmatic SEO: templated pages at scale, service and location matrices, scaled content abuse and doorway page policy, thin page risk, crawl budget, data-driven page generation |

## How it stays current

Two cloud routines run on the 1st and 15th. Research (6am PT) reads feeds and searches per tier, writes dated entries, adjusts scorecard rows only where the rubric says evidence changed, and opens a pull request. QA (9am PT) verifies every link and quote, checks tier changes against `pipeline/rubric.md`, runs `pipeline/lint-prose.py`, and merges when clean. A blocked merge creates a Todoist task. Details in `docs/brief.md`.

## Reading the scorecard

- **Tier:** Required, Core, Supporting, Minor, Myth, Dead.
- **Evidence:** A Google-confirmed, B large-scale study or survey, C practitioner test with data, D opinion.
- **Scope:** organic, local, ai.
- **Lever:** ranking, conversion, trust. Most design factors are conversion or trust, not ranking, and the column keeps them from being mislabeled Myth.
