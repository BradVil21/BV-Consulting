# SEO Launch Checklist: Get BV Consulting Found by Med Spas

The website is built for search: med spa keyword pages for every service, a Fort Lauderdale local page,
6 med spa blog posts, clean URLs, schema markup, an image sitemap, and a `/quote/` funnel.
These steps get it indexed and ranking. Work top to bottom.

## Week 1: Go live and get indexed
- [ ] Push to GitHub. In the repo: Settings → Pages → Custom domain `bvconsulting.live` → **Enforce HTTPS**.
- [ ] Visit https://www.bvconsulting.live/quote/ and submit a test. Click **Activate Form** in the FormSubmit email (check Junk).
- [ ] **Google Search Console**: add `bvconsulting.live` (Domain property, verify via DNS), submit `https://www.bvconsulting.live/sitemap.xml`.
      Then use URL Inspection → Request Indexing for `/`, `/quote/`, `/med-spa-marketing-fort-lauderdale/`, and each service page.
- [ ] **Google Analytics 4**: create a property, paste the ID into `gaId` in `site.js`. Mark `generate_lead` and `click_to_call` as key events.
- [ ] **Bing Webmaster Tools**: import from Search Console.

## Week 1–2: Google Business Profile (for the Fort Lauderdale local page)
- [ ] Create/claim **BV Consulting** at business.google.com. Use your real business name only.
- [ ] Set it up as a **service-area business** (hide your home address). Service areas: Fort Lauderdale, Broward County, Palm Beach County, Miami-Dade County.
- [ ] Primary category: **Marketing agency** (or the closest available, such as Internet marketing service). Secondary: Website designer, Software company, Marketing consultant.
- [ ] Phone **954-825-1009**, website **https://www.bvconsulting.live/med-spa-marketing-fort-lauderdale/** (or the home page), hours Mon–Fri 8am–6pm.
      These must match the NAP block on the Fort Lauderdale page exactly.
- [ ] Add services: AI Agents for Med Spas, Med Spa SEO, Med Spa Website Design, SMS & Booking Automation, AI Automation, API Integrations.
- [ ] Upload the logo (`logo.png`) and real photos of your work.
- [ ] Once verified, replace the map on the Fort Lauderdale page with your profile's **Embed a map** code (there's a comment marking the spot).

## Week 2–4: Listings & authority (consistent name / phone / website everywhere)
Use exactly: **BV Consulting · Fort Lauderdale, FL · 954-825-1009 · https://www.bvconsulting.live**
- [ ] LinkedIn Company Page (and your personal profile)
- [ ] Facebook Business Page + Instagram
- [ ] Apple Business Connect, Bing Places, Yelp, BBB
- [ ] Agency directories: Clutch.co, UpCity, DesignRush, GoodFirms
- [ ] Med spa industry: join the **American Med Spa Association (AmSpa)** vendor/partner programs if available, and look for partner/integration directories of the booking platforms you work with
- [ ] Greater Fort Lauderdale Chamber of Commerce
- [ ] Add these profile URLs to the `"sameAs"` list in `_build/common.py` (inside `BUSINESS`) and rebuild, or send them to Claude to add

## Ongoing: Reviews & proof
- [ ] Ask every med spa client for a Google review after launch milestones. Never offer incentives.
- [ ] Publish case studies (with client permission): what you built, tools used, and measured results.
- [ ] Add real testimonials to the home page once you have them.

## Ongoing: Content (2–4 posts per month)
Send new blog photos and I'll add them. High-intent med spa topics to write next:
- Best AI receptionist options for med spas (how to choose)
- Boulevard vs Zenoti vs Mangomint: integrations and automation compared
- HIPAA and AI chatbots: what med spa owners should know
- Med spa Google Ads vs SEO: where to spend first
- How to reduce med spa no-shows with deposits and reminders
- Med spa membership programs: automating renewals and credits
- Instagram DM automation for med spas
- Local SEO for multi-location med spas
- Treatment page templates that convert (injectables, laser, facials)

For each post: add it to the blog, link it from a related service page, share it on LinkedIn and your Google Business Profile, then Request Indexing in Search Console.

## Monthly: Track
- [ ] Search Console → Performance: queries with high impressions and low clicks → improve titles/descriptions.
- [ ] GA4: `quote_start` → `generate_lead` conversion rate on `/quote/`.
- [ ] Google Business Profile: calls and website clicks.
