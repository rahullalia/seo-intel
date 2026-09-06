# HeyTony Insiders - Master SEO Playbook

Matt Diamante's complete SEO method, distilled from **133 hours** of HeyTony Insiders coaching
calls (124 call replays) plus his structured Video Training curriculum (74 lessons). This is the
master reference: every tactic, rule, threshold, tool, prompt, workflow, tradeoff, and case study
he teaches, organized by theme and deduplicated.

**Source:** `htinsiders.com` (Rahul's membership). Transcripts live in `transcripts/` and
`curriculum/`; per-call digests in `build/extractions/`; category syntheses in `build/syntheses/`.
This continues Rank Week 2026 (`../rankWeek2026/rankWeekPlaybook.md`) - same instructor, same
method, far deeper. Built via a 144-agent map-reduce (extract every call -> reduce by category ->
compose by theme).

**How to use:** skim the Part you need; each opens with a quick-reference number table. The
`/heyTony` skill turns this into an on-demand operator for live SEO work.

---

## Table of Contents

- **[Part I - Core Philosophy, Mental Models & The System](#part-i---core-philosophy-mental-models--the-system)**
  - Quick Reference: Cadence, Patience & Timeline Numbers
  - 1. What SEO Actually Is (The Founding Philosophy)
  - 2. Mental Models & Decision Frames
  - 3. The Golden Rule: Never Touch a Page That's Already Ranking
  - 4. Editing Discipline & Patience Windows
  - 5. Timelines & Expectations
  - 6. The System: The Weekly ~1-Hour Loop
  - 7. Publishing Cadence (The Numbers)
  - 8. Anti-Overwhelm: The #1 Thing That Kills SEO
  - 9. The 30-Day Action Plan (The On-Ramp)
  - 10. The Program as a System (How Execution Actually Happens)
  - 11. The System at Agency Scale (Client-Delivery Cadence)
- **[Part II - Keywords, Search Intent & The Content Engine](#part-ii---keywords-search-intent--the-content-engine)**
  - PART 1 - Keyword & Question Research
  - PART 2 - Search Intent
  - PART 3 - Keyword Cannibalization
  - PART 4 - The Content Engine: The AI Interview Blog Workflow
  - PART 5 - The Two-Prompt Money-Page Rewrite Workflow
  - Cross-Cutting Rules & Cautions
- **[Part III - On-Page SEO & Money Pages](#part-iii---on-page-seo--money-pages)**
  - 1. The Governing Rules (these override every rule below)
  - 2. On-Page Elements
  - 3. Money Pages
  - 4. Auditing a Page
  - 5. Quick-Reference: Every Threshold in One Place
- **[Part IV - Technical SEO, Web Design & Internal Linking](#part-iv---technical-seo-web-design--internal-linking)**
  - Quick Reference: Every Number That Matters
  - Governing Rules for Technical & Structural Work
  - Heading Structure (H1 / H2 / H3)
  - Title Tags, Meta Descriptions & Open Graph
  - Site Speed & Core Web Vitals
  - Images for SEO
  - Schema Markup
  - Sitemaps
  - Robots.txt
  - Canonicals & Duplicate Content
  - HTTPS
  - Indexing & Google Search Console
- **[Part V - Off-Page SEO & AI Search (AEO / GEO)](#part-v---off-page-seo--ai-search-aeo--geo)**
  - 1. Backlinks
  - 2. Press Releases (backlinks + AI-answer citation)
  - 3. Reviews & Reputation
  - 4. Google Business Profile (GBP)
  - 5. Social Media (off-page signal & AI feed)
  - 6. Reddit
  - 7. AI Search - AEO / GEO
  - 8. Off-Page & AI Search - Numbers Quick Reference
  - 9. Off-Page & AI - Master Do / Don't
  - 10. Case-Study Evidence (off-page & AI wins)
- **[Part VI - Tools, Local SEO, Ecommerce, Tradeoffs & Business](#part-vi---tools-local-seo-ecommerce-tradeoffs--business)**
  - PART 1 - TOOLS & PROMPTS
  - PART 2 - LOCAL SEO
  - PART 3 - ECOMMERCE
  - PART 4 - TRADEOFFS & DON'TS
  - PART 5 - BUSINESS & MINDSET

---

# Part I - Core Philosophy, Mental Models & The System

This is the operating system underneath everything else in the playbook: what SEO is actually for, the mental models Matt uses to make every judgment call, and the cadence and discipline that turn the tactics into results. Get this wrong and no tactic saves you. Get it right and mediocre execution still wins, because almost nobody else sustains it.

---

## Quick Reference: Cadence, Patience & Timeline Numbers

| Lever | Rule |
|---|---|
| Time budget | **~1 hour/week** is enough. The whole method is engineered against a 5 to 20 hr/week habit. |
| Publishing cadence (most sites) | **1 post/week minimum, 1 to 2/week ceiling.** One a week is genuinely valuable, not a fallback; two is more progress. |
| Never | Publish both weekly posts on the **same day** (space them, e.g. Mon/Thu). |
| New-site launch exception | May batch **5 to 6 posts at once**, or launch with **10 and drip 2/week**. |
| Established live site | **Never** publish a dozen at once. Mass velocity (up to ~500 pages/week historically) reads as spam; Google "retaliates." |
| HeyTony's own site | **3 to 5 posts/week** (an authority-tier exception, not the default). |
| Agency-client cadence | **2 posts/week** (or 4 to 8 pieces per 28 days) + **4 backlinks/month**. |
| Re-edit a freshly published/updated page | Wait **~1 month** before touching it again. |
| Non-ranking page | Wait **3 months, then 6 months** (internal-linking meanwhile) before rewriting content. |
| Judging an on-page change | Small title/meta/H1 nudges: **~2 weeks to 1 month.** Content-level changes: **~2 to 3 months.** |
| Check performance | **Monthly, not daily.** Compare 28 days vs. the previous 28. |
| First real movement | **3 to 6 months** minimum; inflection can land as late as **month 12 to 14**. Ranking in **2 weeks is "magic,"** not the norm. |
| Brand-new site | **Zero movement for the first 2 weeks to 2 months is normal.** A site under ~1 month old will not rank regardless of on-page work. |
| New-post indexing | **~2 hours to ~1 week** typical (faster with reciprocal internal links). |
| Fixing audit issues | **5 to 10 per week**, never the whole report at once. |

---

## 1. What SEO Actually Is (The Founding Philosophy)

### The origin story Matt retells every cohort
Marcus Sheridan ran a pool-installation company near bankruptcy in 2008 with zero SEO knowledge. Every night, after his kids were asleep, he wrote down and answered the actual questions he heard on sales calls that day, one blog post per question. Result: the **#1 pool website in the world within 2 years**, and eventually a nine-figure exit. This is the "They Ask, You Answer" method, and it is the entire philosophy. *"He was truly helpful. That is what is ranking now."* The AI-interview workflow taught elsewhere in this playbook is just the same idea sped up with tools.

### The core beliefs
- **SEO is answering real customer questions with real expertise, one page at a time.** Not keyword density, not schema, not tricks. *"By just answering this question, you are making it SEO friendly. We're not talking about using the keyword a certain amount of times."*
- **We don't care about SEO, we care about getting clients.** SEO is only the vehicle. *"The objective is not to game the algorithm, it's to write a piece of content so unique it talks to somebody with that specific problem."*
- **Write for the user, always.** The litmus test that settles most "should I write / build / keep this?" questions: *"Would my customers actually need this? And read this? If the answer is yes, then publish it."* / *"Always think of the user. If it's going to be beneficial for somebody, great. If not, leave it."*
- **Ranking and revenue follow helpfulness, not the reverse.** *"If the way you're thinking about things is 'I want to rank on Google because I want people to pay me money' that's kind of the opposite of how we should be thinking."*
- **Google and AI reward niche expertise, not SEO polish.** *"Google isn't looking for SEO experts and properly optimized, perfect sites to rank. They're looking for experts in specific niches."* Don't over-index on technical perfection at the expense of genuine subject-matter depth.
- **Give away 99.99% of your knowledge for free.** The generosity is the strategy. Matt's own teach-first funnel is explicit: people watch him explain exactly how to do it, try it, realize it's more work than expected, and hire him. *"My goal is not to get you guys to hire me. My goal is to get you guys to rank for yourselves and not have to hire somebody."*
- **There is no win too small,** and *"none of us came out of the womb knowing anything, so I will learn."* Progress, not perfection, is the scoreboard.

### The AI-content stance (write human, don't "humanize")
- **Google and AI do not penalize AI-written content. They penalize regurgitated, generic, same-as-everyone-else content.** *"Google doesn't care if it's AI generated. AI doesn't care if it's AI generated, as long as it's helpful."* The penalty is for slop, not for the tool.
- **AI is a tool, never a brain-replacement.** You inject the expertise, experience, opinions, and stories; the AI just frames your words coherently. You still fact-check every specific. *"Although it is written by AI, it's all you."*
- **Don't "humanize" AI output. Write human content in the first place.** Running an AI-detector on your own writing is philosophically incoherent (using AI to look at AI) and pointless. *"We want to write human content and have AI just take our words and frame it in a way that is coherent... not just random AI slop."*
- **Don't fully automate content or posting, even though it's technically possible.** Platforms increasingly detect and label automated content. Spend ~1 hour/day being intentional (use AI to brainstorm, rewrite, generate images, not to generate final work wholesale). *"I do not recommend this because it's a slippery slope if you just let AI do whatever."*

### AEO is not a separate discipline
*"It's all just SEO. AEO is part of SEO."* Rank on Google first and AI recommendations follow, because LLMs run live Google/Bing-style searches at answer time and synthesize from the existing top results rather than crawling the web fresh. *"If you rank on Google, you will get recommended by AI. That's just the plain fact."* The corollary reframes the whole goal (see below).

---

## 2. Mental Models & Decision Frames

These are the recurring analogies Matt reaches for to make calls in real time. Learn them and you can diagnose most situations yourself.

### Pigs get fat, hogs get slaughtered
Never try to grab an entire market, region, or keyword set at once. Take a slice, win it, then expand. This is the single most-repeated frame across every cohort, applied to counties, neighborhoods, service-by-city page matrices, and keyword difficulty (a 100% difficulty head term is *"never going to rank"* for a small site, no matter how much you want it). The paired image: *"Do you want to shoot a shotgun and maybe miss your target, or shoot more of like a sniper rifle?"*

### The avalanche / snowball method
Deliberately target small, low-competition, near-zero-volume question keywords first, even at 10 to 20 searches/month. Each one barely moves traffic alone. But they compound: post #1 brings a couple visitors, post #2 stacks on top, then more, and the accumulated traffic and topical authority is what earns Google's trust, gets you picked up by ChatGPT, and eventually makes the harder, higher-volume head terms rankable. *"Think of it as a snowball rolling down a hill. All these small keywords bundle up, get bigger, start rolling down, collecting more and more keywords."* Low-difficulty keywords also rank with zero backlinks, which is why they are the fastest path to early traction.

### Every page is a door into your business
Build one solid door at a time rather than mass-publishing thin pages. *"You don't want a million doors. You want to build one door at a time to make sure it's solid, that when somebody walks through it, it's not going to collapse on them."* This is the antidote to the urge to spin up hundreds of pages "just in case."

### The new SEO: recommendations over the #1 spot
Ranking-position obsession is outdated. #1, #2, #3, or anywhere on page one all get traffic. The new SEO is **aggregate traffic from many sources plus being recommended**, including surfacing inside LLM answers, not fixation on a single top spot. A business can be *"invisible to every tool"* (shows zero ranking in SEMrush) and still be fully booked. Don't equate rank-tracking data with real-world results.

### 15% of searches are brand new every day
Roughly 15% of Google's ~2 billion daily searches have never been searched before and will never appear in any keyword-research tool. This is the foundational justification for the question-answering method and for writing zero-volume long-tail content: **zero historical volume is not proof of zero future demand.** It cuts both ways: the same white space that lets a niche site sneak past competitor research also means you can't forecast or prove ROI before publishing. You trade measurability for genuine open field.

### The credit-score discipline (checking is not acting)
*"You can look at it every day, but don't make actions on it every day, because that's how you lose money, that's how you lose credit, that's how you lose sanity."* The analogy: *"Don't look at your credit score every day. Instead, do the right thing every day, and then 30 days later, without you looking, it's changed and you can buy a house."* Applies identically to Search Console, analytics, credit scores, and investment accounts. Cancel any tool that pushes daily rank-change alerts; it *"is just giving you anxiety."*

### Marathon, not a sprint (and why Google makes it slow on purpose)
*"SEO is a marathon, not a sprint."* / *"This is not a sprint, it is a marathon."* Google deliberately makes ranking slow specifically to filter out spammers chasing instant results. They come in, see no fast payoff, give up, and go away. That is the mechanism. Therefore **the #1 failure mode is quitting too early, not doing it wrong.** *"The people who get results aren't the ones who learn the most in a single day or a single week. They're the ones who keep going afterwards."* Want guaranteed instant results? *"That's what ads are for, not SEO."* And the closing frame: *"It's a patience game, it's a consistency game, and it's having faith a little bit, praying to our Lord and savior, Google."*

### Doing too little vs. too much
*"Most of the time, if you're not ranking, you're either doing too little or too much."* Under-optimization (thin content, missing keyword) and over-optimization (excess length, excess keyword repetition, too many pages, gray-hat tricks) are equally common failure modes. The resolution is never a fixed absolute number.

### Match what's ranking, never an absolute
The single most repeated diagnostic frame: never optimize to a fixed universal target for word count, keyword frequency, or heading count. **Always benchmark directly against whoever currently ranks in the top 3 for your exact keyword, then match or slightly exceed the lowest of them.** Real competitor pages for one keyword ranged from ~500 to 2,500 words on the same SERP, proving the variable itself isn't the driver. Whatever the #1 competitor is doing, Google likes, so mirror it and slightly outdo it, never blindly add more. (The specific thresholds live in the on-page rules; the mental model is: the SERP is the answer key, not a rulebook.)

### Small steps, not giant leaps
*"We're not trying to make giant leaps here. We're trying to make small steps and be consistent with it."* This governs both editing (change one thing, wait) and cadence (one post a week beats a heroic batch you can't sustain).

### More frames worth keeping
- **Any platform can rank.** *"Google doesn't care about the platform you're using."* WordPress is favored by agencies because it maximizes *their* control, not because Google rewards it. Don't platform-hop chasing a "gold standard"; migrating means redoing everything and risking a dip.
- **Value asymmetry: a hundred 1%s don't equal one NYT.** Not all backlinks (or tactics) are equal. *"You can have a hundred 1%'s, but that still doesn't equal the New York Times backlink."* Weight beats count.
- **Acres of diamonds.** The opportunity is usually local and overlooked, not far away. Repositioning around a real differentiator and serving the large pool of small/local buyers beats fighting 100,000 competitors for a few big global clients.
- **Give yourself grace / the 20% that matters.** A solo owner covering SEO plus social plus everything else is running multiple full-time jobs. Decide priorities deliberately rather than freezing from overwhelm. *"If you're not doing these two things for everything, don't waste your time on number 32."* Explicitly deprioritized as low-ROI by Matt himself: schema markup, FAQ schema (after a year of testing, *"no more or less useful"*), messy HTML, "AI blocks," chasing an audit tool's percentage score, and running AI-detectors on your own content.
- **Always be marketing.** *"The first thing that gets cut when things are good is marketing, and when things are bad, the first thing that gets cut is marketing."* Don't.

---

## 3. The Golden Rule: Never Touch a Page That's Already Ranking

The single most emphatic, most-repeated rule in the entire corpus, stated independently and forcefully in nearly every diagnostic call.

**If a page is ranking, for anything, even a keyword other than the one you intended, leave it alone.** *"Don't edit any pages that are ranking, for the love of God."* / *"If it is ranking, don't touch that page. Even if it's not ranking for the exact keyword that you want to go for or think it should rank for."*

- **The freeze covers content and structure signals**, and it holds even when the page violates every other rule in the playbook: duplicate H1s, keyword stuffed 122 times, hidden overlay text, thin content, zero backlinks. None of it matters if the page ranks and converts. *"I don't give a shit if you have 31 heading one tags when you should only have one. If you have 31 of them and you're ranking number one, I'm not touching that page."*
- **Why:** *"Once you optimize a page, stop touching it. Because if you keep updating it, Google's like, well, I need to restart from zero again."* Fixing a ranking page "for correctness" is pure downside risk (losing the spot) with no upside (you can't rank higher than #1).
- **The one carve-out: UX and CTA polish is still fair game.** You can adjust layout, buttons, and conversion elements. The freeze applies only to the content and structure that could shift rankings.
- **If a page ranks #1 but doesn't convert:** tiny incremental edits only (one sentence, one button, a CTA higher on the page), never a full rewrite at once.
- **Swapping a better-ranking sub-page in as the new homepage is "a little bit risky":** do it if warranted, but the mitigation is monitor-and-revert (watch rankings for days/weeks, revert if they drop), never "avoid testing."

### Set and forget has an expiration date
A page holding #1 for years on relatively little content can quietly lose the spot once competitors escalate. That moment, and only that moment, is the trigger to redo the full competitive audit. Never preemptively.
- **Evidence for:** Matt's own "SEO in Hamilton" service page, built once, minimally optimized, never touched, hit **#1 after ~1 year** purely via blog posts and internal linking with descriptive anchor text. *"I asked my team, did anybody touch this page? All we did was internal link to it."*
- **Evidence for the expiration:** his own website-design page held **#1 for ~2 years on 600 to 800 words**, then got outranked once competitors ran 2,300 to 2,500 words on the same term. Only then was the redo warranted.
- **Evidence you can't game it by copying:** Ellen Mitchell ranks #1 for a probate keyword using it 122 times with two duplicate H1s and hidden text; Brett ranks #2 for "Miami probate Realtor" on a thin page with zero backlinks. Both are *"a nightmare"* and both are left completely alone.

---

## 4. Editing Discipline & Patience Windows

The corollary to the Golden Rule: when you *do* touch something, move one piece at a time and then wait.

- **Change one core element, then let it simmer.** Never batch changes to H1s, target keywords, or multiple pages at once. Rapid, repeated changes read as instability and can trip Google's spam detection. During a live Google core update, touch **one page at a time** and check impact before the next.
- **Freshness-gaming is real; don't fall for it.** When a page is newly published or updated, Google will sometimes purposely suppress its ranking temporarily, then wait a few days to see whether the publisher panics and makes a flurry of edits. That panic-editing itself reads as a gaming signal. Rule: once a page is live, **give it ~1 month** before going back to re-update it. A dip within days or a week of an edit is expected noise, not a problem.
- **Non-ranking page: wait 3 months, then 6 months.** Do internal linking with descriptive anchor text in the meantime. If it still isn't ranking after 6 months, redo the full competitive audit and rework the page.
- **Judge any change over ~2 to 3 months of productive waiting** (keep publishing and internally linking to the changed page). Small title/meta/H1 nudges can be judged sooner, in ~2 weeks to 1 month. The waiting period is active, not passive downtime.
- **Rank volatility after a legitimate change is normal.** A page jumping to #7, then #9, then vanishing for over a week after a real fix is expected. And **page 3 is not position 3**: don't panic-react to page-level movement as if it were exact rank. A member who kept re-optimizing after reaching page 3 fell out of the rankings entirely as a direct result. *"What that tells me is you're probably doing too much."*
- **A drop after a publishing gap is not "Google punishing you."** Resume the normal cadence rather than editing the page.

---

## 5. Timelines & Expectations

Set these expectations up front, for yourself and every client, or people quit before the method has a chance to work.

- **3 to 6 months minimum** of consistent work before a real traffic increase. Inflection points can land as late as **month 12 to 14** even when monthly gains looked flat before. Ranking within **2 weeks is "magic,"** not the baseline.
- **Brand-new sites:** zero visible movement for the **first 2 weeks to 2 months is normal.** *"Don't feel discouraged, because every website that launches, the first two weeks, the first two months, you're not seeing anything."* A site under ~1 month old will not rank meaningfully regardless of on-page work; Google needs time to trust it.
- **New-post indexing:** ~2 hours to ~1 week is normal (reciprocal internal links from already-indexed posts can pull it toward the fast end, sometimes within an hour or two). Don't fixate on one post; keep publishing.
- **Insiders following this method report movement in ~1 to 1.5 months,** faster than the typical agency-client norm of 2 to 3 months.
- **There is no universal "healthy" CTR or impressions-to-clicks ratio.** Don't benchmark against a mythical number. As a site grows and ranks for more (often lower-position) keywords, average CTR naturally drops; that is math, not failure.
- **Most people quit SEO after ~3 months** without seeing results. The long game wins by attrition. One member on her broad head term: *"I've just outlasted everybody."*

Case evidence that the timeline pays off: a blog-only client onboarded from near-zero now nets a typical **$120,000/month** with SEO as the only channel, over a ~2 to 2.5 year horizon. A therapist who blogged one post a week for ~1.5 to 2 years now runs a **3-month waitlist**, is fully booked, cancelled his paid directory listing, and runs no ads, while every keyword tool shows him ranking for nothing.

---

## 6. The System: The Weekly ~1-Hour Loop

The entire method is deliberately engineered to fit in **about one hour a week.** *"I'm trying to make SEO so simple that anybody could do it in an hour a week."* Time-commitment objections get reframed: *"Do you have one hour a week?"* Even minimal, consistent participation outperforms 99% of businesses that do nothing. *"It's the basic things that everybody skips. Just show up an hour, two hours a week, and your rankings will increase over time."*

### The loop (one hour, one fixed day)
1. Find one real customer question or low-competition keyword.
2. Write the post via the interview method (your expertise, drafted with AI).
3. Publish.
4. Internal-link it (out to other pages, and in from older posts).

Then stop and move on. That is the whole recurring drill, repeated week after week.

### Operating rules for the system
- **Deliberately minimal content calendar.** Reject heavy multi-month editorial calendars; opinions and strategy shift and most people won't sustain them. Pick one fixed day, block one hour, do the loop. *"SEO only works if you don't give up."*
- **Don't research keywords far in advance.** Trends and phrasing shift and the research gets wasted. Each week, pick 1 to 2 keywords or questions and write.
- **Batch-write, paced-publish.** Decouple writing effort from publish cadence: write or schedule posts in batches weeks ahead, drip them out on a steady schedule so illness, vacation, or a busy stretch doesn't break the cadence. Never ramp volume up then cut it down; that pattern looks like gaming to Google.
- **Topics never actually run out.** A single seed term in a question finder returns 40+ questions, and a different term yields 40 more. Running dry is a signal to change the seed, not to stop.

---

## 7. Publishing Cadence (The Numbers)

- **Floor: 1 post/week. Ceiling for most sites: 1 to 2/week.** One a week is *"fantastic"* and genuinely valuable, not an inferior fallback; two a week produces *"a lot more progress"* but is the practical max for a solo/small operator. *"I wouldn't do any more than two, because it's going to get sloppy."*
- **Never publish both weekly posts on the same day.** Space them (e.g. Monday and Thursday). Consistency of cadence matters more than which days.
- **Brand-new site launch (the exception):** may batch **5 to 6 posts at once**, or launch with **10 and drip the rest at 2/week** to signal active maintenance and buy a 2 to 3-month buffer against a missed week.
- **Established live site: never publish a dozen at once.** Google treats high, unstable velocity as spam-like. When AI made mass production possible, sites pushing to ~500 pages/week saw quality and rankings drop as Google *"retaliated."* A web-designer rule of thumb: no more than 3, ideally 1 to 2/week.
- **Hub-building exception:** a member ran 5/week while building a ~50-post content hub. Acceptable only if quality genuinely holds and a defined structure justifies it. Explicitly the exception, not the default; forcing a number risks publishing weaker posts just to hit it.
- **HeyTony's own site publishes 3 to 5/week,** but that is an authority-tier exception (prospects scrutinize a paid provider's own site for credibility). It is not the standard for a typical client.
- **Refresh old posts every few months.** Blog posts are living documents; at minimum update the date, ideally revise content. Prioritize by Search Console (high-impression, low-click posts first), don't blanket-redo everything.

---

## 8. Anti-Overwhelm: The #1 Thing That Kills SEO

Overwhelm, not the tactics, is the number one thing that ruins people's SEO. They quit because they feel behind, not because the method stopped working. Guarding against overwhelm is therefore a first-class part of the system, not a soft afterthought.

- **Fix 5 to 10 issues per week, never the whole audit at once.** Start with the red issues that have the lowest count to build momentum. Fixing one instance of a systemic issue often auto-resolves it site-wide (a theme-level setting). *"Don't try to optimize and fix all the issues on your website. Fix 5 to 10 a week, and you'll be astounded at how much progress you make and how not stressed you are, because you're not burning out."*
- **Don't retroactively fix a systemic mistake all at once, even with spare time.** Fix one or two a day/week and otherwise keep moving forward with new content.
- **Scope is capped on purpose.** The 30-day plan asks for 5 issues (not all of them) and 4 posts (not more), specifically to prevent the burnout-driven quitting that stops people by week two. *"I'm not trying to get you guys to do everything. I'm trying to get you guys to make progress."*
- **Don't chase "perfect" before publishing.** A post is never going to be perfect, and more polish doesn't guarantee ranking anyway. *"Get something up rather than not get something up."* Publish, revise later if needed.
- **Don't overthink or go down rabbit holes.** *"Don't let that take you off track and go down a rabbit hole."*
- **Perfect is never the target on audit scores.** 80%+ on a page audit is fine; a 90% site-health score is *"fantastic."* Chasing the last few flags rarely changes rank and reliably wastes time. *"Sometimes you need that D to help you rank."*
- **The failure mode to fear is quitting, not imperfect work.** *"There's no win that's too small."* Progress compounds; abandonment is the only true loss.

---

## 9. The 30-Day Action Plan (The On-Ramp)

The concrete structure that turns the philosophy into a habit. Four weekly cycles, **~1 to 2 hours/week**, the same four tasks each week with a **new** blog post and a **new** money page:

1. Publish 1 blog post that links to 2 to 3 other blog posts + 1 money page.
2. Fix 5 red-flagged (serious) audit issues.
3. Fix that week's money page: title tag + meta description (treated as two sub-tasks so progress feels faster; one prompt does both in ~5 minutes), then H1.
4. Add 3 internal links to that week's money page from other pages.

- If one task already satisfies another (the new post already links to the money page), check it off, don't redo it.
- **Total over 30 days: 4 money pages, 4 blog posts, ~20 red issues fixed.**
- **Commit out loud to 4 specific calendar dates** and paste the plan into each invite. *"If it's in the calendar, it will get done. That's how I live my life."*
- Money-page fix priority order: **title tag, then meta description, then H1** (keyword in all three), then wait 1 to 2 weeks before touching on-page content further.
- *"This is not a sprint, it is a marathon."* The scope is deliberately capped to prevent overwhelm, not to be exhaustive.

---

## 10. The Program as a System (How Execution Actually Happens)

The community mechanics are part of the operating system: they exist to force consistent execution, which is the real bottleneck.

- **Reciprocity norm:** *"The more you put into this, the more you will get out."* / *"These are your results. These are not my results. You're the ones doing the work."*
- **Accountability ritual:** every session ends by posting your new URL, or what you'll fix this week, in the community. Saying it out loud or typing it makes you far more likely to do it. *"If you type it out, if you say it out loud, you're more likely to do it, more likely to remember it, more likely to fix it."*
- **Work-session format:** a quiet 30 to 45-minute writing block (cameras and mics off) where everyone just does the loop, then reconvenes for Q&A. The point is to actually produce, not just learn.
- **Sequential on-ramp:** a Levels 1 to 5 foundations track (technical setup, keyword research, audits, writing, tracking) and a 5-day Rank Week curriculum, both built on heavy repetition of the same core loop at increasing depth.
- **Reporting is taught last, on purpose.** Beginners build momentum first instead of getting discouraged watching flat early metrics. *"Reporting is deliberately taught last so beginners build momentum first."*
- **Meta-process:** even the program improves itself the same way it teaches, by feeding call transcripts and chat logs into Claude and asking *"what were the pain points, how did people feel today?"* to decide what to change next.

---

## 11. The System at Agency Scale (Client-Delivery Cadence)

The same cadence discipline, applied to paid client work. Two proven regimes, both real:

- **With backlink work:** **2 blog posts/week + 4 backlinks/month, and nothing else.** This is the model behind an undisclosed-niche client now doing **$1.3M/year**, grown from ~$20K/month to $100K+/month over 3 years with seasonal spikes to ~$200K, on no other marketing.
- **Without backlink work:** **1 blog post/week + 2 city/location pages/month.** Used on a 3-month engagement that ended with the client *"at capacity"* and hiring more staff.
- **HeyTony's own client standard:** 2 deliverables/week (one new blog post + one existing money-page rewrite), plus **4 backlinks/month**. *"That's all we do,"* and it gets *"crazy results."* Don't chase 10, 20, or 50 links/month.
- **Onboarding = map first, then run the loop.** Map the full content plan up front (topics, which pages link to which, which topics tie to which money pages), get client sign-off on the map, then execute the weekly write-and-link cycle per topic.
- **Revenue is capped by fulfillment capacity, not lead volume.** Past the point where a business can't absorb more work, conversion-rate improvement and pricing become the real growth levers, not more SEO traffic. Model it as a system, not a faucet.
- Flat monthly retainer, never hourly.

---

## 12. Governing Verbatim Quotes

Kept for faithfulness; these are the lines Matt actually repeats.

- *"We don't care about SEO, we care about getting clients. SEO is the way we're doing that."*
- *"The objective is not to game the algorithm, it's to write a piece of content so unique it talks to somebody with that specific problem."*
- *"Most of the time, if you're not ranking, you're either doing too little or too much."*
- *"If it is ranking, don't touch that page."*
- *"Once you optimize a page, stop touching it. Google's like, well, I need to restart from zero again."*
- *"Google isn't looking for SEO experts and properly optimized, perfect sites to rank. They're looking for experts in specific niches."*
- *"If you rank on Google, you will get recommended by AI. That's just the plain fact."*
- *"Pigs get fat and hogs get slaughtered."*
- *"Think of it as a snowball rolling down a hill. We call this the avalanche method."*
- *"You don't want a million doors. You want to build one door at a time."*
- *"SEO is a marathon, not a sprint."*
- *"Don't look at your credit score every day. Do the right thing every day, and then 30 days later, without you looking, it's changed and you can buy a house."*
- *"The people who get results aren't the ones who learn the most in a single day. They're the ones who keep going afterwards."*
- *"It's a patience game, it's a consistency game, and it's having faith a little bit, praying to our Lord and savior, Google."*
- *"It's the basic things that everybody skips. Just show up an hour, two hours a week, and your rankings will increase over time."*
- *"My goal is not to get you guys to hire me. My goal is to get you guys to rank for yourselves."*
- *"There's no win that's too small."*
- *"Would my customers actually need this? And read this? If yes, then publish it."*
- *"The first thing that gets cut when things are good is marketing, and when things are bad, the first thing that gets cut is marketing. Always be marketing."*
- *"None of us came out of the womb knowing anything, so I will learn."*
- *"This is not a sprint, it is a marathon."*

---

# Part II - Keywords, Search Intent & The Content Engine

The engine room of the whole method. Everything here answers two questions: *what do my customers actually type into Google?* and *how do I publish the single most helpful, most uniquely-mine answer to it?* Get these two right and rankings, traffic, and clients follow. Get them wrong and no amount of technical polish saves you.

### Governing Beliefs (read first)

- **SEO is answering real customer questions with real expertise.** The founding story, retold in every cohort: Marcus Sheridan, a pool-installation owner near bankruptcy in 2008 with zero SEO knowledge, wrote down and answered the exact questions he heard on sales calls every night at his kitchen table. Result: #1 pool website in the world within 2 years, and eventually a nine-figure exit. "He was truly helpful. That is what is ranking now." The AI interview method below is that same idea, sped up with tools.
- **We don't care about SEO, we care about getting clients.** SEO is just the vehicle. "The objective is not to game the algorithm, it's to write a piece of content so unique it talks to somebody with that specific problem." If your framing is "I want to rank because I want people to pay me," that is backwards. Write to genuinely help the searcher; ranking and revenue follow.
- **~15% of Google's ~2 billion daily searches are brand new**, never searched before, and will never appear in any keyword tool (SEMrush, Ahrefs, Moz, Ubersuggest only show terms they have already detected). Zero historical volume is not proof of zero future demand. This is the entire justification for answering full-sentence questions instead of only chasing measured keywords. It cuts both ways: a niche site invisible to competitor research is also one you cannot forecast or prove ROI on before publishing.
- **Overwhelm is the #1 thing that ruins SEO**, not the tactics. People quit because they feel behind, not because the method stopped working. The whole program is engineered to fit in **~1 hour/week**. "Don't overthink anything. Don't let that take you off track and go down a rabbit hole."
- **AI is a tool, never a brain-replacement.** Google and AI do NOT penalize AI-written content. They penalize **regurgitated, generic, same-as-everyone content**. "Google and AI hate AI-written posts? They do not. They hate regurgitated information that's the same that everybody else is saying over and over." What avoids the penalty is injecting your own real expertise, experience, opinions, and stories via the interview method.

---

## PART 1 - Keyword & Question Research

### 1.1 What a keyword actually is

- Plain definition: **exactly what people type into Google.** Not random words stuffed on a page. Keywords are the *questions and problems* your customers already search for: "how much does SEO cost," "best coffee shop near me," "how do I fix a leaky faucet."
- **Short-tail** = 3 words or fewer. Broad, high volume, high competition, hard to rank. Avoid as a primary target for a smaller site (e.g. "photographer" pits you against the world).
- **Long-tail** = 4+ words, usually a full question or statement. Specific, lower volume, easier to rank, faster traffic (e.g. "elopement wedding photographer Hamilton"). A long-tail target does not have to be phrased as a question; a plain statement ("how long can I keep my LED lights on for," a "top 10 X" list) works just as well.

### 1.2 The keyword opportunity matrix

| Traffic | Competition | Verdict |
|---|---|---|
| High | High | **Avoid.** Everyone's chasing these; you'll struggle and get discouraged. |
| Low | Low | **Default starting point.** Easiest realistic wins. |
| High | Low | **Unicorns / gold.** Rare. Always prioritize when found. |
| (any) | (any) | **High-intent** long-tail: fewer searches, far higher conversion, bottom-of-funnel. |

Guiding line for competition, repeated constantly: **"Pigs get fat and hogs get slaughtered."** Never try to grab an entire market or head term at once. Take a slice, win it, then expand. "People want the whole pizza. They don't want a slice, they want to take the whole thing" is exactly the mistake.

### 1.3 The research workflow (free-first, then paid)

**Free, tool-less (AnswerThePublic):**
1. Go to **answerthepublic.com**. No account = 1 free search/day; free account = 3/day. Set region to your **target country** (usually United States), not where you live.
2. Type in the **broadest** version of what you sell ("hot sauce," "plumber," "web hosting"). Broad beats specific for seeding. If a narrow term returns nothing ("ColdFusion web hosting," "tiles"), broaden it ("web hosting," "bathroom tile") and fold the niche back into the answer body later.
3. Click **Search Engines -> Questions**. Use the plain **List view**, not the Wheel (unreadable). Ignore Volume/CPC columns at this stage.
4. **Skip page 1. Use page 2, 3, or 4.** Competitors rarely click past page 1, so later pages are less contested. This is the single most-emphasized tactic in the whole discovery step.
5. Scroll further down for a **second, hidden question set sourced from Bing** that most people miss. Bing carries ~4% of global search, and ChatGPT pulls from both Google and Bing, so Bing-only questions are still worth targeting.
6. Pick a question you can **personally answer today** (no research required), that's specific and fits your business.

**Google's own SERP (a fully equivalent substitute):** Google your core term -> scroll to **"People Also Ask"** -> click a question to surface more -> also check **"People Also Search For."** Pull 4 different questions, not near-duplicate angles.

**Paid tools (optional cross-check, never required):** SEMrush (Matt's daily driver), Ubersuggest (cheapest), Ahrefs, KeySearch. Any works. Set the tool's **location to your target country** every time (a recurring self-inflicted bug: leaving it on the wrong default).
- **Method A, single competitor:** Google your industry + location, open the #1-3 organic (never paid) results, paste a domain into Organic Research, scan its easy keywords by Volume + KD.
- **Method B, Keyword Gap / Content Gap:** enter your domain + a big content publisher's domain. The competitor does NOT need to be a direct rival; **the bigger/more authoritative the comparison site, the more opportunities surface** (Matt uses neilpatel.com). Filter to **"Untapped"** (they rank, you don't), ignore "Shared" (targeting those = cannibalization), sort by KD ascending. Live results: 47 untapped vs a small local competitor, 927 vs neilpatel.com.
- **Competitor sitemap gap (no paid tool):** grab `[competitor]/sitemap.xml` (on Yoast sites open the **post-sitemap** to isolate blog posts), paste into ChatGPT with: *"Using my competitor's sitemap, tell me content gaps that I can write about on my website that likely have an easier difficulty."* Red flags that mean pick a different competitor: single-line sitemap, no post links, or no sitemap at all (signals they're not doing well on Google). Jessa got 24 content-gap ideas this way: "a roadmap for the next six months."
- **Reddit mining:** Insiders' **Reddit Keywords tool** crawls subreddits for a seed term and returns the real questions people ask, plus pain points and content ideas. No tool? Google `site:reddit.com [keyword]` (Reddit's own search is weak, Google indexed it thoroughly). Especially powerful for **LLM/AI visibility**: brands are outranking competitors in ChatGPT/Gemini largely off Reddit mentions.

### 1.4 Thresholds: difficulty, volume, referring domains

- **Keyword Difficulty (KD):** ideal band **0-15** (tighten to under 14 for a brand-new/low-authority site); up to **25 "still possible"**; ~31 "a little more difficult than I'd like"; **90-100 = never going to rank** (e.g. "website design," no location, ~60,000 US searches, 100% KD). KD is best read as roughly the Domain Authority you'd need to rank page 1. Higher-volume keywords are "9 or 9.9 times out of 10" harder than low-volume long-tail, even when no difficulty score shows.
- **Volume:** **~10 searches/month is an acceptable target.** Don't dismiss it: "even if there's only 10 people searching that, those 10 people are looking to work with an SEO agency." Rough floors for low-authority sites (not hard rules): product pages **≥~30/mo**, collection pages **≥~50/mo**; go lower for a brand-new site. If a tool shows **N/A** difficulty, refresh/update its metrics (~1 min) rather than treating it as zero.
- **Zero/near-zero volume is NOT a disqualifier** if difficulty is near-zero AND other demand evidence exists (a subreddit already discussing it, a competitor already ranking, an active People Also Ask box). Tools under-report hyper-local and brand-new terms.
- **Referring domains, not raw backlink count**, is the metric to check on a SERP's current winners. A page ranking on page 1 with **0-2 referring domains** is genuinely winnable with no link-building. "Backlinks are expensive and time-consuming to get. If I can avoid it, I will avoid it at all costs." KD itself is calculated largely from the backlink profiles of currently-ranking pages, so a 0-volume term can still score ~60 KD if the incumbents are heavily linked.

### 1.5 Keyword phrasing & variants (match the market, don't educate it)

- **Always follow the keyword research and never guess. Never** - even against your own pride or attachment to a product name.
- When a term has multiple spellings/forms ("stand-up" vs "standup," "web design" vs "website design," "permanent makeup" vs "permanent-makeup," "paddle" vs "padel"): **check which variant the market and competitors actually use and which gets real traffic, then target that.** "Your job is not to train people. Just use the terms that people use in real life and look at what your competitors are doing because they've built a roadmap for you." Matt lost visibility for "website design" while both competitors beating him used "web design."
- **Match competitors' exact phrasing, not a close synonym**, in structural tags (title, H1, meta). Use variants only in body copy. Singular vs plural: use whichever form the research shows people search. Google treats natural variations as equivalent, so don't force an exact-match into a sentence that sounds wrong spoken aloud ("Tampa Bay Boat Rental Tampa").
- **Misspelled / "wrong" / layperson terms:** if the top-volume variant is technically misspelled, backwards, or the non-professional term, still target it and use the post to explain why it's technically wrong. Reputation-sensitive niches (law, plastic surgery) may legitimately choose correctness over matching sloppy search behavior; that's a brand values call, not an SEO rule.
- **Name products/pages what real searchers type, not invented brand language.** A beaver-fur hatmaker renamed off a trendy invented name to "beaver fur hat" (260 searches/mo Canada, 880 US). Jackie's Irish-language candles became "[Scent] Soy Candle" with the Irish name appended at the end. Lead the title with the real keyword; append the brand/invented name last, never the reverse.
- **Novel/category-defining products with no existing demand:** don't force the question workflow. Write an "old thing vs new thing" comparison post instead.
- **Cross-language:** run keyword research natively in the target language from scratch. Don't translate English content; the real search phrase is often different from a literal translation. For blog/general content most solo operators should pick one language and rely on browser auto-translate; only money/service pages need the customer's real language.

### 1.6 Secondary keywords

- Prompt: *"Please give me 10 secondary keywords that are SEO optimized"* (paired with the primary). **Cap at 5-10 per piece.** Only use the ones that fit naturally; no obligation to work every one in.
- One practitioner's personal rule: skip volume/difficulty scoring for secondaries, just check topical relevance ("secondary keywords are a dance"). Build research into **lists/themes** rather than one rigid keyword: "Using it more as a concept. You don't want to jam all of these in, but you have them to use."

### 1.7 Word count & keyword density: benchmark competitors, never a fixed number

**There is no universal ideal word count, keyword count, or density.** The only real benchmark is whatever is *currently* ranking #1-3 for that exact keyword, and it moves as the competitive set changes.

- **Word count:** Google the exact keyword, check the actual top 3 pages, and **match them or add ~100-200 words** (some cohorts phrase it as **"level plus one" / ~10% more / "0.0001% more"**). Real competitor pages for one keyword ranged from ~500 to 2,500 words in the same SERP, proving word count itself is not the driver. **Over-optimization (too long) is one of the most common live failure modes** and gets you told to *trim*, not add. Anchors seen across calls: **~400-500 words** is plenty for a zero-competition long-tail; a **~700-800-word floor** for a normal post; a rough **~2,000-word ceiling** per page. A 2,000-word page has outranked a 3,200-word page in the same niche when intent/format matched better.
  - *Note on the old curriculum:* Level-0 foundations state "~2,000 words correlates with #1-4" and "even the homepage should hit 2,000+." The live calls supersede this: it is a rough anchor only. The competitor-relative rule wins.
- **Keyword density:** no fixed %. "Use it three or four times and see what happens" as calibration, then match the actual #1 competitor's count (seen ranging from once to 27 times). **Split the phrase into components** (location + service) and count each separately across competitors. **Density red flag:** if yours sits meaningfully higher than competitors', you are almost certainly over-optimized. Matt's own page: **5.04% density (keyword used 35 times) vs competitors' 1.76% and 0.9%** correlated with a drop from #1 to #9. "More keywords does not equal better rankings. Google increasingly interprets heavy keyword repetition as over-optimization."
- **Never trust a single tool's word/density number.** Extensions disagree by hundreds of words; tools scrape hidden popups, review-widget text, mobile-duplicated text, and currency selectors. One page: 808 (tool) vs 511 (manual). A plugin was once silently injecting 2,000 words of hidden text onto every page. **Verify by copy-pasting visible text into wordcounter.net.** Tools also lump keyword variants together, inflating counts (a "35 uses" reading was ~5 literal uses plus a related variant).
- **Ignore keyword-density plugins entirely** (Yoast/Rank Math) for long-tail/question content: they are geared toward 3-4-word short-tail phrases and actively work against full-question posts. Chasing a plugin's "use the keyword N times" rule can literally CREATE the over-optimization and cross-page cannibalization problems.

### 1.8 Keyword tools quick reference

| Tool | Use | Notes |
|---|---|---|
| **AnswerThePublic** | Question mining | Free 1/day (no acct) or 3/day; not a full keyword tool |
| **Google People Also Ask** | Question mining | Fully equivalent substitute |
| **Insiders Reddit Keywords / PAA / Quora tools** | Real-question mining | Reddit tool especially strong for LLM visibility |
| **SEMrush** | Volume, KD, Keyword Gap, SERP analysis | ~$130-150/mo; trust **Keyword Difficulty**, don't over-weight "Competitive Density"; cancel free trial immediately (charges, no refund) |
| **Ubersuggest** | Cheapest research | ~$20-40/mo; volume often inflated (grouped) |
| **Ahrefs** | Research, difficulty cross-check | Lite ~$29/mo, 100 searches/mo cap; **trust Ahrefs over Ubersuggest 100% of the time** on difficulty disagreements |
| **KeySearch / Mangools** | Cheaper alternatives | KeySearch ~$20-24/mo, 200 searches/day |
| **Hey Keywords (heykeywords.com)** | Matt's own; pulls live from Google Ads | Base ~$29/mo (50 searches + 10 domain analyses); keyword/backlink/gap views |
| **Insiders Blog Idea Finder / findquestions.com** | Topic/question finder | In-platform, no email gate |
| **wordcounter.net / characterCounter.net** | Manual word/density/char verification | The real source of truth over any extension |

**Cross-tool disagreement is expected** (each vendor applies its own undisclosed adjustment on top of the same Google Ads data). Treat all numbers as directional. Google Search Console is the more accurate ground truth for actual organic traffic; the research tools are for planning. Don't use Google Trends to judge volume.

---

## PART 2 - Search Intent

Intent determines the *format* of the page and whether it should exist at all. Choosing the wrong format loses regardless of content quality.

### 2.1 Funnel mapping (TOFU / MOFU / BOFU)

- **Bottom-funnel (BOFU):** searcher already knows they need your exact service (e.g. "web design" or "personal trainer in Vancouver"). High intent, lower volume.
- **Middle/top-funnel (MOFU/TOFU):** searcher doesn't yet realize your service is the fix ("why aren't I getting business," "when was hot sauce invented"). **Most available search volume sits here**, not at the bottom. Don't stay stuck only answering BOFU questions.
- Client-discovery question to surface MOFU/TOFU topics (Kira): *"If I could wave a magic wand and give you anything, what problem would I solve?"* The literal answer ("I want consistent leads") is raw material: write about the underlying problem, not the service name.
- **The content itself walks the reader down-funnel:** answer the informational question, then a contextual internal link/CTA ("check out our hot sauces ->").

### 2.2 Match content format to what is actually ranking

**Before writing or optimizing any page, Google the exact target phrase and look at the SERP.** Is it dominated by product/collection pages, directories/listicles, service pages, or blog posts? Build the matching format. Writing the "wrong" format for that SERP will not rank regardless of quality.
- "best video production company in NY" is dominated by list/directory sites (Clutch); a single-company "we are the best" page fights the wrong intent.
- "ski t-shirt," "tennis shirts" SERPs are dominated by **collection pages**, so optimizing a *product* page for that term fights the wrong format.
- If the top results are all "platform" types (Vimeo-style, marketplaces) and you're a local service business, that keyword's intent doesn't match you; deprioritize even at 0 difficulty.

### 2.3 Money page vs blog post: the dividing test

- **The test:** if content ends with a "conclusion," is purely informational, or answers a *question*, it's a **blog post**, regardless of what page type it was built as. A **money page** (service, product, collection, location) assumes the visitor is already past education and just needs to know you offer the solution and how to book.
- Rank Week phrasing: if someone would Google the topic for *information*, write a blog post; if they'd Google it to *hire someone*, write a service page. Same topic, different content, never blended.
- **Blog posts are informational-intent by default and usually aren't meant to convert directly.** Their job is trust and topical authority. A high-ranking blog post with weak conversion is not broken; it may just need a business-relevant CTA added, not a rewrite into a sales page. Sometimes a blog post's only job is passing internal-link authority to a money page.
- **You cannot rank for a keyword without a page built around that exact keyword.** "You can't rank for a keyword if you don't have a page about that keyword." Put transactional terms ("Scorpio candle") on collection or product pages, not blog posts.

### 2.4 Homepage targeting by business model

- **Local/service businesses:** target `[service] + [city]` on the homepage ("dentist in Hamilton," "Residential Roofing in Cincinnati").
- **Ecommerce / content / national sites:** do NOT rank the homepage for a keyword. Ranking happens on collections, products, and blog posts; the homepage just orients a visitor who landed from an entry page. Make it a branded page (H1 = brand name, title tag = brand + what you sell).
- **National/virtual with no physical base:** optimize the homepage for the single largest nearby metro, then spin out location pages for smaller markets.
- **A blog post's target keyword should never be your homepage's primary keyword** (self-cannibalization). Use secondary/variant keywords in blog content.

### 2.5 "Near me" and adjacent keywords

- **Never target "near me" as a keyword** or bake it into copy. "The sign of somebody who doesn't know how to do SEO." Google already connects searcher location to your business automatically; you rank locally from other signals. If "near me" is already a top organic referrer, leave the page as-is; don't engineer it.
- **Ranking for an adjacent keyword is fine, not a conflict** (a photographer ranking on "wedding venue" searches). Capture it via a sidebar/popup/downloadable guide rather than fighting it, as long as your real service is clearly stated elsewhere.

### 2.6 The two-question business-priority filter (Kira)

Before picking any tactic, answer: (1) **"What are my priorities for the next 3-6 months?"** (revenue/leads vs authority vs brand) and (2) **"Is my business hyperlocal, or do I serve broadly?"** The combination decides which levers matter now. There is no universal rank-order across businesses.
- Plenty-of-leads-but-wrong-fit (a surgeon getting calls for procedures they don't do): stop chasing more high-traffic keywords; narrow/optimize specific service pages describing exactly what you do and don't do.
- Needs-more-leads, non-hyperlocal: deprioritize Google Business Profile; prioritize high-traffic/low-competition content + conversion-rate work.
- Brand-new/near-zero traffic: prioritize **low difficulty even at low volume** to generate visible momentum fast (a confidence play as much as a traffic play).

**Positioning/differentiation angles (Kira):**
- **Reposition away from head-term competition:** a voiceover artist stopped fighting "voiceover" against 100,000+ competitors and repositioned around a real differentiator ("48 years of business experience") aimed at the much larger pool of small businesses.
- **Competitor brand name as a secondary (never primary) keyword:** you won't outrank a competitor for their own name; work it into body copy as a comparison ("Compared to Suavecito pomade, our pomade is...").
- **Radical-honesty "problems with X" posts:** write about the real downsides of hiring/buying your own product/service type. Title: "The problems with hiring/buying [X] that no one talks about." Competitors won't write it, so you become the honest voice. Must be genuinely honest, never a disguised pitch.

---

## PART 3 - Keyword Cannibalization

**The single most-repeated rule in the entire curriculum: one keyword per page, always.** "If you have the exact same keyword on two different pages, Google looks at them and goes, I don't know which page to rank. Maybe I'm not going to rank either." Google will only ever surface one page from your domain per query, so unmanaged overlap directly costs you.

### 3.1 What is and isn't cannibalization

- **IS:** two pages/posts on your own site whose *topic* (exact keyword or its natural variant) competes. It is about the page's topic, not link destinations, so many blog posts can all link to the same money page without cannibalizing, as long as each post's own topic differs.
- **IS NOT - different locations = different keywords by definition.** "We buy junk cars, Dallas" and "...Houston" never cannibalize no matter how similar the template, provided the exact keyword differs and the local content is genuinely substantive. "If you add a location, that is a whole new keyword." (Live proof: "we buy junk cars, Dallas" at volume 210 beat both the "...Dallas, Texas" and the ChatGPT-suggested root "junk car buyer" variants.)
- **IS NOT - topical authority via many similar pages** is fine and encouraged, as long as (a) no two pages exact-match the same keyword and (b) content is meaningfully different, not re-skinned. Hot-sauce demo: 4 posts plus a money page all mentioning "hot sauce" don't cannibalize, because each *full question* is its own keyword ("what is hot sauce made of" is not "what is the healthiest hot sauce"). "If a dentist could only talk about teeth on one page because teeth is a keyword, that doesn't make sense."
- **IS NOT** - a collection/category page and a blog post on similar subject matter, provided the blog targets a distinctly different (usually longer-tail) keyword. Product-comparison pages (Botox vs Dysport vs Xeomin) are a valid consideration-stage content type, not cannibalization of the individual product pages.

### 3.2 Within-page cannibalization

Using 3+ near-duplicate phrase variants inside one page ("indigenous art fly net hat," "mosquito net hat," "indigenous art protection print fly net hat") confuses the target signal. Commit to one primary phrase per page.

### 3.3 Detection & fixes

- **Detection:** the Insiders **Cannibalized Keywords Scanner** / **keywordconflict.com** (auto-pulls sitemap, ~50-page default scan, adjustable toward 500); Hey Tony **Money Page Tool** (reports which of *your* pages actually ranks #1 for a keyword, surfacing when your homepage is stealing your service page's term); GSC (click a Query -> Pages tab to see every URL ranking for it). **False positives are common:** date-based archive slugs redirecting to the homepage, or pages that 301-redirect to the canonical, get flagged but aren't real conflicts. Cross-check flagged URLs against `sitemap.xml` and `robots.txt`; if absent from both, they're redirect artifacts. Near-synonyms ("photography" vs "photographer") show similar volume because tools group them semantically; don't worry about cannibalization between them.
- **Fix:** consolidate the two pages into one, or 301-redirect the lower-traffic page into the higher. To de-cannibalize, paste both pages' full content into Claude and ask it to compare and recommend what to change on each so they stop competing.
- **Never A/B test two pages/posts for the same keyword** - that IS cannibalization. A/B testing works for Reels or YouTube thumbnails, not blog posts chasing the same term. Test variants sequentially over time instead.
- **Never rewrite/republish a post to "refresh" it.** Edit the existing post in place in the CMS regardless of original publish date; a literal copy-paste repost is a real cannibalization risk.
- **Blog + money-page guard:** the money page owns the exact buyer-intent phrase; blog posts cover adjacent educational angles and reference the exact money-page phrase **at most once**, typically near the bottom as a link back, never repeated throughout.
- **The golden exception:** if a blog post and a service page are already both ranking for the same keyword and it's working, **leave it alone.** Don't "fix" a technically-cannibalizing setup that's delivering results.

---

## PART 4 - The Content Engine: The AI Interview Blog Workflow

This is the recurring weekly drill, taught and re-taught in nearly every session. It is the spine of the whole method.

### 4.1 Why blog posts work (the compounding case)

Blog posts are "the lifeblood of a website. It gives you authority. It shows Google that you know what you're talking about." The seven mechanisms:
1. **Traffic + trust** - easy long-tail ranks fast; visitor engagement (time on site, clicks, form fills) signals quality.
2. **Internal-linking equity** - every post is a fresh chance to pass keyword-anchored links to money pages.
3. **Unlocks harder keywords over time** - accumulated traffic/trust eventually lets you compete for terms you couldn't touch on day one.
4. **Organic backlinks** - unique content earns natural links; people link to informational content far more readily than to a sales page.
5. **The avalanche / snowball method** - keep stacking small, zero-competition, near-zero-volume question posts, all interlinked. Individually they barely move traffic; the accumulated topical authority is what eventually unlocks the harder head keywords. "The snowball's small, then we get more traffic, Google trusts us more, ChatGPT starts picking us up."
6. **Consumer trust/recognition** - answering prospects' exact questions early builds expert positioning that pays off at the purchase decision.
7. **Topical authority** - modern Google favors sites tightly focused on one field.

Case proof: a blog-only client hit **$120K/month** after ~2.5 years with SEO as the only channel. A therapist told to "write one blog post a week and answer your customers' questions" now runs a 3-month waitlist, fully booked, no ads, invisible to every keyword tool for "male therapist Hamilton" yet ranking live on Google and ChatGPT.

### 4.2 The weekly loop (step by step)

1. **Source a real customer question** (Part 1.3). Or use one you personally heard from a customer at an expo, on a client call, or in a niche Facebook group.
2. **Open a brand-new chat** in ChatGPT / Claude / Gemini / any LLM (interchangeable for this step). Paste the **interview prompt** (4.3) with your question substituted in.
3. **Answer the AI's clarifying questions one at a time**, in the same thread. **Voice mode is strongly preferred** ("I'll digress and might reveal something else I wouldn't think of if I was typing"). Tangents are fine; rambling trains the AI to sound like you. 2-3 sentences per answer is enough as long as each reflects genuine experience/opinion. Budget ~1 min/question, ~20-30 min for 10.
4. **Run the write-the-post prompt** (4.3) in the same thread so it references the interview context. Or relay the Q&A into a second AI (4.4).
5. **Copy the entire draft into a blank Google Doc / Word doc first.** Never build directly in the CMS. (Pasting through plain text also strips a hidden AI-generated tag some CMS backends store; alternatively use WordPress's paste-as-code button, or have the AI output raw HTML and paste into the code tab.)
6. **Clean-up pass, line by line** (4.5) - strip the AI tells.
7. **Add images** (4.7) and internal links (4.10).
8. **Write title tag + meta description** by asking the AI (4.3), confirming the target keyword appears in both.
9. **Publish** (4.10). Fine to publish text-first and add images later ("get something up rather than not"); caveat: if Google crawls before images exist, it picks up later-added images noticeably slower.
10. **Close the loop:** go into 3 older, already-indexed posts and add a link from each into the brand-new post.

**Never publish the first draft as-is.** Review every section: is it actually helpful, or a thin bullet list? Verify every first-person claim the AI invented ("I've helped businesses rank for...") against what's actually true for you; cut anything inaccurate. "Don't publish anything that you can't stand behind."

### 4.3 The exact prompts (verbatim, by function)

**Interview / clarifying-questions prompt (canonical):**
> "I'm writing a blog post answering this question: [paste the question]. Ask me anything you need to know the answer to in order to write a blog post that is truly helpful and unique. It should include my experience, expertise, case studies, examples, opinions, etc. Keep it limited to 10 questions. Ask me them one at a time. I'll be using voice mode to answer them. Give me time to breathe as well before going to the next question."
- **Cap the questions at 5-10.** Uncapped it defaults to ~30 ("way too much"). Different cohorts standardized on 5 or 10; 7-8 is common. Add the voice-mode instruction separately if needed: *"I'm going to answer these in voice mode. Ask me one at a time and leave room for me to breathe. Don't write the blog post. I will prompt you after."*

**Write / final-draft prompt (canonical):**
> "Write this as a clean WordPress ready blog post using my expertise, experience, opinion, stories, etc. Use H2 and H3 headings only. No horizontal rules, section dividers, tables, call out boxes or other formatting elements. Just headings, paragraphs, and bullet points where appropriate."
- "Doesn't matter if you're using WordPress or not, it's just verbiage" to make the AI strip its own formatting clutter.

**Simpler relay version (ChatGPT Q&A -> Claude):** *"Write me this blog post using this information."* / *"I just did this with ChatGPT, write me the blog post using my answers."*

**Fuller relay (Carol's):** *"Here's my chat with ChatGPT about writing a blog post. There are questions it asked me and my transcript I did in voice mode to answer. Please write me a blog post using this information plus whatever searches you need to do online to get the most accurate information."*

**Rewrite bullets -> prose:** *"Rewrite the following. I don't want it to be a bunch of bullet points, that's not helpful. Elaborate on it a bit and ensure there's at least one paragraph. It can still include bullets if useful, just not as the whole section."*
- Length control add-ons: *"This is a bit long now, shorten it to three to four paragraphs, and don't end it with 'finally.'"* / *"Same with this, but keep it under 250 words."*
- Subheading breakup: *"Let's do some H3 tags or something to break this up a bit."*

**Direct-answer rewrite (AEO):** *"The first paragraph should directly answer the question posed in the title / main keyword."*

**Key Takeaways / TL;DR:** *"Give me a TL;DR at the top of this blog post. Five points max. Call it 'Key Summary.'"* Prefer "Key Takeaways" / "Key Summary" over "TL;DR" (that term reads Reddit-native). Also: *"write me key takeaways for the end."*

**Secondary keywords:** *"Please give me 10 secondary keywords that are SEO optimized."*

**Meta description:** *"Write me a killer, compelling, click-worthy meta description for this page."* Generate ~5, pick the best.

**Title tag:** *"Write me a title tag for this page under 60 characters. The focus keyword is [X]."* (Or "five compelling title tag options, make sure it includes [keyword]," pick the best.)

**Featured image (attach 2-4 on-brand images as style refs):** *"Using the style of the images attached, create me a featured/cover image for this blog post. Here is [the topic]. You don't need any text on the image (no title, no question). [Optional mood: it should be someone who is frustrated or unsure what to do.]"* Add *"make sure not to include any of the exact images that are in these, make new ones in that style"* to avoid copying reference elements.

**Infographic:** *"Make an infographic for this page."* / *"Create me an infographic for this content."*

**Big Five ideation (Marcus Sheridan's framework, to avoid re-summarizing competitor lists):**
1. First: *"summarize this"* on each of the top-3 ranking articles, one at a time (trains the AI on what's ranking).
2. Then: *"I only want 20 blog post ideas that work for any business, not for specific industries. The keyword I'm trying to rank for is [X]. I want you to come up with topics based on Marcus Sheridan's Big Five blog posts."*
3. Then: *"Write me a blog post based on these ideas. Knowing the keyword is [X], it should be helpful, unique, and include my personal expertise, experience, case studies, etc. Use any relevant info from previous chats."*
- The five categories center on cost & pricing (how much, what affects price, is it worth it, cheap vs expensive), comparisons, "best of," problems, and reviews. Add one external link to the framework's source (Sheridan's own site).

**Knowledge-base seeding (carry context into Claude):** *"I want to make a .md file that has everything you know about me and everything another AI would need to know in order to operate the same way you do with me. Give me that whole breakdown, make it into this file."* Paste the result into Claude as standing context, or save it as a Claude Project / custom GPT. (Condense to ~25-30 pages max; ~50 pages dilutes output.)

**Mining client-call transcripts:** *"What are all the questions and answers that happened in these calls?"* Feed a client Zoom transcript in. Captures real Q&A plus natural brand voice. "A gold mine for content."

**Repurpose a transcript/podcast/video (append to the interview prompt):** *"Here's a transcript from a conversation I had. Use that information when you can and where you can to pull my expertise, experience, all that kind of stuff."* Never just hand over a raw transcript and ask for "a blog post."

**E-A-T self-audit:** after editing, paste/describe the content to Claude/ChatGPT and ask for a grade on each E-A-T category plus specific improvements.

**Reverse-engineer an AI citation (when Google AI Mode/Gemini names your business):** *"what did you analyze to recommend these companies"* and *"what search terms did you search for."*

### 4.4 Model selection & voice mode

- **The dominant split:** use **ChatGPT for the voice/interview stage** (Whisper transcription is "the best of the best"), then **paste the full Q&A into Claude for the actual writing.** "Claude is just better for like 99% of things. All my agency stuff, all the output is with Claude." Reasons Claude wins for writing: follows word-count/format instructions far more precisely, "writes like a person" vs ChatGPT's bullet-point/summary defaults, makes conservative minimal edits on rewrites vs ChatGPT's over-rewriting, and is stronger on spreadsheet/data tasks.
- **Any LLM works for the interview** (ChatGPT, Claude, Gemini, Grok, Copilot, Perplexity). **Gemini** (free tier) is notably strong on meta-description length compliance and image generation from reference photos. Grok is interchangeable.
- **ChatGPT reasoning setting:** use **"Instant"** for the fast Q&A stage, switch to **"High"** for the actual writing (deeper but slower). If ChatGPT degrades to one-line answers after ~10 posts in one thread, switch effort level or move to Claude.
- **Voice mode mechanics:** click the voice icon (not "dictate"), answer one question at a time, and **do not tap the mic again until it has fully stopped** or you risk silently losing the transcript. If screen-sharing on a live call, **stop sharing before pasting real answers** to avoid exposing client data. Personal/sensitive question? Write that answer yourself and use the AI only for the structural framework around it.
- **The Insiders AI Blog Post Writer** (app.htinsiders.com) is a Claude-powered, free alternative that runs this whole workflow: type a topic, it interviews you (~7-10 questions), then drafts following Matt's own rules. Cap: 10 generations/account (a failed run still burns a slot). Output is HTML only.
- **There is no way to fully automate this.** Even the best pipeline needs a human to answer the interview and review the draft. Skipping that is what produces generic "oatmeal" / "AI slop." "There's no way to automate writing blog posts."

### 4.5 Draft cleanup: the AI tells to strip manually

Strip every one of these before publishing (they mark content as AI-written and read as unedited):
- Horizontal rule / divider / spacer bar lines (they paste in as stray blocks).
- Random/unnecessary **bold** text and decorative arrows.
- **Emojis** - a "gratuitous amount" reads as AI; never put emojis in heading tags (pollutes what Google reads as the heading).
- Checkmark-style bullets and plain numbered-list markers (1, 2, 3) unless the post is genuinely a listicle.
- The stray leading space before a line's first word.
- Generic **"Conclusion" / "Final Thoughts"** headers (replace with a specific, content-tied closer) and the closing phrase **"and finally..."**
- Self-promotional/CTA-style subheads that don't belong in a pure answer post.
- Jargon/framework references the reader won't recognize (cut "Big Five" from the body even if you used it as an ideation lens).
- A **"Key Takeaways" H2 on every single post** can itself tip off that copy is unedited ChatGPT; use judgment.

**Em dashes:** treated by most of the community and by Kira's editing bar as an AI tell to cut. (Matt personally has said em dashes are fine to leave in during Rank Week; note this is his stated position, not a universal rule, and it is moot regardless since raw AI output should never go straight to the site.) In WordPress, run **Clear Formatting** after pasting, then manually rebuild real bulleted/numbered lists.

### 4.6 The humanizing stance and the AI-content line

- Content does **not** need to be "100% human." It needs to be **"100% helpful"** and use your own real expertise/experience. Weaving your own offer into educational content is fine; the actual violation is a **bait-and-switch** (searcher wants X, content only pitches unrelated Y).
- **Never run an AI-detector on your own writing and never "humanize" AI output.** Philosophically contradictory ("using AI to look at AI doesn't make any sense"). "We don't want to humanize our content. We want to write human content and have AI take our words and frame it coherently. Every piece should be from you, not random AI slop."
- **AI-generated content is NOT a ranking disadvantage.** Proof: Matt's own "SEO when building a website" post, ~99% AI, ~30 min total, ranked #1 on his machine and #2 on Semrush with **zero backlinks, zero referring domains**, beating Squarespace, Reddit, Shopify, Wix.
- **The unacceptable use is mass unedited publishing at unrealistic volume** - 300-500 AI posts in a day (or even a month) is unrealistic even for a site with a writing staff, and Google reads it as gaming the system. One escape-room site had ~3,000-5,000 fake-name AI pages, ~2,000 indexed, none ranking. AI-generated *images* are fine for ranking; AI-generated *video* is not (YouTube actively cracks down on it).
- The trend is toward **more authenticity, more off-the-cuff, more real** - 30-second real clips of an actual team member on site beat faceless content. "Who wrote this? That is telling who is writing the content on the internet."

### 4.7 Content structure for direct answers and AEO

- **Direct-answer-first:** restate the question as a subheading/lead-in, then answer it immediately and plainly in the first paragraph. LLMs and AI Overviews scan for direct Q->A pairs, so put the pairing at the very top and repeat the keyword/question near the top more than once. Model: *"Yes, ChatGPT can help with SEO, but it can't do it on its own"* (answering "Can ChatGPT do SEO?").
- **Key Takeaways block** at the end of every post: 4-5 bullets, worth doing regardless of length.
- **TL;DR / Summary at the very top:** only for *longer* content whose first paragraph doesn't already carry the direct answer. Write it so an AI Overview could clip it verbatim (~100 words). Matt is actively A/B testing "conclusion" vs "key takeaways" labels; results "mixed but leaning positive," more valuable as a differentiator when rivals aren't doing it.
- **AI Overview citation mechanism (Matt's ~100-query study):** ranking #1 organically does NOT reliably correlate with being cited in AI Overviews. Google's AI generates a claim/statistic first, then finds content that **supports** it. So Google the query, read what the AI Overview asserts, then **state that claim first in your content and pivot after** with your differentiated info: *"The average kitchen renovation costs $50-75,000 in [area]. However, we can do it for $25,000."* Contradicting the claim outright won't get you cited.
- **FAQs are not a free SEO win.** Stacking ~10 generic FAQs at the bottom after the CTA does nothing on its own ("is this actually helpful to a human? Probably not"). If used, **cap at 3-4 questions max**, mark as **H2 with plain question-then-answer text**, never behind an accordion/toggle/dropdown (adds parsing friction for Google and AI crawlers). An FAQ-*style* piece of content overall can genuinely help. Each standalone FAQ question can also become its own blog post.
- **Schema markup / "optimizing specifically for AI search":** largely unnecessary as a separate initiative. "If you rank high on Google and do all that work to get there, you'll likely rank in all these AIs too." Matt's own tool found non-ranking pages had *more* schema than ranking ones (one site, unvalidated). Turn on a plugin's default schema (free), skip complicated custom schema.
- **Reading level: 7th-8th grade throughout.** "If you can't explain it to a kid, you can't explain it." Rule of thumb: if an eighth grader could understand it, you're good. Paragraphs of 2-3 sentences; vary sentence length. Don't chase an all-green Yoast readability score; the algorithm "is not 100% accurate." Ignore transition-word and keyphrase-density complaints entirely.

### 4.8 Images (content side)

- **Density:** roughly one image, video, or chart every **200-300 words**, "as often as makes sense." Separate floor: **at least 4 images per post**, ideally one per H2. Every post needs at minimum a hero/featured image. (An acceptable substitute where an image doesn't fit a section: a heading-tag break.)
- **Sourcing priority:** your own real photos/screenshots (fully unique, unreplicable) > relevant AI-generated (never random filler) > stock. Exception: **AI goes to the top for graphs/graphics** ("they make really great graphics"). Never stock-photo-looking filler. Reduce AI friction by generating only the *featured* image with AI and filling in-body slots with real screenshots (SEMrush, Looker Studio reports) that show recent date ranges to prove recency.
- **Specs:** ~750px wide, 16:9 or square (be consistent sitewide). No text baked into the image. **Compress:** if over ~1MB, convert PNG -> WebP at ~70% quality (Photoshop, or Google "PNG to WebP converter," or tinyjpg.com). Real results: 537KB -> 32KB; 1.9MB -> 102KB, "looks exactly the same." Note: GoHighLevel and one of Wix/Squarespace don't accept WebP uploads.
- **File name + alt text:** rename the actual file to a plain description including the target keyword *before* uploading ("west-african-wedding-ceremony-toronto.jpg," not "1234.jpg") - Google reads the file name as a distinct signal. Set alt text to the same descriptive phrase, ~5-6 words. **Alt-text keyword rule:** use the exact keyword on roughly half (or fewer) of a page's images; never repeat the identical phrase sequentially across every image ("Newborn photographer Chicago 1/2/3/4"). Keep each page's images focused on that page's one keyword; differentiate per variant (each diamond shape gets shape-specific alt text, not all "diamond").
- **Batch images separately from writing.** The writing is fast (~15-45 min); sourcing/formatting/compressing images is what eats time (45 min to 1.5 hrs). Publish text-first, drop images in during a dedicated later block.
- **Canva copyright trap:** never export a bare unmodified stock element from Canva's library (violates their terms; Canva has demanded takedowns). Add something on top (title text, an outline) before exporting. Stick to a small, provable set of licensed sources (Pexels free + Adobe Stock paid) so licensing can be proven if challenged.
- Turn a post into an **infographic**, embed it, then cross-post to Pinterest; infographics are a content type other sites re-embed with credit, which becomes a backlink.

### 4.9 Titles and the search-intent title audit

- **Title the post as the literal question**, tightening only if the AI's version is generic ("SEO when building a website" -> "SEO when building a website, getting it right from day one"). Keyword toward the front; **≤60 characters, ideally under ~55**, or it gets cut off on Google/mobile. "The Ultimate Guide to X" framing is fine if it converts. This is "the psychology of it vs the SEO of it."
- **Never format a title/URL as "[Post Title] - [Target Keyword]"** ("What to Pick in Your Hospital Bag - Chicago Newborn Photographer"). "If it feels spammy, it probably is spammy." The keyword belongs to its own dedicated page.
- **The title-intent audit (Kira/Rank Week):** for every existing title, ask *"what would a real person actually Google to find this?"* Editorial/poetic titles that don't map to a real search query need reworking, even when the content is strong. Live: "When your strength tattoo feels like a lie" reworked toward "strength tattoo pros and cons"; "Soft is not the opposite of strong" flagged as a non-search. Titles that worked: "Are temporary tattoos safe?", "How to stay motivated on low energy days." "It's not that the titles suck, it's the intent of this piece of content."
- **Don't let a title/H1 render with a trailing "..." (truncation)** - Google literally can't read past the cutoff. Note that the on-page rendered title is often the H1, not the actual `<title>` tag; the real title tag shows on Google's results, browser tabs, and social shares. Fixing the wrong layer won't solve a truncation complaint.
- Differentiate near-duplicate topics by **angle/audience**, not just wording ("what to do when my wife has sexual avoidance" vs "...husband..."; or listicle vs explainer vs pros-and-cons).

### 4.10 Publishing mechanics + the internal-link publish loop

- **Categories: exactly one per post** (max 2 for a genuinely cross-cutting piece), never "Uncategorized." **5-10 categories total** sitewide; don't create categories until you've published ~10-20 posts. **Never use tags** ("never, ever, ever") - each tag spins up a thin near-empty archive page that bloats the site; delete existing ones.
- **URL slug = the core target keyword only** (not the long auto-generated slug, not filler words). CMS auto-lowercases and hyphenates.
- Set the SEO plugin's **focus keyphrase** to the exact target. Set **featured image + alt text**. **Disable comments sitewide** ("the only thing you'll get on blogs is spam"). Save as draft frequently; keep a backup copy outside the CMS.
- **Preview before publishing, always** - confirm internal links rendered and lists/code aren't rendering as unstyled paragraphs.
- **Publish as soon as it's ready** ("the sooner you publish, the sooner it indexes"). Don't wait for perfection given the ~3-month SEO lag: "no one's gonna see it yet anyway."
- **The internal-link publish loop** (integral to publishing a post; the fuller architecture lives in the on-page theme):
  - **Outbound:** every new post links to **3-5 other blog posts + 1 money page** (scale down to 2-3 + 1 for a brand-new post/site; 1 link is acceptable if you have nothing else yet). Use descriptive anchor text (never "click here"). Find targets with `site:yourdomain.com "keyword"` in Google.
  - **Inbound (the trick most people skip):** after publishing, run the same `site:` search to find **3 *different* older, already-indexed posts** and add a link from each pointing *into* the new post. Because Google already crawls those old pages, the new page gets discovered fast, "sometimes within an hour to two hours." "This is a trick that a lot of people don't talk about. It's honestly a huge advantage."
- **Speed indexing:** GSC gives **10 free URL-inspection "Request Indexing" submissions/day**; pages often index within ~2 hours. But manual requests are optional; Google usually finds new content on its own within ~3 weeks to a month. New-post indexing anywhere from ~2 hours to a week is normal; don't fixate on one post, keep publishing.

### 4.11 Cadence

- **1-2 posts/week, maximum.** One published post/week is "fantastic," two is "great." "I wouldn't do any more than two, it's going to get sloppy." Agency clients: **4-8 pieces every 28 days**, 2/week reserved for top-paying clients.
- **Never publish two on the same day** - space them (Monday/Thursday). Consistency of cadence beats which days.
- **New-site launch exception:** a brand-new site may batch **5-6 (or launch with 10)** at once, then drip the rest at 2/week. An already-live site should NEVER dump a dozen at once; Google reads high velocity on a steady site as spam-like instability. Historical lesson: sites that pushed to ~500 pages/week saw rankings drop as Google "retaliated."
- Higher sustained cadence (one member ran 5/week building a ~50-post hub) is acceptable only if quality holds and a defined goal justifies it. Framed as the exception, not the default. Topics realistically never run out: one seed term returns 40+ questions, another term 40 more.
- **Batch-write, paced-publish:** write/schedule in batches weeks ahead; decouple writing effort from publish cadence.
- **Don't chase perfect before publishing.** A post is never perfect, and polish doesn't guarantee ranking. Hit publish, revise later.

### 4.12 Repurposing & content-as-asset

- **Podcast/video -> blog:** never publish a raw transcript as an indexed page (a podcast is "a shotgun, you're not going to hit anything"; a blog is "laser focused"). Instead write a blog post answering an actually-searched question and reference the episode inside it as supporting authority ("Jim and I talked about this on our recent episode, here's what Jim said"). Feed the transcript to the LLM as training material: *"remember this for the future when I'm writing a blog post."* Only repurpose a video when it's tied to a real keyword/question (keyword first, blog second, video attached underneath).
- **Recurring support/onboarding question -> one-time blog post**, then send that link instead of repeating the walkthrough. Matt's team wrote "how to add and remove users from Meta Business Manager" once; it replaced a 30-60 min onboarding call for every new client and later earned organic traffic.
- **Free blog post -> longer paid guide** sold standalone (Jackie's curly-hair guide).
- **Blog -> video:** feed a post to ChatGPT for a video script, film it, post it (starts indexing, reaches more people). Fine and not duplicate content as long as you add more/different info than the post and it isn't AI-generated video.
- **Facebook-group / Reddit Q&A -> answer with a blog-post link**, not an inline reply or a bare homepage link. AI and Google now pull from local Facebook groups and Reddit ("real people, community chats").
- **Client-call mining:** run a 30-60 min recorded interview with a new client, feed the transcript into a standing reference doc the LLM pulls from for future posts in their voice. Batch multiple call transcripts into one file for hard-to-reach clients. "You literally look like a genius by asking your client the questions ChatGPT gives you."
- **Social redistribution** (post the link with ~100 words of your own framing on LinkedIn/X/Facebook/Reddit/Pinterest, never a bare link) doesn't move rankings directly but signals a legitimate active business and is an active experiment for AI-citation visibility. Never post links on Instagram/TikTok (no clickable links). Never publish the *same full content* on both your site and LinkedIn (LinkedIn has higher authority; Google can flag your copy as duplicate).

---

## PART 5 - The Two-Prompt Money-Page Rewrite Workflow

The Rank Week Day 3 workflow for rewriting an existing money page against its competitors. Distinct from the blog interview method, but same keyword/content logic.

**Prep (Day 2 audit):** for your money page + the top 3 organic competitors (Google the exact focus keyword incognito; skip ads/Reddit/Yelp/directories), run **pageaudit.com** and record into a shared sheet: word count, keyword occurrences, keyword density %, title tag, meta description, H1, H2/H3 structure, and pagespeed. Ignore the tool's overall score entirely.

**Prompt 1 (metadata rewrite):** paste your title tag, meta description, H1, H2s, and keyword density, then each competitor's column in the same row order. It returns an updated title tag, meta description, H1, and H2s. Copy the output into a separate doc. Confirm the keyword is present and front-loaded; swap in a better-testing variant if your data showed Google prefers it.

**Prompt 2 (full rewrite):** paste your entire existing page content; for each competitor, try pasting just their URL first (ChatGPT can sometimes read the live page), falling back to full content. Set the word-count target from competitor data (competitors at 2,500 and 2,300 -> target ~2,200). Answer any clarifying question it asks first.

*(The exact text of these prompts lives on heytony.ca/prompts and comes down after Rank Week; only their input/output behavior was demonstrated on calls.)*

**Rules:**
- **Never trust the AI's self-reported word/keyword count.** Live: it targeted 2,200 words and delivered ~1,700; targeted a 20-45 keyword band and delivered 13. Paste the output into **wordcounter.net** and land in the *same band* as competitors, not above or below.
- **Whatever the #1 competitor does, Google likes; mirror it, then slightly outdo it** ("level plus one"). Don't just add more (words, keyword repeats); over-optimizing past the competitor who outranks you can suppress rankings.
- **Cross-check every AI suggestion against the real SERP**, especially the *lowest-ranked* of the top 3 (if #3 ranks at 500 words, aim for ~600, not 3,000 because #1 has 3,000). "ChatGPT will bullshit you. It'll lie to you." Don't trust its guess at who your competitors are; verify by Googling the keyword.
- Refine one section at a time by pasting it back: *"can you rewrite this section to be more funny and personable"*; *"you forgot these H2 tags, write a couple paragraphs each"*; or deepen it with *"ask me five questions to write a better unique piece using my expertise"* - which folds the Day-1 interview method into the rewrite (produces stronger results than treating this output as final).
- Re-run the page-audit tool on the new draft before publishing.

**Money-page fix priority order:** (1) title tag, (2) meta description, (3) H1, keyword front-loaded in all three, then **wait 1-2 weeks** before touching on-page content further. Most of this "takes 5-10 minutes."

---

## Cross-Cutting Rules & Cautions

- **Never edit a page that is already ranking (#1-3, or even weakly on page 3).** "Don't edit any pages that are ranking, for the love of God." Even if it violates every rule (duplicate H1s, keyword stuffed 35x, thin content). You can't rank higher than #1, so touching it is pure downside. If #1 but not converting: tiny incremental edits only (one sentence, one button), never a full rewrite. Reinforce it externally instead (blog posts + internal links pointing in). Matt's own SEO page reached #1 after ~1 year on internal links alone, untouched.
- **Freshness-gaming:** Google sometimes suppresses a newly-published/edited page temporarily, then rechecks whether you panic-edit (which itself reads as a spam signal). Give a page **~1 month** after publishing before re-updating; don't knee-jerk to a dip within days.
- **Don't trust an AI's SEO opinions over the data** ("combine these two keywords," "is this a good idea"). ChatGPT tends to agree with whatever you propose and "will make shit up" about best practices. "You are the expert, you're doing the research." Validate any AI SEO claim against what's working for real accounts, human logic, and a second source. Use AI for drafting/orientation, never as the final decision-maker on keyword/architecture calls.
- **Copying a competitor's "trick" isn't automatically safe.** They may rank #1 despite keyword-stuffing/hidden text because their term has near-zero competition; replicating it risks a penalty on your site for no benefit. Correlation (they rank #1 and do X) is not causation (X is why).
- **Timelines:** SEO takes **3-6 months minimum** of consistent work; real inflection can land as late as month 12-14. Ranking within 2 weeks is "magic," not the norm. Most people quit after ~3 months without results; the long game wins. "SEO only works if you don't give up."
- **The human-vs-optimized spectrum (Kira):** every choice (title, hyphenation, grammar, density) sits on a line between fully-human voice and fully-optimized-but-robotic. There is no universal right answer; choose deliberately per business and brand values. "Learn the language before you decide to break it": execute every step exactly as taught first, deviate only once you know why.
- **Quantity-then-quality sequencing:** while working through a backlog, ship everything first; shift to per-post polish once you're on a steady rhythm.
- **Gut checks that override any plugin score:** *"Would my customers actually need this and read this? If yes, publish it."* And after drafting: *"Am I proud of this?"* Don't chase 100% on any audit tool; **80%+ is fine, 90% is fantastic**, and 100% doesn't mean better-optimized than 50%.

---

# Part III - On-Page SEO & Money Pages

The elements you control on the page itself: the keyword each page targets, its title tag, meta description, URL, headings, content depth, keyword usage, images, links, and conversion elements. Plus the two page types that make money (money pages) and the process that diagnoses why any page ranks or doesn't (audits). On-page content is Matt's stated #1 ranking factor, ranked above schema, backlinks, and technical backend. "It all goes back to one keyword per page."

---

## 1. The Governing Rules (these override every rule below)

These five principles decide when to apply everything else. When a specific rule below conflicts with one of these, these win.

### 1.1 One keyword per page. Always. No exceptions.

The single most-repeated rule in the entire curriculum. Every page and every blog post maps to exactly one keyword (a phrase can be 3-4 words, or one full question, or one tight cluster of variants, but one target). "If you have the exact same keyword on two different pages, Google looks at them and goes, well, I don't know which page to rank. Maybe I'm not going to rank either of them." Never combine multiple distinct services, cities, or topics onto one page.

A page can legitimately rank for many *phrasings* of that one intent (people search the same thing differently). That is not a violation. What breaks the rule is two pages chasing the identical or near-identical intent. Word-order and pluralization variants count as identical: "Chicago luxury newborn photographer" / "Chicago photographer newborn" / "Chicago newborn photography" is ONE topic, not three.

### 1.2 Never touch a page that is already ranking #1-#3.

The single most emphatic rule for money pages and audits. "Don't edit any pages that are ranking, for the love of God." Applies even when the page violates every other rule below: duplicate H1s, keyword stuffed 122 times, hidden overlay text, thin content, zero backlinks. You cannot rank higher than #1, so touching it is pure downside (losing the spot) with zero upside.

- **Evidence:** Ellen Mitchell (realtor) ranks #1 for a probate keyword using "probate" 122 times, two duplicate H1 tags, and hidden overlay text behind the nav. Verdict: leave it. Brett ranks #2 for "Miami probate Realtor" on a thin page with zero backlinks and zero referring domains. Leave it. Matt's own "SEO in Hamilton" service page hit #1 after ~1 year on 600-800 words of never-touched content, purely from internal links.
- **If it's #1 but converting at zero:** tiny incremental edits only (one sentence, one button), never a full rewrite. Wait for the rank to actually drop before touching anything larger.
- **The one carve-out:** UX and CTA polish stays fair game on a ranking page (button color, adding a contact link, layout reflow). The freeze applies only to content and structure that could shift rankings, not to conversion-element polish.
- **"Set and forget" has an expiration date.** A page holding #1 for years on little content can lose it once competitors escalate. That drop (not before) is the trigger to redo the competitive audit. Matt's website-design page held #1 for ~2 years on 600-800 words, then got outranked once competitors ran 2,300-2,500 words.

### 1.3 Match what is currently ranking, never a fixed absolute number.

Word count, keyword frequency, keyword density, and H2 count have no universal "ideal." The only real benchmark is whatever is currently ranking #1-#2-#3 for that specific keyword, and that benchmark moves as the competitive set changes. Google the exact keyword, pull the top 3, match or slightly exceed them.

The rule cuts in both directions. Over-optimization (too many words, too much keyword repetition, too many pages) is as common a failure as under-optimization. Sometimes the fix is to trim, sometimes to add depth, depending purely on what the top 3 actually show. "Most of the time, if you're not ranking, you're either doing too little or too much."

### 1.4 Do not chase 100% on any audit tool.

Passing an audit checklist is decoupled from being correctly optimized (or from ranking). 80%+ on a page-audit tool is fine; a 90% site-health score is "fantastic." Chasing the last flags reliably wastes time and can actively produce the cannibalization problem (a plugin telling you to hit a keyword N times regardless of what the #1 competitor does). "Sometimes you need that D to help you rank." The one exception: a paid SEO provider's own site faces a higher credibility bar from prospects than a typical client site does, so Matt keeps his own near-perfect on purpose.

### 1.5 On-page content is the #1 lever.

"If you write good content, then that matters a lot more than just having a schema markup on the page." Content depth and genuine expertise outrank technical polish. Fundamentals before tactics: fix a broken or thin page before adding location pages, channels, or new tools. "You can't optimize what doesn't exist."

---

## 2. On-Page Elements

### 2.1 Title Tags

The blue clickable headline in search results, the browser-tab text, and the title in social-share previews. Directly drives click-through rate; a bad title tag suppresses clicks. "Title tag" and "meta title" are used interchangeably.

| Rule | Spec |
|---|---|
| Length | **50-60 characters**, ideally under ~55. Longer gets truncated with "..." in the SERP. |
| Keyword position | Target keyword **at (or very near) the front** ("really important" / "highest-value tactic"). |
| Structure | Homepage = brand name + focus keyword. Every other page = **focus keyword first, brand name at the end** (or dropped). |
| Uniqueness | Unique per page. Duplicates come from running 2+ SEO plugins (see 4.6). |

- **Do** frame the title as the exact phrase or question people actually search. Good examples cited directly: *"How long should a URL be for SEO?"*, *"Custom WordPress Development,"* *"Fixing 404 Errors,"* *"Disadvantages of Market Mapping: A Comprehensive Guide,"* *"How to Edit Captions in Facebook Reels."*
- **Don't** write editorial or vague titles that map to no real search. Matt's own flagged bad example: *"10 Simple Ways to Improve Your Google Search Ranking"* ("not a well optimized title at all" because the keyword isn't framed as the phrase being searched). Never format a title as "[Post Title] - [Target Keyword]" ("if it feels spammy, it probably is spammy").
- **Don't** panic when Google strips the trailing brand name from the SERP display. That is Google's rendering choice, not a defect; the brand name is still in your HTML (verify with the Detailed SEO extension).
- **AI prompt:** *"Write me a title tag for this page under 60 characters. The focus keyword is [X]."* Or *"five compelling title tag options for this, make sure it includes [keyword]"* and pick the best.
- **Guardrail:** if a page already ranks (or is #1) for a keyword, never strip that exact keyword out of the title while "improving" it. Edit around it, never delete it.

### 2.2 Meta Descriptions

The descriptive snippet under the blue title. Not a direct ranking factor, but it is your pitch to win the click over competing results, so it drives CTR ("the billboard saying click me instead of your competitors").

| Rule | Spec |
|---|---|
| Length | Roughly **120-155 characters** before truncation (guidance clustered at 140-145 and 155-160; a 124-char example was called "kind of where we want it to be"). Precision matters less now: Google increasingly rewrites descriptions on its own, and Yoast cuts them shorter than it used to. |
| Keyword | Include the target keyword **near the front**. |
| Uniqueness | **Unique per page**, never duplicated across the site (duplicates get flagged by audit tools; a common Yoast template bug auto-inserts the same boilerplate into every post). |

- **Do** write it benefit-forward, as an independent sales pitch that names specific services or differentiators and previews the payoff. Never a copy of the title tag.
- **Don't** force a secondary keyword in just because a tool keeps suggesting it ("it'll come up naturally").
- **Don't** rely on an auto-pulled excerpt. Shopify in particular pulls an arbitrary visible text block if none is set (one real case pulled EU product-safety warning copy, a dead giveaway the field was never filled).
- **CTR fix workflow:** ranking well but near-zero clicks almost always traces to a missing or weak meta description and/or an uncompelling title. Write one that includes the keyword and gives a clear, specific preview (for "size of Facebook cover photo," promise the exact dimensions plus a click for full details). First confirm the impressions are current, not a stale spike from months ago.
- **AI prompt:** *"Write me a killer, compelling, click-worthy meta description for this page."* (Generate ~5, pick the best.)

### 2.3 URLs / Slugs

Should reflect the title and tell users what the page is about.

- **Include the focus keyword.** Homepage is the exception (just the bare root domain, already correct, do not "optimize" it further).
- **No character limit, but shorter performs better.** Every page needs a unique URL.
- **Keep the slug short even when the H1 is long.** Put the long natural-language phrase in the H1/title (e.g. "Bookkeeping services in St. Petersburg, Florida for small businesses"), but keep the URL to the core keyword (`/services/bookkeeping`). Matt's own SEO page ranks #1 in Hamilton with "Hamilton" appearing nowhere in the URL, H1, or H2, proof a hard local keyword does not require URL keyword-stuffing.
- **Bad example** (stuffing): `balamedia.ca/hamilton-website-designers-web-design-hamilton`, should have been trimmed to `hamilton-website-designers`. **Good example:** `sociallyinfused.com/services/website-design` (simple, hierarchical, parent → child).
- **Never** put "near me" or "near you" in a URL or on-page copy. Google geolocates the searcher automatically; it does nothing for rankings and reads as "amateur SEO."
- **Never** put a year in an evergreen page's URL (e.g. "best-dental-services-2025"). It signals the page is tied to that year and goes stale. Keep the URL static and update the on-page year in place.
- **URL-change decision framework (check all three before touching a slug):** is it ranking? does it get traffic? does it have backlinks? Change the slug only if **all three** come back negative. Any single "yes" and you leave it: a changed URL is a brand-new page to Google ("new kid at school, nobody knows who they are"), rankings may not carry over, and backlinks to the old URL go void. Even a textbook-correct 301 does not always fully preserve traffic. "Update this with extreme caution."

### 2.4 Headings (H1-H6)

The book analogy: H1 = book title (the page's one topic / target keyword), H2 = chapter titles (subtopics reinforcing the H1), H3 = subheadings within a chapter. Keywords are weighted heavier in headings than in body copy.

**Core rules:**
- **Exactly one H1 per page**, and it must be the **literal first heading in the page's DOM order** (not just visually biggest, and not buried under a hero or a run of H3s). Google reads top-down. "You don't have a secondary title before the book starts."
- **The H1 must contain the exact target keyword and no brand name.** The brand name is already in the title tag and URL; you rank for it automatically. (Brand name in the H1 is more acceptable only on the homepage of a brand-new business establishing recognition.)
- **Never skip a level going down** (H1 straight to H3, or H2 to H4, trips you up). Skipping *up* a level (H3 back to H2) is fine. "If you skip a step going down the stairs, you're gonna trip. But if you skip a step going up, you're fine."
- **H2s must directly support the H1's specific topic**, not be generic value-prop or marketing lines. Demote flowery marketing sentences to plain paragraph text.
- **H2 count:** use **one more H2 than the top-ranking competitor**. 5-10 H2s is "totally fine" for a normal article. Do not drastically overshoot (top page has 50, going to 200 is way over-optimizing).
- **Avoid H4-H6 in practice.** Convert unnecessary H4s to plain paragraph text. Footer titles above menu columns should be H4 or smaller (or plain text), never H1/H2/H3.
- **Semantic tag is independent of visual size.** You can style an H1 small via CSS (the "split H1" trick: real keyword phrase stays inside a small `<h1>`, a punchier tagline sits beside it as a larger H2). Never use a graphic or image as the H1 (Google can't read baked-in image text). Never fake a heading with a styled `<div>` or bolded paragraph.
- **Turn generic step labels into keyword-carrying headings:** "Step 1 / Step 2" adds nothing. Use the action itself ("Clean the door gaskets").

**Duplicate / mis-tagged H1 fixes.** The two-path decision, applied to every extra heading on the page ("does this support what the page is about?"):
- **If it is real topical content mis-tagged as H1:** downgrade the tag to H2. Keep the copy, just fix the level.
- **If it is NOT real content** (a hero box, CTA, testimonial quote, tagline, logo, or client-name callout): strip the heading tag entirely and convert to plain styled paragraph text. Do not even demote to H2.

**Common duplicate-H1 sources to check:**
- **Mobile/desktop block duplication** (Avada, Wix, Squarespace, GoHighLevel, Shopify): a builder encourages duplicating a section and hiding one copy per breakpoint, loading the same heading twice. Fix by building one truly responsive block with per-breakpoint design settings, never by duplicating the block. (Matt's own "website design in Hamilton" page dropped #1 → #7 partly from a mobile/desktop dual-H1 hack; he flags this as gaming the system that "you won't get results" from.)
- **Popup / promo elements** carrying their own heading tag: change the popup's heading to plain paragraph, restyle visually so nothing changes for the visitor.
- **Theme injection:** Avada's Page Title Bar module auto-generates an empty duplicate H1; Kajabi puts a blog-index title above every post's H1; Shopify wires the H1 into the site logo; developers commonly mark every heading H1 by default.
- **Pressing Enter mid-headline** creates two H1 tags. Force the line break with container padding, not a hard return. A heading that wraps to two visual lines can also register as two.
- **Hidden text** (white-on-white) to stuff a keyword invisibly is a cloaking pattern Google devalues; remove on sight.

**Diagnostic tools for headings:** the Detailed SEO or Page Audit Chrome extension shows the live H1/H2/H3 structure and count instantly (use "Copy All Headings"). View Page Source + Ctrl/Cmd-F "h1" locates where a duplicate is injected. A generic "too many H1s" flag lacks specifics; a dedicated heading extension lists each one individually (one case found 13 H1s firing from the logo, signage graphics, and animated elements).

### 2.5 Content Quality, Word Count & Depth

Content is the foundational element. Well-written, genuinely useful, long-form content that answers a question or solves a problem ranks higher and keeps users on the page longer.

**Word count is competitor-relative, never a fixed target.** Google the exact keyword, pull the top 3 ranking pages, and match their count or add roughly **100-200 words (~10%) more**. "I want to do what is proven that Google likes. I just want to do it like 0.0001% more." This is proportional matching, not license to maximize.

| Situation | Rough anchor |
|---|---|
| Program baseline | 750-1,500 words (later refined to 800-1,000) |
| Normal blog post floor | ~500-800 words |
| Zero-volume / zero-difficulty keyword | ~400-500 words is plenty, no need to go deep |
| Ceiling to watch | ~2,000 words on a page; a homepage measured at 10,000 words (2,000 inside heading tags alone) is over-optimized |

- **Over-optimization by length is a common live failure.** A page far longer than the actual top rankers gets told to trim, not add. A 2,000-word page outranked a 3,200-word page from the same niche once intent and formatting matched better. Real competitor pages for one keyword ranged from ~500 to 2,500 words in the same SERP, proving word count itself is not the ranking driver.
- **Measure body content only.** Exclude footer, nav, and sidebar boilerplate.
- **Verify counts manually.** Never trust a single tool. Extension vs. extension vs. a manual copy-paste into wordcounter.net can differ by hundreds of words (one page read 2,000 / 1,900 / 2,400 across three sources). Inflation comes from popups, review-widget text, mobile-version text counted twice, currency/country-selector text, or a plugin injecting hidden duplicate text on every page. If a tool's count is wildly higher than what you can visually count, view the page source.
- **Longer should mean more complete, not padded.** Do not pad with fluff to match a bigger competitor whose length is mostly filler.
- **Cut vague, generic brand copy that does nothing.** Matt's test: if an unrelated business in a different niche could reuse the exact line verbatim ("every woman is uniquely beautiful," "and more"), it is too generic to keep.

### 2.6 Keyword Density & Placement

**No fixed density target exists.** Match the current top rankers, "level plus one."

- **Placement checklist (keyword should appear in):** product/page name (= H1), title tag, meta description, the **first 100 words** of copy, naturally through the body, **at least one H2**, an FAQ, image alt text, and the image file name. Put it **as close to the front as possible** in the title, meta, and H1.
- **Split the phrase into components and count each separately** across the top 3 competitors (e.g. count the service term and the location term individually, not just the literal full phrase). Feed the counts into a spreadsheet, then match or slightly exceed the top competitor ("plus one"). Match the exact phrasing competitors use, not a close synonym (Matt lost "website design" visibility because both competitors beating him used "web design").
- **Red flag:** if your density sits meaningfully higher than competitors', you are almost certainly over-optimized. Matt's own case: 5.04% density (keyword used 35 times) vs. competitors' 1.76% and 0.9%, nearly 5x higher, correlated with his page falling #1 → #9. "Higher density does not equal better rankings. Google increasingly interprets heavy keyword repetition as over-optimization."
- **Low-difficulty and local keywords often need only 2-3 mentions**, not 10-12, to hit the top (one case ranked top-3 for "mechanic" on 3 mentions vs. 0 for all three competitors).
- **Ignore density scoring tools for long-tail / question content.** Yoast and Rank Math are geared toward 3-4-word short-tail phrases and actively work against full-question posts. For a question post the literal question IS the keyword; it appears naturally through writing the answer (~3-4 times) with no deliberate insertion. Do not blindly copy a competitor's keyword-stuffing just because they rank: if their keyword has near-zero competition they did not need to stuff, and copying it risks a penalty on your own site for no benefit.
- **Absurd density readings (600%+, "923%")** mean the keyword field was left blank and the tool defaulted to the domain name. Fix the input, do not trust the number.

### 2.7 Readability

How easily anyone down to grade-school level can follow the writing. Simplifying widens your addressable audience, which is a wider ranking net, not just an accessibility nicety.

- **Target 7th-8th grade** ("if you can't explain it to a kid, you can't explain it"; the model for Matt's own book).
- **Paragraphs of 2-3 sentences; vary sentence length** (drives the Flesch/ease score). Avoid industry jargon that forces a reader to "open a dictionary" ("help desk" → "how do I fix my computer").
- **Do not chase an all-green Yoast/readability score.** The algorithm is "not 100% accurate." Ignore transition-word-count complaints, "key phrase in introduction," and "key phrase density" checks for question content. Yoast flags a page when >25% of sentences run over 20 words (one case flagged at 30.6% vs. the 25% max); use it as a directional prompt to tighten run-ons, not a mandate.

### 2.8 Images & Alt Text

Images improve time-on-page, trust, conversion, and readability (they break up walls of text).

**Density:** roughly **1 image every 200-300 words**, minimum **4 per post**, ideally one per H2 section. Every post needs at least a featured image. Break the 200-word rule where an image does not make sense for a section, compensating with heading breaks.

**Sourcing priority:** real/own photography > AI-generated > stock (real photos build trust; "everyone is a little on high alert on the Internet, nervous about scams"). Exception: for graphs and infographics specifically, AI goes to the top of the list. Never use stock-looking imagery on a page meant to convey a real team or product. AI and stock images are SEO-neutral with proper alt text; the only real concern is brand fit.

**File names and format:**
- **Rename the actual file before upload** to a keyword-descriptive name (4-5 words, e.g. `black-flame-paddle-shirt.jpg`, not `1234.jpg`). Google reads the literal file name as a distinct signal.
- **Use WebP / next-gen formats** (same visual quality as JPEG/PNG at roughly 1/10th the file size). Featured/OG image spec: 1200 x 628.

**Alt text:**
- **Formula:** identify the medium (photo / illustration / graphic / infographic) + be descriptive. Quality ladder: "pancakes" (terrible) → "blueberry pancakes" (thin) → "stack of blueberry pancakes in a kitchen" (good) → "illustration of a stack of blueberry pancakes in a kitchen" (best, if it really is an illustration).
- **Every image needs alt text; none empty.** Alt text serves screen-reader users first, then search engines, then acts as fallback text.
- **Include the target keyword only where it fits naturally, and on at most half the images on a page.** Never repeat the identical keyword phrase sequentially across every image ("Newborn photographer Chicago 1/2/3/4"). Make it specific per variant: every diamond-shape photo (round, cushion, pear, emerald) getting identical alt text "diamond" is a flagged missed opportunity; use shape-specific alt text and file names instead.
- **Proofread the string.** Missing spaces between words break the attribute.
- **AI prompt:** upload the image and ask *"give me an SEO friendly title in alt text for this image."*

### 2.9 Video

- **Never self-host video.** Embed via YouTube or Vimeo even on a strong server ("even then YouTube is just better"). Google indexes one video per page, and an embed still surfaces in search results.
- Video breaks content into digestible sections and increases dwell time (a positive signal). Vimeo embeds still get indexed; the choice is a UX/aesthetics tradeoff, not an SEO penalty.
- **Not required to rank.** Weigh a hero autoplay video's appeal against its page-speed and mobile cost: "is that video appealing to you, or is it appealing to a person looking to hire you?" Embed the matching video *inside* the corresponding blog post (add an H2 like "How to Clean X - Video"), only worth doing when the underlying video already performs.

### 2.10 FAQ Blocks

- **Plain question-then-answer text directly on the page.** Mark each question as **H2** (or plain question-then-answer, no literal "Q:"/"A:" prefix). Answer directly and briefly, then link out to the fuller blog post for depth (FAQ → blog → money page chain).
- **Cap at 3-4 FAQs per page.** 12 on one page is too many; split onto a dedicated page. Each standalone FAQ question can become its own blog post.
- **Never hide FAQs behind an accordion/toggle/dropdown** for genuinely important SEO content. It adds parsing friction for Google and AI crawlers. Supplementary technical detail (product specs) inside an accordion is fine. "Well, if this information is so important, why is it hidden in a box?"
- **Put an FAQ tied to that page's one focus keyword on every page**, not one central FAQ page. "If you have all your FAQs on one page, what are we ranking for?" Never repeat identical FAQ text verbatim across pages.
- A generic FAQ block bolted onto every post after the CTA does not itself help; the bar is "is this actually helpful to a human being?"

### 2.11 Internal Linking (the core on-page growth lever)

The most-repeated fix across every call and one of Matt's highest-performing tactics. "Internal links for the HeyTony site were the biggest factor and the biggest differentiator in why things were ranking really well." "The more internal links you build to a page, the more Google will understand this page is important."

- **Evidence:** HeyTony's own SEO service page climbed from **position 13 to #1** over ~3-4 years on nothing but accumulating internal links from dozens of blog posts, content otherwise untouched. Matt got a page to **rank #1 in 3 hours** using internal linking alone (witnessed live). One member ranked a page #1 for a competitive keyword using internal linking only, after a year of the page sitting dormant.

**The two rules ("your entire internal linking strategy, done"):**
1. **Every new blog post links out to 3-5 other blog posts + 1 money page** (scale to 3 other-post links if the post is short, or fewer for a brand-new site's first post). "Doing half of Google's work for them."
2. **Every time you publish, go back and add a link into the new post from 3 older, already-indexed posts** (different ones than the new post links to), so the new page has inbound links from day one. Because Google already trusts and crawls the old pages, this gets the new page discovered and indexed fast, sometimes within an hour or two. "This is something that experts even forget to do."

**Mechanics:**
- **Descriptive anchor text that names the destination, always.** Never "here," "learn more," "click here," "website," or "get your copy here." Vary the anchor across links pointing at the same money page ("our SEO services," "done-for-you SEO services," "professional SEO services"); repeating the identical anchor reads as manipulation.
- **In-body contextual links, placed higher up, outperform** a "related posts" block dumped at the bottom. Best practice is a mix, weighted toward inline.
- **Direction rule for money pages:** blog posts link TO money pages; money pages link OUT to blog and external sources but do not link out to blog content "as a feature." Money pages reference at most 2-3 essential resource pages. A blog post's only job is sometimes just passing internal-link authority to the money page (it does not always need to rank itself).
- **Link ceiling:** 10-20 links per page (some framing 5-10 at ~1,000 words); hard max 50-100 before it reads as spam. "You'll actually get more out of doing less."
- **Use the CMS's existing-page link picker, never a raw pasted URL**, when linking to your own pages, so the link auto-updates if that page's URL ever changes.
- **Find targets** with `site:yourdomain.com "keyword"` (no space after the colon, phrase in quotes): run once pre-publish to find 3 pages to link the new post TO, once post-publish to find 3 different pages to add links FROM.
- **New sites:** just publish; once you hit ~10-20 posts, go back and add ~3 internal links per post. Retroactively added links still work but take longer to show effect than links present at publish time.
- **Crawl-depth tie-in:** get every page you want ranked to **≤3 clicks from the homepage** (homepage load = 0 clicks; nav/homepage-module links = 1 click). 4+ clicks is the danger zone: "the harder it is for a human to find your page, the less likely Google will care about it." Fix by adding homepage service/recent-post modules and by ensuring the money page is reachable from nav, not buried.

**AI prompts for internal linking:**
> "Using my sitemap, give me three internal linking opportunities from this blog post [using existing text]." Follow-up: "Anchor text, where to place it, give me a sentence where I can add this."

> "I'm looking for 3 incoming internal linking opportunities to this service/product page: [LINK]. Find me 3 relevant opportunities from my sitemap pasted below. [PASTE SITEMAP]"

### 2.12 External Linking

- **At least 1 external link per page** (blog: 1-2, at or near the top, within the first few paragraphs). Zero outbound links reads to Google's crawler as a dead end: "when Google's crawl bots go from another site to yours, it stops there, it can't move on." Cite sources for stats and claims by hyperlinking the exact phrase to the study, not a separate references list.
- **Never link to a direct competitor, for any reason.** Naming, praising, or comparing them in a table is fine; hyperlinking is not. "The number one rule with linking is never link to a competitor."
- **On money pages and the homepage, external-link to your own legitimacy profiles** (Chamber of Commerce, Trustpilot, Glassdoor) rather than an unrelated site. Never link out to a page targeting the same keyword you're trying to rank for (it hands a competitor link equity toward your target). Write the post first, then place external links to sources clearly unrelated to your own target keyword.
- **The "best-of" list technique:** write "best [service] companies in [city]" naming every competitor (say genuinely positive things), but never hyperlink any of them; internally link the page hard toward your own converting pages. You do not have to include your own company. Ranks for "who is the best [X]" / "should I hire [X]" searches.
- Nuance: this is strongest for blog content. Matt's own core SEO service page has zero external links and still ranks; his web-design page does link out. Check what competitors do on their equivalent money pages. Contact and About pages are exempt from linking minimums.

### 2.13 Keyword Cannibalization

**Definition:** more than one page on your own site ranking or competing for the same keyword. Google reliably surfaces only one page per domain per query, so unmanaged overlap costs you the ranking on both. It is about the page's *topic*, not about link destinations (many different blog posts can all link to the same money page without cannibalizing, as long as each post's own topic differs).

- **Same exact keyword or its natural variant on two pages = cannibalization.** Word-order and pluralization variants count as identical.
- **Adding a location makes it a new keyword.** "We buy junk cars, Dallas" and "...Houston" are separate pages, not cannibalization, provided the location content is genuinely substantive (not a template with only the city swapped).
- **Not cannibalization:** a collection/category page vs. a blog post targeting a distinctly longer-tail keyword ("natural granola" collection vs. "benefits of natural granola" post); product-comparison pages (Botox vs. Dysport vs. Xeomin) as their own consideration-stage content type; two genuinely different keyword targets on separate pages ("small business bookkeeping services" vol 40 vs. "outsourced accounting services" vol 440).
- **A blog post's target keyword should never be your homepage's primary keyword.** Use secondary/variant keywords in blog content to avoid self-cannibalizing the homepage.
- **Fixes:** consolidate the two pages into one longer comprehensive piece and 301 the weaker into the stronger; or rewrite each page's tags and content to target distinct variants (or distinct format/angle: a listicle "12 ways to use honeysuckle perfume" vs. an explainer "what's in honeysuckle roll-on"). To de-cannibalize, paste both pages' full content into an LLM and ask it to compare them and recommend what to change on each so they stop competing.
- **The exception:** if a blog post and a service page are already both ranking for the same keyword and both converting, leave it alone. Do not "fix" a technically-cannibalizing setup that is delivering.
- **Never A/B test two pages for the same keyword** (that IS cannibalization). Test variants sequentially over time.
- **Detection tools:** the Money Page Tool (reports which of your own pages ranks #1 for a keyword), keywordconflict.com, and the Insiders Keyword Conflict Detector / Cannibalized Keywords Scanner (default ~50-page scan, adjustable toward 500; not 100% accurate). Cross-check flagged phantom URLs against the sitemap and robots.txt; if absent from both they are likely redirect artifacts, not real pages.

---

## 3. Money Pages

### 3.1 Definition

**A money page is any page a visitor lands on when they are ready to buy or hire.** Product pages, service pages, collection pages, and location pages are all money pages, and they all get the same discipline. The homepage counts as a money page if there is no dedicated page. Blog posts, contact pages, and booking/appointment pages are NOT money pages ("those pages don't rank"), and a third-party booking tool is explicitly not your money page even though your money page is allowed to link out to one. **The money page is the page that sends a visitor TO the intake form; the form itself is not the money page.** If stuck, ask an LLM directly: *"I am a realtor, what would be my money page?"*

Examples: dentist → dental implants / Invisalign; realtor → "homes for sale in Scottsdale"; plumber → 24-hour emergency page; hot sauce co. → "buy ghost pepper hot sauce" / a collection; magician → one page per event type; ecommerce → collection or product page. A single business can and should run multiple money pages (one per service/offer), each pointing to the same lead form.

### 3.2 Homepage vs. Money Page Targeting

Targeting depends on the business model:
- **Local / service business:** target `[service] + [city]` on the homepage (e.g. "dentist in Hamilton," "Residential Roofing in Cincinnati"). The single service that makes the most revenue becomes the homepage's target keyword; every other service gets its own dedicated page.
- **Ecommerce / content / national site:** do NOT target the homepage for one keyword. Ranking happens on lower pages (collections, products, blog posts); the homepage just needs to make a visitor understand what the site is once they land from an entry page. Give each featured product its own homepage section with descriptive text and push actual ranking effort onto individual collection/product pages.
- **National / virtual with no physical base:** optimize the homepage for the single largest nearby metro, then spin out location pages for smaller markets.
- **If your homepage naturally outranks your intended money page** for the target term, stop fighting it: treat the homepage AS the money page (add the keyword/topic there) and point future blog links at the homepage. Jessa's case: her homepage ranked #2 for "online intimacy course for couples" while the dedicated course page ranked nowhere; the fix was to promote the course page to homepage (WP Settings → Reading) and monitor, or accept the homepage as the money page.
- **About, contact, and blog category/taxonomy pages should not be keyword-targeted.** They behave like the homepage, are not expected to independently rank, and duplicate H1s or SEO gaps on category pages usually do not matter (they were never going to rank anyway).

### 3.3 Money Page Structure

The canonical service-business page skeleton (copy first, then layout, message dictates section structure). One section = one H2 = one topic, alternating background tints so each reads distinct ("like a slide deck, one idea per slide"). Most important messages near the top, because "the longer it is, the less likely people reach the bottom."

1. **Hero:** H1 (focus keyword + city for a local page, descriptive/plain language) + supporting subhead + one CTA button, all visible with zero scrolling. A trust signal (stars/stat/logos) in or right below the hero.
2. **Trust row:** pick ~3 of years of experience, # of happy clients, 5-star rating, licensed/insured, awards, association logos.
3. **About / intro:** what you do, how, who you serve; an audience-identifier layout (icon boxes per persona) so visitors self-identify.
4. **Services/products overview:** brief intro to each, each linking to its own dedicated page (two-tier IA: overview/parent page for navigation, individual/child pages where you go hard on SEO per service).
5. **Testimonials:** pasted real reviews or a Google reviews widget.
6. **"How it works" / process:** plain numbered steps of what happens after they book (defuses first-time-buyer anxiety).
7. **FAQ** tied to that page's focus keyword.
8. **Final CTA** at the very bottom of every page (a visitor who scrolls all the way down must still have a next action).

Build the body content with lists, tables, and explicit numbered steps. Shopify collection-page structure specifically ("the biggest missed opportunity when I look at a Shopify store"): intro sentence(s) → product grid → long blog-length paragraphs with images underneath, covering the collection in depth. On a collection page put informational copy BELOW the grid, since someone landing there is ready to buy, not read.

### 3.4 CTAs & Conversion Elements

- **One primary CTA per page.** Solid, bold, single high-contrast color. Any secondary CTA (call vs. form) must visually recede (outline/neutral). "If people have too many choices, they sometimes just choose not to make any choice." Repeated live fix: 5 competing CTAs (Book Now / Call Now / Email Now / WhatsApp Now / Inquire Now) trimmed to one.
- **Do not stop at one CTA top and one bottom.** Add 2-3 more spaced through the body so a reader convinced mid-page can act immediately.
- **CTA copy names the specific action.** Never a bare "Learn more," "Contact Us," or "Book Today." Use "Book a massage appointment," "Start your logo design," "Start your corporate video today." Upgrade keyword-bearing versions where natural: "Shop Now" → "Shop Organic Dog Treats."
- **Phone numbers and emails must be tap-to-call / clickable everywhere**, especially mobile; anchor a labeled clickable number at the bottom of the screen for a mobile-heavy audience.
- **Naming:** call the pricing page "Pricing," not a euphemism like "Investment" (people search "[service] pricing"). Avoid cursive/script for anything read quickly.
- **Reviews belong on every money page**, not just a reviews page. Hand-paste 2-3 real reviews as plain text (Google cannot read text in a screenshot image), rotating which reviews appear on which page so the same text is not repeated everywhere. Put location-specific testimonials only on the matching location page. Never use a review-carousel plugin (found adding ~1,000 words of markup and hurting load; users scroll past carousels).
- **Never use an auto-rotating slider or carousel as a hero.** A carousel that freezes on hover hid a page's own H1 from most visitors; every load still fetches every slide's image. Replace with one static hero (real people/crew) plus persistent descriptive text. "I fucking hate carousels. People don't stick around for it."
- Quote/inquiry forms: keep one dedicated "Get a Quote" page, but also add a small inline quote form (name, phone, email, short message) on each product/service page (more on-page conversion signal, mirrors competitors).

### 3.5 Location Pages (as money pages)

The most fully-worked money-page type. **One page = one keyword = one service = one location.** Never build a page for the same city targeting two services.

- **Home-base exception:** your flagship market can carry a separate page per service ("Chicago Newborn Photographer" AND "Chicago Family Photographer"). Every satellite location gets only ONE service page (whichever service is easiest to rank there); mention other services in passing.
- **Prioritize smaller towns/suburbs over the big nearby city.** Almost nobody targets them, and searchers type their specific town, not a regional abbreviation. A location page usually cannot outrank a genuine local competitor's homepage (their most-backlinked page) without dedicated backlinks, so retarget adjacent smaller markets instead of fighting head-on.
- **Keyword-first title/H1/meta:** "Sell your house fast, Delaware, Ohio," not "Looking to sell your Delaware home quickly." Match the abbreviation people actually type (searchers type "St. Lucie," not "Saint Lucie").
- **Genuinely unique content per location, not a template with the city swapped** (the real cannibalization risk). Reference real local landmarks, venues, neighborhoods, delivery specifics, seasonal color. For non-delivery/remote businesses, anchor in local hooks (nearest hospitals, grocery stores, gyms, trails). Multiplying pages is not the risk; duplicate/templated copy across them is.
- **Do not build every location x service combination "just in case"** (one case would have been 66 pages: 25 cities x 6 event types). Build one page per location with sections per service, and run keyword research to confirm a specific combo genuinely gets searched before building a dedicated combo page. "Pigs get fat and hogs get slaughtered."
- **Word count:** 400-500 words is fine for a low-competition term; if competitive, audit who ranks and match their depth (up to ~2,000). Always organize it so a human reader can consume it and decide to hire you.
- **City-size sizing rule:** a ~500,000-population city (Hamilton, ~15,000 small businesses) justifies targeting the whole city; a 3-4 million metro (Toronto) is too big, target a neighborhood instead.
- **Zero-volume location keywords are still worth a page** if difficulty is near-zero (tools under-report hyper-local terms). Roughly 15% of searches are brand-new each day.

### 3.6 The "Don't Touch a Ranking Money Page" Rule Applied

(See Governing Rule 1.2.) The money-page-specific corollary: **redesign scope is entirely conditioned on ranking status.** Strong existing rankings → preserve verbiage, keywords, and URLs; restructure visually only. Weak or no rankings → free to rewrite from scratch. A "technically broken" money page (duplicate H1s, keyword stuffing, thin content, zero backlinks) should stay broken if it ranks and converts; fixing it "for correctness" risks breaking what drives the business. UX/CTA polish remains the one safe category.

---

## 4. Auditing a Page

### 4.1 Audit Philosophy: what to read, what to ignore

When working a money page, **ignore the audit tool's overall composite score entirely** and read only three things: (a) how many times the target keyword is used vs. competitors, (b) total word count vs. competitors, (c) keyword density vs. competitors. "Ignore everything else. It's there. It's like nothing. Zero."

- **Not every flagged issue needs fixing.** Before fixing anything, ask: do I actually want this page found, indexed, and ranking? Thank-you pages, ad landing pages, contact pages, category/archive pages, and funnel pages routinely trigger "orphan page," "low word count," or similar flags, and that is often intentional and fine.
- **Priority within an audit:** fix red/serious issues first, starting with the lowest-count ones to build momentum. Broken links and missing alt text outrank a title-tag length overage ("having broken links is way worse than having too many characters in your title"). Fix 5-10 issues per week, not the whole report at once (overwhelm is the #1 cause of people quitting).
- **Never run a site-wide audit against a site still mid-construction** (results are dominated by temporary build errors).
- **Cross-check tool output against a non-caching source before "fixing."** Expect a 12+ hour lag before a full site-audit tool re-crawls a fix; an apparent ranking dip right after a fix is often just caching, not a regression.

### 4.2 The 5-Step Money Page Audit (pageaudit.com)

The homework workflow, run for your own money page plus your top 3 competitors, into one shared spreadsheet:

1. Copy the audit spreadsheet. Enter your money-page URL + your one **focus keyword** (never "near me," never a generic un-localized term).
2. **pageaudit.com** → paste URL + keyword → Analyze. **Ignore the overall %.**
3. **Content tab:** copy word count, keyword occurrences, keyword density into the sheet.
4. **Metadata tab:** copy the title tag and meta description.
5. **Chrome extension ("PA" icon)** as the fallback when a page returns all "NA" (usually bot-blocked): surfaces title tag, meta description, H1/H2/H3 (use "Copy All Headings"), word count, and keyword occurrence/density. If it does not populate, wait ~30 seconds or scroll to the bottom then back (lazy-load).
6. **pagespeed.web.dev** on the money-page URL itself (mobile + desktop scores).
7. **Repeat identically for the top 3 organic competitors:** Google the exact focus keyword in incognito, skip sponsored/ad results, skip Reddit/Yelp/IG, skip directories/aggregators, take the next 3 genuine ranking business sites into the same sheet.
8. Do NOT rewrite yet; this is prep for the rewrite (4.4).

pageaudit.com cost ~$30,000-$40,000 to build and is given away free. Word count differs slightly between pageaudit.com and its extension; anything within ~100-200 words is close enough.

### 4.3 The Competitor-Benchmark Method (the core diagnostic)

The single most-repeated diagnostic-and-fix technique. Never optimize to a fixed number; always benchmark against whoever currently ranks #1-#3 for your exact keyword, then match or slightly exceed.

- **Word count:** match the top 3 or add ~100-200 words. Trim if you overshoot.
- **Keyword frequency:** split the phrase into components, count each separately across the top 3, match or "plus one."
- **Heading count:** pull your H1/H2 outline with an extension, use one more H2 than the top competitor.
- **Verify competitor data by eye, not just by tool.** Tool-reported competitor word counts can be flatly wrong (one reported "1300 words" was manually 174; another set of 2,200-3,400 could not be located on the actual page, suspected hidden/popup content). A review-carousel plugin can inflate a real page to 3,000-4,000 phantom words. Sanity-check anything unusual before setting your own target.
- **The full "why doesn't it rank" comparison** (once on-page signals check out): who ranks #1-3, their backlink/referring-domain count, how often and where they use the keyword, whether their content is simply better, whether they use a top summary or key-takeaways block, and how many internal links point at their page.
- **Diagnostic default:** "if you're not ranking, you're either doing too little or too much." Both under- and over-optimization are equally common; always resolve against the actual top 3, never a fixed rule.

### 4.4 The Money Page Rewrite (exact prompts)

**Money Page Doctor** (Insiders tool): paste a money-page/homepage URL; in ~10 seconds it infers the target keyword (double-checking against on-page content), identifies competitors, checks their title/H1/density usage, and flags gaps ("keyword mismatch: competitors appear to target [X] instead," "content is thin," "density too low/high," "blog post detected, competitors ranking are dedicated service pages, consider building one"), or shows a "you're already ranking #1" banner. Always check where you actually rank before acting on any recommendation: if already ranking well (e.g. #2), do not touch the page just because it flags a gap vs. #1.

**Competitor gap analysis:** paste the gap-analysis prompt, then paste your entire audit spreadsheet (your data + all competitor columns) under it. Output analyzes across up to 8 dimensions (title tag, meta description, H1, H2/H3 structure, word count, keyword density, page speed, trust signals), each meaningful gap getting an exact fix with a priority flag (red = do first / yellow = this week / green = nice to have) plus a 3-bullet Quick Wins summary. Challenge vague or self-serving AI claims ("then why aren't I ranking #1?"). Cross-check every suggestion against the real SERP, especially the **lowest-ranked of the top 3**, not the highest (if #3 ranks with 500 words, aim for ~600, not 3,000 just because #1 has 3,000). "ChatGPT will bullshit you."

**SEO tags update prompt (verbatim):**
> "Here are my current tags and my focus keyword. Update them so the keyword appears naturally, is front-loaded where possible, and matches the style and brand of my business. Also make sure each one is better than my two competitors':
> [PASTE YOUR AUDIT]
> Competitor 1 (Same Order As Mine)
> [PASTE COMPETITOR AUDIT]
> Competitor 2 (Same Order As Mine)
> [PASTE COMPETITOR AUDIT]"

**Money page rewrite prompt (verbatim):**
> "Here is the content from my product/service page:
> [PASTE YOUR CONTENT]
> Here are the top 2 competitor pages that rank for my keyword:
> Competitor 1: [paste content]
> Competitor 2: [paste content]
> My focus keyword: [keyword]
> Rewrite my page so that:
> - It is clearer, more helpful, and more persuasive
> - Word count is between: [comp low] - [comp high] words
> - Keyword density is similar to the competitors
> - Includes the keyword in natural positions
> - Adds missing topics my competitors include
> - Improves structure, readability, and expertise
> - Keeps my brand voice
> - Uses headings where appropriate
> - Does NOT keyword-stuff
> Produce the final optimized version I should publish."

**Rewrite discipline:**
- **Never trust the AI's self-reported word count or keyword count.** Verify every time in wordcounter.net (one live demo: targeted 2,200 words, got ~1,700; targeted 20-45 keyword occurrences, got 13). Land in the same band as competitors, not above or below.
- Copy output to a separate blank doc, confirm the keyword is present and front-loaded, swap in the better-testing semantic variant if the data showed one, strip labels/bold, and rewrite any H2 that does not sound like a real person wrote it.
- Refine one section at a time by pasting just that section back: *"can you rewrite this section to be more funny and personable"*; *"you forgot these heading two tags, write a couple paragraphs each and expand on the ideas."*
- **Fix priority order:** title tag → meta description → H1 (keyword in all three, ~5-10 minutes), then **wait 1-2 weeks** before touching on-page content further to see if rankings move. Re-run the page-audit tool on the new draft before publishing.

### 4.5 The 30-Day Money-Page Action Plan

Four weekly cycles, ~1-2 hours/week, same four tasks with a new blog post and a new money page each week:
1. Publish 1 blog post linking to 2-3 other posts + 1 money page.
2. Fix 5 red-flagged audit issues.
3. Fix that week's money page: title tag + meta description (~5 min, one prompt does both).
4. Add 3 internal links to that week's money page from other pages.

Total over 30 days: 4 money pages, 4 blog posts, ~20 issues fixed. Scope is deliberately capped (5 issues, not all of them) to prevent the burnout-driven quitting that stops people by week two. "This is not a sprint, it is a marathon."

### 4.6 Common Flagged Issues & Their Fixes

- **Title tag / meta description "missing / multiple / too long / too short":** "multiple defined" is almost always 2+ SEO plugins running at once (Yoast + Rank Math + AIOSEO each inject their own tags), or a custom build hardcoding the tag twice. Fix: keep exactly one SEO plugin active. "Missing" is hard to trigger (nearly every CMS auto-populates a default). Too long/short: edit in the plugin's SEO Title / meta snippet field at the bottom of the editor.
- **No H1 / multiple H1s:** see 2.4. Detailed SEO extension to count, View Source to locate, demote real content to H2 / strip non-content to plain text.
- **Open Graph issues:** OG Title should mirror the title tag; OG Image is the featured image (set one on any page you'd want shared). If ALL OG issues fire across most pages at once, it almost always means no SEO plugin is installed at all, check that first.
- **Orphan page** (zero inbound internal links): legitimate for thank-you and ad landing pages. If it should be findable, add a link from any relevant page using descriptive anchor text; if it serves no purpose, delete it.
- **Dead-end page** (zero outgoing links): add 3-5 internal links out.
- **Broken link:** manually test the destination. False-positive (external site blocks crawlers): click "manually validate." Real redirect: update your link to point directly at the new URL. No replacement: remove the link.
- **Low word count:** the tool's default 100-word minimum is outdated; real floor is 500+, agency target 1,000-1,500. Measure body only. Fine to ignore on contact, category/archive, and funnel pages.

### 4.7 On-Page Audit Tools

| Tool | Use | Cost |
|---|---|---|
| **pageaudit.com** (free tool + "PA" Chrome extension) | Per-page title/meta/heading/word-count/keyword-density inspector; extension "Copy All Headings" and can see JS-rendered content | Free |
| **Detailed SEO** (Chrome extension) | Non-caching live title tag, meta, canonical, headings, Open Graph | Free |
| **Money Page Doctor** | Auto competitor-gap read on a money page; infers keyword, flags gaps | Insiders |
| **Money Page / Service Page Analyzer** | Analyzes a service page vs. competitors; capped ~20 audits/month | Insiders |
| **HeyTony Site Audit Tool** (audit.heytony.ca) | Site-wide crawl: duplicate/missing tags, orphan pages, broken links, missing H1s, low word count; ~12-24hr recrawl lag; up to 3 sites | $10/mo or $99.99/yr |
| **Rank Report Card** | Full-site score out of 100, pass/fail per factor (H1, page speed, alt text, meta length, mobile) | Insiders |
| **Cannibalized Keywords Scanner / Keyword Conflict Detector** / keywordconflict.com | Flags multiple pages targeting one keyword (~50-page scan cap) | Insiders / free |
| **wordcounter.net / characterCounter.net** | Manual verification of AI-reported word count, keyword density, and character counts (the tool numbers are never trusted) | Free |
| **Image Alt Text Viewer** | Audits every image + alt text + file name on a page in one view | Free |

---

## 5. Quick-Reference: Every Threshold in One Place

| Element | Rule / number |
|---|---|
| Keyword targeting | One keyword per page, always |
| Title tag | 50-60 chars (ideally <55); keyword at the front |
| Meta description | ~120-155 chars; keyword near front; unique per page |
| URL slug | Short, keyword-in, no year, no "near me"; change only if not ranking + no traffic + no backlinks |
| H1 | Exactly one, first heading in DOM, exact keyword, no brand name |
| H2 count | One more than the top-ranking competitor; 5-10 normal |
| Heading order | Never skip a level going down; skipping up is fine |
| Word count | Match top 3 +100-200 (~10%); 750-1,500 baseline; 400-500 for zero-difficulty; ~2,000 ceiling |
| Keyword density | Match competitors "plus one"; your density > competitors = over-optimized |
| Readability | 7th-8th grade; paragraphs 2-3 sentences |
| Images | 1 per 200-300 words; min 4/post; alt text on every image; WebP; keyword in ≤half of alt texts |
| Internal links | 3-5 to other posts + 1 money page per new post; +3 inbound from older posts after publishing; anchor = descriptive |
| Internal link ceiling | 10-20/page (hard max 50-100) |
| External links | 1-2/page, credible, never to a competitor |
| FAQ | 3-4 per page; plain text, never behind accordion; H2 questions |
| Crawl depth | Money pages ≤3 clicks from homepage |
| Audit score | Ignore the composite; 80%+ / 90% is fine |
| Ranking pages | Never edit content/structure of a page ranking #1-#3 (UX/CTA polish only) |
| Money-page fix order | Title → meta → H1, then wait 1-2 weeks |

---

# Part IV - Technical SEO, Web Design & Internal Linking

The infrastructure layer of Matt Diamante's method: how the site is built, structured, crawled, and cross-linked so that genuinely helpful content can actually rank. Content is still the number one ranking factor and internal linking is the single biggest structural lever, but this is the plumbing that lets both work.

## Quick Reference: Every Number That Matters

| Element | Rule / Threshold |
|---|---|
| Title tag | Focus keyword at the very front; 50-60 characters (truncates past ~60) |
| Meta description | Unique per page; keyword in the first 5 words; ~120-150 chars shown, ~155-160 hard cutoff |
| H1 | Exactly one per page; must be the literal first heading in DOM order; contains the exact keyword; never the brand name |
| H2 count | One more than the current top-ranking competitor uses; 5-10 is "totally fine" for a normal article |
| Heading order | Strict descending sequence (H1 to H2 to H3); never skip a level going down; skipping back up is fine |
| Crawl depth | Every page you want ranked reachable in 3 clicks or fewer from the homepage (homepage load is 0 clicks); 4+ clicks = Google effectively ignores it |
| Internal links out (per new post) | 3-5 links to other blog posts + 1 link to a money page |
| Internal links in (per new post) | Add a link from 3 different older, already-indexed posts pointing to the new post |
| Internal-link ceiling per page | 10-20 links; hard maximum around 50-100 before it reads as manipulation |
| Images | One every 200-300 words; minimum 4 per post; never zero |
| Image format | WebP (or AVIF); export at ~70% quality; fall back to compressed JPEG only where unsupported |
| Image size | Under 1000px wide except banners; source under 2K resolution; compress anything over ~1MB before upload; hero ~1440x720 / 1400x740; OG/featured 1200x628 |
| WordPress plugins | 15 or fewer |
| PHP version | 8.2 or higher |
| Mobile page-speed score | Target 80%+ |
| Fonts | 2 safe; more than 3 causes a noticeable slowdown |
| Body font | Never below 16px; 16-20px working range; ~1.8 line-height |
| Categories | 5-10 total site-wide; 1-2 per post; tags never |
| Sitemap | Submit once to Search Console; never hand-build; it auto-updates |
| Request Indexing | 10 free URL submissions/day in GSC; ~2 hours to ~1 week to take |
| Reading level | 7th-8th grade |
| Audit-fix pace | 5-10 fixes per week, not all at once |
| Site health / audit score | 80%+ (Page Audit) or 90% (health) is "fantastic"; never chase 100% |

## Governing Rules for Technical & Structural Work

These override every specific tactic below.

- **Content is the #1 ranking factor; technical is secondary.** "If you write good content, that matters a lot more than just having schema markup on the page." Schema, meta tags, and title tags are required but rank below the actual on-page content and internal-link structure. Fix the fundamentals (a broken or incomplete site) before adding location pages, channels, press releases, or new tools.
- **Google Search Console is "the number one most important tool for SEO."** It sits above keyword tools and even above Analytics because it is the only concrete, real (non-estimated) data straight from Google. Set up GSC before making any keyword-targeting decision. "Without Search Console, you really are just shooting in the dark."
- **One keyword per page, site-wide, no exceptions.** This is a structural rule as much as a keyword rule: it dictates how pages and navigation are organized. Trying to rank one page for several keywords means it ranks for none of them, or ranks lower for all. The single highest-revenue service becomes the homepage's target keyword; every other service gets its own dedicated page. A page can still legitimately rank for many *phrasings* of one intent; word-order and pluralization variants ("Chicago newborn photographer" / "newborn photographer Chicago" / "Chicago newborn photography") are ONE topic, not three.
- **Never touch a page that is already ranking (positions 1-3, or ranking for anything at all).** The most emphatic rule in the entire method: "Don't edit any pages that are ranking, for the love of God." It applies even when the page violates every rule below (duplicate H1s, keyword stuffing 122 times, hidden overlay text, zero backlinks, thin content). "If it is ranking, don't touch that page, even if it's not ranking for the exact keyword you want." You cannot rank higher than #1, so editing is pure downside. UX / CTA polish (a button, one sentence) is the one carve-out; the content and structural signals that could shift rank are frozen. If a page is NOT ranking, you are free to rewrite/rebuild it.
- **Audit-tool warnings are frequently false positives or cache lag, not real ranking problems.** Always cross-check a live, non-caching source (GSC, or the Detailed SEO extension) before "fixing" something that already works. Expect a 12-24 hour (up to a week for Google-side reports) delay before a real fix reflects in an audit tool; an apparent ranking dip right after a fix is usually this lag, not a regression. Distinguishing genuine defects from tool noise is the core skill.
- **Do not chase 100% on any audit or scoring tool.** 80%+ on Page Audit or 90% site health is "fantastic." 100% does not guarantee a #1 ranking, and members with near-perfect scores rank no better than those who ignore the score. "Sometimes you need that D to help you rank." (Matt keeps his own site near-perfect only because prospects scrutinize it for credibility as a paid provider: a different bar.)
- **Freshness-gaming / patience.** When a page is newly published or updated, Google sometimes deliberately suppresses ("tanks") its ranking, then waits days to see whether the publisher panics and makes a flurry of edits: that panic-editing pattern itself reads as a spam signal. Once a page is live, give it about a month before re-editing. Check data daily if you want, but never act on daily noise. Non-ranking page: wait 3 months, then 6 months (doing internal linking meanwhile) before touching its content again.
- **20% of effort drives 80% of results; skip the rest.** Deprioritized by Matt's own repeated testing: schema markup, FAQ schema, messy/inconsistent HTML markup, "AI blocks," chasing an audit percentage, AI-detection tools on your own content.
- **AI (Claude/ChatGPT/Gemini) is a tool for orientation, drafting, and code, never the final decision-maker on architecture.** "Make the decision based on the actual data points, not on what Claude's saying." ChatGPT specifically produces keyword-stuffed headings when asked to architect content and "will make shit up" about SEO best practices.

## Heading Structure (H1 / H2 / H3)

The single most recurring live-audit topic.

### Core rules
- **Exactly one H1 per page.** The only tolerated exception is two H1s containing *identical* text from a separate desktop block and mobile block (an audit tool flags it but it is not a real problem, and Matt now suspects even this dual-render trick can read as gaming, see below).
- **The H1 must be the literal first heading tag in DOM order,** not just the visually biggest. Google's crawler reads top-down; the H1 signals the topic before anything else. A Shopify H1 sitting on a "limited time offer" element far down the page had to be moved to the top.
- **The H1 must contain the exact target keyword** in natural, readable language (not "gobbledygook"). Rewrite marketing-speak to match how people actually search: "romantic storytelling wedding photography in Toronto" became "Timeless wedding photography in Toronto."
- **Never put the business/brand name in the H1 (or any heading).** The brand is already in the title tag and URL; you will rank for your brand name automatically. Brand name in an H1 is more acceptable only on the homepage of a brand-new business establishing recognition.
- **Headings run in strict descending sequence; never skip a level going down** (H1 straight to H3, or H2 to H4, is wrong). Skipping backward *up* a level (H3 back to H2) is fine. "If you skip a step going down the stairs you'll trip; skip a step going up and you're fine." Book analogy: H1 = book title (the one topic/keyword), H2 = chapter titles (subtopics reinforcing the H1), H3 = subheadings within a chapter. Avoid H4-H6 in practice; demote them to plain paragraph text or, if truly needed, use them only in the footer.
- **Keywords carry more weight in headings than in body copy.** Work the target keyword (or a variant, or a local modifier) into headings; avoid generic "Learn More"-style headings. H2s should contain the keyword in all, or at least a healthy majority, but do not force it into literally every H2 if there are 10 of them (that reads as stuffing).
- **H2 count = one more than the current top-ranking competitor.** Pull up the page ranking #1 for your keyword, count its H2s, match or slightly exceed (top page has 5 H2s, go for 7-8). Do not drastically overshoot (top page has 50, going to 200 is over-optimizing). 5-10 H2s is normal.
- **Heading styling never matters for SEO; the semantic tag does.** An H1 does not have to be the biggest visible text: you can style an H1 smaller than an H2 via CSS if you want it to carry SEO weight without dominating the layout. In builders (Elementor, Wix) the visual size and the HTML tag are independent; always verify/set the actual tag (Elementor: the Heading widget's HTML Tag field; Wix: Edit Text to SEO and Accessibility to HTML tag dropdown). Use the Heading element, not a styled text/paragraph element, to lock a real tag.

### Duplicate H1s and mis-tagged elements
The two-path decision when a second heading-level element exists:
- **If it is real topical content** (a genuine subtopic mis-tagged as H1), downgrade the tag to H2. Do not delete the copy: fix the tag level only. Example: a wedding-ring blog's second heading "What Wedding Band Styles Couples Like" was styled as a second H1, corrected to H2.
- **If it is NOT real content** (a hero/lead-magnet box, a CTA, a testimonial quote, a tagline, a logo, a name callout, breadcrumbs, "Related products", cart/quantity modules), strip the heading tag entirely and convert it to plain, restyled paragraph text. Do not demote these to H2 either: they are not subtopics. Go through every heading and ask "does this support what the page is about?" Anything that is pure styling, branding, or a CTA fails and gets demoted to plain text. Footer titles above menu columns should be H4 or smaller (or plain text), never H1-H3.

Common duplicate-H1 causes and fixes:
- **Pressing Enter/Return mid-headline** to force a line break creates two separate H1 tags. Fix by shrinking the container so the text wraps naturally, or (GoHighLevel specifically) use container padding to force the break. A headline spanning more than one visual line can also register as two H1s.
- **Desktop/mobile block duplication** (Avada, Wix, Squarespace, GHL): a designer duplicates an entire block to show separate desktop and mobile copies, loading the same content and heading twice on every pageview. Do not duplicate the block; use per-breakpoint design settings on one truly responsive block (different font size, image size, or background per breakpoint is fine; the text/heading must not be a second element). Claude Code fix: paste the block's default-editor code and prompt "make this mobile friendly in the same blocks without duplicating the content."
- **Theme/logo defaults:** developers commonly mark the logo or every heading as H1 ("very common with developers"). Avada's Page Title Bar / Layout module auto-generates an empty duplicate H1 (disable it per-page or globally). Kajabi puts a blog-index title as an H1 above every post's own H1 (convert the index title to H2/paragraph). Shopify hard-wires the H1 to the site logo (workaround: add a redundant second H1 in `theme.liquid` / `product.liquid` containing the keyword, and escalate to Shopify support for the real fix). Square has no true H1 field at all (its hover image-description reads as alt text).
- **Diagnostic tools:** the Detailed SEO Chrome extension shows H1 count instantly; View Page Source + Ctrl/Cmd+F "h1" locates where a duplicate is injected. A dedicated heading-audit extension lists every H1 individually (one case found 13 firing from the logo, signage graphics, and animated elements that a generic tool only flagged as a vague count).
- **JS-rendered pages** (React + Tailwind, etc.) that do not auto-emit semantic headings: get the framework or AI coding tool to output real `<h1>`/`<h2>` elements, then restyle via CSS. Do not fake headings with styled divs.

### Black-hat heading patterns to remove on sight
- **Never use hidden text** (font color matching the background) to stuff a keyword. Google devalues and ignores it, and a duplicate H1 hidden this way is a cloaking pattern.
- **Never ship a different H1 for mobile vs desktop via responsive show/hide.** Matt copied this from a #1-ranked competitor and now suspects Google penalizes it as gaming the system. Correlation (they rank #1 and do X) is not causation (X is why). His own "website design in Hamilton" page fell from #1 to #7, with the mobile/desktop dual-H1 hack cited as a contributing cause.

## Title Tags, Meta Descriptions & Open Graph

- **Title tag:** the focus keyword at the very front (highest-value tactic). 50-60 characters; longer truncates with "..." in the SERP. Structure: homepage = brand name + focus keyword; every other page = keyword first, then the brand name at the end. Google frequently strips the trailing brand name from the SERP display only (the HTML tag is unchanged); this is display behavior, not a defect. Do not let a title render with a trailing "..." on-page: Google literally cannot read past the cut. Local reorder: "Movers in Washington D.C. | Free Quotes | Your Moving Men", keyword/city front, brand last.
- **Meta description:** unique per page, never duplicated even across near-identical variants. ~120-150 characters displayed, ~155-160 hard cutoff. Keyword near the front (moving it into the first 5 words alone can flip a Yoast score yellow-to-green). Written as a persuasive sales pitch to win the click, not a copy of the title tag: "that's like the billboard saying click me instead of your competitors." Google increasingly rewrites descriptions on its own regardless, so exact character precision matters less than it used to; still always set one. Do not rely on an auto-pulled excerpt (Shopify may grab arbitrary EU product-safety text; that mismatch is a tell the field was never set).
- **Duplicate title tags AND duplicate meta descriptions have the same root cause: two or more SEO plugins running at once.** Yoast, Rank Math, and All in One SEO each inject their own tags. Run exactly one. (Custom sites can hardcode a tag twice.)
- **Missing title is genuinely hard to trigger:** nearly every CMS auto-populates a default from the page name. If it happens, restore an old page revision.
- **Yoast overriding a page-builder meta description:** Yoast set to pull an excerpt silently overrides whatever you set in Elementor. Fix it in Yoast's own meta-description box on that page.
- **Meta keywords field** (flagged "missing" by some plugins): ignore completely, dead since the 90s.
- **Open Graph (OG) tags** control social-share previews. OG Title should mirror the title tag; OG Image = the page's featured image (1200x628), set on pages you would actually want shared. If ALL OG issues are flagged across most pages, it almost always means no SEO plugin is installed. Check via the Detailed SEO extension "Social" tab.

## Site Speed & Core Web Vitals

Causal chain, stated directly: slow load to higher bounce rate (user hits back and picks a faster result) to lower ranking. But page speed is deliberately **the last thing to fix**, only after content and keyword targeting are confirmed equal-or-better than competitors: "You gotta fix your pages first and then you can look at page speed after that." Speed's impact is relative, not absolute: if everyone in a niche is equally slow it does not cost you, and Matt has "seen slow websites outrank fast ones." A subjectively "fast-feeling" site can still score poorly, and vice versa; do not trust the "feels fast" proxy.

**Core Web Vitals = "just think user experience."** The named component members hit most is Cumulative Layout Shift (CLS): the page should render into its final structure immediately and hold, with nothing loading in afterward that pushes existing content (the ad-heavy-site experience of accidentally tapping the wrong thing). A good CWV bar: fast load, readable fonts, fast image load, zero layout shift.

### The fix sequence (least to most disruptive)
1. **Audit and cut plugin count first.** Keep WordPress to 15 plugins or fewer; consolidate/remove old or unused ones even if they seem harmless (they still load).
2. **Install/configure a caching plugin.** WP Rocket is the go-to (~$59/year; separate CDN add-on ~$7-10/month). Walkthrough: File Optimization tab (minify CSS, minify JS, delay JS execution), turn caching on, enable "Add missing image dimensions" (fixes the explicit width/height warning), enable preload, use Advanced Rules to exclude pages that should never cache. If toggling an optimization visibly breaks the site (WP Rocket commonly breaks JS-driven images/animations), un-toggle just that one and clear cache. Alternatives: SiteGround Speed Optimizer, LiteSpeed. One attendee went from ~20 to 75, then to 100 with additional tweaks.
3. **Run image compression to WebP** (see Images below). Imagify or WP Rocket's paid image add-on for bulk conversion.
4. **Only change the theme if the above is not enough,** since a theme change forces a full visual rebuild (last resort).
5. **For advanced fixes, ask Claude Code directly** how to make the site faster.

### Server / platform levers
- **PHP + server (cPanel access):** update PHP to 8.2 or higher (verify plugin compatibility first so you know what to roll back to); enable OPcache, Redis, and Memcached; re-test after each change.
- **Hosting memory/execution limit** defaults to 30 seconds on most hosts; triple to 90 seconds if scripts need it.
- **Delay JavaScript** for specific long-rendering scripts identified in a PageSpeed report, then re-test both the speed gain and full page functionality (load order matters: a delayed script may be a dependency).
- **Self-host Google Fonts** via the OMGF plugin instead of loading them from Google on every page.
- **Shopify speed checklist (four things):** CDN set up; images served as WebP; image lazy loading enabled; CSS/JS deferred. If all four are in place, speed "should be very, very good."
- **Cloudflare** as a CDN to defer scripts. Never use its one-click "block AI bots" toggle: "how else are they going to recommend it?" If AI-crawl volume genuinely crashes your hosting, fix it with better hosting (cloud/VPS, ~$30/month) plus a Web Application Firewall (WAF), not by blocking bots. (Documented case: FAQ schema triggered 100,000+ simultaneous legitimate bot hits crashing shared hosting; the fix was hosting tier + WAF, not removing the schema.)

### Platform speed ceilings
- **Squarespace:** optimizing images is basically the only lever; "unused JS/CSS" flags are not fixable (no dev access); mobile score will likely never be high even with full effort. Optimize what is controllable and move on.
- **GoHighLevel:** Core Web Vitals issues (CLS, Total Blocking Time) are typically unfixable (no code/server access).
- **Kajabi:** unused JS/CSS and large image payloads are largely unfixable.
- **Wix:** no hosting-level access; contact Wix support to adjust those settings; disable non-essential animations (especially mobile), which are the usual template-speed drag.
- **Diagnostic:** run pagespeed.web.dev, check the Mobile tab separately from Desktop (mobile target 80%+); Chrome DevTools "toggle device toolbar" to preview mobile rendering. Reading lazy-loading as a good sign: images visibly popping in as you scroll means only near-viewport assets load.

## Images for SEO

- **Density:** one image/video/chart every 200-300 words; minimum 4 per post; every post needs at least a featured image. Where an image does not make sense for a section, a heading break is an acceptable substitute. Do not stuff photos "because people like pretty pictures": every image should illustrate a specific point (put excess photography on a separate gallery page).
- **Format:** WebP (or AVIF) is the standard; same visual quality as JPEG/PNG at roughly 1/10th the file size. Export WebP at ~70% quality (barely any visible loss). Fall back to compressed JPEG only where the platform lacks support. Squarespace rejects AVIF entirely and WebP support is version-dependent; Wix accepts WebP; GoHighLevel does NOT accept WebP for course/video uploads (use JPEG/PNG there).
- **Conversion tools:** WebP Converter for Media (preferred WordPress plugin over the "heavier" Imagify); Squoosh (one at a time); a Photoshop batch action; free web converters like Free Convert (~10/day free cap, rotate converters when capped); Photoshop File to Save As WebP at ~70%. Canva cannot export WebP: export PNG/JPG then convert. Bulk-convert existing sites with a plugin (Imagify), never all at once.
- **After converting, physically delete the old PNG/JPEG originals from the server;** a "replace" that leaves the old file keeps dragging speed down (a 5.4MB PNG dropped to ~300KB as WebP). Real before/after: 537KB to 32KB, 1.1MB to 27KB, 1.9MB to 102KB, "looks exactly the same."
- **Sizing:** images under 1000px wide except banners; source under 2K resolution (downsize DSLR captures before upload); compress anything over ~1MB before upload; hero ~1440x720 or 1400x740; half-width images ~500-700px; a body image ~750px wide by 400-500px tall. Check for accidental oversize: right-click the live image and "open image in new tab" to see actual pixel dimensions.
- **Lazy loading** loads only near-viewport images (speeds initial load); it can break images with attached effects/animations, so test after enabling. Hey Tony's own production site runs with lazy loading fully disabled.
- **Alt text:** never leave it empty; describe the image accurately (formula: identify the medium, photo/illustration/graphic/infographic, plus a real description, e.g. "illustration of a stack of blueberry pancakes in a kitchen"). Include the target keyword only where it fits naturally, roughly half or fewer of a page's images, and never the identical keyword phrase sequentially across every image ("Newborn photographer Chicago 1/2/3/4"). Alt text is for screen-reader users first, is a mild extra keyword-targeting vehicle, and helps images rank in Google Image search. Proofread the actual string (missing spaces break it). Per-variant, not generic (every diamond-shape photo tagged just "diamond" is a missed opportunity: use round/cushion/pear).
- **File names:** rename the actual file to a plain descriptive keyword phrase before upload ("west-african-wedding-ceremony-toronto.jpg", not "1234.jpg"); Google reads the file name as a signal distinct from alt text. A harmless minor nudge, not a real ranking lever.
- **Sourcing priority:** your own real photos/screenshots (fully unique, can't be replicated) > stock ~ AI-generated (roughly equivalent after real photography). Stock and AI images do NOT hurt SEO with proper alt text; the only concern is brand fit. Exception: for charts/graphics specifically, AI goes to the top of the list ("they make really great graphics"). Pexels/Unsplash (free), Adobe Stock/Creative Market (paid, customizable icons). Stick to a small, provable set of licensed sources so licensing can be defended if challenged.
- **Cross-device bug:** if images render fine on your machine but disappear in incognito/other devices, describe the exact symptom to an AI coding assistant; never batch-convert a whole site's images at once, change one page and verify first.
- **Replace live Google Maps iframe embeds** with a static WebP screenshot linked to the real Maps/GBP listing: PageSpeed flags Google's own embed as a drag, and visitors do not interact with the live map anyway. (Confirmed this is what Hey Tony's own site does.)

## Schema Markup

Deprioritized overall: schema was more important in the past, less so now, and Matt runs no custom schema on his own site. It has NOT moved AI-Overview citation odds in his testing. Notable counter-datapoint: his own page-analyzer found pages with NO ranking having *more* schema than ranking pages (true for one site, not validated broadly).

When you do use it:
- **Yoast's schema toggle** auto-generates standard/generic schema across every page type with zero setup: turn it on, it is essentially free. Enough for most businesses.
- **Manual JSON-LD** for anything more specific (reviews, prices, FAQ): use any schema-markup generator, pick the content type (Product, Article/Blog), fill the fields (include the keyword in the description), copy the JSON-LD, and **paste it into the page's header** (Rank Math has a header dropdown; else a header field or plugin). Header placement is non-negotiable: it loads before the page so the crawler reads it first, same as an analytics script.
- **FAQ schema via AI:** describe your on-page Q&A to Claude/ChatGPT/Gemini, ask it to generate the schema, paste into the code-injection block.
- **Schema is only penalized when the data is wrong or misleading** (wrong hours = slight penalty; claiming "restaurant" when you are a PR firm = major penalty). Missing or incomplete but *accurate* fields are not penalized. Skipping FAQ schema carries no penalty; only worth the manual dev effort for high-competition keywords.
- **Local-business schema for a multi-city service area:** main schema (matching the GBP) on the homepage listing every service-area city; a separate page-specific schema on each city page naming only that one city; a full separate schema per physical location/GBP.
- **FAQ schema is double-edged:** it can drive genuine "Google's AI now recommends me" outcomes but can also draw heavy AI/training-bot crawl traffic. The fix is always to block the bad bots (take the snippet to Claude and ask it to add a bot-blocking rule), never to strip the schema earning the visibility.

## Sitemaps

- **Auto-generated by every major platform** (WordPress via Yoast/Rank Math, Wix, Squarespace, Shopify). Never hand-build one; a plugin keeps it updated automatically. View any sitemap by appending `/sitemap.xml` (some use `sitemap_index.xml`); a valid sitemap can render as a formatted page or raw code, either is fine.
- **The one manual step: submit it to Google Search Console** (Indexing to Sitemaps; in 99% of cases the path is just `sitemap.xml`). Test it loads in a browser first. If status shows "Error" right after submitting, refresh, it often flips to "Success" unchanged. This is "super important": if new pages are not indexed within ~1 month, first confirm the sitemap was actually submitted.
- **Never manually resubmit a sitemap** after publishing or fixing content; it auto-updates and Google auto-recrawls it. (The one exception cited: after a full site redesign.) Do not repeatedly mash "Validate Fix" on the sitemap.
- **One sitemap per site is the norm;** some complex/legacy sites legitimately split into 4-5 by content type (posts, pages, categories, authors), and each segmented sitemap must be submitted individually. To isolate blog posts for AI tools, open the `post-sitemap.xml` specifically. When submitting in GSC, submit the specific sub-sitemap path (e.g. `sitemap/blogs`), not one giant dump.
- **A deleted sitemap is catastrophic:** documented client case where a deleted sitemap dropped traffic "from hundreds of thousands to zero." A dead sitemap reference left in `robots.txt` (e.g. after removing Yoast) silently blocks discovery.
- **Sitemap totals are NOT the true indexed-page count:** sitemaps still list redirected and 404 pages. Verify what is really indexed by running a clean live URL through URL Inspection.
- **GoHighLevel does not auto-surface a sitemap;** it must be manually regenerated inside GHL and resubmitted/re-validated in GSC after each new blog post. GoDaddy's builder has failed to auto-generate one despite claiming to (escalate to GoDaddy support). Showit runs a separate sitemap from its WordPress blog integration: submit both.

## Robots.txt

- **Auto-generated by every major platform;** if yours does not have one, "you need to switch your website builder." A default Yoast/WordPress `robots.txt` blocks nothing (it just allows everyone and declares the sitemap location). Check by appending `/robots.txt`.
- **Only add `disallow` lines for things deliberately hidden** (admin dashboard, throwaway pages). Matt does NOT recommend most people hand-edit robots.txt: it is easy to accidentally block the entire site.
- **Remove any `crawl-delay` directive:** even a small delay can trigger a bot-challenge screen instead of serving real content (diagnosed as the cause of a tool returning "only nine words").
- **Add an explicit user-agent allow rule** for any legitimate SEO-audit crawler being blocked. Many audit tools (including Hey Tony's) crawl on Python, so check `.htaccess` and `robots.txt` for a "Python" block. Prompt used live: "How can I add a user agent to my robots.txt file?"
- **Shopify robots.txt over-blocking** (disallow lines for blog/collections/products) is commonly injected by a third-party app, not done manually: disable the suspect plugin, wait for cache, recheck.
- **CDN blocking a legitimate crawler:** identify the CDN with the BuiltWith extension, then whitelist the crawler's IP/user-agent in the CDN/firewall (Cloudflare is a recurring culprit).
- **Never block AI crawlers,** even when they overwhelm the server; fix it with hosting + a WAF instead (see Site Speed).

## Canonicals & Duplicate Content

- **Every page's canonical must self-reference** (point to its own URL). A page can show as "indexed" in an SEO plugin yet be excluded from the generated sitemap because its canonical points elsewhere: a real, fixable defect. Diagnostic: confirm the page is set to index, confirm it is not sitemap-excluded, View Source and check the canonical, check for redirects or a second competing URL, and if the root cause can't be found, delete and recreate the page to force a clean re-index. WordPress fix: Yoast to Advanced tab to Canonical URL field. If it persists on one page, suspect caching, a theme override, or `functions.php` code generating the tag.
- **"Canonical not self-referencing" is very often just a trailing-slash mismatch** between the live URL and the canonical tag: add the missing slash so they match exactly. A false flag, not a real problem.
- **Dynamic URLs** (a `?` or `=` near the end instead of a clean `/`) are inventory/search-result pages that will not rank and should be ignored in GSC. GSC's "Alternate page with proper canonical tag" flag on these is safe to ignore. Confirm they are NOT in the sitemap. To fix a dynamic page's canonical, build a static page (URL with no parameters) and exclude the dynamic pattern in robots.txt.
- **Duplicate tags** (multiple pages sharing the same title, meta description, or H1) usually signal overlapping/cannibalizing topics. Google cannot determine which page is canonical and may suppress all of them: this is self-cannibalization. Fix by merging into one comprehensive page (301 the old URL to it) or rewriting each page's tags and content to be unique.
- **Blog listing/category pages must never show full post content:** only a thumbnail and an excerpt with a click-through. Full content on both the listing and the post gives Google two identical pages, and it deprioritizes/fails to index one. Truncate auto-excerpts to a fixed length (~200 characters).
- **Never have duplicate content on your site: "that's the number one thing" to avoid.** Location pages must be genuinely unique content, not a template with only the city swapped (that is the real cannibalization risk; multiplying pages itself is not). Low-stakes near-duplicates (an escape-room booking page for two cities) can sometimes get away with differentiating only the title tag + meta description; a page meant to independently rank for its own local keyword needs real unique body copy.
- **Locale/geo duplicates** (Shopify `EN-CA` vs default English across every page): pull GSC to see which variant ranks; for blog content redirect the loser to the winner; for product pages do not force a redirect (use a switcher/prompt); the real fix usually lives in a geolocation app's settings. Bilingual URLs: keep language versions on subfolders (`/fr/`), not subdomains (Google treats a subdomain as a separate site). An English-slug-plus-"fr" URL is "good enough" as long as the on-page content is genuinely in that language; set hreflang.

## HTTPS

- **Every site needs HTTPS** (the encrypted "S"); modern browsers expect it, and it is required to accept payments. Squarespace/Wix/Shopify handle it automatically (effectively impossible not to have it). WordPress is where it can genuinely be missing.
- **Fix = install an SSL certificate** via the registrar or host. Managed WordPress hosts usually handle it; self-hosted/custom servers may require you to purchase and install it.
- **An installed SSL does not guarantee every internal link was updated to `https://`.** After a rebuild, bulk-swap hardcoded `http://` to `https://` with the "Better Search and Replace" WordPress plugin (back up first). A canonical/HTTP audit is standard after any outside-agency rebuild (one broke canonicals on ~60-70% of pages and left HTTP links despite an installed cert).
- **GSC "Page with redirect"** showing non-SSL, `www`, and `www`+non-SSL variants all correctly redirecting to the canonical secure non-`www` URL is a confirmed non-issue: GSC is just reporting variants it saw. Confirm the live site is served over HTTPS; use the GSC Domain property (which aggregates all variants).

## Indexing & Google Search Console

- **GSC is the primary diagnostic instrument.** Use the **Domain property** (aggregates every URL variant: subdomains, http/https, www/non-www), not the URL-prefix property. Setup: Add Property to Domain, verify via a DNS TXT record at the registrar (host `@`), retry Verify through propagation, then submit the sitemap.
- **Check indexing status:** `site:yourdomain.com` in Google (compare indexed count to real page count), or paste a specific URL into GSC's URL Inspection (green = indexed, gray = not indexed, red = a problem). If gray, click **Request Indexing** (10 free/day; not a ranking guarantee but prompts a recrawl). New-post indexing timeline: ~2 hours to up to a week is normal; a properly internally-linked page has been seen to index in ~2 hours; a low-authority site can take up to ~2 months; a brand-new site can take 2-3 weeks (up to ~2 months) before Google crawls at all. "It depends on every single website." Do not request a recrawl on a page you are still editing.
- **"Crawled - currently not indexed":** if you want the page ranking, add on-page content and build more internal links to it. If you do not care about it (leftover sample posts), delete it. This is the one exclusion reason genuinely worth chasing (along with "Not found (404)" on pages that should rank). Ignore "duplicate without canonical," "blocked," paginated/feed/author pages, and "Alternate page with proper canonical tag" on dynamic URLs: these are noise. "There will always be some issues in Search Console that aren't really issues."
- **"Discovered - currently not indexed":** do NOT resubmit URLs manually; increase internal links pointing at those pages, publish content that links to them, and keep publishing so Google crawls deeper.
- **Reviving a stuck old post:** change something so it reads as fresh (update copy, tie it to a newer related post, add a new backlink), then request indexing again every 2-4 days until it resolves. After a fix (alt text, etc.), wait roughly a month before re-checking (account for caching lag).
- **Per-query diagnosis:** Performance report defaults to clicks/impressions; click "Position" to add average position. A page-level average position is a *blend* across every phrasing it ranks for, so a keyword you type by hand can sit on page 30 while the blended average looks fine. Click a Query row, then the Pages tab, to see exactly which URL ranks and its position per query. Minor overlap (many pages at position 15-70) is normal noise, not cannibalization; only worry when a second page seriously competes with your intended target for a real keyword. GSC's query table caps around 1,000 rows; a growing row count is a positive signal of expanding reach.
- **IndexNow / primeindexer:** always use IndexNow (via Bing Webmaster Tools, one-click GSC import) for faster indexing after publishing, per the technical team. (Matt personally is skeptical IndexNow does much; primeindexer.com is a free accelerator observed to index in ~7 days.) Both are optional; Google finds new content on its own, aided far more by internal linking.
- **Reading traffic drops:** GSC vs a platform's own analytics never fully reconcile (expected). GA4 includes every channel, so a "drastic" GA drop can be a non-organic source falling off, not an SEO problem: check GSC's organic trend specifically. Compare 28 days vs previous 28 days, never 7-day vs 7-day (too noisy); for a newer site pull 12-16 months. Read impressions first (trending up = early traction). Rising impressions with flat clicks is normal mid-funnel progress (more keywords ranking, just not top of page 1), compounded by AI Overviews suppressing informational clicks; do not panic.

## Crawl Depth, Orphan Pages & Broken Links

- **Crawl depth: every page you want ranked must be reachable in 3 clicks or fewer from the homepage** (homepage load = 0 clicks; a page linked from the nav = 1; a specific post = 2; a page linked from that post = 3). 4+ clicks and Google effectively stops caring, precisely because a human can't easily find it either. "If I can't get to it from your homepage, Google's not going to index it." Shortcuts: use blog *posts* (auto-populate the roll and category archives) not static pages; add homepage modules (services bar, "recent posts", category links) that make pages 1-click; put "Blog" in the nav (keep the label "Blog", do not rename to "Learn Hub"). Dropdown/mega menus do not add a click themselves (only leaving the page counts) but overstuffed dropdowns hurt usability, especially on the ~50-60% of traffic that is mobile.
- **Orphan page = zero internal links point to it** (reachable only by someone with the direct URL). Google can know the URL exists but reads "nothing links to this" as "not important to these people" and deprioritizes it: crawlable is not the same as link-equity-connected. Orphans are fine ONLY when deliberate (thank-you pages, ad landing pages, lead-magnet quizzes, job postings, internal-only pages); pair those with a no-index tag. Anything you want ranked must never be orphaned. Fix: highlight relevant anchor text on any related page and link to the orphan; re-run the audit. Triage a large orphan count by picking the ~10 most important and adding 1-2 links each, rather than fixing all at once. Diagnose via the manual click-through test (can you reach it from the homepage nav?) or the private/incognito test (does the direct URL load?). A hidden cause: a page can flag as orphan even with inbound links if those links are set to `nofollow` (View Source, Ctrl+F "nofollow").
- **Dead-end page = zero *outgoing* links** (no internal, no external, no nav, no footer): a page that traps the visitor. Every page needs a path onward; target 3-5 outgoing links per page. Even a site needs a handful of outbound external links to non-competitors: an all-inbound, zero-outbound site is a crawl dead end (the crawler arrives and cannot move on).
- **Broken links** (a link to a 404) signal "we're not on top of our site's UX." Work through them in small batches (~10/week) since each points somewhere different. Fix options: update to the correct URL, replace with an internal link to your own content (turn a broken external link into a content + internal-linking opportunity), or remove the link entirely. False-positive case: some external sites block crawler bots, making a working link flag as broken; manually verify, then click "manually validate" to exclude it. Broken links pointing at social platforms (LinkedIn) are usually just blocked bots.
- **Prune dead pages** (zero impressions, zero indexing, zero traffic, and no backlinks) via GSC; if all three are "no", safe to delete. On a black-hat/spam cleanup: set zero-click spam pages to DRAFT (never delete, keeps restore option; drafting also strips their plugin-injected cross-links), re-run the audit for now-broken links, and do NOT manually 404, redirect, or request a recrawl. "If your SEO is already terrible, then you can't really do worse."

## Mobile & Responsive Design

- **Google has done mobile-first indexing since ~2016;** visually cut-off or non-reflowing mobile content is a direct negative regardless of desktop quality. Search engines actively prioritize responsive sites. Failure mode: unresponsive to higher bounce to lower rank (the original Space Jam site is the canonical unresponsive-legacy example).
- **A clean heading audit is not proof of responsiveness:** they are independent axes. Test true responsiveness separately by resizing the browser / using the builder's device toggle and watching whether content reflows smoothly vs gets cut off or forces horizontal scroll (theatregym.co.uk passed the heading audit but failed responsiveness entirely).
- **Build order: always design the largest breakpoint (desktop) first,** then step down through laptop, tablet, phone in sequence. Never start from a mid-size breakpoint and try to hold it in both directions (a client who designed against a "square" ratio first skewed on both desktop and mobile).
- **Mobile hero content order:** Headline to Copy to CTA to Photo, stacked strictly top to bottom; never place a photo beside text on mobile; do not force a full desktop hero photo into a mobile background (place it below the text). Left-align mobile body text; keep side padding so nothing touches the screen edge.
- **A desktop padding value can break mobile outright** (a 255px side-padding trick exceeded an iPhone viewport; mobile needs ~50px). Font size may shrink slightly on mobile (screen sits closer: 17.5px desktop / 16px under a ~720px breakpoint) but this is the *one* thing allowed to shrink; spacing/margins stay generous. After finishing desktop, switch to the phone preview and manually rearrange if the auto-layout looks off. Squarespace and some platforms only support two breakpoints (desktop/mobile), a real constraint to design around.
- **Phone tap targets:** phone numbers and emails must be tap-to-call / clickable everywhere, especially on mobile; anchor a labeled clickable number at the *bottom* of the screen for a mobile-heavy audience (bottom beats top for thumb reach). One profile's icon-only floating button (no visible clickable number) tanked call conversions.

## Internal Linking (The Core Growth Lever)

The single most-repeated structural fix across every call, for orphan pages, stuck indexing, cannibalization, and authority alike. "Internal links for the HeyTony site were the biggest factor and the biggest differentiator in why things were ranking really well." It is what experts forget to do: "They'll publish content, they'll get backlinks, but they won't do internal linking, which is massive." Do not conflate internal links (between your own pages) with backlinks (from other sites); social-media links to your own page also "don't really count for much."

### The two rules ("your entire internal linking strategy, done")
- **Rule 1 (outbound):** every new blog post links out to **3-5 other blog posts + 1 money page** (scale down to 3 other-post links on a short post; on a brand-new site with little content, 2-3 posts + 1 money page, and if you have nothing yet, use the money page + homepage as your only links). At least one link must point to a money/service page (or, absent one, whatever you actually sell, or the homepage).
- **Rule 2 (inbound / the "circle" / reciprocal move):** every time you publish, go back into **3 different older, already-indexed posts** and add a link from each pointing INTO the new post. This is the half everyone skips. Because Google already trusts and crawls those old pages, their links get the new page discovered and indexed fast, sometimes within an hour or two, without ever manually submitting it. "If you join a circle where everybody introduces you to the next person, everybody's going to know about you; if you're standing outside the circle saying 'I know those people over there,' you won't get invited in." Finder mechanic: `site:yourdomain.com "keyword"` (no space after the colon, phrase in quotes) to surface your related indexed pages, run once pre-publish (3 pages to link the new post TO) and once post-publish (3 *different* pages to link FROM). If you do not yet have 3 posts, 1 link is fine for now.

### How internal linking drives indexing and authority
- **The more internal links point at a page, the more Google reads it as important.** "The more internal links you build to a page, the more Google will understand this page is important." Go heavy: "4, 5, 6, just go insane with it" is historically one of Hey Tony's best-performing tactics. Pages receiving the most inbound internal links are treated as the most important.
- **Case evidence:** Hey Tony's own SEO service page, content unchanged for 3-4 years, climbed from position 13 to #1 using *only* accumulating internal links from dozens of blog posts. "I asked my team, did anybody touch this page? All we did was internal link to it." Matt got a separate page to rank #1 in 3 hours using internal linking alone (witnessed live). Doing both linking rules consistently has indexed pages within an hour to two.
- **Blog posts do not always need to rank themselves;** sometimes their only job is passing internal-link authority to the money page. This is a core reason to keep publishing low-competition posts (the avalanche/snowball method): each new post is a fresh chance to pass keyword-anchored links to money pages.

### Anchor text and placement
- **Anchor text must describe the destination page,** ideally the exact primary keyword of the target page (or something close/natural if that does not fit; it does not need to be the literal post title). Never use "click here", "learn more", or "website": banned. Rewrite vague anchors ("get your copy here" to "get your copy of [book title] here"; the single word "most" to "the most common questions about pest control").
- **Vary anchor text** across links pointing at the same money page ("our SEO services", "done-for-you SEO services", "professional SEO services"); repeating the identical anchor every time reads as manipulation.
- **In-body contextual links carry more weight than a sidebar or footer "related posts" block,** and links placed higher up carry more weight than three links stacked at the bottom. A bottom-of-page "related links" block is acceptable only as a fallback when no natural in-body placement exists. If no natural anchor phrase exists in existing text, write a short bridging sentence containing it ("We have a full breakdown on how much does SEO cost at Hey Tony").
- **Every blog post should link to at least one location or service page,** not only to other blog posts. Location pages can cross-link to neighboring location pages; a pricing money page can link to a relevant blog post and vice versa. Cap blog links from any one location/service page at 2-3; do not repeat the same blog link across every location page.

### Mechanics and ceilings
- **Use the CMS's "existing page" link picker,** never a pasted raw URL, when linking to your own pages: an existing-page link auto-updates everywhere if that page's URL ever changes, while a hardcoded URL breaks silently.
- **Internal links open in the same window/tab,** not a new one (a UX call, zero SEO effect either way).
- **Ceiling: 10-20 links per page** as a working limit; a hard maximum around 50-100 before it is unreadable and signals to Google something is off ("you'll actually get more out of doing less"). "You may also like" / related-product blocks count as internal links.
- **Automated interlinking plugins** (Link Juicer / Internal Linking Juicer) are fine to use but Matt avoids relying on them: no human judgment, so they can add a redundant link to a page already linked for that keyword.
- **Money-page vs blog cannibalization guard:** money pages should link OUT to blog content and authoritative sources and always include a convert CTA, but blog posts link TO the money page, not the reverse (link out to at most 2-3 essential resources from a money page). A blog post references the exact money-page phrase at most once, near the bottom as the link back, never repeated throughout.
- **Never build reciprocal internal-link exchanges or PBN "review trains" between sites you or friends control:** direct reciprocity is detectable and discounted. (This governs cross-site links; the inbound-from-old-posts move above is within one site and is exactly what you want.)

## Site Migrations, Redirects & URL Changes

- **Changing a URL/slug, even on "the same page," creates a brand-new page to Google:** it must be re-indexed, existing rankings may not carry over, and backlinks to the old URL go void unless redirected. "New kid at school, nobody knows who they are." Before changing any URL, check three things: is it ranking? does it get traffic? does it have backlinks? Change ONLY if all three are "no." If you do change it, update every internal link that pointed at the old one and set a 301. Even a textbook-correct 301 does not always fully preserve traffic ("we do everything right and the traffic still just doesn't carry over the way it's supposed to").
- **301 vs 404 vs 410:** replacing a page's content (even under a new URL) = 301 old to new, keeping the new content topically related. Deleting content with nothing to replace it = let the old URL 404, do not redirect. A permanently discontinued service = 410 (explicitly tells Google it no longer exists).
- **301 redirect priority order** when retiring low-value pages: a similar already-ranking page, then a similar category page, then a similar blog post, then the homepage (last resort).
- **Never redirect a redirect** (point straight to the final live URL). **Never blindly re-redirect back and forth:** check GSC for which URL actually has the traffic, keep that one, and monitor a month before removing the abandoned duplicate. **Redirect loops that never resolve to a live page are penalized;** straightforward consolidation redirects are not.
- **Seasonal/out-of-stock pages:** never straight-404 a product that might restock; hide the "Add to Cart" or set inventory to zero and leave the page live. Only fully remove (zero stock + 301) permanently discontinued products.
- **Never put a year/date in an evergreen page's URL** (it goes stale). Keep one evergreen URL, update the on-page year/title/H1 in place each year, and 301 any old dated URLs into it.
- **Migration checklist (CMS/platform change does NOT reset SEO if the domain stays the same):** keep a list of every old URL; keep every URL identical (including www vs non-www, which Google treats as different); carry over the same title tags, meta descriptions, and H1s/H2s; launch the *entire* duplicated site at once, never a subset (a half-migrated live site reads missing pages as deleted content, worse than shipping a full unoptimized duplicate). Prioritize internal linking over immediate H1 cleanup post-migration. Do on-page optimization *after* launch, not before. Verify #1 after any relaunch: did any URL change? If yes, 301 every old URL to its exact new counterpart immediately (not just homepage-to-homepage; anything without a clean 1:1 map goes to the new homepage), and confirm GSC/Analytics tracking on the new domain.
- **Full domain changes are high-risk:** expect to lose essentially all rankings and backlink equity even after notifying Google, "almost like starting from scratch" (a January domain change collapsed six years of rankings). Domain *forwarding* (old to new, homepage to homepage) is generally safe. Never change an established, recognizable domain just to force a keyword in or because a bigger name-confusable competitor is winning: exact-match domains "dropped in the last two Google updates" as a ranking help. If a domain is spam-damaged with nothing worth preserving, register a fresh domain and migrate the good content (one site started ranking within a month after the swap). Recovering lost backlinks after a bad migration: email the linking sites and ask them to point directly at the new URL rather than relying on the redirect.

## Web Design Principles for SEO

### Process and page architecture
- **Copy first, then layout.** Write all page copy before opening a design tool; the message dictates the section structure. Wireframe/mock up before building live (Figma, Canva, pencil, anything) to surface bad ideas early and lock image sizes; this step is optional, not mandatory. Reuse, do not rebuild: duplicate a working section, flip which side the image/text sits on, swap the background color.
- **Canonical homepage wireframe** (default service-business skeleton): Hero (H1 = focus keyword in plain language + subhead + one CTA, all visible with zero scrolling, plus a trust signal) to Trust row (~3 of: star rating, years, happy clients, licensed/insured, association logos) to About/intro (with its own CTA and audience-identifier icon boxes) to Services overview (each linking to its own page) to Testimonials to "How it works" process steps to FAQ to Final CTA. Most important messages near the top ("the longer it is, the less likely people reach the bottom"). One section = one H2 = one topic; alternate background tints section-to-section so each reads as distinct ("like a slide deck, one idea per slide"). Product sites reuse the same wireframe with product categories.
- **Hero proportions:** the header/contact block should occupy roughly 1/6 of the page, not half. Shrink oversized logos ("what the fuck is your logo doing so big", one ate a third of the screen). Do not show the logo twice (image + text) in the header.
- **Service-page IA (two tiers):** an overview/parent page that summarizes and links to each service (not pushed for ranking) + individual child service pages, one per service, where you go hard on SEO. Gives clean parent-to-child URL nesting. Long service lists: keep core services prominent, push the long tail into a mega menu/dropdown, each item linking to its own page.
- **Contact page:** phone, email, hours, socials, contact form, map/location; put the highest-priority contact method above the fold; the H1 does not need the keyword (label it "Contact Us"); never two contact forms on one page; use a static linked map screenshot, not a live embed. Anchor-link CTA technique (works in Elementor/Divi/Showit/Squarespace): give a section a CSS ID and point a button at `#contact` to scroll instead of loading a new page.
- **About page** is a trust page, not a life story; keep the exact same palette as the rest of the site (never let an interior page look like a different website); at least one visual element per section; include a real founder/team photo (humanizes: "you are a real person, not just a stock photo template"). Never right-align body text; minimize centered text.
- **Blog roll / archive is optimized for usability, not ranking;** the individual post earns traffic. Blog roll structure: 5-10 category names as plain links at the top (each to a real category archive), then the chronological preview list (newest first, capped ~50), no repeated category links partway down. Never build a filter widget that appends a `?taxonomy=` query string (Google does not treat it as a real page). If blog content was mistakenly built as Pages and is already ranking, leave the URLs alone and use Posts going forward.
- **Landing / funnel pages (paid traffic):** strip navigation to just a logo linking home; never list them in site nav; do NOT chase on-page SEO structure (it is fine, even expected, that an SEO tool flags them as orphaned); consider noindexing; exactly one CTA color; keep the one job undiluted.

### Conversion elements that touch SEO
- **Never use an auto-rotating image slider/carousel or an autoplaying hero video,** especially as the hero. A slider does not auto-advance so most visitors never see slide 2, yet every load still downloads every slide (pure cost, no benefit), and a carousel that freezes on hover hides its own H1 from most visitors. Replace with one static hero image (ideally real people/crew) plus persistent, always-visible descriptive text. On e-commerce specifically, the rotating promo hero should NOT carry the H1: put a fixed keyword-targeted H1 + short paragraph directly below it so the hero can change while the H1 stays put. Avoid the WordPress Revolution Slider (a speed drag).
- **Do not hide important SEO content behind accordions/dropdowns/toggles.** Convert FAQ and service content into always-visible H2 + plain paragraph so crawlers read it without triggering the toggle. FAQ blocks are plain question-then-answer text on the page, never behind an accordion. (Accordions are acceptable only for supplementary technical detail, or to pad thin word count where the expanded content is genuinely substantive.) Put an FAQ tied to that page's one focus keyword on every page, not one central FAQ page ("if all your FAQs are on one page, what are we ranking for?"); never repeat identical FAQ text verbatim across pages.
- **One dominant CTA per page/section,** solid and high-contrast; any secondary CTA must recede (outline/neutral). "If people have too many choices, they sometimes just choose not to make any choice." CTA copy always names the specific action ("Book a massage appointment", "Start your logo design"), never a bare "Learn more". A CTA in the hero, in every section, and at the very bottom of every page. Diagnostic: traffic fine but form fills low? First lever is CTA button color/contrast, not copy.
- **Trust signals:** hero star-rating build (5 gold stars matching Google's color + "Rated 5 stars on Google" hyperlinked to the real Google review link), consolidated into one prominent placement, not repeated. A live Google-reviews plugin can slow the page and sends NO extra trust signal to Google beyond the visible text; pasted review text still contributes word count/SEO. Real photos of the actual team build more trust than stock or AI. Screenshots read as more authentic than over-polished imagery.
- **Simplify navigation:** ~7-8 top-nav items max; move non-essential items (store, careers, policies) into the footer or an About dropdown; collapse per-condition/per-service links into one "Services" hub linking to sub-pages; never build a giant per-niche dropdown (terrible on mobile). Nav labels should match how the business actually breaks down (not a generic "Services"). Hand the site to a non-technical person and watch, unassisted, whether they can find a page. If the header nav is not sticky, replicate its links in the footer so the footer is never a dead end.

### Typography and color for SEO
- **Fonts:** one "spicy" heading font + one "boring" plain body font; the contrast creates hierarchy. More than 3 fonts noticeably slows the site; 2 is safe (extra important on Wix). Google Fonts is the default safe source. Font style does not matter for SEO directly; readability does. Body never below 16px (16-20px range, 20px standard); H1 ~48px start (60/64 used); H2 40px+; H3 32px; CTA 20px; body line-height ~1.8. Avoid cursive/script for anything that must be read quickly ("any friction is friction"). Never use a graphic/image as the H1: it must be live text (Google cannot read baked-in image text, and it does not scale responsively).
- **Color / contrast:** complementary colors (opposite the wheel) for maximum contrast on CTAs; analogous colors (adjacent) for cohesive backgrounds. Keep one color dominant and use the complementary color only as a small pop; never split a complementary pair 50/50 (mute the background, keep the CTA saturated). Contrast self-check: mentally strip color and view in grayscale; if the text is not clearly readable, there is not enough contrast (this manual test caught a failure an automated checker missed, which carries real WCAG/lawsuit exposure). Never pure black on pure white (reads as "vibrating"); use soft dark gray (`#191919`) on near-white. "When in doubt, make it black." Midtone grays fail contrast most often; gold text fails on white but passes on black. Color-to-audience: clean blues = trust/B2B; pinks/pastels = playful/kids; muted greens/beiges = organic/natural; bold lime or red on dark = gym/fitness; gold on black = luxury. Source palettes by searching "[vibe] color palette" on Pinterest. Corner radius as a brand dial: more rounded = friendlier (massage, baby photography), less = serious (cybersecurity, B2B).

## Page-Builder & Platform Playbook

- **Platform is not a ranking lever: "Google doesn't care about the platform you're using."** Any platform can rank with unique URLs, a sitemap, and good content. WordPress just has the most SEO features and control by default (unrestricted custom code, no plugin ceiling, email/push not available elsewhere), which is why agencies favor it. Do not platform-hop chasing a "gold standard": migrating means redoing everything and risks a temporary dip. Real exceptions where the platform IS a blocker: **WordPress.com** (a hosted blogging service, not for a full SEO business site: migrate to WordPress.org), **SmugMug** (templated image URLs like "image12345" get canonicalized as duplicates), and legacy gallery-only templates with zero ability to add text/headings.
- **WordPress:** default stack is WordPress + the **Avada** theme (Matt's go-to, "the number one WordPress theme", deepest tutorial bench); Elementor and Divi also in active use, pick by comfort. Add plugins one at a time as needed, no fixed list. Divi scatters styling controls: use inline CSS with `!important` as the standing workaround. Rank Math's redirect manager can silently "accept" a 301 without applying it (use a dedicated redirect plugin); its no-index toggle backdates a page if used long-term. **Elementor:** the Heading widget (not a text element) locks the semantic tag; a shared Elementor *template* means canonical/heading fixes apply to every page built on it (edit the template only if you intend that); clone a page via WP admin (Pages to Clone) then update Title + slug; paste Google-Docs copy into the *code* editor, not the visual one (which carries hidden style tags). Build a custom blog/single-post template in Theme Builder (Post Content widget auto-pulls the body; a Table of Contents widget anchors only H2/H3); a second active single-post template throws a conflict error (remove the old template's Display Condition first); new templates apply retroactively to every existing post.
- **Shopify:** collection pages CAN and do rank (optimize them like money pages); blog category pages basically never rank. H1 is auto-placed in the logo, and duplicate H1s are commonly injected by page-builder apps (GemPages): fix in `product.liquid` / `theme.liquid` via Edit Code (not the standard editor), self-fixable with ChatGPT or Sidekick (Shopify's built-in AI). Dawn theme auto-appends the store name to titles (find the toggle or the `[store name]` shortcode; flipping it retroactively changes every page, so confirm formatting first). Blog pagination often defaults to 6 posts/page: set to ~30 (raise to 60/100 as the blog grows, since more posts per page slows load). The URL-edit screen has a checkbox to auto-create a redirect. Use the native blog, skip third-party blogging apps.
- **Squarespace:** H1 size/style is globally template-locked (accept the large H1, keep the keyword in it); font-size fields can render in REM/% (switch to pixels for consistency); only two responsive breakpoints; category/tag archives editable only via code injection; animated section reveals are a crawl risk (Google's bot "scrolls" at a set pace and may miss unrendered content: cut reveal timing roughly in half). Image optimization is basically the only speed lever.
- **Wix:** accepts WebP; accent-color swatches capped at exactly 4 (plan the palette to fit); no server/code access (use an online converter for images, Wix support for hosting-level speed); built-in one-click background remover; template lock-in (switching templates means starting over). New-build sequence: skip the AI/ADI wizard, start from a Blank Template, set global Color Theme and Text Theme first (page transitions to None), add the Blog as an App (not a page), then build sections.
- **GoHighLevel:** pressing Return in an H1 field creates two H1 tags (use padding for the line break); developers commonly mark every heading as H1; the sitemap is not auto-surfaced (manually regenerate + resubmit); Core Web Vitals largely unfixable; auto-creates two blog pages by default (delete the unused one); fine for fundamentals but sacrifices CSS/speed control. Not the recommended host unless already tied to the CRM.
- **Square:** no true H1 field (its hover image-description reads as alt text only). **Kajabi:** inflexible blog template auto-pulls a body H2 oversized onto the roll (patch with inline `<span style="font-size:Npx">` or ChatGPT-generated CSS; the underlying heading should be H3/plain). **Showit:** sitemap fetch failures are a suspected platform limit; limited HTML control; migrating off it to WordPress preserves authority if the domain stays. **Ghost:** clean image handling and alt-text support (a positive for photographers vs SmugMug).
- **Building custom on-domain pages/tools with Claude Code:** describe your CMS/theme and ask it to build the page in that same builder so the code pastes directly into your native editor (keeps the page on your own domain). Do NOT build a website directly on Claude Code as the platform: use WordPress as the base and Claude Code for individual layouts/components. Always back up before letting an AI tool touch theme/`functions.php`. Landing pages should stay on your own domain when ranking matters; an externally-hosted page (Netlify) can convert but likely will not rank (still link back to your homepage from it).

## The Weekly Technical Audit-Fix Workflow

- **Audit tools and pricing:** Hey Tony Site Audit Tool / Rank Report Card ($10/mo, up to 3 sites, a full crawl takes ~1 hour; scores out of 100 with pass/fail per factor: page speed, crawlability, heading structure, alt text, meta length). Page Audit Chrome extension (free, pageaudit.com: live title, meta, and full heading breakdown). Detailed SEO extension (free, non-caching: title, meta, canonical, headings, OG). Screaming Frog (free tier / $245-yr). Semrush ($139/mo) and Ahrefs ($129/mo) bundle audits into the full suite.
- **Read the report by severity:** red = serious (blocks/hurts ranking, fix first), orange/yellow = warning (fix eventually), grey = low priority. Anti-overwhelm rule: **do not clear the whole report at once. Fix 5-10 issues per week,** starting with the red issues that have the *lowest count* to build momentum, then post the win and move on. Fixing one instance of a systemic issue often auto-resolves it site-wide (a theme-level setting). Batch on-page edits (titles, metas, H-tags) across many pages in one sitting are safe; publishing a large batch of new blog posts at once is NOT (roll posts out gradually, Google reads a high-velocity burst as spam-like instability).
- **Priority ordering when a site has many problems:** helpful content first (you cannot optimize what does not exist), internal linking as you write (self-solving if done concurrently), then backlinks. Page speed is last. Broken links and missing alt text outrank title-length/heading-count "errors" (which are low-severity, fix because "any variable we can control" is worth controlling, but never urgent). "Your website's never going to be done, fix the big stuff."
- **Before running any audit, never run it against a site still mid-construction** (results drown in temporary build errors); and before acting on any recommendation, **check where the page is actually ranking first**, if it already ranks well, do not touch it just because a tool flags a gap versus #1/#3.
- **Overwhelm, not the tactics, is "the number one thing that ruins SEO":** people quit feeling behind, not because the method stops working. Scope is deliberately capped (5 issues, not all of them) to prevent the burnout-driven quitting that stops people by week two. "This is not a sprint, it is a marathon."

---

# Part V - Off-Page SEO & AI Search (AEO / GEO)

Off-page is everything that builds your site's authority from *outside* your own pages: backlinks, Google Business Profile + citations, reviews, social, press releases, and Reddit. AI Search (AEO/GEO) is the same work pointed at answer engines - and in Matt's framing it is **not a separate discipline**: "everything we're doing is SEO, which AEO is part of SEO."

Two governing truths run through this entire theme:

1. **Content and on-page come first; off-page is authority layered on top.** The build order is always *helpful content → optimize pages → internal linking → then off-page (backlinks/PR/local)*. Don't chase paid backlinks early. In the Insiders curriculum, backlinks/directories training is deliberately gated to Level 5 ("Expert") behind everything else.
2. **"If you rank on Google, you will get recommended by AI. That's just the plain fact."** LLMs don't crawl the web fresh - they run a Google/Bing-style search at answer time and synthesize from the existing results. Rank organically first and AI citation largely follows.

**Off-page authority is now broader than backlinks.** LLMs build an "expertise profile" of you from mentions *everywhere* - guest posts, podcast appearances, Reddit threads, social - not just raw link count. A backlink is one vote; a mention next to your topic anywhere is also a signal.

---

## 1. Backlinks

### 1.1 Core rules & thresholds

- **You do NOT need hundreds of backlinks to rank.** Many Insiders rank #1-#3 on low-competition/long-tail keywords with **zero backlinks** (e.g. a page ranking 3rd for "Metal Roofing Vancouver," #1 for "wedding locations Hamilton" at 880 searches/mo with 0 backlinks). Matt's own LinkGap.io ranks #2 for "backlink gap" on a single 35-word page with **exactly one backlink** and outranks SEMrush, Moz, Ahrefs, and the exact-match domain backlinkgap.com.
- **Quality over quantity, non-literally:** "You can have a hundred 1%'s and that still doesn't equal the New York Times backlink." A link from a high-authority, long-established domain outweighs volumes of low-quality links.
- **Check referring domains, not raw backlink count.** "Backlinks are expensive and time-consuming to get. If I can avoid it, I will." One competitor's "430 backlinks" can collapse to a handful of real domains once you strip low-authority/nofollow. If the actual #1-ranked page for your target has **0 referring domains**, you can rank it with no link building at all.
- **One link from one domain is enough.** Additional links from the same domain hit diminishing returns - "any other links after that, they lose kind of value." (This overturned advice one member had received that a separate blog domain would generate valuable backlinks to the main site.)
- **A single *relevant* backlink to a specific page can outweigh a large sitewide count.** One case sat at position 3-5 with ~700 sitewide backlinks; the fix was 1-2 links pointed at *that exact page*, not more generic volume. Backlinks are **page-specific, not domain-wide** - always check follow vs. nofollow too.
- **Backlinks land more naturally on blog posts than money pages** - people link to genuinely useful informational content, not commercial pages. Write the blog post, then (optionally) point paid links at *it* rather than the sales page.
- **Nofollow links still carry real value** beyond link equity - brand credibility and "training AI" to associate your brand with a topic. Don't fixate on the follow/nofollow attribute; a nofollow link is still "another online mention, another place people can find you."
- **Out-of-region backlinks carry less weight** for a locally-focused business than same-state/same-region ones. Backlinks from your own country are best; other English-speaking countries (US/CA/UK) are fine.
- **Agency benchmark cadence: 4 backlinks/month for clients - "that's all we do," and it gets crazy results.** Explicitly NOT 4-10/week ("that's too many, you don't need that many"). For reference, HeyTony's own profile is 1,229 referring domains but only **598 active + follow**, built over ~5 years - raw counts overstate real equity.

### 1.2 Reciprocal links, ABC linking & PBNs

- **Never reciprocate links - one-directional only.** Even a single reciprocal swap "destroys the link equity you're building." The analogy: a stranger saying "she's the best" carries more weight than two best friends vouching for each other. Getting 10-20 people to link to you while you link to none is fine.
- **ABC linking** (A→B, B→C, C→A - no direct reciprocal pair) is one of Matt's favorite tactics; it's what backlink agencies run specifically to avoid the detectable AB reciprocity pattern that Google discounts.
- **Stop PBNs / friend-and-accountability-group link swaps immediately** ("stop doing that right away"). Four friends all vouching for each other reads as gaming; a Brad Pitt cold endorsement carries the weight.
- **Standard reply when someone asks you to place their link:** "Sure, but I need you to get me a link from a third-party site first" - they source yours, you place theirs.
- **When facilitating a directory/community, link only to members' *social profiles*, not their websites** - avoid the mutual "everybody links to each other" incest-hub pattern.

### 1.3 How to acquire backlinks (favorites, cheap/relationship-driven)

Run a **backlink-gap analysis first** to see what competitors have that you don't (LinkGap.io / Hey Keywords / Link Seeker / SEMrush) - most gaps turn out to be free directories or guest-post-friendly sites already listing your competitors. "They've already done the work for you." Then, in rough order of ROI:

- **Chamber of Commerce** - join, then ask them to build you a member landing page with your logo + **2-3 links to *specific* service pages** (not one generic "visit website"). Most chambers don't know SEO and will let you structure it however you want. Real results: one member went **3 → 12 backlinks for $75**; another paid ~$500/year plus $750 for a homepage link + featured profile. Value varies by chapter - vet the local one.
- **Charity / local sponsorship (Matt's own favorite):** a small donation ($20-50, or a "bronze sponsor" fee) gets your logo listed as a donor. "You're basically buying a backlink, but you're just donating to charity - 100% tax write-off." Make sure the **logo itself links** to your site, not just alt text.
- **Vendor/partner backlinks** - if you buy from or supply a local business, ask to be listed as a vendor/partner ("it'll help me sell your products more").
- **Unlinked mentions** - find every place already naming your business without a link, then **email them the exact paragraph already written with the link inserted** so all they do is paste it in (a weed-store client's rankings "went through the roof" after this). Set up **Google Alerts** on your own name for future mentions. Even paywalled mentions are worth a 5-minute ask.
- **Guest posting** - reach out to adjacent-audience sites offering to write content; **frame it as "I want to help you create content," never "give me a link."**
- **Automatic sources needing no extra claiming** - Chamber/association membership (auto-backlink once listed; add their logo to your site), event listings (Eventbrite auto-creates one), and any directory already listing/ranking your name (reach out and ask them to also link your website).
- **`.gov` domains** carry outsized built-in authority (only real government entities can register them). If a `.gov` directory lists businesses in your category, get on it.
- **HARO / featured.com** (the HARO successor) - browse journalist questions in your niche, submit a short expert answer with your link; batch it at ~20 min/day. Still works but saturated with SEO practitioners.
- **"Powered by / website design by" footer credit links** - a legitimate bootstrap tactic for new web designers, but early-stage only; graduate to press releases and local-association links.

**Guest-post structure (critical):** the host topic doesn't need to match your niche - the backlink is the point. Use **only ONE link back to your own site, placed in the top half** of the article, with **specific/geo-qualified descriptive anchor text** ("clean comedian, Boca Raton"), never a vague brand name. Bonus quality signal: also link to one of the *host's own* existing internal articles. **Never republish the same/similar piece on your own site** - it competes as near-duplicate against a page that's already sending you a backlink. Result to expect: one member converted their first Link-Seeker opportunity into a guest article on a Texas automotive site ("3365 Motoring") that delivered **143 clicks in 24 hours**.

**The "best-of" list technique** (Marcus Sheridan pool-installation case study): write a listicle naming every competitor in your market ("best pool installation companies in [city]"), say genuinely positive things about them, but **never hyperlink to any of them** - internal-link hard toward your own converting pages instead. You don't even have to include your own company (tested both ways, negligible difference in conversions/clicks). It ranks #1 for "who is the best [X]?" / "should I hire [X]?" searches and converts via the on-page internal links.

**Never say the word "backlink" to a non-SEO person** (a chamber, a local paper) - they won't know what it means. Ask instead: "Can I include a link to my business on your site/directory/profile?"

### 1.4 What to avoid & how to price it

- **Never buy backlinks from Fiverr** or similar cheap sellers; **ignore bulk-link spam pitches** ("100 links"). Named bad-value example: **Backlink Management IO** (~$40/mo bulk) - "don't do that."
- **The only real "Google partner" is a Google Ads partner** - nobody has special algorithm access; treat any vendor claiming otherwise as a red flag. A prior vendor charged one member $1,500 for 75 identical directory listings + $199/mo "refresh"; equivalent citation work costs ~$2/citation once.
- **Paid backlink benchmarks:** guest-post placements ~**$20-50** each (occasionally free). Paid services: **HOTH.com** ("good, but not cheap"), **thehoth.com Link Insertions** cheapest tier ~$175/link (DR/DA 20-30+), **GetMeLinks.com** ~$500/mo = 3 guest posts on DR 30 sites (~$166/link). ~90% of paid link-selling services are low-quality spam; only ~10% (legit blogger/publication partners) are worth pursuing.
- **Domain acquisition for consolidation:** if someone owns the exact-match domain you want, DM them directly (Instagram worked for one member), buy cheap (a $100 price is a clear "take that deal"), **migrate the real site to the new domain and 301-redirect the old one** - don't just point DNS. Never post a domain you're eyeing into a public/group chat.

### 1.5 Disavow: never

- **Never disavow backlinks. Full stop.** "In all the years I've been doing SEO, we have never disavowed links... my advice is never disavow. Never." It's impossible to know which "toxic"-looking link is actually propping up your rankings - multiple clients who disavowed after a scary SEMrush/GSC flag saw rankings *drop* as a direct result.
- **Dilute, don't subtract.** A "toxic"/"suspicious" audit flag is a dilution problem - keep earning legitimate links so the bad ratio shrinks - **never** a removal problem. Spammy/zero-authority referring domains (random directories, foreign-TLD junk) are normal for every site.
- **Only consider removal if the domain has no real traffic/rankings to lose.** To remove a genuinely toxic link: if you own the linking site (an old PBN), delete the link yourself; otherwise contact the owner directly (some comply free, some demand ~$50/link - treat a payment demand as extortion). Verify a flagged link is even real first: open the linking page's **View Source + Ctrl/Cmd-F your own domain** - if it's not in the code, the tool's data is stale/wrong. Cross-check SEMrush against GSC → Links → Top Linking Sites before trusting either.
- **Spam-score benchmarks:** keep under ~11%, ideally ~1% (you can't hit 0%). A **manual action** in GSC → Security & Manual Actions is the one signal that genuinely points to a backlink problem worth acting on.

### 1.6 Backlink tools disagree - read the trend, not the number

The same domain checked back-to-back can show wildly different counts: one live example ran **GSC 325 referring domains vs. HeyKeywords ~1,100 domains / 2,700 backlinks vs. SEMrush ~1,300 domains**. None is ground truth. In SEMrush, filter to **Follow** links only and check each linking domain's Authority Score; ignore "Removed/Lost." One domain linking hundreds of times ≠ hundreds of unique referring domains - and a single client-site footer link responsible for **100,000s of backlinks** reads as spam and can suppress indexing of everything but your homepage (**rule: if any single external/client site is responsible for >100 backlinks to you, remove your link from it**).

---

## 2. Press Releases (backlinks + AI-answer citation)

A real, repeated tactic with **three distinct purposes worth pursuing simultaneously:** (1) leverage for direct local-media outreach you couldn't otherwise get; (2) **AI Overview / answer-engine visibility** (the release gets treated as "in the news," and AI descriptions have been observed pulling language *directly from a client's own press release* when asked "who's the best X in [city]"); (3) shareable social proof that lets you talk yourself up without sounding self-promotional. Caveat from direct experience: **a PR-driven ranking bump has sometimes lasted only ~1 week before fading** - "if it works, it works," not guaranteed long-term.

**Case evidence:** one release produced **5 backlinks within ~5 hours**; a client's AI Mode ranking rose to ~3rd for a "best contractor" query the week after; Matt's own book "Get Found" - one AB Newswire release linked to his ranking blog post + Amazon listing - made the standalone term "get found" surface inside Google AI Overviews, picked up by USA Today.

### 2.1 Full build workflow

1. Gather **5-6 recent reviews max** (screenshots fine, from Google or anywhere) → upload the screenshots directly into **Claude** (Matt's pick - "much better than ChatGPT" for PR drafting).
2. Prompt it to write a press release weaving ~5 reviews around the target keyword phrase (e.g. "[Business] is a top-rated [service] in [City]"). Matt's exact press-release prompt is posted in the Insiders community as "press release prompt."
3. Output = "For Immediate Release" + dateline, headline, an aggregate-rating opening ("holds a 5-star average across 111 Google reviews"), a placeholder owner quote to swap for a real one, review quotes, and an "About [Company]" boilerplate.
4. Optional edit pass in a doc - swap in the real owner quote, fix placeholder/location mismatches.
5. Distribute (see providers below); set **PR Type = "web only,"** select all syndication outlets, **skip the meta-tags section.** Title field = headline only ("For Immediate Release" goes in the body). Write a **≤500-character summary.**
6. Upload a **real screenshot** image (or an AI composite: headshot + 5-star graphic + a real review quote). Add links (platform allows up to 5, **use only 2-3**): e.g. a Google Reviews link + a service-page link, with a real keyword phrase as anchor. Use your **CID link** for anything pointing at your GBP (§4.3), not a generic Maps link.
7. Same-day publish, preview links, submit. **~1-day turnaround.** If **rejected for formatting**, paste the rejection notice + your text back into Claude/ChatGPT and resubmit.

### 2.2 Providers & pricing

| Provider | Price | Notes |
|---|---|---|
| **AB Newswire** | **~$80 web-only; +$30 USA Today add-on = ~$110**; ~$500 bulk-credit tier (~$8-20/placement) | Matt's go-to for the DIY approach; syndicates to USA Today, AP News, Benzinga, Globe and Mail, Barchart, broadcast-station news sites. "AI doesn't care what it looks like." |
| **EIN Presswire** | $149/release normal; a June promo bundled 7 for ~$500 | Strong regional coverage in one case |
| **PR Newswire** | Pricier, demo-gated (not self-serve) | "Not ideal," untested live |
| Full human-reviewed PR service | ~$1,500-2,000 | The AB Newswire DIY route is explicitly the cheaper "B/C-tier" alternative |

### 2.3 Rules

- **A press release needs no real news.** Frame it as "[Business] is a top-rated [service] in [City]" and talk about the reviews. **No reviews yet?** Angle as a launch ("[City]'s newest [service]"). **Nothing to announce?** Milestone/anniversary ("celebrates 20 years"). A contest/award win is worth its own release.
- **One release = one topic / one business / one location / one keyword** - never combine two businesses, two locations, or multiple service keywords (same discipline as one keyword per page).
- **Frequency: 1-2 press releases/month max, ~2 weeks apart** (don't confuse this with the separate directory-listing cadence of 8-10/month).
- **Image must always be a real screenshot, never stock.** Use a **never-before-used photo** so that whenever that exact image resurfaces elsewhere (Google Images, other sites) you know it's a press-release pickup, not organic.
- Superlatives ("best") technically aren't allowed in PR copy - **Matt breaks this rule and it still works.** Just make sure something real backs the claim (reviews, an award, even a pay-to-enter contest win) - normal PR practice, not deceptive.
- **Never publish the press-release text on your own website** - the outlets are already linking to you, so hosting the same copy creates a reciprocal-linking pattern. **Share it on social + your email list instead.** PR copy does **not** need a humanizing/de-AI pass the way blog posts do.
- **Proactively pitch local media directly after distribution** - national wires typically don't include small local/regional papers. Go to the local publication's press/media contact: "I was featured in [national outlet], I'm local to you - want to do a write-up or interview?" For local businesses, **also get a release placed through the local newspaper specifically** - it sends a local-relevance signal a national wire doesn't.
- **Posting the win on social:** frame it as a "why we started this business" personal narrative; on Facebook ask friends/family to *share* (not just like) - one case saw ~10× normal views (~2,000 vs. ~50).
- **Book-launch structure:** announcement title = topic keyword + "book" + author ("How to Build a Bookkeeping Business: Book Launched by [Name]"); follow-up = topic keyword + "book" + accolade. **Amazon #1-bestseller play:** check your category ranking daily post-launch (a handful of sales can hit #1 in a narrow micro-category), screenshot the #1 badge immediately (it's fleeting), then issue a release announcing bestseller status and keep reinforcing that exact claim to feed AI answer engines.

**Backfire warning:** publicizing a growth-hack can neutralize it. Edward Sturm posted an Instagram video publicly calling the AB Newswire tactic "manipulating AI" → the resulting attention led the Globe and Mail to take its article down and the AI-cited link now 404s. Keep working tactics low-profile.

---

## 3. Reviews & Reputation

Reviews are a trust signal *and* a direct AI-recommendation lever: "if I type in best Italian restaurant near me, [AI] automatically looks for the ones with the most reviews and the highest average star rating." Businesses with strong reviews rank higher in the local pack; for e-commerce, a product's review volume/rating is itself a ranking factor.

### Do / Don't

**Do:**
- **Ask every single customer, consistently, without stopping** - steady arrival compounds. **Review velocity beats volume** for professions that can't solicit directly (therapists, etc.): ~**1 new review/week** via colleague/character testimonials; **~6 months of 1/week can outpace a stagnant competitor with a bigger total count.**
- **Send review requests as a direct, unfiltered link straight to the Google Business Profile.** A small incentive (e.g. **10% off next service**) is fine - just ask for "a review," never a specific rating.
- **Put reviews on *every* money page** (not just a reviews page): hand-paste 2-3 real reviews as **plain text**, rotating which appear where so the same text isn't repeated everywhere. Link each testimonial to its real source (Google/Yelp) plus a "Read more reviews" button to the full profile.
- **Embed review *text*, not just screenshots** - Google can't read text inside an image. A screenshot is fine for human visual trust; if you want the words to carry SEO/AI weight, feed screenshots into Claude and have it transcribe them as real text.
- AI-drafted review *replies* are fine - review/edit before posting, don't auto-post.
- Put location-specific testimonials only on the matching location page.

**Don't:**
- **Never review-gate.** No NPS/1-5 pre-screen (including inside a CRM workflow) before deciding who gets the review link - Google can **ban the entire Business Profile** for this. Always send the link unfiltered.
- **Never specify "5-star"** - just ask for "a review."
- **Avoid soliciting reviews while the customer is still on-site / being watched** (a restaurant table-tent QR). Google reads on-site solicitation as biased toward artificially positive reviews, and a competitor can report it to shut down the profile. **Texting/emailing the link later, once they're home, is the approved pattern.** (A QR card handed off *after* service completes is used in practice - the non-negotiables are: don't gate, don't watch, don't specify a rating.)
- **Never use a review-carousel plugin** - one added ~1,000 words of markup per page (hurting load time) and users scroll past carousels rather than clicking through.
- **Stop "review trains"** (groups of businesses trading review requests monthly) - reads as gaming, can get those reviews *and* other legitimate ones on the same profile taken down.
- **A sudden review cluster is a red flag** (5 within 20 minutes), especially if reviewers aren't local - **Google sees reviewer IP/location and weights accordingly.** Don't fake a "moved from elsewhere" story to mask location. General rule: **"if it feels sneaky, don't do it."**

---

## 4. Google Business Profile (GBP)

Treat GBP as your **discovery / local-pack asset** - and note up front that in Matt's own repeated testing **GBP appears to have little-to-no pull in AI-recommendation results** (searching "hey Tony reviews" surfaces Reddit and random sites, never his own GBP). So build it for local visibility, not as an AI-answer lever.

### 4.1 Setup & fundamentals

- **Requires a physical location or a service area.** A fully virtual/online-only business gets rejected. Verification now often needs **video** (recording yourself entering the building). A **service-area business** (no public address) is allowed and can upgrade to a physical address later without restarting. Don't publicly list a home address in schema/GBP for a remote business (safety).
- **Must be set to public** - a silent "not public due to missing information" error can block visibility for months.
- A GBP is assigned a **permanent CID once it's ~2 weeks old, valid for life** regardless of whether the share link ever changes.
- **Fill out every field and service** with keyword-rich descriptions. GBP service description limit: **300 characters**; work the city/keyword in **once** per listing (never repeated across every service entry, never a street address in the description text).
- **Address must be a real physical location** - the pin drives map-pack visibility (based on where the pin sits, not where the searcher is). A second GBP at the same address is possible with proof of a separate entrance; two businesses with different names can share one address and each get its own listing.
- **Renaming a GBP is safe** (e.g. adding "Bookkeeping" to the name if every competitor has the service word and you don't) - Google may delay the change but it should go through, and it does not go down/get suspended in the process; it reverts to the old name if declined.
- A GBP with **no website at all** can outrank fully-built competitor sites in local results - "shows how powerful just having a GBP can be." **Missed/unanswered calls hurt local rankings** (Google reads it as a bad user outcome).
- **Never click "Apply All"** on Google's recommended edits (GBP *or* Google Ads) - a client did this and both rankings and ad spend went sideways. Regularly **delete irrelevant auto-added services** (real cases had "telemarketing" and "magazine printing" auto-added).

### 4.2 Posting cadence & formula

- **Post at least 2×/week** for a serious map-pack push (Mon/Wed/Fri ideal); **1×/week is the floor.** Purpose is mainly to signal to Google that the profile is actively maintained - customers seeing it is secondary. Can be AI-drafted, tweet-length; the same content you post on social is fine.
- **Post formula:** start with the exact target keyword ("SEO agency in Hamilton") → link to the specific service page you want that keyword to rank → your **CID link** → a link to your **previous GBP post** (chaining your posts together). Roll the chain forward with each new post. Posting via a scheduler (social cross-poster, BrightLocal) counts the same as posting manually.
- **Photos:** batch ~**10 at a time, then leave a week-to-month gap** before the next batch (steady, not one-time dumps). Recommended size **1,000×1,000**. Geotag to the service location.
- **Recheck the whole profile monthly** - descriptions can be silently declined, publicly edited by others, or disappear "through no fault of your own."

### 4.3 The CID link

The CID link **passes more authority than a generic Maps place-page link.** Get it: open Google Maps → search your business → Share → copy the link → paste into **whatismycid.com** (or Matt's "What is my CID" tool). Fallbacks: View Page Source + Ctrl/Cmd-F **"ludocid"** (the long number next to it), or the **Plerdy** WordPress plugin. Final format = Google Maps URL + `?cid=[number]`. **Reuse the same CID link inside blog posts and service pages** wherever it fits, and make your on-site business **address a clickable CID link** rather than plain text - these links exist for the search engine, not human click-through.

### 4.4 Map-pack strategy (the full recurring pattern)

Post to GBP ≥2×/week → geotag every photo with the target keyword → chain posts via share-links → build service-area pages on the site, each linked to the matching GBP service category → keep NAP (name/address/phone) present and crawlable in the site footer, linking to the GBP via the CID link (Google "looks for that to determine if it's a local business") → ask for reviews continuously. One case sustained this ~1 year across two locations as "a very consistent lead generator." Reality check: a much older, completely inactive competitor (no posts, decades in business, 3× the reviews) can still outrank this "by a mile" - attributed to longevity/authority, not any single tactic gap.

**Diagnosing a dropped map-pack position:** (1) did you change anything recently? (2) compare review count AND *velocity* vs. top competitors; (3) confirm citations are built; (4) confirm NAP + CID in the footer; (5) check GBP services match/exceed the website (a mismatch can look like padding); (6) factor in that Google periodically updates its map-pack algorithm independent of anything you did.

**Geotagging photos** (Geo Imgr / "Geo Imager") is a genuinely disputed, low-cost, outcome-based bet - Google is confirmed to **strip EXIF metadata on ingestion**, yet clients using it still show correlated ranking movement. Vary the geotag across a grid of points in the target zone rather than tagging every photo to one spot; real phone photos are usually already geotagged. ChatGPT calls it "one of the most overrated tactics" - test on 1-2 clients, keep it if it correlates, since the cost (~1 min/photo) is trivial. Fundamentals still come first: more reviews, a complete profile, regular photos, a good connected website.

**Also:** link all active social handles to the GBP (searching the business name can surface recent social posts); replace live Google Maps iframe embeds with a static WebP screenshot linked to the real listing (Google's own PageSpeed flags its embed as a drag).

### 4.5 Citations (directory listings)

- **BrightLocal is HeyTony's preferred citation/local tool** (~6 years; ~$2/citation, roughly **$180-200 per full round, one-time - no ongoing management needed**). Also handles GBP post scheduling and local rank tracking.
- **Yext is an API overlay - you never own the citations built through it;** stop paying and they vanish. If you manage <10 citations, take direct control yourself. Migrating off Yext onto BrightLocal: build duplicates on BrightLocal, then **turn OFF Yext's sync toggle** for anything BrightLocal manages, or Yext will overwrite BrightLocal's data.
- **Bing Places** (import directly from your GBP - "takes two minutes") and **Apple Business Connect/Maps** (needs a DNS TXT record; must include "www" if your site uses www). **brightlocal.com automates** batch directory submission.
- **Never sign up for directories based in a country you don't operate in.** Named directories that function as citation/backlink builders: Bing, Yelp, Apple Maps, BBB (free basic listing; paid tier only buys "accredited" status), Trustpilot, bark.com, Yellow Pages/Yellow Book, Brownbook. Keep name/phone/address **identical across every listing** - inconsistency undermines the "legitimate business" signal.

---

## 5. Social Media (off-page signal & AI feed)

Social is a **minor, tiebreaker-level direct ranking factor** - its real value is indirect (referral traffic → time-on-site + traffic volume, both ranking signals) and as an **input that AI answer engines weigh**. Active social presence is a legitimacy signal for both Google and LLMs even at low follower counts - "any business who's not doing that is going to get left behind."

### Publish-day promotion checklist

After publishing a post, distribute it to prove to Google the content is getting traffic/links from *outside* your own site:
- Share as a **GBP post/update**
- Include in your **weekly customer/email newsletter** (only if genuinely helpful, not a sales pitch)
- Post to **Reddit** (relevant/local subreddit - doubles as a keyword-validity signal)
- Post a summary + link on **LinkedIn**, **X**, **Facebook**, and **Pinterest**
- Ask any **adjacent (non-competing) business contact** to link to it
- For a client: get the **client to post it on their own LinkedIn** (adds validity)

### Social rules

- **Post the identical piece of content to every platform** rather than tailoring per platform - 200 views on each of 10 platforms is 2,000 people/day for free; per-platform versions aren't worth the time. **Transcripts** (not just captions) get indexed/cited - a keyword spoken but never typed still drove a click.
- **Facebook-group tactic:** when someone in a relevant local/niche group asks a question you can answer, don't reply inline or drop your homepage link - **share a blog-post link that answers it.** AI and Google now pull results from local Facebook groups since "they're real people."
- **Never post links inside Instagram or TikTok posts/Reels** - not clickable; only the bio link is. On the bio link, **avoid Linktree/aggregators and link directly** to the destination (link equity passes to the middleman first, plus a redirect hop can fail) - the exception is a creator deliberately spreading attention across many platforms with no single destination.
- **LinkedIn needs professional framing** (content has to "make sense in the business world" even for a comedian/apparel brand) and **skip hashtags** (LinkedIn reportedly treats them like title tags and pulls attention off the post).
- **Cross-post via macro→micro:** treat the blog post as "macro" content covering many points, break each point into its own "micro" post/video (one tip per video), then produce more around whichever points resonate.
- **Embed social content (Instagram posts, YouTube Shorts) on blog pages** to raise time-on-page; **never build a widget that auto-pulls your latest social posts** onto the site (slows it, adds nothing). YouTube embeds carry extra weight since Google owns YouTube.
- **AI avatars / AI-cloned presenters kill trust** - one data point capped ~12 views before going dead vs. ~1,000-2,000/video once the real person appeared. "Where things are going is more authenticity, more off the cuff, more real."
- **Connect social profiles as GSC properties** (Instagram, TikTok, X, YouTube confirmed) - reports then show clicks/impressions for your social posts separately; live example saw ~56-63 clicks / ~130,000 impressions in the first 2 days after connecting, and one YouTube video alone added ~1,500 clicks surfacing for 320 keyword variations.

---

## 6. Reddit

Reddit is disproportionately powerful for **AI/LLM rankings specifically, not classic Google** - "many online brands are outranking competitors especially in LLM rankings (ChatGPT, Gemini), not so much with Google."

- **Insiders "Reddit Keywords" tool** (bright-orange box on the Insiders homepage / Tools section, built ~99% by Matt): type a seed keyword → it crawls multiple subreddits and returns the actual questions people ask, plus keywords, pain points, and content ideas, listing source subreddits. Treat the four output types **independently**: Questions → answer in-thread or via a dedicated blog post; Keywords → verify in Ubersuggest/SEMrush/Ahrefs; Pain points → blog subheadings; Content ideas → separate blogs or a local-service page. **Without the tool:** search `site:reddit.com [keyword]` in Google (Reddit's own on-site search is weak; Google has indexed it thoroughly).
- **Reddit engagement, three interchangeable modes:** (1) simple question → answer in-thread, optionally "if you want to know more, here's an example from [company]" + link; (2) broader question → write the full blog post, then reply on Reddit linking to it; (3) both on the same thread. **Genuine participation as someone who's actually used the product/service** got one member "almost immediate sales."
- **Build your own subreddit** and accumulate brand mentions there - per internal testing across hundreds of keywords, **links back aren't even required; mentions alone move AI Overview visibility "wonders," in every case seen.**
- A conversational post about your own brand/event, upvoted by your community, **got indexed and pulled into a Google AI Overview in under 24 hours.**
- **Reddit backlinks are nofollow** but still count as a genuine positive signal / "another online mention."
- **Reddit and Quora carry real ban risk** (auto-ban/mod-ban for low-engagement self-promotion; the SEO subreddit is especially strict) - even though years-old Reddit/Quora content performs well in AI-cited answers. **Zero measured search volume on a Reddit-sourced question is still real demand if the thread is active** - Google's "People Also Ask" is independent confirmation.

---

## 7. AI Search - AEO / GEO

### 7.1 The core model

- **"It's all just SEO."** Rank on Google first - LLMs run a live Google/Bing search at answer time and synthesize from roughly **5-10 existing results**; they don't have their own fresh crawl of everything. "If you rank on Google, you will get recommended by AI."
- **Google tightened bot crawl depth from the top 100 to the top 10** search results (around Aug/Sept) - a "massive change" that also blinds downstream AI-visibility tools; GSC remains the source of truth for a real position-24 ranking those tools can no longer see.
- **Bing is ~4% of global search but ChatGPT pulls from both Google and Bing** - so Bing-only questions are still worth targeting.
- **You cannot manipulate ChatGPT/Claude recommendations via your own private sessions** - zero effect on what other users see; if private chats fed public ranking "it would be so easy to game the system." Your own chat history only builds a private context that produces better outputs for *you*. **Using multiple AI tools to draft content doesn't improve external AI visibility either** - visibility comes from what's public on your site (though multiple models can improve final content *quality*).

### 7.2 What actually drives AI Overview citation

- **There is NO reliable correlation between ranking #1 organically and being cited in an AI Overview.** Re-running the identical search on 3 separate occasions, the same site was cited only ~**30% of the time** - AI Overview sourcing is unstable session-to-session, not a fixed lookup.
- **Mechanism (from a 100+-query internal study):** Google's AI **generates a claim/statistic first, then looks for content that *supports/agrees* with what it already said.** Citation isn't primarily about formatting, FAQs, or schema - it comes down to whether your content (a) **agrees with the general consensus the Overview is stating** and (b) **adds your own additional expertise on top.**
- **The tactic - "back up the claim, then pivot":** Google your exact target query, read what the AI Overview *asserts*, then **state that same claim first in your content and pivot with your differentiated info.** Don't contradict it outright. Worked example - if the Overview says "average kitchen renovation costs $50-75K" and you charge $25-35K, writing "we do it for $25-35K" alone won't get you cited; instead write *"The average kitchen renovation costs between $50 and $75,000 in [area]. However, we can do it for $25,000."* Origin validation: Matt's "how long does it take to rank on Google" post got out-cited 5 days later by a competitor who copied the idea but wrote it to *align with* Google's stated claims.
- **Broader levers found in internal testing (presence/volume over authority - a real departure from classic backlink-quality thinking):**
  1. **Broaden mentions across as many *different mediums* as possible** (press releases, social posts, Reddit) - presence/volume outweighs the authority of any single source.
  2. **Broaden geographic scope in written content** - write around the full state/province, not just one city, to maximize AI-Overview surface area.
  3. **Bake in time-relevance** - include the current year, matching how models silently append the current year to their own background searches (e.g. Gemini appending "2026").
  4. **Build a Reddit presence** (see §6).
- **Schema is not the deciding factor.** Matt runs **no schema** on his own site; his in-progress analyzer found that on the Hey Tony site, pages with **no ranking/traffic had *more* schema than pages that rank.** AI is optimizing to "pull the answer out and hand it back" - **extractability of the answer matters more than schema's presence.** (Yoast's auto-schema toggle is free and fine to leave on; don't build custom schema for AI purposes. Schema is only a *penalty* risk when the data is wrong/misleading, e.g. claiming "restaurant" when you're a marketing agency.)

### 7.3 Content structure for AI extraction (AEO on-page)

- **Answer the target question immediately, at the very top** - the single most consistent AEO instruction across every call. "There's no way to know how far they crawl on every page, which is why I put the answer right at the top." Restate the question as a subheading, then answer it plainly in the first paragraph and repeat the keyword/question near the top more than once. Model answers: *"Do backlinks help ranking on Google? The answer is yes... however, it depends on which kind and how many."* / *"Yes, ChatGPT can help with SEO, but it can't do it on its own."* Cut hedging ("the short answer is no") - just state it.
- **The "AI Markdown" three-extraction-point structure** (Matt's live experiment; the version that hit Google Discover with no other change):
  1. **TL;DR / Summary at the very top**, labeled, answering the question in 1-2 sentences an AI could clip verbatim.
  2. **Restate the answer** with more context in the opening paragraphs (a second extraction point).
  3. **Key Takeaways** at the end - 4-5 bullets reinforcing the same core facts (a third). Prompt: *"write me key takeaways for the end."*
  - **Collapse redundant closers** - don't stack separate TL;DR + Conclusion + Key Takeaways + FAQ that all restate the same thing. Prefer "Key Takeaways"/"Key Summary" over "TL;DR" as the label (TL;DR reads Reddit-native). A top TL;DR is only worth it for *longer* content whose first paragraph doesn't already carry the direct answer.
  - **Only test this on 2-3 pieces at a time**, never 10-20, or you can't attribute what caused what.
- **Front-load: Google effectively evaluates roughly the first ~500 words** - a real case used the keyword 91 times with deep research but its key-takeaways block sat *after* the dense research and the article stayed stuck "crawled - not indexed." Move takeaways/TL;DR to the very top.
- **FAQ blocks: plain question-then-answer text directly on the page - NEVER behind an accordion/toggle/dropdown**, which adds parsing friction for Google/AI. Cap at **3-4 questions**; a bolted-on generic 10-FAQ block is not a free SEO/AI win ("is this actually helpful to a human being? Probably not"). Each standalone FAQ question can also become its own blog post.
- **Write for humans, not "for AI."** AI evaluates content by how valuable it is to humans - "framing content to please an AI is the wrong mental model."

### 7.4 Crawler policy - never block AI bots

- **Never block AI crawlers, even when they're overwhelming your server.** "I firmly believe we should not be blocking AI from crawling our sites - how else are they going to recommend it?" **Do NOT use Cloudflare's one-click "block AI bots" toggle.** Reacting to falling click traffic by blocking AI crawlers is "the stupidest thing."
- **If AI-crawl volume genuinely crashes your hosting, fix it with better hosting + a Web Application Firewall (WAF), not by blocking bots.** Documented case: adding FAQ schema triggered **100,000+ simultaneous legitimate bot hits** (Apple, Meta, etc.), crashing shared hosting; Cloudflare's AI-block was already on and did NOT prevent it. Fix = move to cloud/VPS-tier hosting (~$30/mo) + a WAF. **If bots are flooding you, feed them more (publish more), don't throttle.**
- **FAQ schema is double-edged:** it can win real "Google's AI is now recommending me" outcomes *and* draw heavy bot crawl traffic (one case spiked to 150,000 visits/day vs. ~40 normal). The fix is to **block the bad bots (take the snippet to Claude and add a bad-bot rule) while preserving the schema earning the visibility** - never strip the schema.

### 7.5 Testing & tracking AI visibility

- **AI visibility cannot be tracked by any tool** - Semrush's "AI visibility" and similar invent their own test prompts and check if you show up, which isn't what real users type. "Anybody selling AI visibility, they are making up terms."
- **AI-*referral* traffic CAN be tracked** - in GA4/Looker Studio, filter dimension **"session source" contains "chatgpt" / "claude" / "perplexity"** to surface every session that arrived from an AI citation (one dashboard showed a **375% YoY increase** with zero deliberate GEO work).
- **Bing Webmaster Tools** already has a live **"grounding queries" report** showing which AI-answer seed queries you're getting cited for and which pages win them (sign in with a Google account, one-click import GSC).
- **GSC's "Generative AI" report** shows impressions only (no clicks) and isn't on every property yet - a partial picture.
- **Manual check:** Google your exact target query and read what the AI Overview asserts/cites.
- **CJ's proven backlink-timing sequence** (got AI to answer with the business *by name within 6 hours* of a program launch): ~2 months before launch, publish a blog post about the program + build its landing page as a placeholder (don't link it yet); on launch day publish a new post about the launch; immediately add a backlink from the original placeholder-era post to the correct new page (verify the URL) → an incognito search 6 hours later returned the business as the sole direct answer.
- **Cross-platform citation test:** write a "who's the best [service] in [city]" post naming your business at #2/#3 → post identical content to your Facebook page, X, and LinkedIn (skip LinkedIn hashtags) → check indexing with `site:` → force indexing via a free tool (primeindexer.com, ~7 days) → recheck the query. Note: **comments reportedly are NOT pulled into AI systems** - only public-facing posts count.

### 7.6 The reviews micro-site tactic (AI reputation)

Openly **not white-hat - "it is to manipulate the search results, which they don't want you to do."** A low-cost, disputed, outcome-based bet:

1. Register a domain like **"[BusinessName]Reviews.com"** - its **own separate root domain**, never a subdomain/hyphenated path off the main site (reads as a more independent third-party source to Google/Bing/ChatGPT).
2. Fill it with **real reviews written out as real TEXT, not screenshot images** (feed screenshots into Claude/Claude Code and have it transcribe while building). Pull reviews from anywhere they exist - Google, Reddit, email, verbal.
3. Build it cheaply/fast via **Claude Code** ("shouldn't take more than a couple hours"); host on Railway (free → ~$5/mo) or Netlify.
4. **Link FROM your main site TO the reviews site** (direction matters) from an already-indexed blog post; keep your on-site testimonials too (additive).
5. **Do NOT connect/verify these domains in Google Search Console.** If registering multiple, don't redirect them into each other.

Genuinely disputed even among practitioners (one call frames it as something Matt does with no seen downside; another as unproven/secondhand and untested by Matt himself, publicly disputed by another SEO) - theory is AI models may pick it up as a positive reputation signal; cheap enough to test either way.

### 7.7 Reverse-engineering an AI citation

Once an AI names your business, interrogate it: *"what did you analyze to recommend these companies"* and *"what search terms did you search for."* To turn it into leads, push further: *"who specifically are the names, phone numbers, mailing addresses of the property managers"* - then use that for direct outreach (personal letters + brochures).

### 7.8 llms.txt & agentic readiness

- Visit `yourdomain.com/llms.txt` to check if it exists - **Yoast auto-generates it** (WordPress, or Shopify via a plugin), no manual setup. Not mandatory, no confirmed ranking impact yet, but low-effort and expected to matter more as agentic crawling grows.
- **PageSpeed Insights' new "agentic browsing" score** (out of 3, at pagespeed.web.dev) covers llms.txt presence, "Web MCP," CLS, and accessibility-tree order - a low score here does **NOT** currently affect ranking in AI Overviews or ChatGPT; it only reflects whether an AI *agent* can operate the site.

---

## 8. Off-Page & AI Search - Numbers Quick Reference

| Item | Rule / number |
|---|---|
| Agency backlink cadence | **4 backlinks/month** per client (not per week) |
| Links needed to rank low-competition | Often **0**; one relevant page-level link can be the whole push |
| Same-domain links | **One is enough**; diminishing returns after |
| Single-source backlink cap | Remove your link if any one site sends **>100 backlinks** to you |
| Spam score | Keep under ~11%, ideally ~1% (can't hit 0%) |
| Press release cost | **~$80** web-only / **~$110** with USA Today / ~$500 bulk (AB Newswire); $149 EIN |
| Press release frequency | **1-2/month max**, ~2 weeks apart |
| PR links | Platform allows 5, **use 2-3**; image = real screenshot only |
| Citation cost | **~$2/citation**, ~$180-200 per full round, one-time (BrightLocal) |
| Review velocity (can't-ask professions) | **~1/week**; 6 months of that beats a stagnant bigger competitor |
| GBP posting | **≥2×/week** (Mon/Wed/Fri); 1×/week floor |
| GBP CID | Permanent after **~2 weeks**, valid for life |
| GBP service description | **300 characters**, city/keyword once |
| GBP photos | Batch **~10**, then week-to-month gap; 1,000×1,000 |
| AI Overview citation consistency | ~**30%** across repeated identical searches (unstable) |
| Google bot crawl depth | Top **10** results (was top 100) |
| Bing share | ~**4%** of global search (ChatGPT pulls both) |
| Content evaluated | First ~**500 words** front-loaded |
| FAQ cap | **3-4** questions, plain text, never accordion |
| AEO structure test | Only **2-3 pieces at a time** |
| AI-referral tracking | GA4 "session source contains chatgpt/claude/perplexity" |

---

## 9. Off-Page & AI - Master Do / Don't

**Do:**
- Rank on Google first; AI citation largely follows.
- Build backlinks from relationships (chamber, charity, vendors, unlinked mentions) - cheap, one-directional.
- Run PR for AI-Overview visibility + local-media leverage + social proof, ~1-2/month.
- Post to GBP ≥2×/week with the keyword-first + CID + chained-post formula; keep NAP+CID in the footer.
- Ask every customer for reviews via a direct unfiltered GBP link; embed real review *text*.
- Answer real questions on Reddit; build a subreddit for AI visibility.
- Structure content answer-first: TL;DR up top, direct answer in paragraph one, Key Takeaways at the end.
- "Back up the AI Overview's claim, then pivot" with your differentiated info.
- Let AI crawlers in; fix crawl load with hosting + WAF.

**Don't:**
- Don't disavow backlinks. Ever. Dilute instead.
- Don't reciprocate links, run PBNs, or say the word "backlink" to a non-SEO person.
- Don't buy Fiverr/bulk backlinks or trust a "Google partner" claim.
- Don't review-gate, specify "5-star," run review trains, or solicit reviews while the customer is on-site.
- Don't use review-carousel plugins or hide FAQ/answer content in accordions.
- Don't publish press-release copy on your own site (reciprocal pattern).
- Don't block AI crawlers or use Cloudflare's "block AI bots" toggle.
- Don't build custom schema hoping for AI citation - extractability beats schema.
- Don't trust any tool's "AI visibility" score, or connect the reviews micro-site to GSC.
- Don't treat GBP as an AI-answer lever - it's a local-pack/discovery asset.

---

## 10. Case-Study Evidence (off-page & AI wins)

- **LinkGap.io** (Matt's tool): #2 for "backlink gap" (behind 3 paid results), #1 in Germany, on a **single 35-word page with one backlink**, domain registered within the prior month, never connected to GSC - Google found and indexed it unassisted; ~14,000-15,000 email-capture form fills; also surfaced inside an AI Overview. Promoted deliberately *without* a direct link (name-dropped on Instagram/podcast) to force manual searches - Matt's working theory is Google uses browsing/engagement/conversion as an undisclosed ranking signal.
- **"Get Found" book:** one AB Newswire release linked to a ranking blog post + Amazon listing → the standalone term "get found" now surfaces in Google AI Overviews; picked up by USA Today.
- **Therapist in Hamilton:** blogged 1×/week ~1.5-2 years; **every public keyword tool shows zero ranking** for "male therapist Hamilton," yet he ranks live on **both Google and ChatGPT** for that exact query - 3-month waitlist, no ads, grossing ~$250K/year off waitlist demand. Proof niche off-page/authority wins are invisible to competitor tools.
- **"Bearded realtor":** ignores all SEO advice, yet ranks inside Google's AI Overview for a branded query - cited sources were **social posts (a colleague's Facebook post, his own Instagram), not his website at all.** Social signals alone won AI/organic visibility.
- **CJ's launch:** an AI answer engine named the business by name **within 6 hours** of a program launch via the pre-placed-backlink timing sequence.
- **Varuna's client** (B2B ERP): 4 blog posts → appeared in **ChatGPT and Perplexity**; posts hit Google's first page within 24 hours.
- **Gabrielle (HVAC):** one blog post + basic setup → ranked #2 and appeared **3× in AI answers** (once as top result, once in the sidebar).
- **Guest post → 143 clicks in 24 hours** (first Link-Seeker opportunity, on "3365 Motoring"); **PR → 5 backlinks within ~5 hours.**
- **Reddit post → pulled into a Google AI Overview in under 24 hours.**
- **Denise** (joined Insiders days earlier): ranking #1 with **Google AI Overviews recommending her site**, within days.
- **Josh:** a post published "yesterday" was already the **#1 cited reference in Gemini.**
- **Chamber of Commerce:** one member went **3 → 12 backlinks for $75**.

---

# Part VI - Tools, Local SEO, Ecommerce, Tradeoffs & Business

Matt Diamante's operating layer: the exact tools and prompts that run the method, how local and ecommerce sites are structured differently from everything else, the hard "don't" rules that override every tactic, and the business/mindset frame that decides whether any of it gets done at all.

---

## PART 1 - TOOLS & PROMPTS

### 1.1 The governing tool philosophy

- **Google Search Console is the single most important tool, ranked above every keyword tool and even above Google Analytics.** It is the only concrete, real (non-estimated) ranking/traffic data source, straight from Google. Set it up *before* making any keyword-targeting decision: "without Search Console, you really are just shooting in the dark." Use GSC as the definitive source of truth whenever third-party tools disagree.
- **Every keyword/backlink tool disagrees with every other tool, and with GSC, by wide margins for the identical domain.** One live example on one domain, checked back to back: GSC showed **325** referring domains, HeyKeywords showed **~1,100** referring domains / **2,700** backlinks, SEMrush showed **~1,300** referring domains. Ubersuggest routinely overstates volume (one term: **3,600/mo** on Ubersuggest vs. **750/mo** SEMrush vs. **600/mo** SE Ranking). Treat any single tool's absolute numbers as directional only; the "who is actually ranking for what" data is the part that's reliable across tools.
- **Set the country filter correctly in every tool, every time.** Data is "very different" per country for the identical term; a wrong country setting silently skews volume, difficulty, and traffic. Set to the country you want to rank in, not necessarily where you live.
- **Refresh cached data before trusting it.** SEMrush/Ubersuggest/Ahrefs show cached data (sometimes weeks or years stale); a keyword showing "N/A" difficulty just needs a metrics refresh (one term went N/A → 38% after refreshing). Click "update"/refresh to force current numbers.
- **A tool blind spot to know:** around Aug/Sept, Google restricted third-party/LLM tool access to roughly page-1-only SERP data ("Google basically spanked every AI LLM"). A genuine position-24 ranking confirmed in GSC simply won't appear in SEMrush/Mangools-style tools. The disagreement is a structural tool limit, not a ranking failure.
- **AI is a tool, never the decision-maker on strategy.** Claude/ChatGPT are fine for orientation, drafting, sanity-checks, and implementation tasks (writing missing code, generating schema). They are not the final call on keyword targeting, location-page expansion, or architecture: "make the decision not necessarily based on what Claude's saying, but on just what the actual data points are." ChatGPT specifically "will bullshit you," tends to agree with whatever you propose, and has produced keyword-stuffed headings when asked to architect content directly. "You are the expert, you're doing the research."
- **Don't chase 100% on any tool's health score.** 80%+ on a page audit is fine; a 90% site-health score is "fantastic." 100% does not correlate with a #1 ranking, and members with near-perfect scores rank no better than members who don't chase the score. "Sometimes you need that D to help you rank." (Exception: a paid SEO provider's *own* site faces a higher credibility bar because prospects scrutinize it.)

### 1.2 Keyword & competitor research tools

| Tool | Price | Notes |
|---|---|---|
| **SEMrush** | ~$130-150/mo; 7-day (sometimes cited 2-week) free trial | Matt's most-cited paid tool, called "most accurate" for volume/difficulty in most sessions. Genuinely contradictory stance: in one Jun-2026 session Matt says he's "stopped using/recommending it," calling it "way too expensive" post-Adobe-acquisition with reported billing/cancellation horror stories. Trust **Keyword Difficulty**; don't over-weight "Competitive Density." Free-trial trap: cancel immediately, they charge and reportedly don't refund. |
| **Ahrefs** | $129/mo; **Ahrefs Lite $29/mo, 100 searches/mo cap** | Comparable accuracy to SEMrush. **Trust Ahrefs over Ubersuggest on difficulty disagreements 100% of the time.** |
| **Ubersuggest** | ~$29-40/mo; lifetime $290 (individual) / $490 (multi-site) | Cheapest, least accurate, overstates absolute volume. Runs on a lifetime-deal model that's profitable because most buyers quit SEO within a month or two. Good for cheap bulk discovery, then verify the shortlist in a pricier tool. |
| **KeySearch** | ~$24/mo billed annually (~$20/mo), 200 searches/day | Named alternative. |
| **Mangools** | Limited free searches/day | Named alternative. |
| **HeyKeywords** (heykeywords.com) | ~$29-31/mo base (50 keyword + 10 domain analyses); upper ~$31-51/mo (150 + 30) | Matt's own tool, built via Claude Code over a weekend; pulls volume live from Google Ads (the source every other tool re-estimates). Discount code **HTKEYWORDS** = 50% off first month. Known gap: per-page backlink lookup returns 0 on pages that do have links. |
| **Google Keyword Planner** | Free | Directional only. **Don't use Google Trends to judge search volume** ("no, don't use that") - use a real keyword tool. |

- **Read the SERP's backlink profile, not just KD.** Referring domains, not raw backlink count, is the metric that matters ("backlinks are expensive... if I can avoid it, I will avoid it at all costs"). If the actual #1 page for your target has 0-2 referring domains, the keyword is winnable with zero link-building regardless of the tool's KD number.
- **KD ideal range: 0-15/20%; up to 25% "still possible"; 31% is "a little more difficult than I'd like"; ~90-100% is unwinnable for a low-authority site.** KD reads roughly as the domain authority you'd need to rank page 1. National KD can badly mislead local intent (a term can show KD 88 nationally with no single city accounting for that volume).

### 1.3 Question / topic discovery tools

| Tool | Notes |
|---|---|
| **answerthepublic.com** | Free: 1 search/day no account, **3/day with a free account.** Type the broadest version of what you sell → **Search Engines → Questions** → List view (skip the wheel). **Skip page 1; use page 2-4** (competitors rarely click past page 1). Scroll further for a **hidden Bing question set** most people miss (Bing = ~4% of global search; ChatGPT pulls from both Google and Bing). Set region to United States for volume. Crashes under heavy live load. |
| **Google "People Also Ask"** | Fully equivalent substitute - same method, same quality. Also check "People also search for." |
| **findquestions.com, alsoasked.com, answersocrates.com** | Interchangeable question-finders; type in what you sell. |
| **HeyTony Blog Idea Finder / Reddit Keywords tool** | In-platform. Reddit tool crawls subreddits for a seed term → returns questions + keywords + pain points + content ideas + source subreddits. Especially strong for LLM/AI-answer visibility, less so for classic Google rank. **Even when tools show zero volume, an active subreddit thread or a PAA box is proof of real demand.** |
| **rankweektraining.com, app.rwideas.com** | Matt's own question portals. |

### 1.4 Site & page audit tools

| Tool | Price | Use |
|---|---|---|
| **pageaudit.com** (+ "PA" Chrome extension) | Free forever | Cost Matt $30-40K to build, given away to lower the barrier; load-tested to ~20,000 concurrent. Content tab (word count, keyword occurrences, density), Metadata tab (title/meta), Overview tab (keyword presence in title/meta/H1). Extension has "Copy All Headings" and can sometimes see JS-rendered content the crawler misses. **Always ignore the overall score/percentage.** |
| **audit.heytony.ca** (Site Audit Tool / Rank Report Card) | **$10/mo or $99.99/yr, up to 3 sites** | Full-site crawler (~1 hr per crawl, 24-hr recrawl cycle): duplicate/missing tags, page speed, orphan pages, broken links, canonical/sitemap mismatches, missing H1s, low word count. Buckets: **Serious / Warnings / Info**, each with an embedded how-to-fix video. **"Manually validate"** clears false positives (e.g. a live link a bot couldn't reach). Does NOT do keyword research. Rotating discount codes each cohort (all mechanically identical, 1 month free, card required, cancel before renewal): RANKWEEK10, rankweek2026/RANKWEEK2026, June2026. |
| **HeyTony Watchdog** (watchdog.heytony.ca) | **$10/mo, 3 sites** | Real-time competitor *change* monitoring (title/meta edits, word-count shifts, pricing changes, pages added/removed, link changes) with a before/after diff. Catches you up in near-real-time instead of 3-6 months later via lagging rank trackers; surfaces unlinked "hidden" competitor pages. |
| **Money Page Doctor / Analyzer** | In-platform, **capped 20 audits/mo** | Paste a money-page URL → ~10-sec competitor-gap read (infers keyword, IDs competitors, flags word-count/density/keyword-mismatch/"blog detected but competitors are service pages"). **Always check where you actually rank before acting** - if already ranking well, don't touch the page just because it flags a gap. Reported competitor word counts can be flatly wrong (2,200-3,400 that couldn't be found on the page). |
| **Keyword Conflict Detector / Cannibalized Keywords Scanner** (+ keywordconflict.com) | In-platform | Auto-pulls sitemap, flags 2+ pages targeting the same keyword. Scan capped ~50 pages/run (bump toward 500). Not 100% accurate - cross-check flagged URLs against sitemap.xml/robots.txt; if absent from both, they're redirect artifacts, not real pages. |
| **Detailed SEO** (Chrome ext.) | Free | Non-caching; instantly shows live title tag, meta description, H1 count, OG/schema. Use to verify actual HTML vs. what Google displays. |
| **wordcounter.net / characterCounter.net** | Free | Verify real word count/keyword density on any AI draft - never trust the AI's self-reported numbers (one demo targeted 2,200 words, delivered ~1,700; targeted 20-45 keyword uses, delivered 13). |
| **whatcms.org / BuiltWith** | Free | Identify an unknown site's CMS / which CDN it runs. |

### 1.5 Other HeyTony Insiders tools (app.htinsiders.com)

Separate login from the community; sign up with the **exact same email attached to your Stripe subscription** (case-sensitive - a mismatched capital or typo silently fails to match). Add your site + set search country first. Full suite: **Blog Post Writer bot** (Claude-powered, interviews you ~7-10 questions, follows Matt's rules - **hard cap 10 generations/account**, and a *failed* generation still burns a slot), **Blog Idea Finder**, **Reddit Keywords**, **Topic Cluster Analyzer** (what Google thinks the site is about vs. what you wrote), **Link Gap Analyzer** (linkgap.io - backlink gaps vs. a competitor, email-gated full report), **Money Page Doctor**, **Keyword Conflict Detector**, a sitewide per-page target-keyword guesser. Built-in **AI help / "Wisdom" search** answers natural-language questions from the full call/transcript archive with source links. Coming: "Matt Bot 3000." Support: **support@heytony.ca** (Angela), not Matt's DMs.

### 1.6 The AI model stack

- **The dominant split: ChatGPT for the voice/interview capture, Claude for the actual writing.** ChatGPT's Whisper voice-to-text is "the best of the best." Claude "writes like a person," follows word-count/format instructions far more precisely, makes conservative edits on rewrites (vs. ChatGPT's over-rewriting), and is markedly better at spreadsheets/data (one member burned 5+ hours in ChatGPT on an Excel task Claude did almost instantly). Matt's recommendation shifted over time: "for writing, for everything... I recommend anybody get away from writing from ChatGPT, go to Claude." ChatGPT is still preferred for image generation and brainstorming.
- **Any LLM works for the interview/draft loop** - ChatGPT, Claude, Gemini, Grok, Copilot, Perplexity are interchangeable for that step. Gemini (free tier) is notably strong at meta-description length compliance and GBP-aligned copy, and at image generation from reference photos.
- **ChatGPT reasoning setting:** use "Instant" for the fast Q&A stage, "High" for the actual writing stage. ChatGPT degrading to one-line answers after ~10 posts in one thread is fixed by switching effort level or moving to Claude.
- **Cost:** Matt runs Claude, Claude Code, ChatGPT, Manus, Gemini - "a fortune in AI subscription fees," ~a couple hundred dollars/month. Claude's annual plan is cheaper than monthly. ChatGPT's ~$20/mo tier roughly doubled his output over the free tier.
- **Claude Code builds tools and on-domain pages, not the whole website.** Matt (a non-coder) built the entire htinsiders.com suite, HeyKeywords, and Money Page Doctor with it: "I don't know how to code, guys. I'm literally working with AI to do this for me." Use it to build a page *in your existing CMS/theme* so the code pastes into your native editor and stays on your own domain - don't run a website *on* Claude Code as the platform. Back up before letting any AI touch theme/functions files. (Its capacity estimates aren't reliable - it promised ~200 concurrent users on a tool that queued badly on the live call.)
- **Reviews micro-site build (see Don'ts §4 for the caveat):** dump review screenshots into Claude/Claude Code, describe the business, "here's what I like, build this out," host on Railway (~$5/mo) or Netlify. Transcribe reviews as real text, never post them as image/JPEG.

### 1.7 The exact prompt library

**Interview / clarifying-questions prompt** (the spine of the whole method; question count varies 5-10 by version). Cohort C / current canonical:
> "I'm writing a blog post answering this question. [paste in the question you found] Ask me five questions you need to know the answer to in order to write a truly unique and helpful blog post. It should include my expertise, experience, case studies, opinions, etc. Ask me the questions one at a time and wait for my answer before asking me the next question."

Fuller 10-question variant:
> "I'm writing a blog post answering this question: [question]. Ask me anything you need to know the answer to in order to write a blog post that is truly helpful and unique. It should include my experience, expertise, case studies, examples, opinions, etc. Keep it limited to 10 questions. Ask me them one at a time. I'll be using voice mode to answer them. Give me time to breathe as well before going to the next question."

- Answer via **voice mode** one question at a time (2-3 sentences each; rambling is fine, it "trains" the AI to your voice). If it defaults to ~30 questions, cap it: "ask me only 10 questions."
- Repurpose a transcript/podcast/video by appending: *"Here's a transcript from a conversation I had. Use that information when you can and where you can to pull my expertise, experience, all that kind of stuff."* Never hand over a raw transcript and ask for "a blog post."

**Write-the-post prompt** (current canonical, strips AI formatting clutter):
> "Write this as a clean WordPress ready blog post using my expertise, experience, opinions, stories, etc. Use H2 and H3 headings only. No horizontal rules, section dividers, tables, callout boxes or other formatting elements. Just headings, paragraphs and bullet points where appropriate."

**Meta description prompt:**
> "Write me a killer, compelling, click-worthy meta description for this page." (Generate ~5, pick the best.) Title tag: *"Write me a title tag for this page under 60 characters. The focus keyword is [X]."*

**Cover/featured image prompt** (attach 2-4 on-brand reference images):
> "Using the style of the images attached, create me a featured image for this blog post. Here is [topic] - you don't need any text on the image. Make sure not to include any of the exact images that are in these; make new ones in that style."

**Internal-linking prompt** (sitemap-based, Cohort C verbatim):
> "I'm looking for 3 incoming internal linking opportunities to this service/product page: [LINK TO PAGE]. Find me 3 relevant opportunities from my sitemap pasted below. [PASTE SITEMAP]"

**Money-page SEO-tags update prompt** (Cohort C verbatim):
> "Here are my current tags and my focus keyword. Update them so the keyword appears naturally, is front-loaded where possible, and matches the style and brand of my business. Also make sure each one is better than my two competitors': [PASTE YOUR AUDIT] Competitor 1 (Same Order As Mine) [PASTE] Competitor 2 (Same Order As Mine) [PASTE]"

**Money-page full rewrite prompt** (Cohort C verbatim):
> "Here is the content from my product/service page: [PASTE]. Here are the top 2 competitor pages that rank for my keyword: Competitor 1: [paste] Competitor 2: [paste]. My focus keyword: [keyword]. Rewrite my page so that: it is clearer, more helpful, and more persuasive; word count is between [comp low]-[comp high] words; keyword density is similar to the competitors; includes the keyword in natural positions; adds missing topics my competitors include; improves structure, readability, and expertise; keeps my brand voice; uses headings where appropriate; does NOT keyword-stuff. Produce the final optimized version I should publish."

**Section refinement prompts** (same thread): "You forgot these heading two tags, write a couple paragraphs each and expand on the ideas." / "Can you rewrite this section to be more funny and personable?" / "Ask me five questions to write a better unique piece of content using my expertise, experience, etc."

**Money-page identification:** "I am a realtor, what would be my money page?"

**Platform-mechanics (get unstuck on any CMS):** "How do I add a link to a blog post or to another page on my site from highlighted words?" then name your platform. General pattern: screenshot the screen/error, upload it, "Where do I click? What do I do?" + "Talk to me like I'm an idiot."

**Bot-blocking diagnostic:** paste the page URL into ChatGPT, Claude, and Google with "How many words are on this page?" Re-run once. If it consistently returns far fewer words than the real page (and title/meta come back "server not verified"), the host is blocking bots.

**Knowledge-base seeding (carry context between AIs):** "I want to make a .md file that has everything you know about me and everything that another AI would need to know in order to operate the same way that you do with me." Paste the result into Claude as standing context. Also: "Make me a document that will teach any AI everything you know about my business." Keep a client's knowledge doc to ~25-30 pages, not 50 - context overload dilutes output.

**Mining client-call transcripts:** "What are all the questions and answers that happened in these calls?" - "a gold mine for content."

**E-A-T self-audit:** after editing content, paste it to Claude/ChatGPT and ask for a grade on each E-A-T category plus specific improvements.

### 1.8 PR, backlink & local tools

- **AB Newswire** - press-release distribution: **$80** web-only, **+$30 USA Today add-on = $110** (recommended tier), **~$500 bulk credit** ("the 501") for repeat testers, or a ~$400 premium tier for ~20 placements (AP News, USA Today, Benzinga, Globe and Mail, Barchart). **EIN Presswire** - $149/release, a June promo bundled 7 for ~$500.
- **featured.com** (HARO successor) - journalist queries; batch 20 min/day. **HARO** - free, ~3 emails/day.
- **thehoth.com** - paid backlinks, $175/link tier (DR/DA 20-30+). **GetMeLinks.com** - $500/mo = 3 guest posts on DR 30 sites (~$166/link). **HOTH.com** - "good, but not cheap."
- **BrightLocal** - HeyTony's preferred local/citation tool (~6 years): **$2/citation, ~$180-200/round or ~$200 flat, one-time.** Also GBP post scheduling and local rank tracking.
- **Geo Imgr / "Geo Imager"** - image geotagging (5 free/day or ~1,000/mo paid). **whatismycid.com / Plerdy** - retrieve a GBP CID link.
- **Google Analytics (GA4)** - the only place to see AI-referral traffic (session source contains "chatgpt"/"claude"/"perplexity") and non-organic channels. **Looker Studio** - free GSC+GA4 dashboarding. **PageSpeed Insights** (pagespeed.web.dev). **Bing Webmaster Tools** - one-click GSC import, supports IndexNow.

---

## PART 2 - LOCAL SEO

### 2.1 The page-vs-post dividing line

- **"We offer this service in this town" = a dedicated page. "X vs. Y" / comparison / informational / local-color content = a blog post.** A brand-new business location gets a page, not a post. Static/evergreen info meant to rank for a money keyword = page; a specific one-off question = post.
- **One keyword = one page = one service = one location, always.** Never build one page for the same city targeting two services ("you're not even getting a slice"). Never combine multiple cities in one post - cycle city by city.
- **Adding a location makes it a whole new keyword.** "We buy junk cars Dallas" and "...Houston" are not cannibalization no matter how similar the template, *provided* the location-specific body copy is genuinely substantive.
- **"Near me" is never a target keyword.** Google connects searcher + business location automatically. Targeting "near me" literally in copy or URLs is "the sign of somebody who doesn't know how to do SEO" / "amateur SEO." Support proximity with real local signals instead (explicit service-area names, a visible address).

### 2.2 Location-page architecture

- **Homepage = your true home-base/flagship market** on the single service that makes the most revenue. Home base can carry one page per service ("Chicago Newborn Photographer" AND "Chicago Family Photographer"); every *satellite* location gets only ONE service page (the one easiest to rank there), mentioning other services in passing.
- **City-size sizing rule:** a ~500,000-population city (Hamilton ≈ **15,000 small businesses**) justifies targeting the whole city as the geo-modifier. A 3-4 million metro (Toronto) is too big - go **neighborhood-level** instead (people won't cross a huge city for a local service). Neighborhood pages work the same for named sub-areas ("junk removal Leslieville," "landscape lighting Montreal").
- **Prioritize smaller towns/suburbs over the big nearby city** - almost nobody targets them, and a location page usually cannot outrank a real local competitor's homepage (their de-facto money page, most-backlinked page) without dedicated backlinks. A Toronto-area photographer was told to drop "GTA wedding photography" entirely for "Toronto wedding photographer," then build individual pages for Hamilton, Stouffville, Mississauga, Oakville, King City.
- **Too small/new to rank at city level → target state-level keywords first, then build pages for the top 10-20 highest-population cities.** A brief mention + link at the bottom of an otherwise-generic post ("if you're looking for website design in West Virginia →") is enough; a full hub/pillar structure isn't required.
- **Service-area hierarchy, not a flat link dump:** top page lists sub-regions/counties → each links to a county page listing its towns → each town gets its own page (which can list neighborhoods). One case replaced a flat list with ~10-20 pages.
- **Avoid the combinatorial explosion.** Don't build every location × service (one case would have been 66 pages: 25 cities × 6 event types). Build one page per location with sections per service, and only build a dedicated combo page where keyword research confirms real volume (~5 of 66 in one case). A ~200-page HVAC service×city matrix was flagged as overreach.
- **Location pages must be genuinely unique per location** - real landmarks, venues, funeral homes/hospitals/high schools (for a florist), delivery-time specifics, seasonal color. **"You need 100 original, my friend."** Copy-paste-with-city-swapped at scale risks demotion. For non-delivery/remote services, anchor each city page in genuinely local hooks (nearest hospitals, local grocery stores carrying your product, local gyms/trails).
- **Rollout: ~1-2 unique pages/week.** A 12-location build finishes in ~3 months without burnout; even a huge client is paced at ~2/week ("sniper rifle" over "shotgun"). **Stop once a subset is already ranking/converting** - you don't have to finish the whole list. **Expect 3-6 months (up to a year) for a new location page to move.**
- **Nav:** a "Locations" hub in header/footer → hub lists every location → each links to its page. Link new local pages directly from the homepage ("areas we serve") to index faster; footer-only links index slower. Nest location pages under a standalone Locations hub, never inside one service page.
- **Layer local into broad content:** even a broad how-to post should carry a local CTA with an anchor link ("If you're looking for a hairstylist in Denver, [link] give us a call") plus NAP in the footer and a link to your GBP.

### 2.3 Google Business Profile (the full playbook)

- **GBP post formula:** target keyword at the very top (optionally in quotes) → link to the specific service page you want that keyword to rank for → your CID link → a link to your *previous* GBP post at the bottom (chain posts together). Roll the chain forward with each new post. Signals an active, interconnected profile.
- **Getting your CID link:** Google Maps → your business → Share → copy → paste into whatismycid.com (or the Plerdy plugin, or View Source + find "ludocid"). A GBP gets a permanent CID ~2 weeks after creation that stays valid "for life." Matt's claim: the CID link passes authority where a generic Maps place link doesn't. Reuse it in blog posts, service pages, and as the linked business address on your site.
- **Posting cadence: at least 2×/week (Mon/Wed/Fri is the working minimum); 1×/week is the floor.** One aggressive test case ran 6×/day. Purpose is primarily to signal Google the profile is actively maintained; a scheduling tool counts the same as posting manually. Posts don't need to be promotional - a tweet-length weekly summary works; start every post with the exact keyword you want the profile to rank for.
- **Service description: 300-character limit.** Work the city/keyword in **once** per listing in natural copy; never repeat it across every service entry; never put a street address in the description text. Fill out **every** listed/suggested service with a brief keyword-rich description. Caution: listing *more* services than your website documents can read as padding - audit for a services/website mismatch.
- **Photos:** batch ~10, then wait a week to a month before the next ~10 (steady, not one dump). Recommended **1,000 × 1,000 (square)**. Geotag to the service location.
- **Recheck the description and full profile monthly** - descriptions get silently declined or publicly edited "through no fault of your own." Regularly delete irrelevant auto-added services (real case had "telemarketing" and "magazine printing" auto-added).
- **Profile must be set to public** (a silent "not public due to missing information" error can block visibility for months). Profile strength can drop 100% → 80% on its own; clicking "complete" routes to Google's paid ~$27/mo bundle and doesn't restore 100% free.
- **Verification:** fully online-only/no-service-area businesses get rejected; multi-location now often requires **video verification** (recording yourself entering each building). A **service-area business** (no public address) is allowed and can upgrade to a physical address later without restarting. A second GBP at the same street address generally needs proof of a physically separate entrance (a window sticker sufficed once). Don't publicly list a home address in schema/GBP for a remote business (safety).
- **Never click "Apply All" on Google's recommended edits** (GBP services or Google Ads recommended changes) - a client did both and rankings + ad spend went sideways.
- **A GBP with zero website can outrank fully-built competitors** in local results - for a business with no web presence, get a real GBP live before anything else. Missed/unanswered calls hurt local rankings (Google reads poor call responsiveness as a bad outcome). The GBP pin must sit at the actual physical address (a Mexico rental targeting US bookers still pins in Mexico).
- **Rename a GBP freely** (e.g. add "Bookkeeping") if every local competitor has the service word in their name and you don't - Google may delay it, but it should go through, and it keeps existing reviews. A name change tied to a DBA/press release is safe to run in parallel (if declined, it reverts, no suspension).
- **GBP appears to have little pull on AI-answer results** in Matt's own repeated testing - treat it as a discovery/local-pack asset, not an AI-visibility lever.

### 2.4 Citations

- **Do local directories with a real physical presence/service area** - chamber of commerce, local newspaper, local business directory (they send local-relevance signals). National/global generic directories are lower-value but not harmful. **Never sign up for directories in a country you don't operate in.** Skip local directories entirely for a nationally-shipped ecommerce brand with no storefront.
- **BrightLocal builds citations at ~$2 each** (~$180-200/round, one-time, no ongoing management). **brightlocal.com** also auto-submits to a batch of directories. Also import to **Bing Places** (from GBP, ~2 min) and **Apple Business Connect** (needs a DNS TXT record; include "www" if your site uses it). Pull a dominant competitor's backlink/citation profile and get listed on the same ones - "they've already done the work for you."
- **Yext is an API overlay - you never own the citations.** Stop paying and they disappear (one case: an annual plan built "4-5 pages," a year later only 8 citations remained). If you manage fewer than ~10 citations through Yext, take them over yourself. If migrating to BrightLocal, turn OFF Yext's sync toggle for anything BrightLocal manages or Yext will overwrite it.
- **Never say the word "backlink" to a non-SEO person/org.** Ask: "Can I include a link to my business on your site/directory/profile?"

### 2.5 Reviews, reputation & the map pack

- **Never review-gate.** No NPS/1-5 pre-screen before sending a review link; that includes a CRM automation that pre-screens sentiment. Google can **ban the entire Business Profile.** Always send a direct, unfiltered link straight to the GBP.
- **Never ask for a "5-star" review - just ask for "a review."** A QR-code business card + a small incentive (e.g. 10% off next service) is fine; specifying the rating is not.
- **Avoid in-person QR-code review asks** (a customer or competitor can report it and get the whole account shut down); text/email the link later once the customer is home - the Google-approved, more-honest pattern.
- **Review pace beats volume, especially for professions that can't ask clients directly** (therapists/counselors → colleague character-testimony reviews). ~1 new review/week; ~6 months of 1/week can outpace a stagnant competitor with more total reviews.
- **Sudden review clusters are a red flag** (5 within 20 minutes), especially if reviewers aren't local - Google sees reviewer IP/location. **Stop "review trains"** (groups trading review requests) - reads as gaming, gets reviews taken down, and drags down other legitimate reviews as collateral. General rule: **"if it feels sneaky, don't do it."**
- **Never use a review-carousel plugin** (adds ~1,000 words of markup, hurts load, users scroll past). Hand-paste 2-3 real reviews as plain text on each money page, rotating which appear where. **A review screenshot is fine for human trust but Google can't read text inside an image** - embed the review's actual text if you want it to carry SEO weight. AI-drafted review replies are fine (review before publishing, don't auto-post).
- **Map-pack playbook (the recurring winning pattern):** post to GBP ≥2×/week; geotag every photo with the target keyword in the file/metadata; CTA/click-to-call + website link on every post; chain posts via previous-post share links; build service-area pages linked to matching GBP service categories; ask for reviews continuously. One case sustained this ~1 year across two locations for a "very consistent lead generator" - but a decades-old, completely inactive competitor can still outrank it "by a mile" on longevity/authority alone.
- **Diagnosing a dropped map-pack position:** check whether you changed anything; compare review count AND **velocity** vs. competitors (velocity can beat higher total count); confirm citations; confirm crawlable NAP in the footer linking to the GBP via CID; check GBP services match/exceed the website; factor in that Google updates its map-pack algorithm independently.
- **Geotagging is genuinely disputed** - ChatGPT calls it "one of the most overrated tactics," Google strips EXIF on ingestion, yet Matt's agency reports correlated results. Test on 1-2 clients, keep it if it correlates; the cost is low enough to run regardless. Fundamentals (more reviews, complete GBP, regular photos, a good connected website) come first.

### 2.6 The local + broad-content tradeoff

Out-of-area traffic that can never convert locally is still worth it - it costs nothing extra and builds engagement/authority signals (time on site, page visits, form fills, newsletter opens) that indirectly help your local/transactional rankings. "If I'm getting traffic from five towns over, somebody's not going to hire me. That's totally fine. That is helping my website show up higher in my local area." Do **not** jam your target city into general how-to posts to force geo-relevance - one member's edit inserting a town name into broad-ranking posts (on ChatGPT's advice) dropped traffic; reverting all affected posts at once is fine, give it 1-2 months.

---

## PART 3 - ECOMMERCE

### 3.1 Homepage / collection / product keyword split

- **Stop trying to rank the ecommerce homepage for one keyword.** Give each featured product a clean homepage section with descriptive text; push actual ranking onto **collection and product pages.** The homepage just needs to make a visitor understand what the site is once they land from an entry page.
- **Collection page = the broad, competitive keyword** (repeated in the collection title, every product title in it, and body copy). **Product page = specific/attribute-based** ("polyester paddle shirt," "18-karat gold engagement ring"). Reinforce a collection by repeating its exact keyword phrase in every product title inside it.
- **Shopify collection pages CAN and do rank** (unlike blog category/tag pages, which basically never do) - optimize them like money pages.
- **You cannot rank for a keyword without a page built around it.** "Everybody's trying to get through the front door... I want to go through the back door where nobody else is going." Put high-intent/transactional terms ("Scorpio candle," "buy ghost peppers hot sauce") on collection or product pages, not blog posts.
- **Rough volume floors for a low-authority site:** product pages ≥ ~30 monthly volume, collection pages ≥ ~50 (can go lower for a brand-new site). Singular vs. plural can carry very different difficulty - check both ("tennis t-shirts" KD ~16 vs. "tennis t-shirt" KD 8 at higher volume; the singular won).

### 3.2 Shopify collection-page structure

**"The biggest missed opportunity when I look at a Shopify store":** intro sentence(s) → product grid → long blog-length paragraphs with images underneath, covering the collection in depth. Put marketing/info copy **below** the grid, never above it (someone on a collection page is ready to buy, not read; especially on mobile). Add real product photography (a person using/wearing the item) with descriptive alt text.

- **FAQs on collection pages first** (broadest reach, far less labor than per-product), built as Shopify's native collapsible-row component. Write them as plain H2 questions (not labeled "FAQ") answered in natural human language that reincorporates the keyword a few more times ("How long does the temporary tattoo last?"). Two payoffs: preempt purchase-blocking questions (conversion) and feed long-tail/AI search, since people now type full sentences. For near-identical SKUs (jewelry, collectibles), write product-specific FAQs (carat, metal, care) - **never duplicate the same FAQ block across every page.**
- **Use the native blog, skip third-party blogging apps.** Shopify blog pagination often defaults to 6 posts/page - set to ~30 (then 60, 100 as it grows). Ensure every post has a featured image.

### 3.3 Product naming, keywords & duplicate SKUs

- **Name products what real searchers type, not invented brand language.** Type the plain physical/functional description into a keyword tool, find the phrase with real volume + low competition, and rename the actual product title (not just alt text) to that phrase; append the cute/brand name at the end, never the reverse. Cases: a "cream beaver fur hat" under a made-up name → "beaver fur top hat" (260/mo Canada, 880/mo US); Irish-named candles → "Vanilla Soy Candle" (~30/mo) with the Irish name appended; a product filed under generic "novelty bongs" → "octopus bong." Get explicit client sign-off before overriding a preferred name.
- **Novel product with no search demand:** don't force the keyword nobody Googles - identify the underlying problem the user searches ("nobody buys my book, what do I do") and build content around that. Or write an "[established competitor product] alternative" page.
- **Portfolio strategy when no single head term has enough volume:** build many small transactional variants (per zodiac sign, per birth month, "funny tennis shirts") plus one hub/master post linking to each. "Cosmos Within" candle brand: "horoscope candles" ~19 KD/~110 mo, "Scorpio candle" zero difficulty.
- **Duplicate content across near-identical SKUs/locations:** for low-stakes near-duplicates (an escape-room booking page for Anaheim vs. Connecticut), differentiating only the title tag + meta description ("Booking - Anaheim") can be enough. A page meant to independently rank for its own local keyword still needs genuinely unique body copy.
- **Multi-niche stores** (tennis + padel + horseback apparel) create real per-niche research friction - each niche needs its own research and doesn't share an audience - but can work under a unifying "sports" frame.

### 3.4 Seasonal, reviews & pipeline

- **Publish supporting content BEFORE the thing is ready** so it's indexed and ranking when demand hits. A florist should optimize for major gifting holidays ~6 months out, not a month before; a Super-Bowl-driven location page starts ~6 months ahead. Write "gifts for a May birthday" months before that demand spike.
- **Seasonal/annual pages:** keep ONE evergreen URL with no year in it; update the title/meta/H1 to the new year each year (2026 → 2027) rather than making a new page - preserves accumulated equity. Never put the year in an evergreen URL.
- **Seasonal money pages:** build a dedicated page per key season (Black Friday, Christmas, Valentine's); keep the URL live year-round but pull the nav link out of season (Google still knows the URL exists).
- **Reviews are a direct ranking factor for ecommerce product listings** - a product with ~5,000 five-star reviews gets surfaced above comparable products with fewer/weaker reviews.
- **Blog-to-paid-product pipeline:** publish the free/shorter version as a blog post, then sell a longer detailed version as a standalone paid guide (Jackie's curly-hair guide sold to people who never come in). **Turn a recurring support question into a reusable asset** - write the how-to once, send that link to every new customer (Matt's team's "how to add/remove users from Meta Business Manager" post replaced a 30-60 min onboarding call for every new client and later earned organic traffic).
- **Directory/aggregator SERP:** if directories outrank you, get listed on them (free) rather than out-content them - it sends a legitimacy signal. **GBP for ecommerce** is only for a real storefront/service area - a nationally-shipped brand skips it.

---

## PART 4 - TRADEOFFS & DON'TS

### 4.1 The cardinal rule: never touch a page that's already ranking

The single most-repeated rule in the entire body of teaching, stated independently and forcefully in nearly every call: **if a page is ranking for anything - even a keyword other than the one you intended - leave its content and URL alone.**

- It applies **even when the page violates every other rule**: duplicate H1s, keyword stuffed 122×, hidden overlay text, thin content, zero backlinks. "I don't give a shit if you have 31 heading one tags when you should only have one. If you have 31 of them and you're ranking number one, I'm not touching that page." / "If it's ranking, don't touch the text. I don't care if it doesn't match your brand guidelines."
- **You can't rank higher than #1 - touching it is pure downside risk.** Proof: Matt's own "SEO in Hamilton" page hit #1 after ~1 year on internal links + anchor text alone, never edited ("did anybody touch this page? All we did was internal link to it"); his web-design page held #1 for ~2 years on 600-800 words. The trigger to re-audit is *after* rankings actually drop, never before.
- **If it's #1 but converting poorly:** tiny incremental edits only (one sentence, one button, a CTA). UX/CTA polish is the one still-safe category - never a full content rewrite.
- **If it's ranking but flat-traffic:** don't rewrite it; keep publishing easier-keyword blog posts and internally link them to it.
- **If it's NOT ranking:** wait 3 months, then 6 months (internally linking with descriptive anchor text meanwhile) before touching content. Only rewrite from scratch once you're sure it isn't ranking. "Most of the time, if you're not ranking, you're either doing too little or too much" - resolve by comparing against the actual top 3, never a fixed rule.
- **Freshness-gaming caveat:** Google sometimes deliberately suppresses a newly-published/updated page, then waits to see if you panic-edit (which itself reads as a spam signal). Give a page ~1 month after publishing/editing before touching it again.

### 4.2 The consolidated Don'ts

**Don't**
- **Don't chase 100% / perfect scores** on any audit tool (Page Audit, Yoast, Rank Math, accessibility). 80%+/90% is enough.
- **Don't disavow backlinks. Full stop.** "In all the years I've been doing SEO, we have never disavowed links... never." Some clients who disavowed after a scary flag saw rankings drop - a "toxic" link may be secretly helping and there's no way to know which. Dilute (build more good links) instead. Only consider disavowing if the domain has no real traffic/rankings to lose.
- **Don't act on "toxic"/"suspicious" backlink flags by default.** Verify a flagged link is even real (View Source + Ctrl-F your domain; cross-check GSC Links vs. the tool). Spam-score benchmark: stay under ~11%, ideally ~1% (you can't hit 0%).
- **Don't buy cheap backlinks from Fiverr** or reply to unsolicited backlink-selling emails. Ignore bulk-link spam ("100 links"). ~90% of paid link-selling is low-quality spam. The only real "Google partner" status is a Google Ads partner - nobody has special algorithm access.
- **Don't reciprocal-link.** "As soon as you link back to the person, you're destroying the link equity you're building." Getting 10-20 sites to link to you while you link to none is fine. Use **ABC linking** (A→B→C→A) not direct A↔B swaps. Stop friend-group "private blog networks" and "review trains" immediately.
- **Don't use "near me" / zip codes / "near you"** as target keywords or in copy/URLs.
- **Don't keyword-stuff.** Match the actual #1 competitor's exact-phrase count "plus one," never wildly exceed it. Higher density does not equal better rankings - Google increasingly reads heavy repetition as over-optimization (Matt's own page dropped #1→#9 at 5.04% density / 35 uses vs. competitors' 1.76% and 0.9%). Even when a competitor ranks *with* stuffing, don't copy it - they only got away with it because the keyword had near-zero competition; copying it risks a penalty for no benefit.
- **Don't use hidden text** (font matching background), a duplicate desktop/mobile H1 hack, or hover-hidden keyword text - Google reads it as cloaking/gaming ("Google does not like this"). Matt cites his own mobile/desktop dual-H1 hack as the cause of one page's drop.
- **Don't change a URL that has any ranking, traffic, OR backlinks.** All three must be "no" before it's safe. A changed URL is a brand-new page to Google that starts from zero, and even a textbook 301 doesn't always preserve traffic. "Update this with extreme caution."
- **Don't fully automate content creation/publishing.** "It's a slippery slope if you just let AI do whatever." Platforms increasingly detect and label automated content. Spend ~1 hour/day being intentional; use AI to brainstorm/rewrite/generate images, not to publish unsupervised.
- **Don't "humanize" content or run an AI-detector on your own writing** - philosophically backwards. "We don't want to humanize our content. We want to write human content and have AI just frame it." Every piece should come from your real expertise, not "AI slop."
- **Don't block AI crawlers**, even when they overwhelm your server ("how else are they going to recommend it?"). Fix crawl floods with better hosting + a WAF, not by throttling bots.
- **Don't publish a "coming soon" placeholder**, allow blog comments (spam), use tags (thin archive pages), or mass-dump a batch of posts on a live site (Google reads high velocity as spam-like instability).
- **Don't over-check.** "You can look at it every day, but don't make actions on it every day - that's how you lose money, lose credit, lose sanity." Cancel any tool pushing daily rank-change alerts. Check monthly averages.

### 4.3 Gray-hat: acknowledged but not endorsed

Matt names several tactics people run that he explicitly does not recommend and calls out as manipulation: the **reviews micro-site** ("not a white-hat strategy... it is to manipulate the search results"), stuffing the keyword into the **GBP business-name field** ("I'm not recommending you do this"), a **second GBP via a subleased office** in a target city, and the **press-release → AI Overview** play (which sometimes only lasts about a week, and which publicizing can burn - the Edward Sturm/Globe and Mail case had the AI-cited link taken down after a viral video called it "manipulating AI"). The through-line: **"if it seems like you're trying to game the system, don't do it. If it feels bad, if it feels sneaky, don't do it."**

### 4.4 Key tradeoffs (the genuinely unsettled calls)

- **Word count / keyword count / heading count are competition-relative, and cut in both directions.** The same "match the top 3" rule means sometimes trim excess, sometimes add depth - benchmark the *lowest*-ranked of the top 3, not the highest (if #3 ranks with 500 words, aim ~600, not 3,000 because #1 has 3,000). There is no universal "more is better."
- **SEMrush stance is genuinely unresolved** - "most accurate" in most sessions, "stopped recommending it, way too expensive" post-Adobe in another. Both are Matt's real view at different points.
- **Blog cadence 1-2/week is a ceiling for newer sites, not a hard cap for established operators** - experienced batch-writers (CJ) run well above it without being flagged. The ceiling protects sustainable onboarding.
- **Deleting vs. drafting old content:** the safe rule is draft-and-wait 6 months to a year, but Matt's own aggressive mass-delete of 70 posts (no backlinks/traffic/indexing) had zero negative impact. He doesn't reconcile this.
- **Geotagging, custom schema, FAQ schema, and the reviews-microsite are all low-cost, outcome-based bets, not proven mechanisms.** Matt's position on each: "the cost is low enough to test regardless of whether we can prove why it works." Schema and most "AI SEO" tactics haven't moved the needle in his own testing; FAQ schema (after a year of testing) showed no measurable difference and can draw a bot storm.
- **AI citation and organic rank are decoupled** - you can rank #1 and not be cited; AI-Overview citation was only ~30% consistent across repeated identical searches in one test. Don't over-read a single "why did a competitor beat me in the AI Overview" snapshot.
- **Whether to invest in SEO at all is conditional on where a business already converts.** Matt told an attendee thriving via Instagram/events/referrals it was legitimate *not* to prioritize organic SEO; for a novel marketplace, he was openly for partnerships/influencers/community distribution over SEO. "Everybody runs a business in a different way."
- **Aged/used domains carry real but unquantifiable risk** - a clean-looking backlink profile doesn't guarantee no past-owner penalty. Matt now defaults to registering new domains (a client's ~$500 marketplace domain did "all the right things" for a year with zero movement; a fresh domain with the same content ranked within a month).
- **Reverse-engineering a competitor's odd on-page pattern** (duplicate H1s, etc.) is a reasonable experiment only when you have nothing to lose (not ranking anyway) - and keep the actual copy unique.

---

## PART 5 - BUSINESS & MINDSET

### 5.1 The agency model & pricing

- **Flat monthly retainer, never hourly.** Benchmark package (the answer to "what should we charge"): **$3,000 USD/month or more; 8 pieces of content/month** (8 blog posts, OR 8 page updates, OR 8 new pages such as location pages); **4 backlinks/month; ongoing technical fixes; monthly reporting; a dedicated point of contact.** "If they're not charging at least $1,500/month, they can't do enough work for you." Matt's own agency charges **$2,500/month** per client.
- **Two proven client cadences, contrasted:**
  - *With backlink work:* **2 blog posts/week + 4 backlinks/month, nothing else** - the model behind a 3-year anonymized client now at **$1.3M/year**, ranking for ~9,600 keywords, grown from ~$20K/month to $100K+/month (seasonal spikes to ~$200K).
  - *Without any backlink work:* **1 blog post/week + 2 city/location pages/month** - a 3-month engagement that ended with the client "at capacity" and hiring more staff. Delivered via a pre-mapped, client-signed-off content plan (12 blog topics + 6 city pages) and a ~4-general-questions-per-topic interview shortcut.
- **HeyTony's own disclosed cadence: two deliverables/week per client** (one new blog post + one existing service/product-page rewrite), i.e. **4-8 pieces every 28 days**, and **4 backlinks/month** ("that's all we do" and it gets "crazy results" - not 4-10/*week*, "that's too many").
- **Map the full content plan up front** - topics, which pages link to which, which topics tie to which money pages - and get client sign-off before the interview-and-write cycle.
- **Revenue is capped by fulfillment capacity, not lead volume.** More SEO traffic doesn't move the bottom line once a team can't absorb the work; past that point, conversion-rate work and pricing are the growth levers (Matt's own agency: 2.5% lead-to-client conversion, inbound already exceeding fulfillment, now in sales training / considering price increases rather than chasing more leads).
- **List pricing/cost ranges on your own site** even as a premium provider - "if you don't have any prices, you're getting left out entirely" from price-shoppers who will shop regardless. (Nuance: a luxury provider whose buyer decides through an in-person/call experience can validly hide prices - the test is your buyer's actual decision process.)
- **Client auto-publish:** default is pre-approval; ask around month 3-4 whether they'll allow auto-publish. Clients who allow it "typically get the best results."

### 5.2 Cadence, patience & the compounding game

- **Cadence: 1-2 posts/week, max.** One/week is "fantastic," two is "great," 1/week is a genuine baseline (not an inferior fallback), and **never both on the same day.** Daily/365-a-year is "too much" (reads as AI-spam churn). New-site launch can batch ~5-6 (or ~10, then drip 2/week) - the exception, not live-site practice.
- **SEO is a marathon: 3-6 months minimum before a real win, sometimes month 12-14 even when monthly gains looked flat.** Ranking within 2 weeks is "magic," not the norm. Insiders following the method report movement in ~1-1.5 months, faster than the typical agency's 2-3 months. New location pages: 3-6 months, up to a year.
- **Check performance ~once a month, not daily.** "Don't look at your credit score every day. Do the right thing every day, and 30 days later, without you looking, it's changed and you can buy a house." Day-to-day rank bouncing is normal noise. "Page 3 is very different from position 3" - don't panic-react to page-level movement.
- **The avalanche / snowball method:** deliberately target small, low-competition, near-zero-volume question keywords first (even 10-20 searches/month), all interlinked. Each barely moves traffic alone, but the accumulated topical authority is what eventually unlocks the harder head keywords the site couldn't touch on day one - and feeds LLM-recommendation visibility. "A KD of 21 is still easy." Google/ChatGPT "start picking us up" as trust compounds.
- **~15% of Google's daily searches are brand new**, never searched before, invisible to every keyword tool (SEMrush/Ahrefs/Moz only show what they've already detected) - and rising. Zero historical volume is not proof of zero future demand; "I guarantee there's nothing too niche that people aren't searching." This cuts both ways: a niche invisible to competitor tools is also harder to forecast/prove ROI on before publishing. "Keyword research is becoming less important than it was."

### 5.3 The mindset that actually decides outcomes

- **The #1 failure mode is quitting too early, not doing it wrong.** "Google does that on purpose because spammers come in... but then they give up, they go away. The people who get results aren't the ones who learn the most in a day. They're the ones who keep going." **Overwhelm is explicitly named as the top cause of quitting** - the whole method is engineered against it.
- **~1 hour a week is enough.** "I'm trying to make SEO so simple that anybody could do it in an hour a week." The 30-day plan is deliberately capped low (fix 5 issues not all of them, 4 posts not more) specifically to prevent the burnout-driven quitting that happens by week two. **Fix 5-10 site-health issues per week, not everything at once** ("you'll be astounded how much progress you make and how not stressed you are"). Fixing a systemic mistake at one or two per day/week, not retroactively all at once.
- **Focus on the 20% that drives 80%; explicitly skip the rest** - schema, FAQ schema, messy HTML, "AI blocks," chasing an audit percentage, running AI-detectors. "That only gets you 20% of the results and takes 80% of the time. I don't want to do that."
- **"Pigs get fat and hogs get slaughtered."** Never grab a whole market/region/keyword set at once. Take a slice, win it, expand. "Do you want to shoot a shotgun and maybe miss, or a sniper rifle and hit the target?"
- **Every page is "a door into your business"** - build one solid door at a time, not a million thin ones that "collapse when somebody walks through."
- **The core litmus test for any content: "Would my customers actually need this? And read this? If yes, publish it."** And after an AI draft: "Am I proud of this?"
- **The real objective isn't the algorithm.** "We don't care about SEO, we care about getting clients - SEO is the way we're doing that." / "The objective is not to game the algorithm, it's to write a piece of content so unique it talks to somebody with that specific problem." / "If the way you're thinking is 'I want to rank because I want people to pay me money' - that's the opposite of how we should think." Write to genuinely help; ranking and revenue follow.
- **AI-written content is NOT penalized** - Google and AI penalize *regurgitated, generic* content, not AI assistance. "Google and AI hate AI written posts. They do not. They hate regurgitated information that's the same everybody else is saying." What avoids the penalty is your own real expertise injected via the interview method.
- **Ranking position obsession is outdated.** #1, #2, #3, anywhere on page 1 all get traffic; "the new SEO" is aggregate traffic from many sources plus being recommended inside LLM answers. Rank in AI tools by ranking on Google first - "if you rank on Google, you will get recommended by AI."
- **Reciprocity is the community norm and the growth flywheel.** "What you put into this is what you get out of it... these are your results, not my results." "All ships rise with the tide."

### 5.4 Proof it works (case-study evidence)

- **Marcus** (pool installation, near bankruptcy 2008, zero SEO knowledge): answered real customer questions nightly → **#1 pool website in the world within 2 years.** The founding story of the entire method.
- **The $1.3M/year anonymized client:** 2 posts/week + 4 backlinks/month, no other marketing, ~$20K→$100K+/month over 3 years.
- **$120K/month blog-only client:** blog content as the *only* channel, ~2-2.5 years to full compounding.
- **The Hamilton therapist:** "write one blog post a week and answer your customers' questions," ~1.5-2 years → 3-month waitlist, fully booked, hiring, no ads, cancelled his Psychology Today listing - while every keyword tool shows **zero ranking** for "male therapist Hamilton," yet he ranks live on Google and ChatGPT for it. Grossing "probably a quarter million a year" off waitlist demand alone.
- **The bin-rental client** (Matt's book's opening): built in school, zero backlinks, heading tags not even done right → ~11 rental bins to **120+** on on-page fundamentals alone.
- **Marvin** (age 76): after 10 months of self-driven SEO with no movement, 4 days of Rank Week took his site from the bottom of page 1 into the map pack; landed a **$799/month recurring** client from a prior Rank Week.
- **Todd** ("Cosmos Within"): search-driven sales up **60% month-over-month.** **David** (Chuck's Garage): broad "common issues" posts drove traffic from <1,000 to 40,000; GSC average position ~13-15 → 5.7. **Peter** (Bulgaria): #1 in six cities for GBP after ~1.5 weeks; site scored 96% vs. a named competitor's 64% after ~3 months on the program.

---

*Cardinal takeaways: pick tools for the job and treat their numbers as directional (GSC is truth); structure local and ecommerce around one-keyword-one-page and the money-page hierarchy; never touch a ranking page and never do anything that "feels sneaky"; and win by outlasting competitors at one hour a week, not by chasing perfection.*
