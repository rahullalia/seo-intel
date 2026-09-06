# Rank Week Day 3 Replay (Call 117)

Source: HeyTony Insiders — Call Replay (hash: pqz0Pjd7DK) | 59m 11s | ~9,684 words

## Tactics & step-by-step how-to
- **Step 1 — Turn yesterday's audit into new SEO tags (Prompt 1):**
  1. Open the Money Page Audit spreadsheet from Day 2. Copy columns A and B (your own title tag, meta description, H1, H2s, keyword density, etc.) exactly as-is — messy formatting is fine, ChatGPT parses it correctly.
  2. Paste that into ChatGPT under Prompt 1's `[PASTE YOUR AUDIT]` placeholder. Don't press enter yet.
  3. Copy competitor #1's column (same row order as yours) and paste it under "Competitor 1 (Same Order As Mine)."
  4. Copy competitor #2's column and paste it under "Competitor 2 (Same Order As Mine)."
  5. Press enter. ChatGPT returns an updated title tag, meta description, H1 tag, and updated H2 tags.
  6. Open a separate blank document (don't work only inside ChatGPT). Copy the new title tag, meta description, and H1 into it.
  7. Manually review each: confirm the keyword is present and front-loaded; if a semantic variant tested better on Day 2 (e.g. Google preferring "web design" over "website design"), swap it in even if ChatGPT didn't.
  8. Take the new H2 tags, paste into the doc under a "page outline" / "content outline" heading, strip the "H2 number 1" labels and bold formatting, and rewrite any that don't sound like something a real person would say (e.g. reworked "Hamilton website design that actually works" into "web design in Hamilton" / "Hamilton-based website design that actually works").
- **Step 2 — Rewrite the full money page (Prompt 2):**
  1. Select the entire existing page's content (Cmd+A or drag-select to the bottom) and copy it into `[PASTE YOUR CONTENT]`.
  2. For each competitor, try pasting just their URL first under "Competitor 1:" / "Competitor 2:" — ChatGPT can sometimes read the live page directly. If it doesn't work, paste the full competitor page content instead.
  3. Fill in your focus keyword.
  4. Set the word-count range using competitor word counts from the audit (comp low–comp high), e.g. spotting competitors around ~2,500 and ~2,300 words and setting a 2,200-word target.
  5. If ChatGPT asks a clarifying question first (e.g. keep your current structure vs. rebuild the structure vs. a third option), answer it before it writes.
  6. Do not trust the word count or keyword count ChatGPT claims to have hit — verify manually every time.
  7. Paste the output into wordcounter.net to check actual word count and keyword occurrence count/density.
  8. Compare your keyword's occurrence count against both competitors' counts and land in that band (not above or below).
  9. Edit the draft by hand: confirm it accurately describes your real process/product/service, remove artificial numbered-list phrasing unless it's a genuine list, and fold in real case studies/personal experience if the page didn't already have them (existing on-page case studies get pulled in automatically since the source content was pasted in).
  10. To refine one section: paste just that section back into the same ChatGPT thread and ask something like "can you rewrite this section to be more funny and personable," or ask it to expand a specific section — do this one section at a time.
  11. To restore skipped headings: tell ChatGPT "you forgot these heading two tags, write a couple paragraphs each and expand on the ideas."
  12. To deepen a section with real expertise: paste the section and add "ask me five questions to write a better unique piece of content using my expertise, experience, etc." Answer by typing or using ChatGPT's voice mode, then have it rewrite using your answers.
  13. Before publishing, re-run the page-audit tool (browser extension or pageaudit.com) on the new draft to recheck keyword density/word count.
- **Sanity-check any AI draft against real buyer questions**, regardless of what ChatGPT itself asked: price, timeline/shipping time, use cases/applications, ingredients/specs — whatever's relevant to what you sell.
- **Location pages**: build one page per service area you actually serve, each with genuinely unique content — reference local specifics (different utility companies, local permit requirements, area-specific pricing) rather than swapping only the city name across identical copy.
- **Expanding to new states/regions**: for a more competitive expansion, consider a fully separate website per state/region instead of just subpages, and set up one Google Business Profile per physical location, each linking to its matching location page (or dedicated site).
- **"Backdoor" strategy for keywords too competitive to rank on directly**: instead of fighting for the hard product/category keyword, write blog posts answering the adjacent questions buyers actually ask (e.g. "can you take pre-workout when pregnant?", "can you take pre-workout with high/low blood pressure?", "how long before a workout should you take pre-workout?"). Publish 1–2 posts/week, not all at once. Route blog traffic to the product via in-post mentions/links or a pop-up discount code.
- **When a competitor ranking #1 has thin or no on-page SEO** (no H2/H3s, minimal words): you likely don't need much either — match roughly what the #1 result actually has instead of over-building.
- **If a competitor outranks you**, don't change many things simultaneously — isolate one variable at a time (e.g., try building backlinks first) before a full overhaul.
- Matt frames this 2-prompt process as a fast starting point, not the full method — for stronger results, blend it with the Day 1 technique of having ChatGPT ask clarifying questions before writing, rather than treating this output as final.

## Rules / dos & don'ts (keep every threshold, number, specific)
- Do NOT keyword-stuff — repeated verbally and built directly into Prompt 2.
- Do NOT hide pages or content from users or from Google. Called out directly on an example of unlinked, duplicate "areas we serve" location pages that only swap the city name: "If we hide pages, we hide them from people, we hide them from Google."
- DO build location pages — they're legitimate and effective — but only for areas you actually service, and only with unique localized content per page.
- Keep a page's content matched to what you currently actually offer. A mismatch (visitor calls, finds you don't offer what the page says) makes them bounce back to Google and try the next result — Google reads that as a negative signal and it hurts rankings.
- Alt text should be roughly 5–6 words. It should never visibly add to the page's on-page word count — if it does, that's a bug/rendering glitch (flagged live as likely a Shopify issue), not normal behavior.
- Product pages: keep the essential info (images, short description, add-to-cart) in the top section; put fuller detail below reviews/related products. Avoid hiding key info inside dropdown/accordion menus — some evidence dropdowns are being used just to stash extra words and "don't work as well anymore."
- Prefer registering a brand-new domain over buying an aged/used domain when you can't verify its backlink/penalty history. Domain age is only a slight positive ranking factor and doesn't offset the unknown risk — a domain can look clean (non-spammy backlink profile) and still be inexplicably suppressed by Google due to the previous owner's history.
- Don't bother manually forcing Google to index a page via Search Console — "not really going to have that much of an impact... it really doesn't do anything and it's extra work."
- Set client/personal expectations at 3 to 6 to 9 months before meaningful ranking improvement typically shows, for any new SEO work.
- Duplicate city names across countries (e.g. London, Ontario vs. London, UK): don't manually disambiguate on-page — Google already uses IP geolocation, the on-site phone number's area code, and the business address to determine locale.
- A keyword-density reading over 100% in an audit tool (one caller saw 923.44%) means no keyword was entered — the tool defaulted to the domain instead. Not a real density, not related to page structure.
- Work in a separate document, not only inside the ChatGPT window — stage and edit everything there before it goes anywhere near the live site.

