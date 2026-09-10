import json, os, html, re

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://bvconsulting.live"
OUT = os.path.dirname(HERE) if os.path.basename(HERE) == "_build" else os.path.join(HERE, "out")
PHONE = "954-825-1009"
TEL = "+19548251009"
EMAIL = "bvconsultings@outlook.com"
TODAY = "2026-09-10"
TODAY_HUMAN = "September 10, 2026"
QUOTE = "/quote/"
LOCAL = "/med-spa-marketing-fort-lauderdale/"

exec(open(os.path.join(HERE, "icons_block.py")).read())
ICONS.update({
    "syringe": '<path d="M18 2l4 4M17 7l3-3M19 9L9 19l-4 1 1-4L16 6zM14 8l2 2M11 11l2 2M5 19l-3 3"/>',
    "sms": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 10h.01M12 10h.01M16 10h.01"/>',
    "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
    "flag": '<path d="M4 22V4M4 4h13l-2 4 2 4H4"/>',
    "cpu": '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 9h6v6H9zM9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    "repeat": '<path d="M17 2l4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14M7 22l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>',
    "gift": '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v9H5v-9M7.5 8a2.5 2.5 0 1 1 0-5C11 3 12 8 12 8s1-5 4.5-5a2.5 2.5 0 1 1 0 5"/>',
})

IMG = json.load(open(os.path.join(HERE, "images.json"))) if os.path.exists(os.path.join(HERE, "images.json")) else {}


def ic(name, size=24, sw=1.7):
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>') % (size, size, sw, ICONS[name])


def esc(s):
    return html.escape(s, quote=True)


def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").replace("&nbsp;", " ")


def picture(key, alt, sizes="(min-width: 960px) 50vw, 100vw", cls="", eager=False, fallback_icon="sparkle"):
    """Responsive, compressed <picture> (AVIF > WebP > JPEG). Falls back to a gradient block if the photo is missing."""
    if key not in IMG:
        return '<div class="photo photo-fallback %s" role="img" aria-label="%s">%s</div>' % (cls, esc(alt), ic(fallback_icon, 56, 1.3))
    m = IMG[key]
    w = min(1200, m["w"]); h = round(w * m["ratio"])
    load = 'fetchpriority="high" loading="eager"' if eager else 'loading="lazy"'
    def ss(ext):
        return ", ".join("/images/%s-%d.%s %dw" % (key, x, ext, x) for x in (480, 800, 1200))
    return ('<picture class="photo {c}">'
            '<source type="image/avif" srcset="{avif}" sizes="{s}">'
            '<source type="image/webp" srcset="{webp}" sizes="{s}">'
            '<img src="/images/{k}-800.jpg" srcset="{jpg}" sizes="{s}" width="{w}" height="{h}" alt="{a}" {l} decoding="async"></picture>'
            ).format(c=cls, avif=ss("avif"), webp=ss("webp"), jpg=ss("jpg"), s=sizes, k=key, w=w, h=h, a=esc(alt), l=load)


def img_url(key):
    return SITE + "/images/%s-1200.jpg" % key if key in IMG else SITE + "/og-image.png"


SERVICES = [
    {"key": "agents", "name": "AI Agents", "long": "AI Agents for Med Spas", "url": "/med-spa-ai-agents/", "icon": "bot",
     "img": "med-spa-consultation-mirror",
     "short": "24/7 AI receptionists for calls, texts, website chat, and DMs that answer questions and book consultations."},
    {"key": "sms", "name": "Automated SMS & Booking", "long": "Med Spa SMS & Booking Automation", "url": "/med-spa-sms-booking-automation/", "icon": "calendar",
     "img": "med-spa-payment-terminal-booking",
     "short": "Online booking, confirmations, reminders, deposits, waitlists, and rebooking texts that keep your calendar full."},
    {"key": "automation", "name": "AI Automation", "long": "AI Automation for Med Spas", "url": "/med-spa-ai-automation/", "icon": "sparkle",
     "img": "med-spa-lip-filler-treatment",
     "short": "Lead follow-up, review requests, membership renewals, and reactivation campaigns that run on autopilot."},
    {"key": "seo", "name": "Med Spa SEO", "long": "Med Spa SEO", "url": "/med-spa-seo/", "icon": "search",
     "img": "med-spa-laser-hair-removal",
     "short": "Rank on Google and Google Maps for the treatments people search for, in every city you operate."},
    {"key": "web", "name": "Website Development", "long": "Med Spa Website Design & Development", "url": "/med-spa-website-design/", "icon": "web",
     "img": "med-spa-consultation-mirror",
     "short": "Fast, elegant, mobile-first med spa websites built to turn visitors into booked consultations."},
    {"key": "api", "name": "API Integrations", "long": "Med Spa API Integrations", "url": "/med-spa-api-integrations/", "icon": "nodes",
     "img": "med-spa-payment-terminal-booking",
     "short": "Connect your booking software, EMR, CRM, payments, and ads so patient data flows without double entry."},
]
SVC = {s["key"]: s for s in SERVICES}

