# Rank Week 2026 — Day 2: Money Page Audit (Matt Diamante)

## Tactics & step-by-step how-to

- **Define your money page**: any page on your site that makes you money — a service page or product page, the page someone lands on when they're ready to buy/hire. Not your contact page, booking page, or appointments page ("those pages don't rank"). Homepage counts if you don't have a dedicated one.
  - Examples given: dentist → dental implants page; wedding photographer → luxury wedding photography packages page; realtor → "home for sale in Scottsdale, Arizona"; hat store → baseball hats / a collection / a specific product; hot sauce company → "buy ghost peppers hot sauce" / "Carolina reaper hot sauce"; plumber → 24-hour emergency page; personal trainer → "personal trainer in Vancouver"; lawyer → car accident lawyer page; garage door company → "garage door installation [city]"; ecommerce → shop/collection/product page; psychotherapist → "couples counseling" or "PTSD therapy" page (not a generic "therapy" page).
  - If stuck, literally ask ChatGPT: "I am a realtor, what would be my money page?"
- **5-step audit workflow** (homework: do this for your money page + your top 3 competitors before the next session):
  1. **Set up the audit spreadsheet** (copy link below). Add two things: your money page URL, and your focus keyword (e.g. "Hamilton Electrician," "Wedding Photographer Birmingham"). One keyword per page.
  2. **Go to pageaudit.com**, paste your money page URL + keyword, hit Analyze. Go to the **Content tab** and copy 3 numbers into the sheet: **word count**, **keyword occurrences**, **keyword density** (%, auto-calculated).
  3. **Install the Page Audit Chrome extension**, click it while on your money page, grab: **title tag**, **meta description**, **H1/H2/H3 tags** (use the "Copy All Headings" button in the extension's Headings tab, paste, then manually sort into H1/H2/H3 columns).
  4. **Run pagespeed.web.dev** on the money page URL (not the homepage unless that's your money page) — record **mobile score** and **desktop score**.
  5. **Repeat all of the above for your top 3 competitors**: Google your exact focus keyword in an incognito window, skip sponsored results and directories (no Reddit, no aggregators), open the top 3 real business sites, run the identical audit on each into the same spreadsheet.
  - End state: a side-by-side comparison — more/fewer words than competitors, keyword usage frequency, page speed, whether competitors use the keyword in title tag/H1.
- **Location/service-page architecture**: one keyword = one page, always.
  - Local business serving one area: keyword = service + city (e.g. "web design Hamilton").
  - Local business serving many areas: build "location pages" (one per area), start with **5**, add more over time — don't try to rank all territories/counties at once.
  - Multiple distinct service types (e.g. wedding photography vs. portrait painting; weddings vs. corporate events vs. birthday parties for a magician): separate dedicated page per type/keyword. A general overview page can mention all services and internally link out to each dedicated page, but don't blend multiple keyword-topics onto one page.
  - Multi-location businesses under one brand (dental clinics, franchises): favor location-specific pages (or even separate sites) over one shared generic service page — a searcher looking for a dentist "near them" doesn't care that you also have a location across town.
- **EMF protection "back door" tactic** (heavily censored/regulated keyword): stop fighting directly for the saturated head term. Write supporting content around adjacent questions a concerned-but-not-keyword-literate searcher would type instead (e.g. "Is WiFi dangerous for you?", "Does EMF cause cancer?") — you don't need to use the flagged/technical term at all.
- **Directory competition tactic**: if directories (or larger competitors) outrank you, get your business listed on those directories for free rather than trying to out-content them — it sends a signal ("the site ranking #1/#2 is linking to this business too").
- **Ranking in ChatGPT/AI tools**: rank on Google first — LLMs query existing search engines and pull from those results rather than scanning the live web fresh each time (cited: Edward Sturm's public IG/TikTok breakdowns of what happens when ChatGPT does a search).

## Rules / dos & don'ts (keep every threshold, number, specific)

- **One keyword per page** — non-negotiable, repeated throughout ("every page on your website should be focused on one keyword" — can be a 3–4 word phrase, but one phrase per page).
- **Never use "near me" as your target keyword.** Google already knows searcher + business location and connects them; using "near me" in your copy/keyword targeting is "the sign of somebody who doesn't know how to do SEO."
- **Don't obsess over the overall audit score.** A 76% (or lower) can still rank #1 — look at the specific metrics, not the aggregate percentage.
- **Only one H1 tag per page.** If everything is currently tagged H1, that's a problem to flag (fix comes "tomorrow," not today).
- **Wait 3–6 months** after making changes before re-auditing/re-checking a page — give Google time to process. Keep publishing blog posts that link back to the money page in the meantime.
- **No crawl-budget cap or "domain age" waiting period exists.** Anyone who tells you a new domain (under a year) gets a limited crawl allowance is wrong — "you need to go slap them" (not literally). Proof: a domain Matt registered in 2014 went from 0 to 4 million monthly visitors (Google + Facebook combined) within 6 months.
- **Bad backlinks**: might have a small negative effect, but "likely not impacting it at all." Focus on content first.
- **Ignore pingback notifications entirely** — don't approve them. Comment-section pingbacks/spam can appear even on sites with no visible comment section.
- **Skip sponsored results and directories** when identifying your top 3 competitors for the audit — must be real, ranking business websites.
- **Shopify**: use the native blog. Don't install a third-party blogging app.
- **Word count will differ slightly between pageaudit.com and the browser extension** — don't chase perfect precision; if both tools are within ~100–200 words of each other, treat that as close enough. Background bloat is real: one inactive/unused plugin was found adding 2,000 words to every page's count.
- **Keyword Planner showing zero search volume for a local long-tail term doesn't mean skip it** — volume tools are estimates; low/no reported volume often just means the exact phrase variation hasn't been picked up yet, or traffic is bucketed under "near me" style queries instead.
- Franchise/multi-territory constraint: build location pages per city, but don't cross into a market a fellow franchisee legally owns (business/legal constraint, not an SEO one).
- Blog content strategy: keep how-to/evergreen posts **generalized** rather than hyper-localized to one narrow reader, even if the AI draft naturally leans specific — "go as general as the question requires, or as specific as the question requires."

## Tools, prompts & resources

- **Audit spreadsheet** (copy required, do not edit the shared master): https://docs.google.com/spreadsheets/d/1qkz0xRMEct_eqkWl86II0rva8TcwdE573JL2_LJNezQ/copy
- **pageaudit.com** — free tool built by Hey Tony ("free forever," per Matt, "for now... this is available to the public"). Paste money-page URL + focus keyword → Analyze → overall score + Content tab (word count, keyword occurrences, keyword density).
- **Page Audit Chrome extension** ("PA" icon) — install via "Add to Chrome" on pageaudit.com. Surfaces title tag, meta description, H1/H2/H3 on the live page; has a "Copy All Headings" button. Chrome-only. If it doesn't populate: you clicked too fast or the site is loading too slowly — wait ~30 seconds, scroll to bottom then back to top (can be a lazy-load issue).
- **pagespeed.web.dev** — free Google tool, mobile + desktop scores, ~30 seconds to run.
- Both pageaudit.com and its Chrome extension reportedly cost Matt **$30,000–$40,000** to develop; given free to reduce the cost barrier to doing SEO.
- **ChatGPT** — tomorrow's session uses it to analyze the audit-spreadsheet gaps and generate exactly what to change on the money page (no prompt text given yet in this session).
- **Google Keyword Planner** — referenced as one option for checking search volume on a target keyword (flagged as unreliable for local long-tail terms, see Tradeoffs).
- **WordPress** — confirmed fine as a platform after 15 years' use (Paro's question). **Rank Math** vs **Yoast**: Matt personally uses Yoast, clients use Rank Math, "it honestly doesn't make a difference" which one you use.
- **Shopify's native blog** — recommended over any third-party blogging app.
- **HeyTony Insiders** membership: $57/month normally; **rankweek2026** discount code deducts the $10 Rank Week registration fee from month one (~$47 first month). Insiders calls run 3–4x/week, ~20 people per call, standing time 10am Eastern (this Rank Week call itself runs at 1pm Eastern; Matt is considering moving the standard Insiders time to 1pm Eastern since it works best across the most timezones globally — pending a member vote). Replay access: $10 Rank Week ticket = replays good ~10 days; ~$17 ticket or full Insiders membership = replays available forever, no separate purchase.
- Support/help contact referenced verbally (garbled in transcript, likely **support@heytony.ca**) for replay/access issues.

## Case studies / examples / results

- **Day 1 recap stats**: 1,600 people attended (Matt's biggest single call ever); 403 people wrote and posted a blog post during/after the call — over 25% of attendees. Testimonials read aloud: Susan — "this blog looks glorious, much better than the blogs currently on my website that I've paid a lot of money for"; Andy Zed — "This is the best document I've seen from working with ChatGPT. Having the right prompts is definitely critical"; Glenn J. — "This is an aha moment for me"; Catherine — "I'm pumped because it is authentically showing up, not playing a keyword game."
- **Client results screenshot** (referenced from Day 1, shown again as proof): every client's SEO trending upward, on content that is "heavy, heavy, heavy AI" but human-edited/verified — cited as evidence that AI-assisted content is not penalized when it's genuinely helpful.
- **Stack Electric** (Hamilton electrician, friend of Matt's, no SEO work done by Matt's team) — ranks #1 for "Hamilton Electrician" using their homepage as the money page. Audit numbers: **829 words**, keyword used **3 times**, overall pageaudit.com score **76%** (Matt's own site also scored 76% — reinforcing "don't obsess over the score").  Page speed: **53 mobile / 79 desktop**. In the live competitor-audit demo, the #2/#3 competitor for the same term used the keyword only once (density ~0.11%) and scored **68 on desktop** with mobile stalling to load (flagged as a bad sign).
- **Tim (EMF protection business)** — main keyword "EMF protection" gets **~6,000 searches/month** vs. ~100 for alternative terms; wrote ~60 blog posts, 58 about EMF protection, none of them ranking — the only 2 posts that rank are on unrelated topics (vortex mathematics, Taurus stones). Got investigated by the UK Advertising Standards Authority over a "completely neutral vanilla" Facebook ad; ASA cited GDPR to withhold the complainant's identity and the complaint details, then told him to remove the word "protection" from his site.
- **Bernard** — domain under a year old, worried about a crawl-budget cap (debunked, see Rules); also noted word-count mismatch between pageaudit.com and the extension.
- **Chris** (custom home builder, outside Austin, TX) — serves 20–30 counties; searched "custom home Burnett County" and couldn't find his own site by page 5. Advised to pick 5 counties to start (see "pigs get fat, hogs get slaughtered" quote) rather than targeting all 20–30 at once.
- **Brianne** (portrait photographer + oil portrait painter, Birmingham) — advised two separate money pages: "Portrait Photographer/Photography Birmingham" and a distinct oil-painting-portraits page, since photography clients can be upsold into painting.
- **Gleb** (dental practice, 6 clinics under one partnership brand) — one shared generic "dental implants" page with no location split, despite each clinic having its own Google Business Profile. Matt recommended considering individual websites per clinic/location instead of unifying under one brand site, contradicting advice Gleb got from the agency that built the site.
- **Paro** (magician, Sussex UK, 22 years in business, 20 years doing own SEO) — previously ranked #1 for "London magician," lost the position after an algorithm change; serves London (~1 hr away), Sussex, Surrey; does weddings, corporate events, private parties. Advised: separate dedicated pages per event type ("Wedding Magician Kent," "Corporate Magician Kent"), with a general "Magician Kent" page linking out to each.
- **Sabrina** (therapist, "brain spotting" niche) — competing against VC-backed directory sites (e.g. "Growth Therapy") and two aggregator directories; already outranked by only one small local practice once sponsored results/directories are excluded. Advised to get listed (free) on the directories currently outranking her rather than trying to out-content them.
- **William Vega's business (wife Brenda asking)** — dumpster rental company, 16 counties served, 16 existing county pages already live. Advised to run the audit one county page at a time, not all 16 at once, to avoid redoing work if the approach changes.
- **Katie** — brand-new site, pageaudit.com score of **38%**, zero keyword density, no meta title/description, no keyword occurrences recorded.
- **Sarah Hodge** (Australia, trades/Google Business Profile content) — her page **passed** Core Web Vitals while the #1-ranked competitor **failed** it, despite being outranked overall. Her Day-1 ChatGPT-drafted blog post (on getting customers via Google Business Profile) got auto-tailored to her specific region ("Northern Rivers," Australia) after she answered ChatGPT's clarifying questions on business type + geography — Matt's read: keep such evergreen guides more generalized.
- **Ivan / two-franchise owner** (bathroom remodeling + kitchen remodeling franchises, each covering multiple cities/territories) — advised one page per city/keyword, never mixing multiple cities on one page; also has to avoid targeting cities owned by fellow franchisees.
- **Maurice** (mobile entertainment: game trucks, laser tag, phone parties) — asked about AEO/GEO strategy ahead of a website rebuild; answer reduced to "rank on Google first" for LLM visibility.
- **Melanie** — subdomain SEO confirmed to work identically to a main domain.
- **Danielle B.** — Shopify product-based business; told to use the native blog, not a third-party app; also asks about audit timing — audit can be run immediately after publishing (you're not changing anything yet, just benchmarking against the top 3).
- **Ritva McGinn** — affiliate marketer targeting a demographic/gender/age niche rather than a location; advised to genuinely review/use products (opinions, pros/cons, ideally video) and add a blog to the affiliate sales site.

## Notable verbatim quotes

- "Google doesn't care if you're using AI to write your content... they care if it's helpful... We shouldn't be creating content to game the algorithm. We should be creating content to help real people to solve their problems."
- "Pigs get fat and hogs get slaughtered" — Matt's old accountant's line, applied to trying to claim too many counties/keywords/locations at once instead of starting with 5.
- "SEO is not a sprint. It is a marathon. And we get through it by not overwhelming ourselves, not doing too much, but by outlasting our competition and just being consistent with it."
- "Every page on your website should be focused on one keyword."
- On the crawl-budget myth: "there's no 100% rules... I can tell you this is the 100% proper way to optimize a page and it's going to rank, and somebody doing a [bad] job can keep their number one spot because they're doing something else."
- "If you can show up for one hour a week, you're doing more SEO than 99% of people."
- "Does this really work better than ads? ... SEO is free. Everything we've done today is free. I gave you tools as well."
- On backlinks: "It might impact it negatively. It is likely not impacting it at all, though."

## Tradeoffs & nuance

- The audit's **overall percentage score is deliberately de-emphasized** — a page can score 76% (same as a #1-ranked competitor) and still win; the individual metrics (word count, keyword usage, page speed, tag usage) are what matter, not the composite number.
- **Search-volume tools understate local/niche demand.** Zero reported volume for a specific local phrase doesn't mean don't target it — it may just mean the tool hasn't caught that exact variation, or that real searches are being bucketed under generic "near me" queries instead (which you still shouldn't target directly).
- **Backlinks are a real but overrated worry** — bad backlinks might hurt, but Matt frames it as a low-priority concern relative to fixing content/on-page factors first.
- **Directories aren't always the enemy.** Rather than fighting a directory or aggregator that outranks you, getting listed there (free, usually) can work in your favor as an association/legitimacy signal.
- **Franchise/multi-location branding tension**: business owners often want one unified brand site (for consistency/partnership reasons), but Matt's SEO advice pulls the other way — separate location pages or even separate sites capture more total keyword real estate, at the cost of diluting the "one unified brand" feel the owners may have chosen deliberately (e.g. Gleb's dental partnership, explicitly built as one brand per doctors' preference).
- **Generalized vs. specific content**: AI will happily hyper-localize a blog draft if you feed it your specific region during the interview step, but Matt's guidance is to pull back toward general applicability for ranking purposes — the more specific/useful draft isn't necessarily the better-ranking one.
- **Time-commitment objection handling**: explicitly reframed as a "loaded question" — Matt's answer to "I don't have much time" is always "do you have one hour a week," positioning even minimal, consistent participation as outperforming most competitors, rather than requiring full-time effort.
- **Domain-age/crawl-budget and AI-content-penalty are both treated as myths to actively debunk**, not just downplay — Matt frames both as things members were told by other "SEO people" that actively hold them back if believed.
