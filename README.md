# BV Consulting Website

AI Automation, Web Design & API Integrations for small businesses in Fort Lauderdale, FL.
Live site: https://bvconsulting.live

## Files
| File | Purpose |
|---|---|
| `index.html` | Home page |
| `services.html` | Services overview |
| `ai-automation-fort-lauderdale.html` | AI Automation landing page |
| `web-design-fort-lauderdale.html` | Web Design & Local SEO landing page |
| `api-integration-fort-lauderdale.html` | API Integrations landing page |
| `about.html`, `contact.html`, `quote.html` | Company, contact, free consultation wizard |
| `blog.html` + `blog-*.html` | Blog index and 6 SEO articles |
| `privacy.html`, `terms.html`, `404.html` | Legal + not-found page |
| `site.js` | Shared scripts + **settings** (form email, Google Sheet, Google Analytics) |
| `styles.css` | All styles |
| `sitemap.xml`, `robots.txt`, `CNAME` | SEO + custom domain for GitHub Pages |
| `og-image.png`, `logo.png`, `favicon.svg`, `apple-touch-icon.png` | Social share image and icons |

See `GOOGLE-SHEET-SETUP.md` to activate lead emails and `SEO-LAUNCH-CHECKLIST.md` for the steps that get you found on Google.

## Adding a new blog post
1. Copy an existing `blog-*.html` file and rename it with a keyword-rich name (e.g. `blog-hurricane-prep-small-business.html`).
2. Update the `<title>`, meta description, canonical URL, `og:url`, the JSON-LD blocks, and the article content.
3. Add a card for it on `blog.html` and a `<url>` entry in `sitemap.xml`.
4. Link to it from at least one related service page or post.
