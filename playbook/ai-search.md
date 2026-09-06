# AI Platform Optimization

Reference document for seoForge. Covers optimization strategies for Google AI Overviews, ChatGPT/SearchGPT, Perplexity, and cross-platform alignment. Includes GEO and AEO frameworks.

Last updated: May 2026 (v2, post-I/O 2026)

---

## Google AI Overviews (AIO)

AI Overviews appear at the top of Google search results for 48% of queries (up from 34.5% in December 2025; Semrush, March 2026). AI Overviews now serve 2.5 billion monthly active users. Being cited in an AIO can drive significant visibility even without a traditional top-10 ranking. Sites cited within an AI Overview see 35% more organic clicks than a standard position-one result. The shift is from "ranking for a position" to "earning a citation."

**Traffic impact:** Position-one organic CTR dropped from 27% to ~11% on queries with AI features. This means even winning the top organic spot delivers less traffic than before if an AI Overview appears above it.

**Citation patterns:**
- 62% of pages cited in AI Overviews are NOT in the traditional top 10 organic results (Semrush, "AI Overview Citation Study," January 2026)
- Domain Authority correlation with AIO citation has collapsed to r=0.18, meaning high-DA sites have only a marginal advantage (Moz, "AIO Ranking Factors," February 2026)
- This is a fundamentally different selection mechanism than organic search. Topical depth and semantic completeness matter more than backlink profiles

**What gets cited:**
- Semantic completeness is the #1 factor. AIO pulls from passages that comprehensively answer a specific question in 134-167 words (Semrush, January 2026)
- FAQ schema gives a 3.2x advantage in AIO citation rates compared to pages without FAQ markup (Schema App, "Structured Data and AI Overviews," March 2026)
- Multi-modal content (pages with relevant images, diagrams, tables, and video) are selected 156% more often than text-only pages (Semrush, January 2026)

**Practical approach:**
- Write comprehensive, self-contained answer passages for each key question your page addresses
- Keep answer passages in the 134-167 word range
- Implement FAQ schema for question-answer pairs
- Include relevant visuals, tables, and diagrams alongside text explanations
- Do not rely on domain authority alone. Depth of coverage is what gets selected

Source: Semrush, "AI Overview Citation Study" (January 2026). Moz, "AIO Ranking Factors" (February 2026). Schema App, "Structured Data and AI Overviews" (March 2026).

---

## Google AI Mode

AI Mode is a separate, conversational search interface that users actively select (clicking the "AI Mode" button). It is Google's answer to ChatGPT and Perplexity. Launched at I/O 2025, it surpassed 1 billion monthly active users within a year. Powered by Gemini 3.5 Flash as of I/O 2026.

**How it works:**
- Uses "query fan-out": breaks a question into subtopics and runs up to 16 simultaneous searches
- Synthesizes results into a comprehensive, cited response
- Supports follow-up questions in a conversational thread
- Only 14% of URLs cited in AI Mode overlap with AI Overview citations. These are separate optimization targets requiring different strategies

**Citation factors (study of 2.3M pages, 500K+ prompts):**

| Factor | Impact |
|---|---|
| Domain traffic | Sites with 1.16M+ visitors earn ~6.4 citations vs 2.4 for low-traffic sites. Domain traffic matters 3x more than content quality |
| Referring domains | 24,000+ backlinks: 6.8 citations. Under 300: 2.5 citations |
| Content length | Articles exceeding 2,300 words: 5.1 citations. Under 500 words: 4.1 |
| Content freshness | Updated within 2 months: 5.0 citations average |
| Section length | 100-150 words between headings: 4.7 citations (optimal) |
| FAQ sections | Pages with FAQ blocks: 4.9 citations vs 4.4 without |
| Readability | Flesch-Kincaid Grade 6-8: 4.6 citations. Complex Grade 11+: 4.0 |

**Key finding:** 68% of pages cited sit outside the organic top 10, but pages ranking in Google's top 10 show noticeably higher citation probability, creating a reinforcement loop. 85-97% of citations came from long-tail and niche sites, meaning smaller sites can win with the right approach.

**Social signals matter:** Reddit mentions (35K-718K) yield 5.5 citations vs 3.1 for minimal presence. User-generated content platforms (Reddit, YouTube, Quora, Medium) account for significant citation share.

**FAQ schema nuance:** FAQ schema markup shows negligible impact on AI Mode citations (approximately 3x weaker than actual FAQ content blocks). AI Mode cares about the content itself, not just the markup. Structured answers matter more than technical metadata.

**Practical approach:**
- Optimize for both AI Overviews AND AI Mode separately (only 14% URL overlap)
- Keep sections at 100-150 words between headings
- Write at Flesch-Kincaid Grade 6-8 readability
- Include actual FAQ content blocks (not just schema)
- Update content at least every 2 months for competitive topics
- Build social proof on Reddit, Quora, and industry forums

