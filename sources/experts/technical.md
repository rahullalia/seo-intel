# experts | technical

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2026-09-16 | Crawl and snippet access rated the strongest of 13 Google AI factors at +2.20
- Source: Zyppy, Cyrus Shepard, "Google AI Ranking Factors", 2026-09-16, https://signal.zyppy.com/p/google-ai-ranking-factors
- Quote: "Access works as a hard gate ahead of any ranking consideration."
- Means: The line is Fili Wiese of Search Brothers, quoted in a survey whose respondents scored AI crawl access and snippet eligibility +2.20, the highest of the 13 AI factors scored. Check robots.txt and the firewall for Google-Extended and Google's other AI user agents before spending on anything else for AI visibility.
- Factor: ai-crawler-allow | Evidence: B | Lever: ranking | Scope: ai | Stage: both

## 2026-06-15 | Most published llms.txt files sit unread by any crawler
- Source: Ahrefs, "We Analyzed 137K Sites: 97% of llms.txt Files Never Get Read", 2026-06-15, https://ahrefs.com/blog/llmstxt-study/
- Quote: "More than one in four domains (38,000) in our population have adopted llms.txt, despite the fact that no major AI platform has ever committed to reading it."
- Means: Ahrefs checked 137,000 sites and found about 28 percent publish an llms.txt file, but AI citation bots account for only 1.1 percent of the requests those files get, and 97 percent get no traffic at all. This adds a large scale study to the Myth tier alongside Google's own guidance.
- Factor: llms-txt | Evidence: B | Lever: ranking | Scope: organic ai | Stage: build

## 2026-05-07 | Schema shows a small but repeated positive relationship with AI citations across studies
- Source: Zyppy Signal, Cyrus Shepard, "AI Citation Ranking Factors Analysis", 2026-05-07, https://signal.zyppy.com/p/ai-citation-ranking-factors
- Quote: "We’re here because practically every study that looks at schema and AI citations finds a positive relationship"
- Means: Shepard scored 23 factors against 54 published AI citation experiments, patents and case studies covering ChatGPT, Gemini and Perplexity, and put structured data 20th at 5.6 out of 9.5, writing that the effect is typically small but consistent across studies. Keep schema on the page for AI visibility, and do not expect it to move citation counts on its own.
- Factor: schema-markup | Evidence: B | Lever: ranking | Scope: organic ai | Stage: both

## 2026-05-07 | AI engines treat text that needs a click to reveal as low visibility
- Source: Zyppy Signal, Cyrus Shepard, "AI Citation Ranking Factors Analysis", 2026-05-07, https://signal.zyppy.com/p/ai-citation-ranking-factors
- Quote: "Important information is in visible HTML text, not hidden"
- Means: Shepard's Content Visibility factor scored 7.6 of 9.5 across the same 54-source review that ranked answer-first structure eighth and Domain Authority 22nd. Render the primary answer as static HTML rather than content that only appears after a script runs.
- Factor: static-html-rendering | Evidence: B | Lever: ranking | Scope: ai | Stage: build

## 2026-01-21 | A 2026 robots.txt template splits AI crawlers into blocked trainers and allowed retrieval agents
- Source: Cubitrek, "Robots.txt for AI Crawlers: 2026 Template", 2026-01-21, https://cubitrek.com/blog/robots-txt-2026-managing-ai-crawler-budgets
- Quote: "consume bandwidth and return zero referral traffic"
- Means: The guide recommends blocking GPTBot, CCBot and ClaudeBot as training scrapers that it says send no referral traffic, and allowing OAI-SearchBot, ChatGPT-User and Claude-SearchBot as retrieval agents that do. This is a practitioner recommendation with no measured before and after test attached.
- Factor: ai-crawler-allow | Evidence: D | Lever: ranking | Scope: ai | Stage: both

## 2026-01-09 | Entity linking correlated with an AI Overview visibility gain on Schema App's own site
- Source: Schema App, "Case Study: Entity Linking Increases AIO Visibility by 19.72%", 2026-01-09, https://www.schemaapp.com/schema-markup/case-study-entity-linking-increases-aio-visibility/
- Quote: "Schema App measured a 19.72% increase in AI Overview visibility after implementing robust Entity Linking with Entity Hub."
- Means: Schema App's own site gained 19.72 percent AI Overview visibility after adding Entity Linking between October and December 2025, and one Fortune 500 customer gained 8.5 percent. Schema App discloses this as its own before and after comparison, not a controlled study with a disclosed sample size.
- Factor: schema-markup | Evidence: C | Lever: ranking | Scope: organic ai | Stage: audit

## 2022-09-30 | A framing page ranked for text that existed only inside its iframe, cross-domain included
- Source: Search Engine Land, Bastian Grimm, "Technical SEO testing: How Googlebot handles iframes", 2022-09-30, https://searchengineland.com/how-googlebot-handles-iframes-388243
- Quote: "The parent URL can, in some instances, rank for content that only exists in the iFramed URL and not in the parent URL."
- Means: One controlled test with same-domain and external-domain frames saw the parent rank for framed text until the framed page carried noindex or a robots.txt block. The credit can happen, which matches Google's best-effort wording rather than contradicting it.
- Factor: iframe-content-attribution | Evidence: C | Lever: ranking | Scope: organic | Stage: both

## 2022-01-31 | Ahrefs found a third of sites passing Core Web Vitals and no conclusive ranking effect
- Source: Ahrefs, "Core Web Vitals Data Study w/ CrUX & 5.2M Pages", 2022-01-31, https://ahrefs.com/blog/core-web-vitals-study/
- Quote: "Overall, we saw nearly 33% of websites passing Core Web Vitals thresholds"
- Means: Patrick Stox combined Chrome User Experience Report origin data with 5.21 million pages carrying Core Web Vitals metrics out of 43.66 million pages in Ahrefs Site Audit, found 21.2 percent of pages passing against 33 percent of origins, and wrote that the rollout timing left no conclusive method to measure the ranking impact. Largest Contentful Paint was the metric sites failed most, so treat it as the first fix rather than First Input Delay.
- Factor: core-web-vitals | Evidence: B | Lever: ranking | Scope: organic | Stage: audit
