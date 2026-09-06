# Style

Applies to everything a routine or a person writes in `factors/`, `sources/`, `playbook/`, `changelog.md`, `docs/`. Enforced by `lint-prose.py` (deterministic) and the QA checklist (judgment).

## The one rule

Every sentence carries at least one of: a fact, a number, a date, a source, a decision. A sentence that carries none is deleted. This is what keeps the corpus free of filler, because filler has nothing to carry.

## Writing rules

- Plain words. Say what happened, who measured it, when, and what it means for a page or a profile.
- Verbatim quotes are 40 words or fewer and match the source exactly. Paraphrase is marked as paraphrase.
- Numbers keep their unit and their window: "12 percent CTR drop over 28 days," never "significant drop."
- Hyphens only. No em dashes, no en dashes. Use a comma, a period, or a colon.
- No emojis, no bold for emphasis inside sentences, no exclamation marks.
- No hedging stacks. One qualifier is fine when the evidence is weak: "one test," "Google has not confirmed."
- Name the person or organization. Never "experts say," "many believe," "studies show," "it is widely known."
- No adjectives of importance: crucial, key, vital, essential, pivotal, game-changing, powerful, robust, seamless.
- No claims about what "Google wants" or "the algorithm rewards" unless quoting Google.
- Do not summarize the summary. One "what it means" line per entry, then stop.

## Entry format (sources/*)

```
## YYYY-MM-DD | Short claim in plain words
- Source: Publisher, "Title", YYYY-MM-DD, https://...
- Quote: "verbatim, 40 words or fewer"
- Means: one or two plain sentences on what changes for a page, a profile, or a client.
- Factor: factor-id | Evidence: A|B|C|D | Lever: ranking|conversion|trust | Scope: organic|local|ai
```

Newest entry at the top of the file, directly under the header line. One entry per finding. If two sources report the same event, one entry with two Source lines.

## Banned vocabulary (lint enforced)

delve, landscape (abstract), leverage (verb), robust, seamless, seamlessly, unlock, elevate, empower, game-changer, game-changing, cutting-edge, groundbreaking, revolutionize, transformative, holistic, synergy, tapestry, testament, underscore (verb), pivotal, crucial, vital, essential, paramount, navigate (abstract), realm, journey (abstract), foster, harness, streamline, supercharge, skyrocket, in today's, ever-evolving, fast-paced, it's important to note, it is worth noting, in conclusion, ultimately, at the end of the day, not only ... but also, it's not just ... it's, stands as, serves as, boasts, showcases, highlights (verb), a reminder that, dive into, deep dive, unpack, embark, navigate the, comprehensive guide, best practices (as a noun without a list following).

## What QA reads for that the linter cannot

Rule of three padding, sentences that restate the previous one, "what it means" lines that mean nothing, claims without a source line, quotes that do not appear in the source, dates missing or inferred, factor ids that are not on the scorecard, and paragraphs that sound written to impress instead of to inform. Delete, do not decorate.
