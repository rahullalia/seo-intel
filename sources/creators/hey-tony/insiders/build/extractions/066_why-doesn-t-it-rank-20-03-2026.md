# Why Doesn't It Rank: 20.03.2026 (Call #066)

Format: live Q&A, raise-hand queue, live screen-share audits, run solo by Matt Diamante (about 92 minutes). Denroy's separate technical Q&A call is pausing 2 to 3 weeks for paternity leave; Elliot is covering some of those duties meanwhile.

## Tactics & step-by-step how-to

- **First check on any site that "isn't ranking": is Google even seeing it.**
  1. Search `site:yourdomain.com` in Google to see every page Google currently has indexed.
  2. Compare that count to your real page/post count (Courtney's case: about 30 pages showed as indexed versus 30+ actual blog posts, and several "indexed" items were testimonials mislabeled as blog posts).
  3. Open the sitemap URL referenced inside `robots.txt` and confirm it actually resolves (Courtney's pointed to a dead Yoast sitemap URL left over after she removed the Yoast plugin).
  4. Switch to the native "WP version" sitemap and update the `robots.txt` reference to point at it.
  5. Remove any `crawl-delay` directive in `robots.txt`. A 10 second (or 10 millisecond) delay was diagnosed as the likely cause of the audit tool returning "only nine words" on Courtney's page: the delay triggers a bot challenge screen instead of serving real content.
  6. Add an explicit user-agent allow rule in `robots.txt` for the Hey Tony/Money Page Doctor crawler. Prompt used: ask ChatGPT "how you can add a user agent to your robots.txt file."
  7. Re-run the audit tool after fixing.
- **Live keyword-guessing process (used repeatedly, e.g. Morvi's dog treats brand):**
  1. Type a guessed phrase into Semrush (e.g. "goat milk cookie").
  2. Add the qualifier that disambiguates audience if volume/intent looks off (e.g. "goat milk cookie for dogs," since the plain phrase reads as a human recipe).
  3. Push flavor/variant detail into a bracketed suffix, not the core phrase (e.g. "Goat Milk Cookie for Dogs (Peanut Butter Flavored)").
  4. Apply the same logic to category and homepage copy: rename vague labels ("Nutrition") to what's actually searched ("Nutrition Supplements for Dogs"), and make sure the homepage states plainly what you sell and for whom.
- **Trimming an oversized money page (ceramic coatings example, reported at 8,700 words by the audit tool, closer to 9,000-10,000 by eye):**
  1. Google the target keyword and open the top 2-3 ranking competitor pages.
  2. Note their word count as your ceiling (competitors here ran roughly 1,100-2,500 words; the audit tool's own "match competitor word count" suggestion targeted 1,400).
  3. Keep content nobody else can copy (your own shop/work photos, specific process detail).
  4. Cut generic education the searcher already has (what a warranty means, what ceramic coating is), since someone searching "ceramic coating Red Deer" already knows the category.
  5. Move cut material to a blog post and link back internally.
  6. Put one clear call to action near the top ("Book an appointment"), not buried below a long scroll.
  7. Prompt to hand ChatGPT: "This is my current money page for [keyword]. I need to trim this down to [1400] words. Can you do that for me?" Optionally paste in competitor page text as added context.
- **Fixing a text-heavy collection page (Jorg's tennis shirt store):**
  1. Move long descriptive copy below the product grid, not above it. Someone landing on a collection page is ready to buy now.
  2. Put the H1 at the very top of the page. Jorg's true H1 was buried mid-page under an H2-styled block that came first.
  3. Don't trust ChatGPT's on-page SEO suggestions over the rules taught on these calls: "ChatGPT will make shit up. It doesn't know the SEO best practices."
  4. Check singular versus plural keyword variants separately; they can carry very different difficulty. Jorg's "tennis t-shirts" (plural) matched what Rank Week's process had already surfaced (about KD 16-17 per both Jorg's tool and Matt's own Semrush check); "tennis t-shirt" (singular) came back at KD 8 with volume around 7,050, the better target for the difficulty tradeoff.
  5. Test a novelty/niche phrasing when the plain head term is too generic to be a good keyword: Matt steered Jorg away from plain "tennis shirts" (called "a very not so good keyword") toward "funny tennis shirts," found to have close to zero competition and real search volume.
- **Preventing internal-link keyword cannibalization:** if one target keyword/anchor phrase is used as internal link text pointing to more than one page, consolidate it to point at ONE page only. Genuinely distinct product lines (tennis polo shirts vs. tennis hoodies) can each keep their own link.
- **Recovering GBP performance after a bad site rebuild (Victor, moving company, Washington DC):**
  1. Confirm NAP (business name, address, phone number) is present in the footer.
  2. Re-add the Google Business Profile CID link wherever it lived pre-rebuild, or add it somewhere new if that placement is gone.
  3. Audit canonical tags site-wide (Victor's rebuild broke canonicals on roughly 60-70% of pages).
  4. Confirm site-wide HTTPS even if an SSL cert is installed; check for pages the audit tool still flags as starting with HTTP.
  5. Set up an HTTP to HTTPS redirect.
  6. Use the "Better Search and Replace" WordPress plugin to bulk-swap hardcoded `http://` internal links to `https://`. Back up the site first.
- **Launching a new site without a separate dev environment (Maritza, comedian, about 66 planned location pages):**
  1. Point the live domain straight at the WordPress install and build it live, page by page, rather than building offline first (pushing a dev build live later creates its own set of technical problems).
  2. Finish the homepage plus a couple of core pages, then submit a sitemap to Google Search Console before building out every location page.
  3. Run one domain live only. She owned two (spelled in the transcript as "marisacomedy.com" and, inconsistently, "marisabrucelo.com"/"marissabrussalo.com"); Matt's rule: people only find the unused domain if you tell them about it, so don't bother.
  4. Set the homepage's target keyword to the single highest-priority head/location term.
- **Early-stage keyword-guessing loop, repeated across several attendees:** guess a phrase, check it in an AI tool, search it on Google to see who already ranks (sometimes directories, not direct competitors), cross-check volume/difficulty in Semrush's free tier, and if a long-tail guess shows no data, shorten it (e.g. "comedian Boca Raton" instead of "stand up comedian in Boca Raton") before lengthening again.
- **Retrofitting internal links onto early blog posts (Christina, 6-8 posts live, none linked):** don't force links before there are enough related posts. Publish first (aim for 1-2 posts/week), then once you're at roughly 10-20 posts, go back and add about 3 internal links per post. Links added after the fact take longer to show ranking effect than links present at publish time, but still work.
- **A/B test before matching a keyword-stuffing industry norm (Carolina):** publish one page following best practice and, separately, one page keyword-stuffed like the top-ranking competitors; leave both a month or two and compare results rather than guessing.
- **Handling a competitor running ads on your trademarked name (Christina):** screenshot the evidence and send it directly to a contact at the competitor with a direct ask to stop, framed around concrete customer harm (guests arriving expecting a reservation that was actually redirected to the competitor).
- **Turning an awkward literal keyword into natural copy (UK magician attendee, brand "Matt Paro"):** keyword variations (London magician / magician London / magician in London) can be used interchangeably through a page since Google treats them as one topic; if the literal phrase reads badly, rewrite it naturally or as a brand line ("Matt Paro, London's premier magician") instead of forcing the exact string.
- **Deciding whether a sub-service needs its own page:** check how competitive the sub-keyword is (e.g. "corporate magician" or "wedding magician" under a city page). Low competition: fold it into the existing city page's content. Only build a separate page if the keyword is competitive enough to need dedicated content.
- **Using the Insiders portal's built-in tools:** a search bar surfaces every past transcript/video mentioning a typed topic (e.g. "location page"), with clickable timestamps that jump straight to that moment; a separate AI Q&A tool (referred to on the call as something like "Wisdom," Matt himself seemed unsure of its exact name) answers free-form questions using only the Insiders transcript/comment library, not the open web.

## Rules / dos & don'ts (keep every threshold, number, specific)

- One H1 per page, positioned at the very top. Josh's ceramic coatings page started at six H1 tags; still had two to three left at review time and needed to get to exactly one.
- One clear call to action per money page. Courtney's page offered five competing options ("speak with Courtney," "meet Courtney," "retain your workforce," "upscale your team," "calibrate your communication") and was flagged for it.
- Keyword placement formula: target keyword in the title tag, the meta description, the H1, at least one H2, and a couple more times in body copy (frequency depends on the keyword).
- Navigation menu belongs next to the logo, not wrapping/pushing content down; trim menu items (nest "About" under "Blog") if space is tight.
- Never use an autoplay video as a hero/background element that "freezes" when a visitor navigates away and back; it reads as a broken image and slows load time, which hits SEO and conversion. Use a static image instead.
- Money page word count should match the top 3 competitors' actual count, not just be padded because "more is better." Ceramic coatings target was 1,400 words against competitors running roughly 1,100-2,500.
- Don't build individual client/session blog posts as keyword-optimized SEO posts using the same city keyword across many posts (e.g. "Chicago Newborn Photographer" reused post after post). That's cannibalization: "you're now competing against yourself... Google's going to be like, well all these pages are about the same keyword, so why am I ranking?" Treat these as case study pages instead.
- Reciprocal linking between similarly low-authority sites carries little weight. "ABC linking" (A links to B, B links to C, C links to A, no direct reciprocal pair) is called one of Matt's favorite backlink tactics.
- Standard reply when someone asks for a link placement: "sure, but I need you to get me a link from a third party site first." They source it, you place their link in return.
- Don't link out to your full set of social media profiles from prominent site content; keep social links to the contact page, footer, or a small header placement. External links inside blog content to non-competitor, non-social resources (a stat source, a studio you're referencing) are fine.
- A location page (one service, one city) can also be a money page. Definition given for money page: any page a visitor lands on while looking for your product or service.
- Geotagging images isn't required but is recommended.
- You do not need to manually request indexing for every new page; Google should discover new pages automatically.
- Not every backlink you build will show up in Google Search Console; that's normal, not a sign anything is broken. Semrush and similar tools surface more (but still not all) backlinks than GSC does.
- Keyword stuffing typically doesn't get you "penalized"; worst case, the page just doesn't get indexed or ranked. Real penalty territory: being part of a spam link network, or having a pile of spam backlinks pointing at you.
- Aged domains are a real ranking factor but a minor one: "I don't think that has as big of an impact as people think it does, but it definitely is one of the ranking factors."
- Semrush free-trial abuse: you can retrigger free trials with different email addresses, but cancel immediately. Semrush charges and will not refund (cited frustrated users on Reddit).
- Focus a whole site on one main topic. Sites spanning many unrelated subjects (finance, health, everything) struggle to read as a "topical expert" under Google's algorithm shifts of the last two years, which directly hurts ranking.
- Depending on Google Ads alone as a revenue model is risky even at large scale.
- Don't run multiple owned domains promoting the same site "just in case." Pick one; the other is only found if you tell people about it.
- EPUB files need a dedicated e-reader app; they won't just open on their own.

## Tools, prompts & resources (exact prompt wording if quoted; tool names; settings)

- **Money Page Doctor** (also called "Money Doctor" on the call): crawls/audits a single money page. Output reads like a checklist, e.g. "add [keyword] to your page title," "add a clear call to action button," "match competitor word count" (with the actual target number, e.g. 1,400 words). It also reports which keyword the page is currently optimized for and who's ranking for it. When a site blocks crawlers via `robots.txt`, the tool itself fails (returned "only nine words on the page" for Courtney), itself a diagnostic signal of a crawl/indexing problem.
- **Hey Tony Site Audit Tool** ("the hey Tony one"): referenced by Josh alongside a competitor gap analysis to help settle on a keyword.
- `site:yourdomain.com` Google search operator: first-line check for what's indexed.
- `robots.txt`: check for a broken sitemap reference, a `crawl-delay` directive to remove, and a missing user-agent allow rule for the Hey Tony/Money Page Doctor bot.
- Prompt: "How can I add a user agent to my robots.txt file?" (asked to ChatGPT).
- Prompt: "This is my current money page for [keyword]. I need to trim this down to [1400] words. Can you do that for me?" (paste competitor page text in alongside, optional).
- **Semrush**: Matt's default keyword tool, used live on screen repeatedly to check search volume and keyword difficulty and pull competitor pages/word counts. Matt confirmed he personally pays for it, no discount or affiliate relationship.
- **Ubersuggest**: cheapest keyword tool option; Matt dislikes its layout/design.
- **Ahrefs**: mentioned as having a cheaper plan than Semrush.
- **Squoosh**: used to convert JPEG images to WebP one at a time.
- **Photoshop batch "action"**: recommended for bulk JPEG-to-WebP conversion on Squarespace (download images locally, record an action, run it against the batch). Photoshop can be rented month to month for about $10-20, then cancelled.
- **Geo Imager**: standalone (non-WordPress) tool to geotag images via metadata; 5 free geotags/day, or roughly 1,000/month on a paid tier.
- **Better Search and Replace** (WordPress plugin): bulk find/replace for swapping hardcoded `http://` links to `https://`. Back up the site first.
- **Get Found**: Matt's book, explains backlinks (the "vote" analogy) in more depth; available as an ebook, on Audible, and on Spotify.
- Insiders portal search bar: type a topic (e.g. "location page") to surface every past call/video transcript mentioning it, with clickable jump to timestamp.
- Insiders portal AI Q&A tool (name unclear, something like "Wisdom"): answers questions using only the Insiders content library, not the open internet.
- **NotebookLM**: used by Diana (outside this call's core SEO topic, shared as a win) to build an infographic and slide deck explaining her "AI readiness accelerator" internally, then generate an explainer video to send to prospective clients.
- **Google Search Console**: submit/resubmit an XML sitemap to trigger (re)indexing; check backlink reporting (incomplete by design, doesn't show every backlink built).
- **Search Atlas**: SEO tool Courtney switched to after removing Yoast.
- Community members offering paid help inside Insiders: **Muhammad** (technical/web work) and **Jennifer DeMarco** (website design, WordPress).

## Case studies / examples / results (names, niches, numbers)

- **Diana**: used NotebookLM to build an infographic and slide deck explaining her "AI readiness accelerator" to a team member internally, then generated a video from it to send to potential clients.
- **Carolina**: ranking on page 1 for the first time ever; also informally runs SEO for several family members' businesses. Separately discovered via Rank Week that her site had never been indexed by Google at all, despite ranking well through 2-3 Google Business Profile updates a week; submitted a sitemap, got indexed, and was told to wait a month or two to see movement.
- **Courtney**: leadership development/keynote speaking coach, hosted on SiteGround, moved from Yoast to Search Atlas. `site:` search showed about 30 indexed pages against 30+ actual blog posts, several mislabeled as testimonials. Sitemap reference in `robots.txt` pointed to a dead Yoast URL. H1 read "Tough Conversations at Work," flagged as unclear about what the business offers.
- **Ariel**: photographer, cleaned up orphaned WordPress category pages (improved her own audit score); host doesn't support WebP ("ironically... for photographers"); advised against building individual per-client-session blog posts optimized around a repeated city keyword.
- **Morvi**: dog treats/supplements brand built on goat milk (treats, "paw bombs," a nutrition line), sells in Canada only. Homepage copy read "helping pets thrive one home at a time," flagged as reading like a humane society or adoption org rather than a retailer.
- **Josh**: auto detailing/ceramic coatings, Red Deer. Money page for "ceramic coating Red Deer" ran 8,700 words per the audit tool (closer to 9,000-10,000 by Matt's eye) against top-3 competitor pages of roughly 1,100-2,500 words; an earlier revision had six H1 tags, down to two or three at review time. Used an auto-detailing-specific AI plus the Hey Tony audit tool and a competitor gap analysis to find local competitors weren't targeting "Red Deer" by name.
- **Jorg**: tennis apparel ecommerce store. Rank Week's gap analysis pushed him to add three extra paragraphs to a collection page; Matt had him cut it instead. Keyword iteration: his original working phrase ("tennis shirts for matches, practice and everyday wear") was too long and not a real query; Matt suggested "funny tennis shirts" instead, calling plain "tennis shirts" too weak/generic and "funny tennis shirts" close to zero competition with real volume. Separately, his own existing target "tennis t-shirts" (plural) checked out at roughly KD 16-17 in both Rank Week's process and Matt's live Semrush check; the singular "tennis t-shirt" came back at KD 8, volume around 7,050, the better tradeoff. Top-ranking competitor pages showed Money Page Doctor word counts of 2,200-3,400 that Matt and Jorg couldn't visually locate on the actual pages (suspected hidden/pop-up content).
- **Victor**: moving company, Washington DC. Previously ranked well via Google Business Profile (geotagged photos, CID link, phone number on the profile). After a rebuild by an outside agency, rankings dropped: found roughly 60-70% of pages/links with broken canonical tags, and HTTP links still present despite an installed SSL certificate.
- **Al**: directory/personal-finance blog running since 2018 (money-saving/making tips), monetized via Google Ads, affiliate links (Amazon, cashback apps), and sponsored posts; recent algorithm changes "destroyed" his traffic. Matt's comparison case: ran a publication around 2014 pulling about 4 million monthly visitors and about $13,000/month in Google Ads revenue with a team of 7 writers, cited as proof that even large-scale ad-only revenue is a rough business model.
- **Maritza**: stand-up comedian, Boca Raton, rebuilding on WordPress (builder name transcribed as "Aveda," likely a mis-transcription of an actual builder name), planning about 66 location pages; owned two domains ("marisacomedy.com" and, inconsistently spelled, "marisabrucelo.com"/"marissabrussalo.com") but told to run only one live. Her real competitive set for comedian-related searches turned out to be entertainer directory sites (Gigsalad, Bash), not other individual comedians.
- **Christina**: seasonal, river-based hospitality/recreation business; 6-8 blog posts live with no internal links between them yet; a competitor on the same river is running ads using her trademarked business name, causing guests to be misdirected about reservations.
- **UK magician attendee ("Matt," brand "Matt Paro")**: 20 years in SEO, now applying it to his own magic business; working through city-page architecture (London, Kent, Surrey) plus sub-niches (wedding, corporate, close-up magician) and natural keyword phrasing.

## Notable verbatim quotes

- "If this can't find it, then it's being blocked."
- "This robots.txt file tells search engines and bots, like, what they're allowed and not allowed to do."
- "Don't fall for any of that. Like, yeah, it's somebody trying to scam you somewhere overseas likely. And they're not going to do anything for you."
- "Think of a backlink as a vote, right? So it's another website saying, I'm voting for this website."
- "This crappy site's linking to this other crappy site... doesn't really make sense. But if you get backlinks from higher credibility sites... that's them saying, Josh has a great business, Josh has a great site, we should go check them out."
- "Show me that you know what you're doing... but this page is just so long."
- "This is not an educational page. This is a page that you want somebody to take an action."
- "ChatGPT will make shit up. It doesn't know the SEO best practices, all that kind of stuff. So don't worry about following exactly. Follow what I say and not ChatGPT."
- "Now you're confusing Google. Like, what page does this? Like, tennis t-shirts means 10 pages on your website instead of just one."
- "It's kind of the downfall of what Google has done in the recent, like, last two years, where if you're not specific on one topic... your ranking is going to be a lot more difficult... because Google's like, okay, are you a topical expert on this topic?"
- "Anybody can start a website and just paste blog posts and not really have authority or reputation. How's Google gonna know to trust you?"
- "Marketing is all about A/B testing. SEO is all about A/B testing."
- "You don't really get a penalty, they just won't index it or they won't rank it."
- "Never going to be perfect, right? Start with your homepage, get your homepage up, and then start building the other pages on your website."
- "The keyword should read naturally to a human... if the keyword research says London Magician and you're like, well, how do I put London Magician on my site, that doesn't make sense. It would be Magician in London."
- "You're literally taking food from my mouth."

## Tradeoffs & nuance

- The audit tool's word-count numbers for competitor pages didn't match what was visibly on the page during multiple live reviews (Jorg's case: 2,200-3,400 reported words on pages that plainly had far less visible text). Matt's working theory is hidden or pop-up content being counted, left unresolved on the call; guidance was still to use the numbers as a rough range, not an exact target.
- Whether to match a keyword-stuffing industry norm has no single answer. Matt frames it as needing an A/B test per case rather than a universal rule, since backlink volume on the stuffed competitor pages may be doing the real work, not the stuffing itself.
- Aged domains: acknowledged as a real ranking factor but explicitly downplayed relative to popular belief.
- Location pages and money pages aren't separate categories requiring different treatment. A location page can be a money page depending on what the visitor is looking for.
- Josh's case shows a keyword win can come from a small competitor gap (nobody targeting "Red Deer" by name) rather than raw effort, while Al's case (broad, years-long directory site) shows the opposite: heavy sustained effort without topical focus still lost to the algorithm shift.
- Directory/aggregator-adjacent niches face a structural handicap against the directories themselves. Maritza is outranked on her own name-adjacent keywords by sites like Gigsalad and Bash that list many providers; the fix suggested is playing within that reality (get listed better on those directories) rather than trying to outrank them outright.
- Retroactively added internal links (Christina) still work but take longer to show effect than links present at publish time; a timing tradeoff, not a lost cause.
- Matt's own 2014 publication (4 million visitors/month, $13,000/month in Google Ads revenue) is offered as proof that even large-scale traffic plus ad revenue can be an unstable foundation, reinforcing his advice to always have something to sell beyond ads.
