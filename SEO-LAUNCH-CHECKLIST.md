# SEO Launch Checklist: Get BV Consulting Found in Fort Lauderdale

The website is built for local SEO (keyword-targeted pages, schema markup, sitemap, fast mobile pages, and 6 blog posts).
These off-site steps are what put you on Google Maps and in search results. Work top to bottom.

## Week 1: Go live and get indexed
- [ ] Push the site to GitHub and confirm https://bvconsulting.live loads with **https** (GitHub Pages → Settings → Pages → Custom domain `bvconsulting.live` → Enforce HTTPS). At your domain registrar, point the domain to GitHub Pages (A records for the apex domain, per GitHub's docs).
- [ ] Submit a test on the quote form and click **Activate Form** in the FormSubmit email (see `GOOGLE-SHEET-SETUP.md`).
- [ ] **Google Search Console**: add `bvconsulting.live` as a Domain property, verify via DNS, and submit `https://bvconsulting.live/sitemap.xml`.
- [ ] **Google Analytics 4**: create a property and paste the ID into `gaId` in `site.js`.
- [ ] **Bing Webmaster Tools**: import from Search Console (also feeds Bing, DuckDuckGo, and Copilot results).

## Week 1–2: Google Business Profile (biggest local ranking lever)
- [ ] Create/claim your profile at business.google.com as **BV Consulting** (your real business name, no extra keywords).
- [ ] If you work from home or at client locations, set it up as a **service-area business**, hide the address, and add Fort Lauderdale, Wilton Manors, Oakland Park, Plantation, Davie, Hollywood, Pompano Beach, Coral Springs, and Weston.
- [ ] Primary category: pick the closest match available, such as **Website designer**. Add secondary categories you genuinely offer (e.g. Internet marketing service, Marketing consultant, Software company).
- [ ] Phone **954-825-1009**, website **https://bvconsulting.live**, hours Mon–Fri 8am–6pm. These must match the website exactly.
- [ ] Add services (AI Automation, Web Design, Local SEO, API Integrations) with short descriptions and links to the matching pages.
- [ ] Upload a logo (`logo.png`), a cover image, and real photos of you working.
- [ ] Post an update each week (share each blog post as a GBP update).

## Week 2–4: Citations (consistent Name / Phone / Website everywhere)
Use exactly: **BV Consulting · Fort Lauderdale, FL · 954-825-1009 · https://bvconsulting.live · BVConsultings@outlook.com**
- [ ] Apple Business Connect (Apple Maps)
- [ ] Bing Places for Business
- [ ] Yelp for Business
- [ ] Facebook Business Page + Instagram
- [ ] LinkedIn Company Page (and add BV Consulting to your personal LinkedIn)
- [ ] Better Business Bureau
- [ ] Nextdoor Business
- [ ] Clutch.co and UpCity (directories for agencies)
- [ ] Greater Fort Lauderdale Chamber of Commerce (membership also earns a local backlink)

After creating profiles, add their URLs to the `"sameAs"` list in the JSON-LD schema on `index.html` and `contact.html`, for example:
`"sameAs": ["https://www.linkedin.com/company/...", "https://www.facebook.com/...", "https://www.instagram.com/..."]`

## Ongoing: Reviews
- [ ] Get your Google review link (GBP → "Ask for reviews") and send it to every client after a project.
- [ ] Reply to every review within a few days.
- [ ] Never offer incentives for reviews and don't only ask happy clients (both break Google's policies).
- [ ] Once you have real reviews, add a few to the home page where the `<!-- REVIEWS -->` note is.

## Ongoing: Content (drives clicks and traffic)
- [ ] Publish 2–4 new blog posts per month. Ideas:
  - Hurricane season tech and data backup plan for Broward small businesses
  - Best AI tools for Fort Lauderdale real estate agents
  - How restaurants on Las Olas can automate reservations and reviews
  - Website checklist for South Florida contractors
  - GoHighLevel vs HubSpot for small businesses
  - How marine businesses can get more leads during boat show season
  - Case studies of your own client projects (with permission): these build the most trust
- [ ] Share every post on Google Business Profile, LinkedIn, Facebook, and Instagram.
- [ ] Add each new post to `blog.html` and `sitemap.xml`, then request indexing in Search Console.

## Monthly: Track
- [ ] Search Console → Performance: which searches show your site; improve pages with high impressions but low clicks.
- [ ] GBP Performance: calls, website clicks, direction requests.
- [ ] GA4: `generate_lead` and `click_to_call` events.
- [ ] Ask every new client how they found you.

## Nice next steps
- Add a real founder photo and short bio to `about.html` (people hire people).
- Build portfolio/case-study pages as you complete projects.
- Consider Google Local Services Ads or Google Ads for "web design Fort Lauderdale" while SEO builds.
