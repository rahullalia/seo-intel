# experts | ai-search

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2026-09-16 | Fan-out coverage rated the fifth strongest Google AI factor, just above ranking for the main query
- Source: Zyppy, Cyrus Shepard, "Google AI Ranking Factors", 2026-09-16, https://signal.zyppy.com/p/google-ai-ranking-factors
- Quote: "When someone searches with Google AI, Google may run multiple related fan-out queries to help answer the question. Ranking highly in Google results for these fan-out queries is associated with better AI visibility."
- Means: Shepard's survey of over 130 respondents scored organic fan-out coverage +1.91 on a scale of +3 to -3, fifth of the 13 AI factors scored and above ranking for the main query at +1.89. Write the page to rank for the sub-questions a prompt splits into, not only the head term.
- Factor: query-fan-out-targeting | Evidence: B | Lever: ranking | Scope: ai | Stage: both

## 2026-09-16 | Publisher reputation scored +1.78 as a Google AI citation factor
- Source: Zyppy, Cyrus Shepard, "Google AI Ranking Factors", 2026-09-16, https://signal.zyppy.com/p/google-ai-ranking-factors
- Quote: "In traditional SEO, site/domain authority is an important signal Google uses to rank results. Most of our experts believe Google AI uses a similar system of trust when forming answers."
- Means: Shepard's respondents placed source and publisher reputation ninth of 13 AI factors at +1.78, which runs against the 2026-05-07 meta-analysis on file that ranked Domain Authority 22nd of 23 with a weak relationship. The two numbers measure different things: one records what 130 practitioners believe, the other correlated scores against observed citations.
- Factor: domain-authority-aio | Evidence: B | Lever: ranking | Scope: ai | Stage: audit

## 2026-09-16 | Answer prominence near the top of the page scored +1.65 for AI citation
- Source: Zyppy, Cyrus Shepard, "Google AI Ranking Factors", 2026-09-16, https://signal.zyppy.com/p/google-ai-ranking-factors
- Quote: "How prominently the answer appears on the page, especially near the beginning."
- Means: Shepard's respondents scored answer prominence +1.65, 11th of 13 AI factors, below query-answer match at +2.15 and citable facts at +2.07. This is the first graded study evidence on the row, which until now rested on one creator source.
- Factor: aio-citation-answer-first | Evidence: B | Lever: ranking | Scope: ai | Stage: build

## 2026-07-28 | ChatGPT referrals convert at roughly double the rate of organic search on ecommerce sites
- Source: HubSpot, "How AEO drives higher-intent site visitors than other channels", 2026-07-28, https://blog.hubspot.com/marketing/aeo-drives-higher-intent-visitors
- Quote: "ChatGPT referrals convert at 11.4% versus 5.3% for organic search across ecommerce sites"
- Means: Report AI referral sessions separately in GA4 rather than folding them into organic, because a smaller AI session count can carry more revenue per session. HubSpot is relaying Similarweb 2025 research here rather than publishing its own test, so this is grade D until the Similarweb report itself is cited.
- Factor: ai-referral-conversion | Evidence: D | Lever: conversion | Scope: ai | Stage: audit

## 2026-06-09 | Google searches ending without a click passed 68 percent in early 2026
- Source: SparkToro, "In 2026, Less than One Third of Google Searches Still Send a Click", 2026-06-09, https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/
- Source: Search Engine Land, "Google zero-click searches reach 68% in early 2026: Study", 2026-06-09, https://searchengineland.com/google-zero-click-searches-2026-study-479717
- Quote: "In the first four months of 2026, a whopping 68.01% of Google searches ended without a click."
- Means: A Similarweb-based clickstream panel found 68.01 percent of US Google searches from January through April 2026 ended with no click, up from 60.45 percent in 2024. This is the most current verified zero-click figure, higher than either figure in the existing playbook dispute.
- Factor: zero-click-rate | Evidence: B | Lever: conversion | Scope: organic ai | Stage: audit

## 2026-05-07 | Content near the top of the page is the eighth strongest AI citation factor across 54 studies
- Source: Zyppy Signal, Cyrus Shepard, "AI Citation Ranking Factors Analysis", 2026-05-07, https://signal.zyppy.com/p/ai-citation-ranking-factors
- Quote: "Important content placed near the top of the page is more likely to be cited"
- Means: Shepard scored 23 AI citation factors against 54 published experiments, patents and case studies, and ranked answer near the top eighth at 8.8 out of 9.5, citing Dan Petrovic on Gemini applying a retrieval cap per URL. State the direct answer above the context and the background, because the lower half of a long page may never be retrieved.
- Factor: answer-first-structure | Evidence: B | Lever: ranking | Scope: ai organic | Stage: both

