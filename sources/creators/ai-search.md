# creators | ai-search

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2026-10-10 | The searches ChatGPT runs can be read out of the browser network tab
- Source: Edward Sturm, "I'm going to remind you one more time, ChatGPT gets its answers from search engines", 2026-10-10, https://www.youtube.com/shorts/x_LLGHec2d8 (video description, date from the channel feed https://www.youtube.com/feeds/videos.xml?channel_id=UCDxhBSgPvrFvyXLdpmygDhg)
- Quote: "Find the searches ChatGPT does so you can influence the answers it gives."
- Means: Sturm's method is to open the network tab on a ChatGPT conversation, search the response for the word queries, then reuse that wording in the page title, slug, H1 and opening sentences. He reports no test and no site, so this is a way to read the fan-out and not evidence that matching it earns a citation.
- Factor: query-fan-out-targeting | Evidence: D | Lever: ranking | Scope: ai | Stage: both

## 2026-09-20 | A $6 press release ranked first and was cited in the AI Overview within hours
- Source: Edward Sturm, "King of AEO: The Exact Tactics Ranking Pages and Changing AI Overviews in Hours", 2026-09-20, https://edwardsturm.com/articles/king-of-aeo-seo-tactics/
- Quote: "Both of these releases immediately ranked high on Google and were used in Google's AI Overview"
- Means: James Dooley paid $6 for an AB Newswire release carrying the phrase king of AEO in the title, subheading and first sentence, and the AI Overview called him king of AEO a few hours later. The same AI Overview repeated a stadium ceremony that existed only inside Jesper Nissen's EIN Presswire release.
- Factor: press-release-links | Evidence: C | Lever: ranking | Scope: ai | Stage: both

## 2026-07 | Google's AI states a claim first, then finds content that supports it
- Source: HeyTony master playbook, Part V 7.2, 2026-07 (skills/skills/heyTony/reference/part-5-offpage-and-ai-search.md), local file
- Quote: "Google's AI generates a claim/statistic first, then looks for content that supports/agrees with what it already said."
- Means: Read what the AI Overview asserts, state that claim first in your own copy, then pivot to your differentiated information. Contradicting it outright does not get cited.
- Factor: ai-overview-claim-alignment | Evidence: C | Lever: ranking | Scope: ai | Stage: build

## 2026-07 | The same site was cited in about thirty percent of repeated identical searches
- Source: HeyTony master playbook, Part V 7.2, 2026-07 (skills/skills/heyTony/reference/part-5-offpage-and-ai-search.md), local file
- Quote: "Re-running the identical search on 3 separate occasions, the same site was cited only ~30% of the time"
- Means: AI Overview sourcing is unstable session to session. Do not read a single snapshot as a ranking result, for yourself or a competitor.
- Factor: aio-citation-instability | Evidence: C | Lever: ranking | Scope: ai | Stage: audit

## 2026-07 | Rank on Google first and AI recommendation largely follows
- Source: HeyTony master playbook, Part V 7.1 and Part I 1, 2026-07 (skills/skills/heyTony/reference/part-5-offpage-and-ai-search.md), local file
- Quote: "If you rank on Google, you will get recommended by AI. That's just the plain fact."
- Means: LLMs run a live search at answer time and synthesise from about five to ten existing results rather than crawling fresh.
- Factor: aio-outside-top-10 | Evidence: D | Lever: ranking | Scope: ai | Stage: build

## 2026-07 | Extractability of the answer beats schema for AI citation
- Source: HeyTony master playbook, Part V 7.2, 2026-07 (skills/skills/heyTony/reference/part-5-offpage-and-ai-search.md), local file
- Quote: "AI is optimizing to "pull the answer out and hand it back" - extractability of the answer matters more than schema's presence."
- Means: Write the answer so a machine can lift one self-contained passage out of the page, and treat schema as secondary to that. This conflicts with Schema App's measured entity linking gain, recorded as a dispute.
- Factor: aio-citation-answer-first | Evidence: D | Lever: ranking | Scope: ai | Stage: build

## 2026-07 | No tool can measure AI visibility
- Source: HeyTony master playbook, Part V 7.5, 2026-07 (skills/skills/heyTony/reference/part-5-offpage-and-ai-search.md), local file
- Quote: "Anybody selling AI visibility, they are making up terms."
- Means: AI referral traffic can be tracked in GA4 by session source containing chatgpt, claude or perplexity. A vendor visibility score cannot.
- Factor: ai-referral-conversion | Evidence: D | Lever: conversion | Scope: ai | Stage: audit

## 2026-03-21 | ChatGPT runs one to three web searches per prompt and those queries can be read
- Source: Edward Sturm, "AI SEO/GEO/AEO: How to Get Shown in LLMs in 2026", 2026-03-21, https://edwardsturm.com/articles/ai-seo-geo-aeo-get-shown-llms-2026/
- Quote: "You’ll typically see 1-3 searches that ChatGPT used."
- Means: Sturm reads the queries out of the ChatGPT network response, calls them the query fan-out, and builds a page per query carrying that phrase in the page title, meta description, URL slug, H1 and first sentence. The factor id query-fan-out-targeting is new, because no scorecard row covers targeting the queries an assistant runs rather than the prompt a person types.
- Factor: query-fan-out-targeting | Evidence: D | Lever: ranking | Scope: ai | Stage: build
