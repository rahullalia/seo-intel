# Citations

Verified 2026-08-31. Primary sources: Whitespark Local Search Ranking Factors 2026 (Nov 2025), BrightLocal, Near Media, Sterling Sky.

## How much citations matter now (be honest with clients)

- 2014: the #1 local ranking factor. 2026: ~6-7% of local pack weight and still declining. GBP signals (32%) and reviews carry the pack now.
- They are **table stakes, not a growth lever**: foundational trust/verification data that Google cross-checks before deciding you are a real business. Get them right once, maintain, move the budget to reviews, GBP, and links.
- **The twist: citations are rising again for AI visibility.** Whitespark's new AI Search Visibility category has citation factors in 3 of its top 5 slots, led by *unstructured* citations (mentions in articles, lists, local press, not NAP-in-a-box directories). Their line: "mentions (citations) are the new link." Sterling Sky's data on Google's AI local packs: they surface only ~32% as many unique businesses as traditional 3-packs, on ~7% of tracked keywords, US mobile so far. Fewer winners; mentions help pick them.
- Sell citation work as risk-reduction + AI-visibility groundwork, never as "this will move your pack rank."

## Which citations to claim (in order)

**Core five, every client, always:**
1. Google Business Profile
2. Apple Business Connect (needs a DNS TXT record; include "www" if the site uses it)
3. Bing Places (imports straight from GBP, ~2 minutes)
4. Facebook business page
5. Yelp

**Second tier:** BBB (free basic listing; paid only buys "accredited"), Nextdoor, Foursquare, Yellow Pages/YP.com, local chamber of commerce (+ ChamberofCommerce.com), Trustpilot, Brownbook, Bark.

**US data aggregators (feed hundreds of downstream directories; commonly credited with ~80% of US citation distribution, directional figure):**
- Data Axle (formerly InfoUSA)
- Foursquare (merged with Factual; now a location-data provider)
- TransUnion Digital Business Profile (formerly Neustar Localeze; search the new name)

**Canada (starting list, weaker sourcing):** YellowPages.ca, Canada411.ca, 411.ca, Yelp.ca, BBB Canada, Canpages. No true aggregator equivalent; the core five + .ca directories carry it.

**Industry-specific (pick 5-10 per client):**

| Vertical | Directories |
|---|---|
| Contractors / home services | Angi (HomeAdvisor is now "Angi Leads"), Houzz, Thumbtack (thriving, integrated with ChatGPT/Alexa/Zillow), Porch (deprioritized: pivoted to insurance) |
| Lawyers | Avvo, Justia, FindLaw, LawInfo |
| Medical | Healthgrades, Vitals, Zocdoc, RateMDs |
| Restaurants / hospitality | TripAdvisor, OpenTable |

Niche and topically-relevant directories are explicitly weighted higher than generic ones in both the pack and AI factor lists.

**Rules:** never sign up for directories in a country the business doesn't operate in. Skip local directories entirely for a nationally-shipped ecommerce brand with no storefront. Never say the word "backlink" to a chamber or a paper; ask "can I include a link to my business on your site?"

## How to find the niche ones: citation gap analysis

Run the client + 3-5 top local competitors through Whitespark's Local Citation Finder (or pull competitor backlink profiles). Everywhere they are listed and you are not is the build list. "They've already done the work for you." This is also where industry directories you'd never guess show up.

## How many

**No source has measured a stopping point.** The competitor gap from the section above sets the number, not a target count. Niche, city and competition all move it, so a fixed number is a guess dressed as a rule.

What is actually published: Darren Shaw of Whitespark recommends the top 30 to 50 directories plus industry and city specific sites (2024-10-28), and says further listings on low authority directories are not worth the time. That is his recommendation, not a test. The Uberall study he cites compared 3,000 locations listed only on Google, Apple, Facebook and Bing against 3,000 with wider distribution, and the wider group showed 89% more direct searches, 91% more map views and 102% more driving directions. No ceiling was tested, so nothing measured says more stops working.