## 2026-05-07 | Domain Authority ranks 22nd of 23 AI citation factors and the relationship is weak
- Source: Zyppy Signal, Cyrus Shepard, "AI Citation Ranking Factors Analysis", 2026-05-07, https://signal.zyppy.com/p/ai-citation-ranking-factors
- Quote: "Several studies looked at the relationship between Domain Authority and AI citations. While many found a relationship, it was often weak."
- Means: Across the 54 sources Shepard reviewed, Domain Authority scored 5 out of 9.5 and placed 22nd of 23 factors, below freshness, brand trust and content length. Do not use a Moz Domain Authority number to predict or report AI Overview citation odds for a client.
- Factor: domain-authority-aio | Evidence: B | Lever: ranking | Scope: ai | Stage: audit

## 2026-03-02 | Most AI Overview citations go to pages outside the top 10 organic results
- Source: Ahrefs, "Update: 38% of AI Overview Citations Pull From The Top 10", 2026-03-02, https://ahrefs.com/blog/ai-overview-citations-top-10/
- Quote: "37.9% of URLs cited in AI Overviews also appeared within the first 10 blocks."
- Means: Only 37.9 percent of AI Overview citations match a page in the top 10 organic results, so most citations, about 62 percent, go to pages ranking lower or not ranking at all. This independently confirms the direction of the seed's Semrush and SE Ranking figures with a different publisher.
- Factor: aio-outside-top-10 | Evidence: B | Lever: ranking | Scope: ai | Stage: audit

## 2025-12-15 | High traffic sites earn far more AI Mode citations than low traffic sites
- Source: SE Ranking, "How to Optimize for AI Mode: Google Visibility Matters 3x More Than Content", 2025-12-15, https://seranking.com/blog/how-to-optimize-for-ai-mode/
- Quote: "Websites with over 1.16M visitors earn about 6.4 citations, compared to just 2.4 citations for those with under 2.7K visitors (roughly 3x difference)."
- Means: A small site will not be cited into AI Mode by on-page work alone, because site-level traffic is the strongest predictor in this analysis. Sites over 1.16 million monthly visitors averaged 6.4 citations against 2.4 for sites under 2,700.
- Factor: ai-mode-domain-traffic | Evidence: B | Lever: ranking | Scope: ai | Stage: audit

## 2025-09-26 | Four Semrush articles rewritten for fan-out queries went from two citations to five
- Source: Semrush, Zach Paruch, "We Tested Query Fan-Out Optimization (Here's What We Learned)", 2025-09-26, https://www.semrush.com/blog/query-fan-out-experiment/
- Quote: "In our small sample of four articles, we more than doubled citations in tracked prompts from two to five."
- Means: Paruch researched 10 to 20 fan-out queries per article, had a writer edit the four articles to answer them, and re-measured after one month in Semrush Enterprise AIO, mainly against Google AI Mode. Three extra citations across four articles is a small result the author calls a mixed bag, so cover fan-out sub-queries on a page that already ranks and do not promise a citation from it.
- Factor: query-fan-out-targeting | Evidence: C | Lever: ranking | Scope: ai | Stage: both

## 2024-07-02 | For every 1,000 US Google searches in 2024, 360 clicks reached the open web
- Source: SparkToro, "2024 Zero-Click Search Study: For every 1,000 EU Google Searches, only 374 clicks go to the Open Web. In the US, it's 360.", 2024-07-02, https://sparktoro.com/blog/2024-zero-click-search-study-for-every-1000-us-google-searches-only-374-clicks-go-to-the-open-web-in-the-eu-its-360/
- Quote: "for every 1,000 searches on Google in the United States, 360 clicks make it to a non-Google-owned, non-Google-ad-paying property"
- Means: Datos clickstream data from September 2022 to May 2024 found 36 percent of US Google searches sent a click to a non-Google property, against 37.4 percent in the EU. This is the primary 2024 baseline behind the seed's disputed zero-click figures, and it does not match either number the seed cited.
- Factor: zero-click-rate | Evidence: B | Lever: conversion | Scope: organic ai | Stage: audit
