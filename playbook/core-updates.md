# Google Core Updates and Quality Signals

Reference document for seoForge. Covers major algorithm updates, the Helpful Content System, E-E-A-T, AI content policy, penalty triggers, and key ranking statistics.

Last updated: May 2026 (v2, post-I/O 2026)

---

## Major Core Updates

### March 2024 Core Update

Google's largest spam-focused update. Rolled out over 45 days (completed April 19, 2024).

**Key changes:**
- Targeted three abuse types: scaled content abuse, site reputation abuse (parasite SEO), and expired domain abuse
- Resulted in a 40% reduction in low-quality, unoriginal content in search results (Google, March 2024 blog post)
- Roughly 50% of sites penalized during this update had used AI-generated content at scale (Search Engine Journal analysis, April 2024)
- Google confirmed the update penalizes based on intent and quality, not production method. Sites using AI responsibly were unaffected

**Impact:** This update merged the standalone Helpful Content System into the core ranking algorithm. No more separate "helpful content updates." The signals now run continuously as part of every core update.

Source: Google Search Central Blog, "March 2024 core update and new spam policies" (March 5, 2024). Search Engine Journal, "March 2024 Core Update Impact Analysis" (May 2024).

### December 2025 Core Update

Rolled out December 12, 2025 through January 6, 2026.

**Key findings:**
- 87% negative impact on AI-generated content published without expert oversight or editorial review (Semrush Sensor data, January 2026)
- 23% average visibility gains for pages demonstrating experience-backed content (first-person case studies, original research, practitioner insights)
- Pages with LCP (Largest Contentful Paint) exceeding 3 seconds experienced 23% more traffic loss than fast-loading counterparts, confirming Core Web Vitals as a meaningful tiebreaker

**Takeaway:** Quality gates on AI content became non-negotiable after this update. Raw AI output without human expertise layered on top lost ground systematically.

Source: Semrush Sensor, "December 2025 Core Update Volatility Report" (January 2026). Ahrefs, "Core Update Winners and Losers" (January 2026).

### March 2026 Core Update

Rolled out March 10, 2026 through April 2, 2026. The most volatile update since March 2024.

**Key findings:**
- Volatility scored 9.5/10 on Semrush Sensor (compared to 7.2 average for prior core updates)
- 80% of top-3 positions shifted across tracked keyword sets
- Strong preference for first-party sources: original research, proprietary data, and practitioner-authored content consistently gained positions
- Thin AI-generated output (low depth, no unique insight, no supporting evidence) dropped 30-50% in visibility
- Experience-backed content gained 15-25% visibility on average

**Takeaway:** Google is now actively rewarding content that could only come from someone who has done the work. Aggregated, reworded information without original contribution is losing ground fast.

Source: Semrush Sensor, "March 2026 Core Update Analysis" (April 2026). Search Engine Roundtable, "March 2026 Core Update Observations" (April 2026).

---

### Google I/O 2025-2026: The AI Search Overhaul

Google announced "the biggest change to Search in more than 25 years" across two consecutive I/O events.

**I/O 2025 (May 20, 2025):**
- AI Mode launched: conversational search interface, no Labs signup required
- Deep Research: hundreds of simultaneous searches, expert-level cited reports
- Shopping AI: natural language product discovery with Shopping Graph (50B+ listings)

**I/O 2026 (May 19-20, 2026):**
- AI Mode surpassed 1 billion monthly active users, upgraded to Gemini 3.5 Flash
- Intelligent Search Box: biggest search box redesign in 25 years, accepts text/images/files/video
- Information Agents: autonomous background monitoring, alerts when conditions change
- Generative UI: custom interactive layouts with tables, graphs, simulations
- Mini-Apps: AI-generated custom applications from natural language descriptions
- Agentic checkout: AI completes purchases via Google Pay

**Publisher traffic impact:**
- Zero-click searches: ~60% of all Google queries
- Global publisher referral traffic: down 33% year-over-year
- Individual publisher declines: HubSpot 70-80%, Chegg 49%, DMG Media up to 89%
- Ads in AI Overviews: 25.5% of results (up 394% YoY)
- Google's search market share: dropped from 92.9% (2023) to 89.6% (mid-2025)

**Google's stated position on publishers:**
- Claims AI features increase overall search usage
- Added subscription content highlighting, social attribution, inline link expansion
- Sites cited within an AI Overview see 35% more organic clicks than standard position-one

Source: TechCrunch (May 2026). Google Blog (May 2026). TIME (May 2026). Press Gazette (2026). Digiday (2025-2026).

---

## Helpful Content System

Originally launched as a standalone ranking system (August 2022). Merged into the core algorithm with the March 2024 core update.

**What it evaluates:**
- **Depth:** Does the content thoroughly address the topic, or does it stop at surface-level information?
- **Expertise:** Is the content written by (or reviewed by) someone with demonstrable knowledge?
- **Usefulness:** Does the reader leave with something actionable, or just a summary of what they already knew?
- **Information Gain:** Does this page add something new that other pages on the same topic do not?

Information Gain is the critical concept. Google's patent filings (US Patent 11,769,017, granted September 2023) describe scoring pages based on how much novel, non-redundant information they provide relative to other documents ranking for the same query.