Source: SE Ranking, "How to Optimize for AI Mode" (2026). The Slide Factory, "Google AI Mode SEO 2026" (2026). TechCrunch (May 2026). Google Blog (May 2026).

---

## ChatGPT / SearchGPT

ChatGPT with browsing and SearchGPT pull citations from the web and present them inline. Optimization here is closely tied to Bing indexing and on-page structure.

**Citation patterns:**
- 87% of ChatGPT citations match pages in the Bing top 20 for the same query (Zyppy, "ChatGPT Citation Analysis," February 2026)
- Static HTML with clean schema markup achieves 94% parsing success rate by ChatGPT's browsing system (Zyppy, February 2026)
- 44.2% of citations come from content in the first 30% of the page, meaning placement of key information near the top is critical (Zyppy, February 2026)

**What gets cited:**
- Answer capsules: concise, self-contained answers in 40-80 words that directly address a specific question
- Pages using both Article and FAQPage schema together see 2.8x higher citation rates (Schema App, March 2026)
- Clean HTML structure. JavaScript-heavy pages that require rendering are parsed less reliably

**Practical approach:**
- Place your most important answers in the top third of the page
- Write 40-80 word answer capsules for key questions
- Use both Article and FAQPage schema markup
- Ensure your site is indexed in Bing (submit sitemap to Bing Webmaster Tools)
- Prefer static HTML or SSR/SSG over client-side rendering for content pages

**Why Bing matters:** The 87% citation correlation between ChatGPT and Bing rankings means Bing indexing is not optional for AI visibility. Submit your sitemap to Bing Webmaster Tools and verify your site. This takes 10 minutes and has outsized impact on ChatGPT/SearchGPT citations.

Source: Zyppy, "ChatGPT Citation Analysis" (February 2026). Schema App, "Structured Data and AI Citation" (March 2026).

---

## Perplexity

Perplexity uses a three-layer reranking pipeline that evaluates pages differently from traditional search engines. It prioritizes recency, structure, and source credibility in that order.

**How the pipeline works:**
1. **Retrieval layer:** Pulls candidate pages from multiple search indices
2. **Relevance reranking:** Scores candidates on topical match and semantic completeness
3. **Quality reranking:** Evaluates structure, source authority, and freshness to select final citations

**What gets cited:**
- BLUF format (Bottom Line Up Front): pages that state the key answer in the first paragraph, then provide supporting detail, are cited at significantly higher rates
- Well-structured pages (clear headings, logical flow, supporting evidence) achieve 2.8x higher citation rates (Previsible, "Perplexity Citation Patterns," March 2026)
- Freshness is critical. Perplexity's reranker penalizes stale content more aggressively than Google does

**Practical approach:**
- Open every section with the key takeaway, then support it
- Use clear H2/H3 hierarchy
- Include dates, data points, and named sources
- Update content regularly (quarterly at minimum)
- Ensure fast page loads. Perplexity's crawler times out on slow pages

Source: Previsible, "Perplexity Citation Patterns" (March 2026). Perplexity documentation, "How Perplexity Search Works" (2025).

---

## GEO (Generative Engine Optimization)

GEO is a framework from Princeton University research (Aggarwal et al., 2023) that measures which content strategies improve visibility in AI-generated responses.

**Top strategies by visibility increase (Princeton study, 2023):**

| Strategy | Visibility Improvement | Notes |
|---|---|---|
| Cite sources | +115% | Adding named, verifiable citations to claims |
| Add quotations | +30-40% | Including expert quotes with attribution |
| Add statistics | +30-40% | Specific numbers, percentages, data points |
| Fluency optimization | +15-20% | Clear, well-structured writing |
| Keyword stuffing | WORSE than baseline | Actively hurts AI citation rates |

**The best combination:** Fluency + Statistics. Pages that combine clear writing with specific data points consistently outperform other strategy combinations across all tested generative engines (Princeton, 2023).

**Critical finding:** Keyword stuffing, the traditional SEO tactic of repeating target phrases, performs WORSE than baseline in generative engines. AI systems can detect and deprioritize keyword-stuffed content. This is the opposite of traditional SEO behavior and requires a mindset shift.

Source: Aggarwal et al., "GEO: Generative Engine Optimization," Princeton University (2023). arXiv:2311.09735.

---

## AEO (Answer Engine Optimization)

AEO focuses on optimizing for zero-click and AI-driven answer experiences where the user gets their answer without visiting a page.

**Key statistics:**
- Zero-click searches now account for 69% of all Google searches (SparkToro/Datos, "Zero-Click Search Study," 2024)
- Visitors arriving from AI-generated answers convert at 4.4x the rate of traditional organic visitors (HubSpot, "AI Search Conversion Study," January 2026). These visitors arrive with high intent and pre-qualified understanding of what the page offers