SOFTWARE = ["Boulevard", "Zenoti", "Mangomint", "Vagaro", "Mindbody", "AestheticsPro", "Aesthetic Record", "PatientNow",
            "GoHighLevel", "HubSpot", "Stripe", "Square", "Google Business Profile", "Meta Ads"]
AI_TOOLS = [
    ("Claude", "by Anthropic", "Natural, on-brand conversations, careful reasoning, and long-context knowledge of your treatments and policies."),
    ("ChatGPT", "by OpenAI", "Versatile language and voice capabilities for chat, text, and content workflows."),
    ("Gemini", "by Google", "Multimodal AI that works well alongside Google Workspace and Google Business tools."),
    ("Automation platforms", "Zapier, Make, n8n", "The connective tissue that moves data between your booking system, CRM, and messaging tools."),
    ("Messaging & voice", "Twilio and more", "Reliable, registered business texting and calling infrastructure for SMS and AI voice agents."),
    ("CRM & marketing", "GoHighLevel, HubSpot", "Pipelines, campaigns, and reporting that tie every lead back to revenue."),
]

BUSINESS_ID = SITE + "/#business"
WEBSITE_ID = SITE + "/#website"

BROWARD = ["Fort Lauderdale", "Las Olas", "Wilton Manors", "Oakland Park", "Lauderdale-by-the-Sea", "Plantation", "Davie",
           "Weston", "Coral Springs", "Parkland", "Pompano Beach", "Deerfield Beach", "Hollywood", "Dania Beach",
           "Pembroke Pines", "Miramar", "Sunrise", "Boca Raton", "Delray Beach", "Aventura", "Miami"]

BUSINESS = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "@id": BUSINESS_ID,
    "name": "BV Consulting",
    "description": "BV Consulting builds AI agents, automated SMS and booking, SEO, websites, and API integrations for med spas and aesthetic practices. Based in Fort Lauderdale, FL, serving med spas nationwide.",
    "url": SITE + "/",
    "logo": SITE + "/logo.png",
    "image": SITE + "/og-image.png",
    "telephone": "+1-954-825-1009",
    "email": EMAIL,
    "priceRange": "$$",
    "slogan": "Fill your med spa's calendar with AI, SEO, and automation.",
    "address": {"@type": "PostalAddress", "addressLocality": "Fort Lauderdale", "addressRegion": "FL", "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", "latitude": 26.1224, "longitude": -80.1373},
    "areaServed": [{"@type": "Country", "name": "United States"}],
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                   "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                   "opens": "08:00", "closes": "18:00"}],
    "knowsAbout": ["Med spa marketing", "Medical spa SEO", "AI agents", "AI receptionists", "SMS marketing automation",
                   "Online booking automation", "Website development", "API integration", "Claude AI integration",
                   "HIPAA-conscious automation"],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Med Spa Growth Services",
                        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["long"], "url": SITE + s["url"]}} for s in SERVICES]},
}
WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": WEBSITE_ID, "url": SITE + "/",
           "name": "BV Consulting", "inLanguage": "en-US", "publisher": {"@id": BUSINESS_ID}}


def ld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, indent=1, ensure_ascii=False) + '\n</script>'


def breadcrumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": strip(n), "item": SITE + u}
                                for i, (n, u) in enumerate(items)]}


def crumbs(items):
    lis = []
    for n, (name, url) in enumerate(items):
        if n == len(items) - 1:
            lis.append('<li aria-current="page">%s</li>' % name)
        else:
            lis.append('<li><a href="%s">%s</a></li>' % (url, name))
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>%s</ol></nav>' % "".join(lis)


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]}