## Tools, prompts & resources
- **Prompt 1 (SEO tags update), exact wording:**
  > "Here are my current tags and my focus keyword. Update them so the keyword appears naturally, is front-loaded where possible, and matches the style and brand of my business. Also make sure each one is better than my two competitors':
  > [PASTE YOUR AUDIT]
  > Competitor 1 (Same Order As Mine)
  > [PASTE COMPETITOR AUDIT]
  > Competitor 2 (Same Order As Mine)
  > [PASTE COMPETITOR AUDIT]"
- **Prompt 2 (money page rewrite), exact wording:**
  > "Here is the content from my product/service page:
  > [PASTE YOUR CONTENT]
  > Here are the top 2 competitor pages that rank for my keyword:
  > Competitor 1: [paste content]
  > Competitor 2: [paste content]
  > My focus keyword: [keyword]
  > Rewrite my page so that:
  > • It is clearer, more helpful, and more persuasive
  > • Word count is between: [comp low] – [comp high] words
  > • Keyword density is similar to the competitors
  > • Includes the keyword in natural positions
  > • Adds missing topics my competitors include
  > • Improves structure, readability, and expertise
  > • Keeps my brand voice
  > • Uses headings where appropriate
  > • Does NOT keyword-stuff
  > Produce the final optimized version I should publish."