**Core AEO practices:**
- **Answer-first format:** Lead with the direct answer, then expand. Do not bury the answer below introductory paragraphs
- **Entity consistency:** Use the same terminology and naming across your entire site. AI systems build entity graphs and inconsistent naming fragments your topical authority
- **Quarterly updates:** Updated content receives an average of 6 AI citations compared to 3.6 for stale content (Semrush, "Content Freshness and AI Citations," March 2026). Set a quarterly review cadence at minimum
- **Structured answers:** Use tables, numbered lists, and definition patterns for information that AI systems commonly extract

Source: SparkToro/Datos, "Zero-Click Search Study" (2024). HubSpot, "AI Search Conversion Study" (January 2026). Semrush, "Content Freshness and AI Citations" (March 2026).

---

## Cross-Platform Alignment

Several patterns consistently improve visibility across Google AIO, ChatGPT, and Perplexity simultaneously:

**FAQ patterns are rising for AI extraction.** All three platforms preferentially cite content structured as question-answer pairs. FAQ schema serves double duty: it helps Google's traditional rich results AND AI citation systems across platforms.

**Schema serves double duty.** Article + FAQPage + HowTo schema markup helps both traditional search features (rich snippets, featured snippets) and AI citation systems. There is no trade-off.

**Answer capsules in the top third.** Both ChatGPT (44.2% of citations from first 30% of page) and Perplexity (BLUF preference) reward front-loaded answers. Place your most important content early.

**Content freshness across platforms.** Updated content gets 6 AI citations vs 3.6 for stale content (Semrush, March 2026). Quarterly refresh is the minimum cadence. Monthly is better for competitive topics.

---

## llms.txt

The llms.txt proposal (llmstxt.org) suggests placing a machine-readable file at `/llms.txt` to help AI systems understand your site.

**Google's official position (May 2026):** Google's AI optimization guide explicitly says "you can ignore tactics like creating unnecessary AI text files (like llms.txt)." For Google Search, llms.txt has no effect.

**Other AI platforms:** Perplexity, ChatGPT retrieval agents, Claude-Web, and developer tools (Cursor, GitHub Copilot) DO index and use llms.txt. Adopted by Anthropic, Stripe, Zapier, and Cloudflare.

**Current adoption (May 2026):** Approximately 10% among surveyed sites (Ahrefs, April 2026). Zero measurable correlation with AI citation rates on Google specifically.

**Recommendation:** Implement as a Business-to-Agent signal, not a Google SEO play. The effort is minimal and the upside covers non-Google AI platforms. Best practices: keep under 10KB, curate 20-50 high-value links (not a sitemap dump), first line should be a blockquote with the site's core description, update quarterly.

Source: Ahrefs, "llms.txt Adoption Study" (April 2026). llmstxt.org specification. Google Developers, "AI Optimization Guide" (May 2026). Presenc.ai, "State of llms.txt 2026" (2026).

---

## AI Crawler Management

Not all AI crawlers are equal. Training crawlers scrape your content to improve their models without citation. Retrieval agents fetch your content in real-time to cite it in AI answers. Block the first, allow the second.

**Block (training crawlers):**
- `GPTBot` (OpenAI training, +55% traffic YoY)
- `CCBot` (Common Crawl, used by many AI companies)
- `ClaudeBot` (Anthropic training, nearly doubled YoY)
- `Google-Extended` (Gemini training, separate from Googlebot)
- `FacebookBot` (Meta AI training)
- `Meta-ExternalAgent` (Meta AI training)

**Allow (retrieval agents that cite your content):**
- `OAI-SearchBot` (ChatGPT live search)
- `Claude-Web` (Claude live retrieval)
- `PerplexityBot` (Perplexity search)
- `ChatGPT-User` (ChatGPT browsing)
- `anthropic-ai` (Anthropic live retrieval)

**Critical distinction for Anthropic:** ClaudeBot (training) and Claude-Web (retrieval) are separate user agents. Blocking both loses all Claude citations. Block ClaudeBot, allow Claude-Web.

**Monitoring:** Audit server access logs monthly. If training scrapers outnumber retrieval agents 5:1, you are subsidizing someone else's model for free.

Source: Cubitrek, "Robots.txt for AI Crawlers in 2026" (2026). Nohacks.co, "The AI User-Agent Landscape in 2026" (2026). ClickRank, "Crawlers to Allow or Block" (2026).

---

## AI Content Disclosure

**Google's position:** Google does not require AI content disclosure. There is no penalty for using AI and not disclosing it, and no ranking benefit for disclosing it.

**The data:** 86.5% of top-ranking pages use some form of AI assistance (Originality.ai, February 2026). Disclosure is a brand trust decision, not an SEO decision.

**Recommendation:** Decide based on brand positioning and audience expectations. From a pure SEO perspective, disclosure has no measurable impact, positive or negative.

Source: Google Search Central, "Google Search's guidance about AI-generated content" (February 2023). Originality.ai, "AI Content in Search" (February 2026).
