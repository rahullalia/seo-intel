# google | ai-search

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2025-12-10 | Google says no AI text file and no special schema is needed to appear in AI features
- Source: Google Search Central, "AI features and your website", 2025-12-10 (page last updated), https://developers.google.com/search/docs/appearance/ai-features
- Quote: "You don't need to create new machine readable files, AI text files, or markup to appear in these features. There's also no special schema.org structured data that you need to add."
- Means: Adding an llms.txt file or extra markup to chase AI Overviews and AI Mode citation is ruled out by Google's own documentation. The same page states there are no additional requirements and no special optimizations for these features.
- Factor: llms-txt | Evidence: A | Lever: ranking | Scope: ai | Stage: build

## 2025-12-10 | Indexing and snippet eligibility are the stated requirements for an AI Overviews link
- Source: Google Search Central, "AI features and your website", 2025-12-10 (page last updated), https://developers.google.com/search/docs/appearance/ai-features
- Quote: "To be eligible to be shown as a supporting link in AI Overviews or AI Mode, a page must be indexed and eligible to be shown in Google Search with a snippet"
- Means: A page carrying noindex or nosnippet cannot appear as a supporting link in AI Overviews or AI Mode. Google states there are no additional technical requirements beyond those for classic Search.
- Factor: indexable | Evidence: A | Lever: ranking | Scope: ai | Stage: both

## 2025-12-10 | Googlebot robots.txt rules are the control over a site's use in AI features
- Source: Google Search Central, "AI features and your website", 2025-12-10 (page last updated), https://developers.google.com/search/docs/appearance/ai-features
- Quote: "AI is built into Search and integral to how Search functions, which is why robots.txt directives for Googlebot is the control for site owners to manage access to how their sites are crawled for Search."
- Means: Blocking Googlebot in robots.txt, at the CDN, or at the firewall removes a site from AI Overviews and AI Mode along with classic results. Google-Extended is the separate control for training and grounding in Google's other systems.
- Factor: ai-crawler-allow | Evidence: A | Lever: ranking | Scope: ai | Stage: both

## 2025-12-10 | Google claims higher quality clicks from AI Overview result pages and publishes no figure
- Source: Google Search Central, "AI features and your website", 2025-12-10 (page last updated), https://developers.google.com/search/docs/appearance/ai-features
- Quote: "We've seen that when people click from search results pages with AI Overviews, these clicks are higher quality (meaning, users are more likely to spend more time on the site)."
- Means: Google defines the benefit as time on site rather than click volume and attaches no number to it, so the click lift figure the scorecard needs is still unsourced. Track time on site in Analytics for queries carrying an AI Overview instead of quoting a rate.
- Factor: aio-cited-click-lift | Evidence: A | Lever: conversion | Scope: ai | Stage: audit
