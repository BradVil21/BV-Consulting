# BV Consulting Website

AI agents, automated SMS & booking, SEO, website development, and API integrations for **med spas**.
Based in Fort Lauderdale, FL, serving med spas nationwide. Live site: https://www.bvconsulting.live

## Clean URLs
Every page lives in its own folder as `index.html`, so URLs have no `.html`:

| URL | File |
|---|---|
| `/` | `index.html` |
| `/quote/` (lead funnel, all "Get a Free Quote" buttons point here) | `quote/index.html` |
| `/thank-you/` (shown after a quote is submitted; good for ad conversion tracking) | `thank-you/index.html` |
| `/services/` | `services/index.html` |
| `/med-spa-ai-agents/` | `med-spa-ai-agents/index.html` |
| `/med-spa-sms-booking-automation/` | `med-spa-sms-booking-automation/index.html` |
| `/med-spa-ai-automation/` | `med-spa-ai-automation/index.html` |
| `/med-spa-seo/` | `med-spa-seo/index.html` |
| `/med-spa-website-design/` | `med-spa-website-design/index.html` |
| `/med-spa-api-integrations/` | `med-spa-api-integrations/index.html` |
| `/med-spa-marketing-fort-lauderdale/` (local SEO page) | `med-spa-marketing-fort-lauderdale/index.html` |
| `/about/`, `/contact/`, `/privacy/`, `/terms/` | `<name>/index.html` |
| `/blog/` and `/blog/<post>/` | `blog/index.html`, `blog/<post>/index.html` |

Links use root paths like `/styles.css`, so **double-clicking an HTML file won't display correctly**.
To preview on your Mac, open Terminal in this folder and run:

```bash
python3 -m http.server 8000
```

then visit http://localhost:8000

## Images
Compressed photos live in `/images/` in three sizes (480, 800, 1200px) as AVIF, WebP, and JPEG. Browsers download only the smallest format and size they need (a typical page loads about 30–110 KB of images).

## Settings
`site.js` (top of file) holds the lead email, optional Google Sheet URL, and Google Analytics ID.
See `GOOGLE-SHEET-SETUP.md` to activate lead emails and `SEO-LAUNCH-CHECKLIST.md` for launch steps.
