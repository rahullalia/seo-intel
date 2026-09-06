# Technical Replay with Denroy — 2025.12.04 (Call #121)

Format: small live Q&A (3 attendees: Brett, Monica via submitted written questions, James). Denroy = ~5 years working with Matt at Hey Tony; background spans WordPress, Wix, Squarespace, Shopify, HubSpot, Storyblok CMS builds, Google Search Ads, and some YouTube/Reddit/Pinterest SEO. Duration 51m25s.

## Tactics & step-by-step how-to

- **Auditing/cleaning up ranking tag pages (Brett's realtor site):**
  1. Run `site:yourdomain.com` in Google to see everything indexed.
  2. In Google Search Console: Performance → Search Results → Add Filter → Page filter → "URL containing" → paste the path up to `/tag/` (e.g. everything before `blog/tag/`). This surfaces every indexed tag page regardless of the ending slug.
  3. Click "Pages" to see per-page impressions/clicks.
  4. If traffic is insignificant, delete the tag pages in WordPress and 301 redirect them.
  5. Redirect target priority: a similar page already ranking → a similar category page → a similar blog post → homepage (last resort).
  6. If tag pages DO carry meaningful traffic, keep them live for now; first publish better content to outrank them for the same keywords, then once that new content ranks, delete the tag pages and redirect.

- **Diagnosing a drastic ranking/authority drop (Monica's site — DR 36→4, homepage visits from hundreds to <100/month):**
  1. Go into Search Console, run a period comparison (a few months ago vs. now).
  2. Filter the dropped pages by clicks — identify whether it's a specific page or a specific search query losing clicks.
  3. Manually search the losing query in Google — check for a new competitor going heavy on that keyword, or new competing content that's displaced you.
  4. Check Search Console → Security & Manual Actions (left sidebar) — a manual action signals a backlink problem; may require disavowing low-quality/spammy backlinks.
  5. Get the full scope from Search Console before doing anything drastic (e.g. before disavowing).
  6. Separately, treat a huge Ahrefs DR swing with suspicion — it can be a false flag if their crawler hasn't fully refreshed; run a secondary Ahrefs crawl to confirm before acting on it.

- **Changing permalink/URL structure:** always 301 redirect old URL → new URL for every changed slug, AND manually force an XML sitemap refresh/recrawl inside the SEO plugin (Yoast/All in One SEO usually auto-update, but can lag).

- **Improving location pages live 1+ year with low visibility:**
  - Add the location-page link into Google Business Profile posts, with descriptive copy naming the service + location.
  - Build more internal links to those pages: scan existing blog posts for mentions of that neighborhood/area and link back to the location page from there. More internal links = more authority Google assigns that page.

- **Realtor/local-business keyword research (Brett's problem: generic "Realtor" SEMrush searches return industry/practitioner content, not buyer/seller intent):**
  - Break location pages down by neighborhood, not just by city (east/west, named communities, "by the beach," etc.) — lower search volume but far easier to rank, especially for a lower-authority site.
  - Structure content around buy vs. sell intent per neighborhood, e.g. "buy a beach home in Miami."
  - Mine actual past-client questions as keyword seeds ("what is the average house cost in Miami," "can I get approved for a mortgage on minimum wage") — type these verbatim into SEMrush/Google to see real volume and variations.
  - Cross-reference SEMrush and Google's own autosuggest until you find a term with real (even low, e.g. 10–20/mo) volume at low difficulty.

- **Looker Studio: tracking trending pages/posts (Monica's Q4), step by step:**
  1. Open the landing-page chart, edit its filter (or add one).
  2. New filter → Include → field = landing page → condition "contains" (or "equals to" if using UTM/tracking codes) → paste the page URL → save.
  3. To track multiple pages on one chart: edit the filter again, use the "OR" option, add another "landing page contains [url]" line, repeat per page/post.
  4. Output: individual growth per page plus a combined growth total across everything included.
  5. To isolate one page again, delete the extra OR conditions.
  6. There is no dynamic way (yet) to pull GSC/GA4's native "Trending"/Insights tab into Looker Studio — fully manual, copy-paste each URL. They're watching for Google to add a trending dimension to Looker Studio; doesn't exist yet.

- **Blending Google Analytics into the same Looker Studio report:** Add Data Source → Google Analytics → select the GA account (must share the same signed-in email) → Accept. Once added, GA and Search Console data can combine in the same report.

- **Tracking AI/LLM referral traffic in Looker Studio (via GA4):** create a filter on dimension "session source," condition "contains," value = the AI platform name (e.g. "chatgpt" for ChatGPT traffic, or the model name for Perplexity). Surfaces every session where that AI referenced/cited the site. Same pattern for any additional LLM — just swap the string.

- **YouTube → blog traffic migration (James's son's cleaning-content channel, site: letscleanthatup.com):**
  - Link the matching blog post in the YouTube video description whenever topics are the same.
  - Reword the anchor phrase to include the actual target keyword next to the link — e.g. "Read our blog on the best way to clean your oven" instead of generic "Read the blog here." This creates pseudo-anchor-text so Google associates the keyword with that URL even without a literal hyperlinked keyword.
  - Put that blog link **above the fold** in the description (visible before "show more"/"view more") — links higher up carry more weight than links buried lower.
  - Embed the matching YouTube video directly inside the corresponding blog post.
  - Image alt text: must contain the target keyword (or a variation) for that page, while still accurately describing what's actually in the image — never keyword-stuff for its own sake.
  - Internal linking: "go crazy" — 4, 5, 6+ internal links per post; called one of their historically best-performing tactics.

- **Local/physical-presence SEO for a business with an office (even if mostly online):** a verified physical location + properly set-up Google Business Profile can produce a fast #1 local rank; also unlocks Google Maps visibility to nearby people who don't already know the brand; also unlocks citation-building (directory listings functioning as backlinks), which raises domain authority.

- **Social bio-link strategy (Instagram/TikTok → website):** avoid Linktree/aggregators — link directly to the destination site/page wherever the platform allows it. Reasoning covers both SEO (link equity passes to the middleman domain first, only the remainder reaches your site) and UX (extra redirect hop can fail if the aggregator is slow, or if the visitor's ad-blocker/anti-spam extension blocks the redirect).

- **Email/newsletter strategy:** recommended core technique is behavioral list segmentation — automate moving a subscriber to a different list/segment based on which email(s) they open (open one → move to list A; open another → move to list B, etc.).

## Rules / dos & don'ts (keep every threshold, number, specific)

- Tag pages: safe to delete + 301 redirect if traffic is insignificant. Threshold given: keep them live if they're bringing in **more than 5% of your total site traffic** — otherwise cut them.
- Redirect priority order: similar already-ranking page → similar category page → similar blog post → homepage (last resort only).
- Any permalink/slug change: ALWAYS 301 redirect old→new, and always manually force an XML sitemap refresh rather than trusting plugin auto-update timing.
- Before disavowing backlinks or taking drastic action on a traffic/ranking drop: fully check Search Console first (period comparison, clicks by page/query, Security & Manual Actions).
- A large authority-score swing (e.g. Ahrefs DR 36→4) may be a stale-crawl false flag — always re-crawl/verify before treating it as real and acting on it.
- Alt text must include the keyword/variation AND still accurately describe the image — no keyword stuffing "for the sake of it."
- Internal linking has no stated ceiling in this call — "go insane with it," 4–6+ per post encouraged.
- Avoid Linktree/link aggregators — link directly to the destination whenever the platform permits.
- YouTube descriptions: put the blog link above the fold, and word the anchor phrase with the actual target keyword rather than a generic "read the blog here."
- Denroy's DM response commitment: replies within 48 hours, or as soon as possible.

## Tools, prompts & resources (exact prompt wording if quoted; tool names; settings)

- **Google Search Console** — Performance → Search Results → Add Filter → Page → "URL containing" (isolating tag-page/path-pattern traffic); Security & Manual Actions (left sidebar) for backlink-penalty checks; period comparison for diagnosing drops.
- `site:domain.com` — quick indexed-page check via Google search.
- **Ahrefs** — Domain Rating (DR) / authority metric used in this call; flagged as capable of a stale-crawl false flag on big swings.
- **SEMrush** — primary keyword-research tool discussed; cross-referenced against Google's own autosuggest.
- **Serpstat** — Brett's former tool, described by him as "not highly effective."
- **Answer the Public** (free tier) — Brett's tool for long-tail/question-based keyword ideas.
- **Looker Studio** — custom dashboard for multi-page/post traffic trends; filter mechanics: landing page "contains" + OR chaining across multiple URLs; Add Data Source → Google Analytics to blend GSC + GA4; session source "contains chatgpt" (or other AI name) for LLM referral tracking. Demoed live on the Hey Tony profile itself.
- **WordPress + Yoast / All in One SEO** (or similar) — sitemap auto-update with a manual "recrawl/refresh" option.
- A WordPress redirect plugin (unnamed) — for 301s after deleting tag pages.
- **Google Business Profile (GBP)** — posting location-page links with descriptive copy; also the mechanism for fast local ranking off a verified physical address.
- **Citation directories** — Brownbook, Yellow Book/Yellow Pages named as examples that function as backlinks/authority builders.
- **Linktree** — named specifically as the bio-link tool to de-prioritize/avoid.
- **Beehiiv** — James's current newsletter platform; founded by the team behind Morning Brew (built after they sold it); described as "high level" on features/segmentation.
- **Mailchimp** — Denroy's suggested simpler fallback if advanced automation isn't required.
- **GoHighLevel (GHL)** — Matt's own preferred email platform; Denroy explicitly said he's "not too experienced" with it and deferred detailed GHL questions to Matt.
- Sites referenced live: "Brett Sells Miami.com" (redirects to "Advanced Realty Miami," has MLS search on homepage), and "letscleanthatup.com" (James's son's oven-cleaning content site).

## Case studies / examples / results (names, niches, numbers)

- **Brett — realtor site (Brett Sells Miami → Advanced Realty Miami):** `site:` search revealed many low-value tag pages ranking. Live-pulled numbers: impressions of 29, 10, 3, 12, 2, 7 across tag pages over 3 months, with only 3 total clicks combined — confirmed insignificant, cleared for deletion + 301 redirect.
- **Monica's site:** homepage visits dropped from "hundreds" to fewer than 100/month; Ahrefs Domain Rating dropped from 36 to 4 over the same period. Only recent site changes were heading-tag corrections and title/meta description improvements. Denroy's read: more likely backlink-related (spam/quality) than the on-page edits, but also flagged the DR number itself as a possible stale-Ahrefs-crawl artifact needing re-verification.
- **Matt (Hey Tony) internal linking case:** got a page to rank #1 in 3 hours using internal linking alone — Denroy says he personally witnessed it happen live.
- **James's son — YouTube/TikTok creator, now building a website/blog backwards:** built a large following during COVID; described as "already an authority" — already surfacing in ChatGPT search results for his video topics. Team is backfilling SEO/website infrastructure after audience-first growth.
- **James's/his son's newsletter (Beehiiv):** ~7,000 subscribers, entirely organic, "no push," no active list-building lift. Paused during a family caregiving period (mother passed away, father had Alzheimer's and has since also passed away); now being relaunched as a priority.
- **letscleanthatup.com — oven-cleaning post/video live audit:** blog link found buried below the fold in the YouTube description with generic "read the blog here" phrasing; images missing alt text; heading structure otherwise good (clean single H1) but one empty H2 found; good use of timestamps; heavy use of Amazon affiliate links (assessed as fine as-is); internal linking gap flagged as the top priority to fix going forward.

## Notable verbatim quotes

- "Google's not dumb. It can still tell... this was meant to go with this." — on keyword-adjacent-to-link pseudo-anchor-text in YouTube descriptions.
- "Matt got a page to rank one in three hours. Just internal linking." / "I was there when you did that blog... that blog made me double check. Like wait, how'd mine do?"
- "If you go, go crazy with internal links... 4, 5, 6, just go insane with it. And that, that has historically given us some of the best results."
- "I always say link directly to the website or the page you want. You don't want to link to the middleman." / "I am very against this, this link tree link, if possible."
- "Don't just keyword stuff for the sake of keyword stuffing. That doesn't help anyone."
- "Email is one of the best platforms for conversion optimization. It beats almost everything when you manage your email list properly."

## Tradeoffs & nuance

- Tag-page deletion is conditional, not automatic: if a tag page already carries meaningful traffic (>5% of site total), the safer sequence is to out-rank it with better content first and only then delete/redirect — deleting first is riskier once a page has real traffic.
- A domain-rating collapse has two very different possible causes needing different responses: a real backlink-quality problem (→ disavow candidate) vs. third-party tool crawl staleness (→ just re-crawl and re-check). Jumping straight to disavowing without confirming which is discouraged.
- Neighborhood-level location pages trade search volume for winnability — lower monthly volume than a city-wide "Realtor [city]" term, but much more realistic to rank, especially on a lower-authority or structurally awkward site (one bouncing between an MLS tool and a blog).
- Linktree-style aggregators aren't banned outright: acceptable when a creator deliberately spreads attention across many platforms with no single preferred destination, but work against you when the actual goal is funneling one platform's audience toward one specific destination.
- Physical/local presence is a real SEO lever (fast GBP ranking, Maps visibility, citation backlinks) but remains a business-model decision, not just an SEO checkbox — James was explicit that going physical/storefront is still an open business decision separate from the SEO upside discussed.
- Email platform choice (Beehiiv vs. Mailchimp vs. GHL) is framed as "it depends what you need": Beehiiv already supports full open-based segmentation/automation (being built by the Morning Brew team), so there's no urgency to migrate off it; Mailchimp is only floated as a simpler fallback if heavy automation isn't required; GHL is Matt's preference, but Denroy explicitly deferred on it as outside his expertise.