- **Follow-up prompts used live (paraphrased, in-thread):** "You forgot these heading two tags, write a couple paragraphs each and expand on the ideas"; "Can you rewrite this section to be more funny and personable?"; "Ask me five questions to write a better unique piece of content using my expertise, experience, etc." (answerable via ChatGPT voice mode or typed).
- **wordcounter.net** — paste generated content here to check actual word count and keyword occurrence/density; don't trust ChatGPT's self-reported numbers.
- **pageaudit.com** / the **PageAudit Chrome extension** — re-check keyword density and other audit metrics after editing, before publishing.
- **Watchdog** — Matt's own tool, **$10/month**, sends a roughly weekly email listing any changes on tracked competitor sites: text changes, link changes, new products, pricing changes — even a one-word count change gets flagged.
- **SEMrush vs. Mango** — rank/keyword tools; Mango is noted as cheaper than SEMrush. Both can fail to show real rankings beyond page one, because (per Matt) Google cut third-party/LLM tool access to search results down from page ten (~top 100) to page one (~top 10) around the end of August/September — so a genuine position-24 ranking (page 3) won't show up in these tools at all, even though Search Console confirms it.
- **Google Search Console** — the trustworthy source when a rank tool disagrees with reality; use it to confirm actual position.
- ChatGPT's own optional add-on suggestion (schema markup) was raised in the demo but Matt's agency doesn't typically implement it — not every AI suggestion needs to be followed.
- **"Get Found"** — Matt's SEO book; Insiders members get an advance ebook version (bonuses are retroactive to your sign-up date). Endorsed, per Matt, by Marcus Sheridan and "SEM." QR codes printed in the physical book aren't functional yet — pages/automation not built.
- **HeyTony Insiders** — membership, **$57/month**, cancel anytime; includes group coaching calls and a dedicated training called **"Why Doesn't It Rank"** (walks through a page + backlinks + competitor diagnostic when something isn't ranking despite being live for months).
- Arriving **15 minutes early** to a live call unlocks a bonus session not given to on-time/late joiners (that day's early bonus covered social media results/strategy).

## Case studies / examples / results
- **Shawnee (chat)** — blog already ranking #1 on page one for the keyword "process mapping mistakes," within the first three days of Rank Week.
- **Matt's own site** — originally shipped with 695 words because the #1-ranking competitor at the time had only ~600 words; matched rather than over-built.
- **Matt's live tag rewrite (Hey Tony / web design Hamilton)** — drafted title tag: "Get web design in Hamilton that actually drives sales. Hey Tony builds fast, modern, SEO-ready sites your customers love. Get your free quote today." H1 landed on "Web design in Hamilton, Ontario."
- **Matt's own keyword density** — his page scored 5.04% (flagged too high) vs. competitors at 1.76% and 0.90%.
- **Matt's live Prompt 2 demo** — targeted a 2,200-word rewrite (competitors were roughly 2,500 and 2,300 words); ChatGPT actually delivered ~1,700 words per wordcounter.net. Keyword ("web design") appeared 13 times vs. competitors' 45 and 20 — target band was 20–45.
- **Location-pages client** — Matt's agency built ~40 location pages for one client in about a month and a half; client is "ecstatic," now getting orders from small towns nobody else was targeting.
- **Anecdote (Matt's SEO-expert friend)** — a 40-year-in-business owner didn't know what a Google Business Profile was when told she needed more Google reviews there — used to illustrate that GBP basics still get missed even by established businesses.
- **Whitley Electric caller (Vancouver residential electrician)** — his boss wanted to copy a competitor's hidden "areas we serve" pages (unlinked duplicate pages per city, e.g. Richmond, with only the city name swapped). Matt: legitimate location pages good, hidden/duplicate ones not. Same caller's follow-up: pageaudit.com showed 923.44% keyword density — traced to not entering an actual keyword (tool defaulted to the domain), unrelated to the hidden pages.
- **Richard (crypto/Bitcoin site)** — owns the aged domain "makingmoneywithbitcoin.com," considering registering "makingmoneywithcrypto.com" instead. Matt told him live to register the new exact-match domain immediately before anyone else on the call could grab it, and recommended the new domain over the aged one given unknown backlink/penalty history.
- **Vladika/Vlad (Shopify product page)** — alt text bug inflated visible on-page content to ~2,000 words, apparently hurting rankings; traced to alt text rendering as visible text (site glitch). Also asked about ideal product-page length; advised keep primary content compact, push extra detail below reviews/related products, avoid stuffing dropdowns.
- **Camila Quinones (Botox business)** — 2 existing locations in one city, expanding to more in-state and some out-of-state. Advised: location pages in the nav (not hidden) with unique local content, or a separate website per state/city if competition is stiffer, plus one Google Business Profile per physical location.
- **Xavier** — worried competitors are reactively matching/exceeding his word count and keyword usage in real time. Matt: "you're giving your competitors way too much credit" — most aren't watching that closely; use Watchdog ($10/month) if genuinely worried. Same caller also asked about duplicate city names (London, Ontario vs. London, UK) — Matt: Google already resolves this via IP/phone/address, don't worry about it.
- **Ebad's client** — ~2 months of SEO work, 10 blog posts published, using Mango (cheaper alternative to SEMrush). Google Analytics showed 120 organic searches last month. Google Search Console confirmed a real ranking of position 24 (page 3) for the target keyword, while Mango/SEMrush-type tools showed no ranking at all — explained by Google's page-one-only restriction on third-party tool access.
- **Ilya (Miami biohacking/wellness Shopify store)** — sells personalized supplements via AI quiz + at-home health tests. Example product "Pre Workout Powder": SEMrush showed a domain-adjusted keyword difficulty of 10 for their new, low-authority domain, but SEMrush's AI-based general difficulty score for the same terms was 42–65 — meaningfully harder, ruled out for direct ranking. Advised the "backdoor" blog-content route instead. Also asked about a paid 1:1 audit; Matt doesn't do 1:1s, pointed to the Insiders group calls ($57/month).
- **Jacob (Poland, security-lines/infrastructure client)** — top target keyword competes directly against a government page and a Wikipedia page (government pages in his market are typically "no-follow"). Matt: outranking government/Wikipedia directly on that exact keyword is "very difficult" — advised finding more specific related keywords instead.

## Notable verbatim quotes
- "This is not theory. Not 'one day you'll figure this out.' We actually built the page you're going to publish."
- "You now have a money page that's better than your competitors — and we did it live."
- "This is the kind of work most SEO agencies charge thousands for… and you just did it yourself in under an hour."
- "You ARE doing SEO — and you're getting better every single day."
- "It's not rocket science. It's not crazy."
- "We're using AI as a tool. We're not using it as a replacement for our brain."
- "If we hide pages, we hide them from people, we hide them from Google. Just remember that."
- "You're giving your competitors way too much credit."
- "If you rank number one, there's no guarantee that you're going to keep that ranking... it's a free market, so you just kind of need to be on top of it."
- "Google basically spanked every AI LLM and was like, you can't access past page one of our search results."
- "There's no judgment. There's only room for improvement for all of us, including myself."
- "I wrote this book so that my mom could basically understand what I do and do SEO herself, and she doesn't know anything about SEO."

## Tradeoffs & nuance
- ChatGPT's word-count and keyword-density instructions in Prompt 2 are unreliable — it undershot a 2,200-word target by roughly 500 words in the live demo, and separately can ignore supplied H2 headings entirely. Always verify externally (wordcounter.net, page-audit tool); never trust the model's self-report.
- Pasting a competitor's raw page content is "a lot, a lot, a lot" and looks messy/cluttered once pasted, but ChatGPT parses unlabeled, jumbled pasted data correctly regardless.
- Pasting just a competitor's URL sometimes lets ChatGPT read the live page directly — "sometimes it works, sometimes it doesn't"; fall back to pasting full text when it fails.
- Matching a thin-content #1 competitor (e.g. 600 words, no headings) can be enough today, but that balance can erode over time as rankings shift — especially if the page stops accurately reflecting what you actually offer, since the resulting bounce-back-to-Google is itself a negative signal.
- Dropdown/accordion content is increasingly seen as risky for hiding page text ("some people saying dropdown menus don't work as well anymore") — acceptable only for genuinely supplementary content below the primary buy-box/reviews, not as a stuffing tactic.
- Aged/used domains carry a real but hard-to-quantify risk: registration age is a minor positive ranking factor, but a clean-looking backlink profile doesn't guarantee Google hasn't penalized the domain over past-owner behavior — Matt's own experience with aged domains has been mixed enough that he now defaults to registering new ones.
- Disagreement between rank-tracking tools (SEMrush/Mango) and Search Console doesn't necessarily mean something is broken on-site — it can reflect a structural blind spot (tools now capped at page-one visibility) rather than an indexing or ranking problem. Search Console is the more trustworthy source when the two disagree.
- Outranking Wikipedia/government pages on a shared head keyword is framed as very difficult, not flatly impossible — the practical path is shifting to more specific, related long-tail keywords rather than a direct assault on entrenched SERP leaders.
- Location-page strategy scales down deliberately to very small, low-search-volume towns precisely because competitors ignore them ("the smaller the town... somebody might look up that keyword in that small town and then you're the only one") — low tool-reported volume doesn't mean low real-world value.
- The day's process (2 prompts) is explicitly positioned as a fast starting point, not the final method — combining it with Day 1's "ask me clarifying questions first" technique is presented as the higher-quality path.