Practical build: core five + aggregators + second tier + niche, sized to close the competitor gap. Past that it is accuracy maintenance rather than growth. Never buy "500 directories" blasts: wasted spend at best, and BrightLocal warns mass identical-NAP submission to junk directories can trigger a manual spam action.

## NAP consistency (2026 strictness)

- **Exact-match critical:** phone number, city, ZIP, website URL.
- **Least critical:** suite/unit number. Don't burn hours chasing suite-number or punctuation perfection on low-value directories.
- **Business name:** one canonical string everywhere, matching GBP. Pick a position on the LLC/Inc suffix (usually drop it, matching signage) and apply it identically.
- **Call tracking:** never a tracking number in any citation. The one real number goes on GBP and every listing; dynamic number insertion swaps the displayed number on your own website only.
- Keep one canonical NAP record per client (the `nap-canonical.md` pattern from `../rsla/local-seo/`) and build only from it.
- Scan quarterly (BrightLocal or Moz Local tracker); fix the top 10-15 authoritative sites first.

## Build methods and costs

| Method | Model | Cost | Ownership |
|---|---|---|---|
| BrightLocal Citation Builder | One-time, human-submitted | ~$3.20/listing ($2 in bulk credits) | **Owned forever** |
| Whitespark citation packages | One-time, manual, human-verified | $20-$999 by volume; $399/location "Yext Replacement Service" | **Owned forever** |
| Manual DIY | One-time | Time only | Owned |
| LeadSnap citations add-on | Subscription feed-sync (~50-53 publishers) | $20/mo per location | Tested 2026-08-31: no crawlable directory listings found for active OR lapsed locations; see `tools.md` |
| Yext / Uberall / Moz Local (Uberall white-label) | Subscription API overlay | Yext $199-999/location/yr; Uberall quote-only, 25-location minimum | **Rented** |

**The rented-citation problem, measured:** Whitespark tracked 60 Yext-synced listings after cancellation (study published Oct 2024, still the standing reference): 25% vanished, 35% reverted to wrong data, only 5% kept both accuracy and enhanced fields. ~60% degraded within ~60 days. Default to one-time owned builds; use subscription tools only as a monitoring layer. If a client is on Yext, rebuild the core set manually BEFORE cancelling, and turn off Yext sync per-listing as each rebuild lands or Yext overwrites it.

## Duplicate listings

Why: duplicates split reviews and engagement, confuse Google about the canonical record, and create NAP conflicts.

1. Pick the canonical (most reviews/history, correct NAP); optimize it fully first.
2. Request the merge on Google Maps: open the duplicate, Suggest an edit > Close or remove > Duplicate of another place, and pick the canonical profile. Google's help names this as the merge route (support.google.com/business/answer/12756178, read 2026-10-02); no access to the duplicate is needed. A merge combines the reviews (owner replies may be lost), the two profiles should show the same info, and Google answers by email to the account that reported it. If it is refused or nothing comes within about a week, contact GBP support (support.google.com/business/gethelp) with both profile links. Mark the duplicate permanently closed only if no merge is possible, since that drops its reviews.
3. Re-point any citations referencing the duplicate's NAP.
4. Recheck quarterly: aggregator resyncs resurrect duplicates.

## Citations for AI answers

- Structured NAP directories alone do NOT carry the AI benefit. The top AI factors are unstructured: mentions in articles, "best X in [city]" roundups, local press, association pages, Reddit.
- Practical build list for AI mentions: press releases (1-2/month max), local newspaper coverage, chamber/association member pages, sponsorship pages with the business named, industry roundups, an active Reddit presence. Breadth of mediums beats authority of any single source.
- The context text around a mention now matters ("citation description optimization"): a directory blurb saying what you do and where beats a bare NAP row.
- Ranking organically still comes first: LLMs synthesize from live top results (the HeyTony rule: rank on Google and AI recommendation follows).
