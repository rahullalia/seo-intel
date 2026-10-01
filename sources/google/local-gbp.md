# google | local-gbp

Dated evidence entries, newest first. Format in `pipeline/style.md`. Every entry: source, date, link, verbatim quote, plain meaning, factor id, evidence grade, lever.

## 2026-10-01 | Google's Profile Strength Indicator names the profile fields it asks a business to fill
- Source: Google Business Profile Help, "Manage your Profile Strength", 2026-10-01 (no page date), https://support.google.com/business/answer/15691556
- Quote: "Identify and fill in missing info in your profile. This includes your business description, hours of operation, and contact info."
- Means: Google ships a completeness tool inside the profile and names business description, hours of operation and contact info as the fields it checks, on verified listings only. The page claims connecting with more customers, not a ranking effect.
- Factor: gbp-profile-completeness | Evidence: A | Lever: conversion | Scope: local | Stage: both

## 2026-09-15 | A virtual office address is not eligible for a Business Profile
- Source: Google Business Profile Help, "Guidelines for representing your business on Google", 2026-09-15 (no page date), https://support.google.com/business/answer/3038177
- Quote: "If your business rents a physical mailing address but doesn't operate out of that location, also known as a virtual office, that location isn't eligible for a Business Profile."
- Means: A rented mail drop used as a Business Profile address is barred by Google's own guidelines, which on the same page also reject P.O. boxes and mailboxes located at remote locations. A co-working desk qualifies only with clear signage, customers received at the location during business hours, and the business's own staff there during those hours.
- Factor: fake-address-listing | Evidence: A | Lever: trust | Scope: local | Stage: both

## 2026-09-15 | Google's review policy names selective solicitation of positive reviews as rating manipulation
- Source: Google Business Profile Help, "Prohibited and restricted content", 2026-09-15 (no page date), https://support.google.com/business/answer/7400114
- Quote: "Discourage or prohibit negative reviews, or selectively solicit positive reviews from customers"
- Means: Asking only satisfied customers for a review is listed under Rating Manipulation as an action Google does not allow merchants to take, so review gating is a stated policy breach rather than a grey area. The same list bars a merchant from asking staff to collect a set number of reviews or to request reviews that name a staff member.
- Factor: review-gating | Evidence: A | Lever: trust | Scope: local | Stage: both

## 2026-09-10 | Google Business Profile chat and call history stopped working July 31, 2024
- Source: Google Business Profile Help, "Changes to Google Business Profile chat and call history", 2026-09-10 (no page date), https://support.google.com/business/answer/14919056
- Quote: "As of July 31, 2024, the chat and call history features are no longer available in your Business Profile."
- Means: This is Google's own removal notice for gbp-messaging, which the scorecard held at Dead on a seed document with no primary source. A workflow that reads or replies to Business Profile messages, or pulls a call history report, describes a feature Google turned off in mid-2024.
- Factor: gbp-messaging | Evidence: A | Lever: conversion | Scope: local | Stage: audit

## 2026-09-06 | Google's review policy bars pressuring or directing reviews on the premises
- Source: Google Business Profile Help, "Prohibited and restricted content", 2026-09-06 (no page date), https://support.google.com/business/answer/7400114
- Quote: "Merchants should not require or pressure users to leave ratings or write reviews while on the premises, nor should they request that specific content be included."
- Means: Asking for a review on site, or telling a customer what to say in it, breaks Google's own review policy. A business that filters which customers get asked, rather than asking everyone, runs the same risk.
- Factor: review-gating | Evidence: A | Lever: trust | Scope: local | Stage: both

## 2026-09-06 | Google bans paying for reviews as its own policy, separate from the FTC rule
- Source: Google Business Profile Help, "Prohibited and restricted content", 2026-09-06 (no page date), https://support.google.com/business/answer/7400114
- Quote: "Offer incentives, such as payment, discounts, free goods and/or services, in exchange for posting any review or revision or removal of a negative review."
- Means: This is listed as a prohibited action in Google's own policy, so a client loses Google standing for a paid review independent of whatever the FTC rule would separately cover.
- Factor: review-incentives | Evidence: A | Lever: trust | Scope: local | Stage: both

## 2026-09-06 | Video verification must be one unbroken take of at least 30 seconds
- Source: Google Business Profile Help, "Verify your business with a video recording", 2026-09-06 (no page date), https://support.google.com/business/answer/14271705
- Quote: "An unedited, unique, and complete recording with no breaks."
- Means: Google requires a live, continuous phone recording at least 30 seconds long, filmed and uploaded from the same device in one session. A pre-recorded or edited clip fails verification.
- Factor: gbp-verified | Evidence: A | Lever: ranking | Scope: local | Stage: both

## 2026-09-06 | A service-area business must hide its address if it does not serve customers there
- Source: Google Business Profile Help, "Manage your service areas for service-area and hybrid businesses", 2026-09-06 (no page date), https://support.google.com/business/answer/9157481
- Quote: "If you don't serve customers at your business address, remove your address from your Business Profile."
- Means: Showing a home or office address that customers never visit is itself a policy problem for a service-area business, not just a privacy choice.
- Factor: sab-address-hidden | Evidence: A | Lever: trust | Scope: local | Stage: both