**Practical implication:** Two pages covering the same topic with the same structure and similar wording will not both rank well. The one offering unique data, examples, or perspective will win.

Source: Google Search Central, "Creating helpful, reliable, people-first content" (updated March 2024). US Patent 11,769,017, "Information gain score for a document" (September 2023).

---

## E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

Google's quality rater guidelines use E-E-A-T to evaluate page quality. Not a direct ranking factor, but it shapes the algorithms that are.

**The four signals:**
- **Experience:** Has the author actually done or used the thing they are writing about? (Added December 2022)
- **Expertise:** Does the author have formal knowledge or deep skill in the topic?
- **Authoritativeness:** Is the author or site recognized as a go-to source?
- **Trustworthiness:** Is the content accurate, transparent, and honest?

**Post-March 2026 reality:** Experience is now the strongest differentiating signal. After the March 2026 core update, pages with specific examples, real outcomes, verifiable credentials, and first-person accounts consistently outperform pages with technically accurate but impersonal content.

Google's Search Quality Evaluator Guidelines (version 13.0, updated January 2026) dedicate more space to Experience evaluation than any prior version, including explicit instructions for raters to look for "evidence the content creator has direct involvement with the topic."

Source: Google Search Quality Evaluator Guidelines, v13.0 (January 2026). Google Search Central, "E-E-A-T and the helpful content system" (updated 2024).

---

## Google's Official AI Content Policy

**The policy (established February 2023, unchanged as of May 2026):** AI-generated content is acceptable if it is helpful, reliable, and people-first. Google does not penalize content based on how it was produced. The focus is on quality, not method.

Key quote from Google's February 2023 blog post: "Our focus on the quality of content, rather than how content is produced, is a useful guide that has helped us deliver reliable, high quality results to users for years."

Google Search Central documentation (updated 2024) reiterates: "Appropriate use of AI or automation is not against our guidelines. It is used to generate content, including to generate content that is helpful, that is used responsibly."

**What this means in practice:** Using AI to draft, outline, research, or structure content is fine. Publishing unreviewed AI output at scale that adds nothing new to the web is what triggers penalties, and that is a quality issue, not a tools issue.

Source: Google Search Central Blog, "Google Search's guidance about AI-generated content" (February 8, 2023). Google Search Central, "Spam policies for Google web search" (updated 2024).

---

## Six Penalty Triggers for AI Content

Based on patterns observed across the March 2024, December 2025, and March 2026 core updates. These are the behaviors most consistently associated with ranking drops:

1. **Publishing velocity spikes.** Going from 2 posts/month to 50 posts/month without a corresponding increase in team size or stated editorial capacity. Google's systems detect unnatural publishing cadence changes.

2. **Thin content at scale.** High volume of pages that cover a topic at surface level without unique insight, original data, or practitioner experience. Depth per page matters more than total pages.

3. **Topical mismatch.** Publishing content outside the site's established topical authority to chase traffic. A plumbing company publishing articles about cryptocurrency is a classic example.

4. **Factual errors.** AI hallucinations that go unedited. Incorrect statistics, fabricated citations, wrong dates, and misattributed quotes. Google's systems are increasingly able to cross-reference claims.

5. **Duplicate intent pages.** Multiple pages targeting the same search intent with minor wording variations. This includes creating separate pages for "best CRM software" and "top CRM tools" when the intent is identical.

6. **Unedited AI output.** Content that reads like a language model wrote it: generic structure, no specific examples, no original perspective, hedging language, and the same information available on every other page. The absence of a human editorial layer is detectable.

Source: Lily Ray, Amsive Digital, "AI Content and Google Penalties: What We Know" (March 2026). Search Engine Journal, "Sites Hit by March 2024 Core Update" (May 2024). Glenn Gabe, "December 2025 Core Update Analysis" (January 2026).

---

## Key Statistics

| Stat | Detail | Source |
|---|---|---|
| 86.5% of top-ranking pages use AI assistance | Survey of 10,000 top-ranking URLs across 500 keywords | Originality.ai, "AI Content in Search" (February 2026) |
| Human-written content is 8x more likely to rank #1 | Comparison of purely human vs purely AI content | Surfer SEO, "AI vs Human Content Study" (January 2026) |
| AI-assisted content with quality gates performs 23% better | Content using AI for drafting but with expert review, original examples, and editorial polish | Clearscope, "Content Quality Benchmark" (March 2026) |
| Pure AI content collapses by month 3 | Unedited AI content typically loses 40-60% of initial rankings within 90 days | Ahrefs, "Longevity of AI Content" (December 2025) |
| 48% of Google queries show AI Overviews | Up from 34.5% in Dec 2025 | Semrush (March 2026) |
| 60% zero-click search rate | Up from 56% in 2024 | SparkToro/Datos (2026) |
| 33% global publisher traffic decline | Year-over-year to November 2025 | Multiple sources (2025-2026) |
| 35% more clicks for cited sources | Sites cited in AI Overviews vs standard position-one | Multiple sources (2026) |
| 50% of AI-cited content is under 13 weeks old | Freshness is critical for AI citation | SaleSpeak AI (2026) |

**The interpretation:** AI is a production tool, not a quality shortcut. The best-performing content uses AI for efficiency while layering in human expertise, original research, and editorial judgment. The worst-performing content uses AI to skip those steps entirely.