def faq_html(faqs):
    return "\n".join('<details class="faq-item"><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in faqs)


NAV = [("Home", "/"), ("Services", "/services/"), ("About", "/about/"), ("Blog", "/blog/"), ("Contact", "/contact/")]


def header(active, funnel=False, has_demo=False):
    if funnel:
        return '''<header class="site-header">
  <div class="container nav-wrap funnel-nav">
    <a class="brand" href="/" aria-label="BV Consulting home"><span class="brand-badge">BV</span><span>BV Consulting</span></a>
    <span class="secure-badge">%s<span>Secure &amp; Confidential</span></span>
  </div>
</header>''' % ic("shield", 15, 2)
    links = []
    for name, url in NAV:
        cur = ' aria-current="page"' if url == active else ""
        links.append('<a href="%s"%s>%s</a>' % (url, cur, name))
    links.append('<a class="nav-demo" href="%s">%s<span>View Demo</span></a>' % ("#demo" if has_demo else "/#demo", ic("sms", 17, 2)))
    links.append('<a class="nav-cta" href="%s">Get a Free Quote</a>' % QUOTE)
    return '''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="/" aria-label="BV Consulting home"><span class="brand-badge">BV</span><span>BV Consulting</span></a>
    <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button>
    <nav id="nav-links" class="nav-links" aria-label="Main">
      %s
    </nav>
  </div>
</header>''' % "\n      ".join(links)


def footer(funnel=False):
    if funnel:
        return '''<footer class="footer-slim funnel-foot">
  <div class="container">
    <nav class="ff-links" aria-label="Legal"><a href="/privacy/">Privacy Policy</a><a href="/terms/">Terms of Service</a><a href="/contact/">Contact Us</a></nav>
    <p>BV Consulting is an independent consultancy based in Fort Lauderdale, FL, serving med spas nationwide. We never sell your information, and we never ask for patient or health information.</p>
    <p class="ff-tm">Logos shown are trademarks of their respective owners and do not imply endorsement.</p>
    <p class="ff-copy">&copy; <span id="year">2026</span> BV Consulting</p>
  </div>
</footer>'''
    svc = "\n        ".join('<li><a href="%s">%s</a></li>' % (s["url"], s["name"]) for s in SERVICES)
    return '''<footer>
  <div class="container">
    <div class="foot-grid">
      <div>
        <div class="brand"><span class="brand-badge">BV</span><span style="color:#fff">BV Consulting</span></div>
        <p class="foot-brand-text">AI agents, automated SMS &amp; booking, SEO, websites, and API integrations built for med spas and aesthetic practices.</p>
        <p class="foot-based">{pin} Based in Fort Lauderdale, FL &middot; Serving med spas nationwide</p>
        <a class="btn btn-primary" href="{quote}" style="margin-top:6px">Get a Free Quote</a>
      </div>
      <div><h4>Services</h4><ul>
        {svc}
        <li><a href="/services/">All Services</a></li>
      </ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="/about/">About</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li><a href="{local}">Fort Lauderdale Med Spa Marketing</a></li>
        <li><a href="/contact/">Contact</a></li>
        <li><a href="/privacy/">Privacy Policy</a></li>
        <li><a href="/terms/">Terms &amp; Conditions</a></li>
      </ul></div>
      <div><h4>Reach Us</h4><ul>
        <li><strong style="color:#fff">BV Consulting</strong></li>
        <li>Fort Lauderdale, FL</li>
        <li><a href="tel:{tel}">{phone}</a></li>
        <li><a href="mailto:{email}">{email}</a></li>
        <li>Mon&ndash;Fri 8am&ndash;6pm ET</li>
      </ul></div>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span id="year">2026</span> BV Consulting. All rights reserved.</span>
      <span class="foot-tm">Product names and logos shown on this site, such as Claude, ChatGPT, OpenAI, Gemini, Google, Zapier, Make, Calendly, Facebook, and HighLevel, are trademarks of their respective owners. BV Consulting is an independent consultancy and is not affiliated with or endorsed by them.</span>
    </div>
  </div>
</footer>'''.format(pin=ic("pin", 14, 2), quote=QUOTE, svc=svc, local=LOCAL, tel=TEL, phone=PHONE, email=EMAIL)


PAGES = []  # (path, priority) for sitemap
PAGE_IMAGES = {}


def page(path, title, desc, body, schemas=(), og_type="website", active="", extra_head="", noindex=False,
         scripts_after="", og_image=None, funnel=False, images=(), priority="0.7", sitemap=True):
    """path like '/', '/quote/', '/blog/slug/'. Writes out/<path>/index.html."""
    canonical = SITE + path
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large"
    og = og_image or (img_url(images[0]) if images and images[0] in IMG else SITE + "/og-image.png")
    doc = '''<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="canonical" href="{canonical}" />
<meta name="robots" content="{robots}" />
<meta name="theme-color" content="#2BA0EE" />
<meta property="og:type" content="{og_type}" />
<meta property="og:site_name" content="BV Consulting" />
<meta property="og:locale" content="en_US" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="{og}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{desc}" />
<meta name="twitter:image" content="{og}" />
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" onload="this.onload=null;this.rel='stylesheet'" />
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" /></noscript>
<link rel="stylesheet" href="/styles.css" />
{extra_head}{schema_html}
</head>
<body{bodycls}>

{header}

<main id="main">
{body}
</main>

{footer}

<script src="/site.js" defer></script>
{scripts_after}
</body>
</html>
'''.format(title=esc(title), desc=esc(desc), canonical=canonical, robots=robots, og_type=og_type, og=og,
           extra_head=extra_head + ("\n" if extra_head else ""), schema_html="\n".join(ld(s) for s in schemas),
           bodycls=' class="funnel"' if funnel else "", header=header(active, funnel, "data-sms-demo" in body), body=body,
           footer=footer(funnel), scripts_after=scripts_after)
    target = os.path.join(OUT, path.strip("/"), "index.html") if path != "/404" else os.path.join(OUT, "404.html")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    open(target, "w").write(doc)
    if sitemap and not noindex:
        PAGES.append((path, priority))
        PAGE_IMAGES[path] = [k for k in re.findall(r'/images/([a-z0-9-]+)-800\.jpg"', body)]
    return target


def cta_strip(h, p, btn="Get Your Free Quote"):
    return '''<section class="section">
  <div class="container">
    <div class="cta-strip">
      <h2>%s</h2>
      <p>%s</p>
      <div class="hero-ctas" style="justify-content:center;margin:0">
        <a class="btn btn-secondary" href="%s" style="background:#fff;color:var(--blue-dark);border-color:#fff">%s</a>
        <a class="btn btn-secondary" href="tel:%s" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.7)">%sGet Started</a>
      </div>
    </div>
  </div>
</section>''' % (h, p, QUOTE, btn, TEL, ic("phone", 18, 2))


def post_card(p):
    if p.get("img") in IMG:
        art = picture(p["img"], p["img_alt"], sizes="(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw", cls="pc-photo")
    else:
        art = '<div class="pc-art %s" aria-hidden="true">%s</div>' % (p["art"], ic(p["icon"], 46, 1.5))
    return '''<a class="post-card" href="{url}" data-cat="{cat_key}" style="color:inherit">
  {art}
  <div class="pc-body">
    <span class="pc-cat">{cat}</span>
    <h3>{title}</h3>
    <p>{excerpt}</p>
    <span class="pc-meta">{mins} min read &middot; <time datetime="{date}">{date_h}</time></span>
  </div>
</a>'''.format(url=p["url"], cat_key=p["cat_key"], art=art, cat=p["cat"], title=p["title"], excerpt=p["excerpt"],
               mins=p["mins"], date=p["date"], date_h=TODAY_HUMAN)


def software_strip(label="Works with the software med spas already use"):
    return '''<div class="soft-strip"><p class="soft-label">%s</p><ul class="soft-list">%s</ul></div>''' % (
        label, "".join("<li>%s</li>" % s for s in SOFTWARE))


def ai_tools_section(bg="", carousel=True):
    cards = "\n".join('<div class="tool"><div class="tool-top"><b>%s</b><span>%s</span></div><p>%s</p></div>' % t for t in AI_TOOLS)
    return '''<section class="section %s" id="ai-tools">
  <div class="container">
    <div class="center" style="margin-bottom:30px">
      <span class="eyebrow">The AI behind your system</span>
      <h2>We Build With Leading AI Tools, Including Claude</h2>
      <p style="max-width:760px;margin:0 auto">BV Consulting isn't locked into one vendor. We build and integrate AI agents and automations using several leading AI tools, including <strong>Claude by Anthropic</strong>, then connect them to your booking software, CRM, and phone system. You get the right model for each job, set up with your brand voice, your treatment menu, and clear guardrails.</p>
    </div>
    %s
    <div class="tools" style="margin-top:26px">%s</div>
    <p class="center tools-note">We choose tools and settings based on your needs, budget, and privacy requirements. Where protected health information is involved, we use services and configurations that support a Business Associate Agreement (BAA).</p>
  </div>
</section>''' % (bg, logo_carousel("Tools &amp; platforms we integrate") if carousel else "", cards)


LOGOS = [("zapier", "Zapier", 353), ("google", "Google", 293), ("calendly", "Calendly", 396), ("claude", "Claude by Anthropic", 443),
         ("facebook", "Facebook", 97), ("make", "Make", 465), ("openai", "OpenAI", 349), ("highlevel", "HighLevel", 428)]


def logo_carousel(label="Integrations &amp; AI tools we build with"):
    def items(hidden):
        out = []
        for key, name, w in LOGOS:
            sq = ' class="logo-sq"' if key == "facebook" else ""
            alt = "" if hidden else name
            out.append('<li><picture><source type="image/webp" srcset="/logos/%s.webp"><img%s src="/logos/%s.png" alt="%s" width="%d" height="96" loading="lazy" decoding="async"></picture></li>'
                       % (key, sq, key, alt, w))
        return "".join(out)
    return '''<div class="logo-carousel-wrap">
  <p class="logo-label">%s</p>
  <div class="logo-carousel">
    <div class="logo-track">
      <ul class="logo-set">%s</ul>
      <ul class="logo-set" aria-hidden="true">%s</ul>
    </div>
  </div>
</div>''' % (label, items(False), items(True))


DEMO_ICONS = {"lead": "sms", "missed": "phone", "reminder": "calendar", "rebook": "repeat"}


def sms_demo(demo_id="sms-demo", bg="bg-soft", eyebrow="Try it yourself", title="Text Our Demo AI Agent and See How It Works",
             lede="This is how an AI agent texts with your clients. Pick a scenario or type anything a real client might ask, like pricing, booking, or a treatment question.", start="lead"):
    tabs = [("lead", "New lead texts in"), ("missed", "Missed call text back"), ("reminder", "Appointment reminder"), ("rebook", "Rebooking nudge")]
    tab_html = "".join('<button type="button" class="demo-tab" data-demo-tab="%s" data-scenario="%s" aria-pressed="%s">%s%s</button>'
                       % (demo_id, k, "true" if k == start else "false", ic(DEMO_ICONS[k], 15, 2), n) for k, n in tabs)
    return '''<section class="section %s demo-section" id="demo" aria-label="Interactive SMS demo">
  <div class="container">
    <div class="demo-grid">
      <div class="demo-copy demo-top">
        <span class="eyebrow">%s</span>
        <h2>%s</h2>
        <p>%s</p>
        <div class="demo-tabs" role="group" aria-label="Demo scenarios">%s</div>
      </div>
      <div class="phone-wrap">
        <div class="phone" id="%s" data-sms-demo data-start="%s">
          <div class="phone-screen">
            <div class="phone-notch" aria-hidden="true"></div>
            <div class="phone-status" aria-hidden="true"><span>9:41</span><span>%s%s</span></div>
            <div class="phone-head"><div class="phone-avatar" aria-hidden="true">YM</div><div class="phone-id"><div class="phone-name">Your Med Spa</div><div class="phone-sub"><i></i>AI assistant<span class="ps-extra"> &middot; online</span></div></div><button type="button" class="phone-reset">%s<span>Restart</span></button></div>
            <div class="chat" role="log" aria-live="polite" aria-label="Demo text conversation"></div>
            <div class="chips"></div>
            <form class="phone-input" autocomplete="off">
              <label class="hp" for="%s-input">Type a message</label>
              <input id="%s-input" type="text" maxlength="280" placeholder="Text message" enterkeyhint="send" />
              <button type="submit" aria-label="Send message">%s</button>
            </form>
          </div>
        </div>
      </div>
      <div class="demo-copy demo-bottom">
        <ul class="check-list">
          <li>Answers treatment, pricing, and hours questions in your brand voice</li>
          <li>Books consultations and syncs them to your calendar and CRM</li>
          <li>Routes medical questions to your licensed team and honors STOP opt-outs</li>
        </ul>
        <p class="demo-note">Interactive demo with sample replies. Nothing you type is sent or saved. Your real agent is trained on your treatments, pricing, policies, and schedule.</p>
        <p class="demo-cta"><a class="btn btn-primary" href="%s">Get an AI Agent for My Med Spa</a></p>
      </div>
    </div>
  </div>
</section>''' % (bg, eyebrow, title, lede, tab_html, demo_id, start,
                 ic("chart", 13, 2.4), ic("zap", 13, 2.4), ic("repeat", 13, 2.2), demo_id, demo_id, ic("arrow", 18, 2.4), QUOTE)


CALL_BTN = ic("phone", 18, 2) + "Get Started"

DEMO_SCRIPT = '<script src="/sms-demo.js" defer></script>'