## 2026-09-06 | Keyword-stuffed business names can get a profile suspended
- Source: Google Business Profile Help, "Guidelines for representing your business on Google", 2026-09-06 (no page date), https://support.google.com/business/answer/3038177
- Quote: "Including unnecessary information in your business name isn't permitted, and could result in the suspension of your Business Profile."
- Means: A name field padded with a city or service keyword is a named suspension risk in Google's own policy, not a soft best practice.
- Factor: gbp-name-policy-risk | Evidence: A | Lever: trust | Scope: local | Stage: both

## 2026-09-06 | A Business Profile must have real in-person contact during its posted hours
- Source: Google Business Profile Help, "Business eligibility and ownership guidelines", 2026-09-06 (no page date), https://support.google.com/business/answer/13763036
- Quote: "To qualify for a Business Profile, a business must make in-person contact with customers during its stated hours."
- Means: Listed hours have to match when the business is actually staffed and reachable. Hours that do not match real staffing are an eligibility problem, not just a convenience issue for searchers.
- Factor: gbp-hours-accuracy | Evidence: A | Lever: ranking | Scope: local | Stage: both

## 2026-09-06 | Distance from the searcher is one of Google's three named local ranking factors
- Source: Google Business Profile Help, "How results on Google are ranked", 2026-09-06 (no page date), https://support.google.com/business/answer/7091
- Quote: "Distance refers to how far each business is from the customer who's searching."
- Means: Google names distance alongside relevance and prominence as one of the three inputs to local ranking. A profile cannot change its distance, which is why the other two carry the optimization work.
- Factor: proximity | Evidence: A | Lever: ranking | Scope: local | Stage: audit

## 2026-09-06 | Business Profile edits go through review that can take up to 30 days
- Source: Google Business Profile Help, "Understand what happens to your Business Profile edits", 2026-09-06 (no page date), https://support.google.com/business/answer/3038311
- Quote: "Edits usually take up to 10 minutes to review, but sometimes it can take up to 30 days."
- Means: A batch of edits to name, address, category or hours can sit in review for weeks rather than post instantly, which is the mechanism behind rapid-edit suspensions.
- Factor: rapid-core-field-edits | Evidence: A | Lever: trust | Scope: local | Stage: audit

## 2026-08-28 | Google shut off the Business Profile Q&A API on November 3, 2025
- Source: Google for Developers, "Q&A API change log", 2026-08-28, https://developers.google.com/my-business/content/qanda/change-log
- Quote: "On November 3, 2025, we will be discontinuing the My Business Q&A API as we are in the process of updating the Q&A functionality and user experience."
- Means: Any tool or workflow that read or posted Q&A through the API stopped working on that date. Q&A is gone as a lever, not just deprioritized.
- Factor: gbp-qa | Evidence: A | Lever: conversion | Scope: local | Stage: audit

## 2026-04-16 | Google removed 292 million policy-violating reviews
- Source: Google, "New ways we're protecting businesses on Maps", 2026-04-16, https://blog.google/products-and-platforms/products/maps/new-ways-were-protecting-businesses-on-maps/
- Quote: "Our advanced systems and expert analysts blocked or removed over 292 million policy-violating reviews"
- Means: Google removed 292 million reviews and 13 million fake profiles in 2025, so a burst of reviews on one profile is being read against active filtering at that scale. Space review requests out rather than running a campaign that lands dozens in a week.
- Factor: review-velocity | Evidence: A | Lever: ranking | Scope: local | Stage: audit

## 2024-08-14 | The FTC rule bans compensation conditioned on a review's sentiment
- Source: Federal Trade Commission, "Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials", 2024-08-14, https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials
- Quote: "The final rule prohibits businesses from providing compensation or other incentives conditioned on the writing of consumer reviews expressing a particular sentiment, either positive or negative."
- Means: A discount, freebie or prize entry offered for a positive review breaks a federal rule the FTC can seek civil penalties under, on top of Google's own policy. The FTC adds that the condition can be conveyed implicitly, so hinting at a reward counts.
- Factor: review-incentives | Evidence: A | Lever: trust | Scope: local | Stage: both

## 2024-08-14 | The FTC rule bans showing a filtered review set as if it were all reviews
- Source: Federal Trade Commission, "Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials", 2024-08-14, https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials
- Quote: "The final rule also bars a business from misrepresenting that the reviews on a review portion of its website represent all or most of the reviews submitted when reviews have been suppressed based upon their ratings or negative sentiment."
- Means: A review widget that publishes only four and five star feedback while implying it shows every review submitted breaks the federal rule. The rule covers what the site displays; pre-screening who gets asked is covered separately by Google's review policy.
- Factor: review-gating | Evidence: A | Lever: trust | Scope: local | Stage: both
