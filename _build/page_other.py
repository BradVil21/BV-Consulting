from common import *
from posts_meta import POSTS, CATS

US_STATES = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia",
             "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
             "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
             "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
             "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
             "Washington", "West Virginia", "Wisconsin", "Wyoming"]


# ---------------------------------------------------------------- About
def about():
    body = '''
<section class="page-hero bg-warm">
  <div class="container">
    {crumbs}
    <span class="eyebrow">About BV Consulting</span>
    <h1>The Growth Partner for Med Spas That Want to Book More and Do Less Busywork</h1>
    <p class="lede">We combine AI, automation, SEO, and web development into one system designed around how aesthetic practices actually run.</p>
    <p class="foot-based" style="color:var(--blue-deep)">{pin} Based in Fort Lauderdale, FL &middot; Serving med spas nationwide</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split-photo">
      <div>
        <span class="eyebrow">Our story</span>
        <h2>From hands-on tech support to med spa growth systems</h2>
        <p>BV Consulting started in Fort Lauderdale solving technology problems for local businesses. Some of the busiest clients we worked with were med spas, and they all shared the same frustrations: inquiries piling up after hours, no-shows leaving gaps in the schedule, booking software that didn't talk to anything else, and websites that didn't show up on Google.</p>
        <p>So we built our services around fixing exactly that. Today we design websites and SEO strategies, create custom AI agents, automate SMS and booking workflows, and integrate the software med spas depend on, for practices across the country.</p>
        <p>We work with several AI tools, including Claude by Anthropic, and we're not tied to any single vendor. Our job is to pick what works best for your practice and make it simple for your team.</p>
      </div>
      {photo}
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">What we stand for</span><h2>How We Work With Med Spas</h2></div>
    <div class="values">
      <div class="value"><div class="ic">{i_shield}</div><div><h3>Privacy first</h3><p>We treat client information with care, minimize PHI in every tool, and document how data moves.</p></div></div>
      <div class="value"><div class="ic">{i_chat}</div><div><h3>Plain English</h3><p>No jargon. You'll always understand what we're building, why it matters, and how to use it.</p></div></div>
      <div class="value"><div class="ic">{i_chart}</div><div><h3>Results you can see</h3><p>We track inquiries, bookings, no-shows, and rankings so you can see what your investment is doing.</p></div></div>
      <div class="value"><div class="ic">{i_heart}</div><div><h3>Client experience matters</h3><p>Every automation should feel as thoughtful as your front desk team on its best day.</p></div></div>
    </div>
  </div>
</section>

{tools}

{cta}
'''.format(crumbs=crumbs([("Home", "/"), ("About", "/about/")]), pin=ic("pin", 16, 2),
           photo=picture("growth-strategy-session", "Strategy workshop with a presenter and a team working on laptops", fallback_icon="heart"),
           i_shield=ic("shield", 22), i_chat=ic("chat", 22), i_chart=ic("chart", 22), i_heart=ic("heart", 22),
           tools=ai_tools_section(""),
           cta=cta_strip("Let's grow your med spa together", "Get a free quote and a clear growth plan for your practice."))
    page("/about/", "About BV Consulting | Med Spa Growth & AI Partner",
         "BV Consulting builds AI agents, SEO, websites, SMS booking automation, and integrations for med spas. Based in Fort Lauderdale, FL, serving med spas nationwide.",
         body, schemas=[{"@context": "https://schema.org", "@type": "AboutPage", "url": SITE + "/about/", "name": "About BV Consulting", "about": {"@id": BUSINESS_ID}},
                        breadcrumb_ld([("Home", "/"), ("About", "/about/")])],
         active="/about/", priority="0.6", images=["growth-strategy-session"])


# ---------------------------------------------------------------- Contact
def contact():
    style = '''<style>
.contact-grid{display:grid;grid-template-columns:1fr;gap:24px}
.contact-info{display:flex;flex-direction:column;gap:14px}
.ci-item{display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px}
.ci-item .ic{flex-shrink:0;width:44px;height:44px;border-radius:11px;background:linear-gradient(135deg,var(--blue-soft),#fff);border:1px solid var(--blue-soft);display:flex;align-items:center;justify-content:center;color:var(--blue-dark)}
.ci-item h2{margin:0 0 2px;font-size:1.05rem}
.ci-item p,.ci-item a{margin:0;font-size:.95rem}
.form-note{font-size:.82rem;color:var(--muted);margin-top:8px}
.form-success{display:none;background:var(--blue-soft);border:1px solid #bfe3fb;color:var(--blue-deep);border-radius:12px;padding:16px;font-weight:600;margin-top:10px}
.form-success.show{display:block}
@media(min-width:880px){.contact-grid{grid-template-columns:1fr 1.1fr;gap:36px;align-items:start}}
</style>'''
    opts = "".join("<option>%s</option>" % strip(s["name"]).replace("&", "&amp;") for s in SERVICES) + "<option>The complete growth system</option><option>Not sure yet</option>"
    body = '''
<section class="page-hero bg-warm">
  <div class="container">
    {crumbs}
    <span class="eyebrow">Get in touch</span>
    <h1>Contact BV Consulting</h1>
    <p class="lede">Have a question about AI agents, SEO, booking automation, or integrations for your med spa? Send a message or call. Ready for pricing? <a href="{quote}">Get a free quote</a>.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-info">
        <div class="ci-item"><div class="ic">{i_arrow}</div><div><h2>Want a quote?</h2><p style="color:var(--ink-2)">Answer a few quick questions about your practice and get a free growth plan and quote.</p><a class="btn btn-primary" href="{quote}" style="margin-top:10px">Get a Free Quote</a></div></div>
        <div class="ci-item"><div class="ic">{i_phone}</div><div><h2>Call us</h2><a href="tel:{tel}">{phone}</a><p style="color:var(--muted)">Mon&ndash;Fri 8am&ndash;6pm ET</p></div></div>
        <div class="ci-item"><div class="ic">{i_mail}</div><div><h2>Email us</h2><a href="mailto:{email}">{email}</a><p style="color:var(--muted)">We reply within 24 hours</p></div></div>
        <div class="ci-item"><div class="ic">{i_pin}</div><div><h2>Location</h2><p style="color:var(--ink-2)">Based in Fort Lauderdale, FL. Serving med spas nationwide, with in-person meetings in South Florida.</p></div></div>
      </div>
      <div class="form-card">
        <h2 style="margin-bottom:6px;font-size:1.4rem">Send us a message</h2>
        <p style="font-size:.92rem">Tell us about your practice and what you'd like to improve.</p>
        <form id="contact-form" novalidate>
          <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true" />
          <div class="field-row">
            <div class="field"><label for="cname">Name</label><input id="cname" name="name" type="text" required autocomplete="name" placeholder="Your name" /></div>
            <div class="field"><label for="cbiz">Practice name</label><input id="cbiz" name="business" type="text" autocomplete="organization" placeholder="Your med spa" /></div>
          </div>
          <div class="field-row">
            <div class="field"><label for="cemail">Email</label><input id="cemail" name="email" type="email" required autocomplete="email" placeholder="you@yourmedspa.com" /></div>
            <div class="field"><label for="cphone">Phone</label><input id="cphone" name="phone" type="tel" autocomplete="tel" placeholder="(000) 000-0000" /></div>
          </div>
          <div class="field"><label for="cinterest">I'm interested in</label><select id="cinterest" name="interest">{opts}</select></div>
          <div class="field"><label for="cmsg">How can we help?</label><textarea id="cmsg" name="message" required placeholder="Tell us about your practice and goals. Please don't include patient health information."></textarea></div>
          <button type="submit" class="btn btn-primary" style="width:100%">Send Message</button>
          <p class="form-note">By submitting, you agree to be contacted by BV Consulting about your request. See our <a href="/privacy/">Privacy Policy</a>.</p>
          <div class="form-success" id="contact-success" role="status">Thanks! Your message has been sent. We'll reach out within 24 hours.</div>
          <div class="form-error" id="contact-error" role="alert"></div>
        </form>
      </div>
    </div>
  </div>
</section>
'''.format(crumbs=crumbs([("Home", "/"), ("Contact", "/contact/")]), quote=QUOTE, i_arrow=ic("arrow", 22), i_phone=ic("phone", 22),
           i_mail=ic("mail", 22), i_pin=ic("pin", 22), tel=TEL, phone=PHONE, email=EMAIL, opts=opts)
    page("/contact/", "Contact BV Consulting | Med Spa Marketing & AI | 954-825-1009",
         "Contact BV Consulting about AI agents, SEO, websites, SMS booking automation, and integrations for your med spa by phone, text, or email.",
         body, schemas=[BUSINESS, {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/contact/", "name": "Contact BV Consulting", "about": {"@id": BUSINESS_ID}},
                        breadcrumb_ld([("Home", "/"), ("Contact", "/contact/")])],
         active="/contact/", extra_head=style, priority="0.6")


# ---------------------------------------------------------------- Blog index
def blog_index():
    filters = '<button type="button" class="filter active" data-filter="all" aria-pressed="true">All articles</button>' + "".join(
        '<button type="button" class="filter" data-filter="%s" aria-pressed="false">%s</button>' % (k, v[0].replace("&", "&amp;")) for k, v in CATS.items())
    body = '''
<section class="page-hero bg-warm">
  <div class="container">
    {crumbs}
    <span class="eyebrow">Med spa growth guides</span>
    <h1>The BV Consulting Med Spa Blog</h1>
    <p class="lede">Practical guides on AI agents, SEO, booking automation, websites, and software integrations for med spa owners and managers.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="filters" role="group" aria-label="Filter articles by topic">{filters}</div>
    <div class="blog-grid">{cards}</div>
  </div>
</section>
{cta}
'''.format(crumbs=crumbs([("Home", "/"), ("Blog", "/blog/")]), filters=filters, cards="\n".join(post_card(p) for p in POSTS),
           cta=cta_strip("Want this built for your med spa?", "Skip the DIY. Get a free quote and we'll build it for you."))
    blog_ld = {"@context": "https://schema.org", "@type": "Blog", "@id": SITE + "/blog/#blog", "url": SITE + "/blog/",
               "name": "BV Consulting Med Spa Blog", "publisher": {"@id": BUSINESS_ID}, "inLanguage": "en-US",
               "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": SITE + p["url"], "datePublished": p["date"]} for p in POSTS]}
    page("/blog/", "Med Spa Marketing Blog: AI, SEO & Automation | BV Consulting",
         "Guides for med spa owners on AI agents, SEO, SMS and booking automation, website design, and software integrations.",
         body, schemas=[blog_ld, breadcrumb_ld([("Home", "/"), ("Blog", "/blog/")])], active="/blog/", priority="0.8")


# ---------------------------------------------------------------- Quote funnel
# Add real client reviews here to show them in the card slider, e.g.
# ("Client quote text...", "Name", "Practice / City"). Leave empty to show service highlights instead.
REVIEWS = []

HIGHLIGHTS = [
    ("bot", "AI", "Never miss a lead again", "Your AI agent answers texts and missed calls in seconds, day or night, and books the consultation for your team.", "AI Agents &amp; SMS"),
    ("calendar", "BK", "Fewer no-shows, fuller books", "Automated confirmations, reminders, and rebooking nudges that sync with the booking software you already use.", "Booking Automation"),
    ("search", "SEO", "Get found on Google", "Local SEO and treatment pages built around what clients actually search for, like lip filler or laser hair removal near me.", "Med Spa SEO"),
    ("nodes", "API", "Your tools, finally connected", "Your booking software, CRM, forms, and payments talking to each other, so there's less double entry for the front desk.", "API Integrations"),
    ("shield", "BV", "Compliance-minded from day one", "Opt-in consent, STOP handling, and no medical advice from AI. Clinical questions are routed to your licensed team.", "Built for Med Spas"),
]

QUOTE_STYLE = '''<style>
body.funnel{background:#f3f8fc}
.funnel-nav{max-width:700px}
.secure-badge{display:inline-flex;align-items:center;gap:6px;background:#e8f7ef;color:#0a7a45;border:1px solid #c9ecd8;border-radius:999px;padding:6px 12px;font-size:.8rem;font-weight:700;white-space:nowrap}
.q-wrap{padding:22px 0 44px}
.q-wrap .container{max-width:700px}
.qcard{background:#fff;border-radius:26px;box-shadow:0 24px 60px rgba(15,94,147,.10),0 2px 6px rgba(10,13,18,.04);border:1px solid #e8eef5;padding:28px 18px 24px}
.q-intro{text-align:center}
.q-pill{display:inline-flex;align-items:center;gap:7px;background:var(--blue-soft);color:var(--blue-deep);border-radius:999px;padding:8px 14px;font-size:.74rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.q-pill svg{fill:currentColor}
.q-intro h1{font-size:clamp(1.75rem,6.4vw,2.55rem);line-height:1.14;margin:16px auto 12px;max-width:560px;letter-spacing:-.01em}
.grad{background:linear-gradient(90deg,var(--blue-deep),var(--blue));-webkit-background-clip:text;background-clip:text;color:transparent}
.q-lede{color:var(--ink-2);font-size:1rem;line-height:1.7;max-width:460px;margin:0 auto 22px}
.q-progress{display:none;margin-bottom:18px}
.qcard.started .q-progress{display:block}
.qcard.started .q-intro{display:none}
.progress-meta{display:flex;justify-content:space-between;font-size:.8rem;color:var(--muted);font-weight:700;margin-bottom:8px}
.progress-track{height:8px;border-radius:999px;background:var(--blue-soft);overflow:hidden}
.progress-fill{height:100%;width:0%;background:linear-gradient(90deg,var(--blue),var(--blue-deep));border-radius:999px;transition:width .4s var(--ease)}
.step-panel{display:none;animation:fadeIn .35s var(--ease)}
.step-panel.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.step-q{font-family:'Poppins',sans-serif;font-weight:700;color:var(--black);font-size:1.25rem;margin:0 0 4px;line-height:1.25}
.step-help{color:var(--muted);font-size:.9rem;margin-bottom:16px}
.step-panel[data-step="1"] .step-q{font-size:1rem;text-align:center;color:var(--ink-2);margin-bottom:12px}
.opt-grid{display:grid;grid-template-columns:minmax(0,1fr);gap:9px}
@media(min-width:560px){.opt-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
.opt{display:flex;align-items:center;gap:11px;text-align:left;background:#fff;border:2px solid var(--line);border-radius:12px;padding:12px 14px;cursor:pointer;font-size:.95rem;font-weight:600;color:var(--ink);transition:border-color .15s,background .15s,transform .15s,box-shadow .15s;font-family:inherit;width:100%;min-height:var(--tap)}
.opt:hover{border-color:var(--blue);background:var(--blue-50)}
.opt.selected{border-color:var(--blue);background:var(--blue-soft)}
.opt .opt-ic{flex-shrink:0;width:34px;height:34px;border-radius:9px;background:var(--blue-soft);display:flex;align-items:center;justify-content:center;color:var(--blue-dark)}
.opt.selected .opt-ic{background:var(--blue);color:#fff}
.choice-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.opt.opt-card{flex-direction:column;justify-content:flex-start;text-align:center;gap:6px;padding:20px 10px 18px;border:2px solid #dfe8f1;border-radius:18px;background:#fbfdff}
.opt.opt-card .opt-ic{width:54px;height:54px;border-radius:14px;margin-bottom:8px}
.opt.opt-card b{font-family:'Poppins',sans-serif;font-size:1rem;color:var(--black);line-height:1.25}
.opt.opt-card small{font-size:.8rem;color:var(--muted);font-weight:500;line-height:1.35}
.opt.opt-card:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(15,94,147,.10)}
@media(max-width:359px){.choice-grid{grid-template-columns:minmax(0,1fr)}}
.opt.multi .opt-check{margin-left:auto}
.wiz-nav{display:flex;justify-content:space-between;align-items:center;margin-top:16px;gap:12px}
.qcard:not(.started) .wiz-nav{display:none}
.btn-back{background:transparent;border:0;color:var(--muted);font-weight:700;font-family:inherit;font-size:.95rem;cursor:pointer;padding:8px 4px;min-height:var(--tap)}
.btn-back:hover{color:var(--ink)}
.summary-box{background:var(--bg-soft);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin-bottom:16px;font-size:.86rem}
.summary-box .srow{display:flex;justify-content:space-between;gap:12px;padding:3px 0;color:var(--ink-2)}
.summary-box .srow b{color:var(--black);font-weight:600;flex-shrink:0}
.summary-box .srow span:last-child{text-align:right;color:var(--blue-dark);font-weight:600}
.q-trust{display:flex;flex-wrap:wrap;justify-content:center;gap:8px 18px;list-style:none;margin:22px 0 0;padding:18px 0 0;border-top:1px solid var(--line)}
.q-trust li{display:flex;align-items:center;gap:6px;font-size:.84rem;font-weight:600;color:var(--ink-2)}
.q-trust svg{color:#12a26a;flex-shrink:0}
.qslider{margin-top:18px}
.qslides{display:grid;background:#f8fbfe;border:1px solid #e3ebf3;border-radius:18px;overflow:hidden;touch-action:pan-y}
.qslide{grid-area:1/1;margin:0;padding:18px 18px 16px;opacity:0;visibility:hidden;transition:opacity .45s var(--ease),visibility .45s}
.qslide.is-active{opacity:1;visibility:visible}
.qs-top{display:flex;align-items:center;gap:8px;margin-bottom:8px}
.qs-top .qs-ic{width:30px;height:30px;border-radius:9px;background:var(--blue-soft);color:var(--blue-dark);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.qs-top b{font-family:'Poppins',sans-serif;color:var(--black);font-size:1rem;line-height:1.3}
.qs-stars{display:flex;gap:2px;color:#f5b301}
.qs-stars svg{fill:currentColor}
.qslide p{font-style:italic;color:var(--ink-2);font-size:.95rem;line-height:1.65;margin:0 0 14px}
.qslide figcaption{display:flex;align-items:center;gap:11px}
.qs-av{width:42px;height:42px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--blue-deep));color:#fff;font-weight:800;font-size:.78rem;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.qslide figcaption strong{display:block;color:var(--black);font-size:.92rem;line-height:1.2}
.qslide figcaption small{display:block;color:var(--muted);font-size:.78rem;margin-top:2px}
.qs-dots{display:flex;justify-content:center;gap:4px;margin-top:8px}
.qs-dots button{width:24px;height:24px;border:0;background:transparent;padding:0;cursor:pointer;display:flex;align-items:center;justify-content:center}
.qs-dots button:before{content:"";width:8px;height:8px;border-radius:50%;background:#d3dee9;transition:background .2s,transform .2s}
.qs-dots button[aria-current="true"]:before{background:var(--blue);transform:scale(1.25)}
.q-contact{text-align:center;margin-top:12px;font-size:.92rem;color:var(--ink-2);line-height:1.8}
.q-contact a[href^="tel"]{white-space:nowrap}
.q-contact a{font-weight:700;color:var(--blue-deep);text-decoration:underline;text-underline-offset:2px;overflow-wrap:anywhere}
.q-consent{font-size:.76rem;color:var(--muted);margin-top:10px;text-align:center;line-height:1.5}
.q-tools{background:#fff;border-top:1px solid #e3ebf3;border-bottom:1px solid #e3ebf3;padding:34px 0 26px;text-align:center}
.q-tools h2{font-size:1.15rem;margin:0 0 18px}
.q-tools .logo-label{display:none}
.q-tools .logo-set{gap:14px;padding-right:14px}
.q-tools .logo-set li{background:#fff;border:1px solid var(--line);border-radius:12px;height:62px;padding:0 22px;box-shadow:0 1px 2px rgba(10,13,18,.03)}
.q-tools .logo-set img{height:28px}
.q-tools .logo-set img.logo-sq{height:32px}
.q-tools-note{font-size:.76rem;color:var(--muted);max-width:560px;margin:14px auto 0;line-height:1.5}
.q-faq{padding:36px 0 10px}
.q-faq .container{max-width:700px}
.q-faq h2{font-size:1.3rem;text-align:center;margin-bottom:14px}
.funnel-foot{background:#f3f8fc;border-top:0;text-align:center;padding:18px 0 30px}
.funnel-foot .container{max-width:700px}
.ff-links{display:flex;flex-wrap:wrap;justify-content:center;gap:4px 20px;margin-bottom:10px}
.ff-links a{color:var(--ink-2);font-weight:600;font-size:.86rem}
.funnel-foot p{font-size:.8rem;color:var(--muted);line-height:1.6;margin:0 0 6px}
.load-overlay{position:fixed;inset:0;background:rgba(255,255,255,.96);display:none;flex-direction:column;align-items:center;justify-content:center;z-index:300;padding:24px;text-align:center}
.load-overlay.show{display:flex}
.spinner{width:46px;height:46px;border:4px solid var(--blue-soft);border-top-color:var(--blue);border-radius:50%;animation:spin 1s linear infinite;margin-bottom:18px}
@keyframes spin{to{transform:rotate(360deg)}}
@media(min-width:640px){.qcard{padding:34px 34px 28px}.q-wrap{padding:30px 0 56px}.qslide{padding:20px 22px 18px}}
.funnel-nav .brand{white-space:nowrap}
@media(max-width:480px){.secure-badge{font-size:.72rem;padding:5px 10px;gap:5px}.secure-badge svg{width:13px;height:13px}.funnel-nav .brand{font-size:.98rem;gap:8px}.funnel-nav .brand-badge{width:34px;height:34px}}
@media(max-width:359px){.secure-badge span{display:none}.secure-badge{padding:7px}.qcard{padding:22px 14px 20px}.q-pill{font-size:.64rem;letter-spacing:.06em;padding:7px 11px}}
@media (prefers-reduced-motion:reduce){.qslide{transition:none}}
</style>'''


def quote():
    def opts(items, multi=False):
        out = []
        for i, v in items:
            chk = '<span class="opt-check">%s</span>' % ic("check", 14, 3) if multi else ""
            out.append('<button type="button" class="opt%s" data-value="%s"%s><span class="opt-ic">%s</span>%s%s</button>' % (
                " multi" if multi else "", v, ' aria-pressed="false"' if multi else "", ic(i, 18, 1.7), v, chk))
        return "\n".join(out)

    cards = "".join('<button type="button" class="opt opt-card" data-value="%s"><span class="opt-ic">%s</span><b>%s</b><small>%s</small></button>' % (v, ic(i, 26, 1.7), v, sub)
                    for i, v, sub in [("pin", "Single Med Spa", "One location, or opening soon"),
                                      ("building", "Multi-Location Group", "Several locations or a franchise")])
    steps = [
        ("services", "What do you want help with?", "Choose all that apply.", True,
         [("bot", "AI agent / AI receptionist"), ("calendar", "Automated SMS &amp; booking"), ("sparkle", "AI automation workflows"),
          ("search", "Med spa SEO"), ("web", "Website development"), ("nodes", "API &amp; software integrations"), ("layers", "The complete growth system")]),
        ("software", "Which booking or EMR software do you use?", "We'll check integration options before your consultation.", False,
         [("calendar", "Boulevard"), ("calendar", "Zenoti"), ("calendar", "Mangomint"), ("calendar", "Vagaro"), ("calendar", "Mindbody"),
          ("calendar", "AestheticsPro"), ("calendar", "Aesthetic Record"), ("calendar", "PatientNow"), ("dots", "Other software"), ("question", "Not sure / none")]),
        ("challenge", "What's your biggest challenge right now?", "We'll focus your growth plan here.", False,
         [("phone", "Missed calls &amp; slow follow-up"), ("calendar", "No-shows &amp; cancellations"), ("search", "Not showing up on Google"),
          ("web", "Website doesn't convert"), ("edit", "Too much front desk admin"), ("repeat", "Low rebooking &amp; retention")]),
    ]
    panels = ['''<div class="step-panel active" data-step="1" data-key="size">
              <h2 class="step-q">Which best describes your practice?</h2>
              <div class="choice-grid" data-choices>%s</div>
            </div>''' % cards]
    for n, (key, q, help_, multi, items) in enumerate(steps):
        cont = '<button type="button" class="btn btn-primary wiz-continue" data-continue disabled>Continue</button>' if multi else ""
        panels.append('''<div class="step-panel" data-step="%d" data-key="%s"%s>
              <h2 class="step-q">%s</h2><p class="step-help">%s</p>
              <div class="opt-grid" data-choices>%s</div>%s
            </div>''' % (n + 2, key, ' data-multi="1"' if multi else "", q, help_, opts(items, multi), cont))
    total = len(panels) + 1
    states = "".join('<option%s>%s</option>' % (' value=""' if s == "" else "", s) for s in [""] + US_STATES)

    star = ic("star", 17, 1.2)
    if REVIEWS:
        slides = ['''<figure class="qslide" aria-roledescription="slide" aria-label="%d of %d">
          <div class="qs-top qs-stars" aria-label="5 out of 5 stars">%s</div>
          <p>%s</p>
          <figcaption><span class="qs-av" aria-hidden="true">%s</span><span><strong>%s</strong><small>%s</small></span></figcaption>
        </figure>''' % (n + 1, len(REVIEWS), star * 5, txt, "".join(w[0] for w in name.split()[:2]).upper(), name, where)
                  for n, (txt, name, where) in enumerate(REVIEWS)]
        slider_label = "Client reviews"
    else:
        slides = ['''<figure class="qslide" aria-roledescription="slide" aria-label="%d of %d">
          <div class="qs-top"><span class="qs-ic">%s</span><b>%s</b></div>
          <p>%s</p>
          <figcaption><span class="qs-av" aria-hidden="true">%s</span><span><strong>%s</strong><small>Included in your growth plan</small></span></figcaption>
        </figure>''' % (n + 1, len(HIGHLIGHTS), ic(i, 17, 2), t, d, av, tag)
                  for n, (i, av, t, d, tag) in enumerate(HIGHLIGHTS)]
        slider_label = "What BV Consulting builds for med spas"
    slides[0] = slides[0].replace('class="qslide"', 'class="qslide is-active"', 1)

    faqs = [
        ("Is the quote really free?", "Yes. The consultation, growth plan, and quote are free with no obligation."),
        ("How fast will I hear back?", "We typically respond within 24 hours on business days, by phone, text, or email, whichever you prefer."),
        ("Do you work with med spas outside Florida?", "Yes. BV Consulting is based in Fort Lauderdale and works with med spas nationwide."),
        ("Should I include patient information?", "No. Please don't share any patient or health information in this form. We only need details about your practice."),
    ]
    body = '''
<section class="q-wrap">
  <div class="container">
    <div class="qcard" id="quote-form-wrap">
      <div class="q-intro">
        <span class="q-pill">{star_sm}Free quote, no obligation</span>
        <h1>Get a Free <span class="grad">Med Spa Growth Plan</span> in About a Minute</h1>
        <p class="q-lede">Answer a few quick questions and we'll send a clear plan and quote for AI agents, automated texting and booking, SEO, and your website.</p>
      </div>
      <div class="q-progress">
        <div class="progress-meta"><span id="step-label">Step 2 of {total}</span><span id="step-pct"></span></div>
        <div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div>
      </div>
      <form id="quote-form" novalidate>
        <input type="text" name="_honey" id="q-honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true" />
        {panels}
        <div class="step-panel" data-step="{total}" data-key="contact">
          <h2 class="step-q">Where should we send your growth plan?</h2>
          <p class="step-help">Last step. We'll reach out within 24 hours.</p>
          <div class="summary-box" id="summary-box"></div>
          <div class="field-row">
            <div class="field"><label for="q-name">Full name</label><input id="q-name" type="text" required autocomplete="name" placeholder="Your name" /></div>
            <div class="field"><label for="q-business">Practice name</label><input id="q-business" type="text" required autocomplete="organization" placeholder="Your med spa" /></div>
          </div>
          <div class="field-row">
            <div class="field"><label for="q-email">Email</label><input id="q-email" type="email" required autocomplete="email" placeholder="you@yourmedspa.com" /></div>
            <div class="field"><label for="q-phone">Phone</label><input id="q-phone" type="tel" required autocomplete="tel" placeholder="(000) 000-0000" /></div>
          </div>
          <div class="field-row">
            <div class="field"><label for="q-state">State</label><select id="q-state" required>{states}</select></div>
            <div class="field"><label for="q-city">City</label><input id="q-city" type="text" autocomplete="address-level2" placeholder="City" /></div>
          </div>
          <div class="field"><label for="q-site">Website <span style="font-weight:400;color:var(--muted)">(optional)</span></label><input id="q-site" type="text" placeholder="yourmedspa.com" /></div>
          <div class="field"><label for="q-details">Anything else? <span style="font-weight:400;color:var(--muted)">(optional, no patient info please)</span></label><textarea id="q-details" placeholder="Goals, tools you use, timeline..."></textarea></div>
          <button type="submit" class="btn btn-primary" style="width:100%">Get My Free Growth Plan</button>
          <p class="q-consent">By submitting, you agree to our <a href="/privacy/">Privacy Policy</a> and consent to be contacted by BV Consulting by phone, text, or email about your request. Consent isn't a condition of purchase. Msg &amp; data rates may apply. Reply STOP to opt out.</p>
          <div class="form-error" id="quote-error" role="alert"></div>
        </div>
        <div class="wiz-nav">
          <button type="button" class="btn-back" id="btn-back">&larr; Back</button>
          <span style="font-size:.8rem;color:var(--muted)">Free &bull; No obligation</span>
        </div>
      </form>

      <ul class="q-trust">
        <li>{i_check}Serving Med Spas Nationwide</li><li>{i_check}100% Free Quote</li><li>{i_check}No Spam, Ever</li><li>{i_check}Reply Within 24 Hours</li>
      </ul>

      <div class="qslider" aria-roledescription="carousel" aria-label="{slider_label}">
        <div class="qslides" aria-live="off">
        {slides}
        </div>
        <div class="qs-dots" role="group" aria-label="Choose slide">{dots}</div>
      </div>

      <div class="q-contact">
        <div>Rather talk to a person? Call or text <a href="tel:{tel}">(954) 825-1009</a></div>
        <div>Questions? Email <a href="mailto:{email}">{email}</a></div>
      </div>
    </div>
  </div>
</section>

<section class="q-tools" aria-labelledby="q-tools-h">
  <div class="container">
    <h2 id="q-tools-h">Built with <span class="grad">trusted AI &amp; booking tools</span></h2>
    {carousel}
    <p class="q-tools-note">We build with leading AI tools, including Claude by Anthropic, and connect them to the software your med spa already uses. BV Consulting is an independent consultancy and is not endorsed by these companies.</p>
  </div>
</section>

<section class="q-faq">
  <div class="container">
    <h2>Quick Questions</h2>
    {faqs}
  </div>
</section>

<div class="load-overlay" id="load-overlay" role="status" aria-live="polite"><div class="spinner"></div><h3>Sending your request&hellip;</h3><p style="color:var(--muted)">This only takes a moment.</p></div>
'''.format(star_sm=ic("star", 12, 1), i_check=ic("check", 15, 3), panels="\n        ".join(panels), states=states, total=total,
           slides="\n        ".join(slides), slider_label=slider_label, tel=TEL, email=EMAIL,
           dots="".join('<button type="button" aria-label="Slide %d"%s></button>' % (n + 1, ' aria-current="true"' if n == 0 else "") for n in range(len(slides))),
           faqs=faq_html(faqs), carousel=logo_carousel(""))

    script = r'''<script>
document.addEventListener("DOMContentLoaded",function(){
  var TOTAL=__TOTAL__, current=1, answers={services:[]};
  var card=document.getElementById("quote-form-wrap");
  var panels=document.querySelectorAll(".step-panel");
  var fill=document.getElementById("progress-fill"), label=document.getElementById("step-label"), pct=document.getElementById("step-pct");
  var back=document.getElementById("btn-back");
  var LABELS={size:"Practice",services:"Services",software:"Software",challenge:"Challenge"};
  var started=false;
  function show(step,scroll){
    current=step;
    panels.forEach(function(p){p.classList.toggle("active", +p.dataset.step===step);});
    card.classList.toggle("started", step>1);
    var percent=Math.round(step/TOTAL*100);
    fill.style.width=percent+"%"; label.textContent="Step "+step+" of "+TOTAL; pct.textContent=percent+"%";
    if(step===TOTAL) buildSummary();
    if(scroll){ var top=card.getBoundingClientRect().top; if(top<0||top>window.innerHeight*.4){ window.scrollTo({top:top+window.scrollY-12,behavior:"smooth"}); } }
  }
  document.querySelectorAll("[data-choices]").forEach(function(grid){
    var panel=grid.closest(".step-panel"), key=panel.dataset.key, multi=panel.dataset.multi==="1";
    var cont=panel.querySelector("[data-continue]");
    grid.querySelectorAll(".opt").forEach(function(btn){
      btn.addEventListener("click",function(){
        if(!started){started=true; if(window.BV) window.BV.track("quote_start");}
        if(multi){
          var on=!btn.classList.contains("selected"); btn.classList.toggle("selected",on); btn.setAttribute("aria-pressed",on?"true":"false");
          answers[key]=Array.prototype.map.call(grid.querySelectorAll(".opt.selected"),function(b){return b.dataset.value;});
          cont.disabled=answers[key].length===0;
        } else {
          grid.querySelectorAll(".opt").forEach(function(b){b.classList.remove("selected");});
          btn.classList.add("selected"); answers[key]=btn.dataset.value;
          setTimeout(function(){ if(current<TOTAL) show(current+1,true); },220);
        }
      });
    });
    if(cont){ cont.addEventListener("click",function(){ show(current+1,true); }); }
  });
  back.addEventListener("click",function(){ if(current>1) show(current-1,true); });
  function escHtml(s){var d=document.createElement("div");d.innerHTML=s;return String(d.textContent).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
  function val(k){var v=Array.isArray(answers[k])?answers[k].join(", "):(answers[k]||""); var d=document.createElement("div"); d.innerHTML=v; return d.textContent;}
  function buildSummary(){
    document.getElementById("summary-box").innerHTML=Object.keys(LABELS).filter(function(k){return val(k);}).map(function(k){
      return '<div class="srow"><b>'+LABELS[k]+'</b><span>'+escHtml(val(k))+'</span></div>';}).join("");
  }
  var form=document.getElementById("quote-form");
  form.addEventListener("submit",function(e){
    e.preventDefault();
    if(document.getElementById("q-honey").value) return;
    var ids=["q-name","q-business","q-email","q-phone","q-state"];
    for(var i=0;i<ids.length;i++){ var el=document.getElementById(ids[i]); if(!el.checkValidity()||!el.value.trim()){ el.reportValidity(); el.focus(); return; } }
    var g=function(id){return document.getElementById(id).value.trim();};
    var data={form:"Med spa quote funnel (/quote)",practice_size:val("size"),services:val("services"),
      software:val("software"),biggest_challenge:val("challenge"),name:g("q-name"),practice:g("q-business"),email:g("q-email"),
      phone:g("q-phone"),state:g("q-state"),city:g("q-city"),website:g("q-site"),details:g("q-details")};
    var err=document.getElementById("quote-error"), ov=document.getElementById("load-overlay");
    err.classList.remove("show"); ov.classList.add("show");
    window.BV.submitLead(data,"New med spa quote request: "+data.practice+" ("+data.state+")").then(function(){
      try{ sessionStorage.setItem("bv_lead_name", data.name.split(" ")[0]); }catch(x){}
      window.location.href="/thank-you/";
    }).catch(function(){
      ov.classList.remove("show");
      err.innerHTML='We couldn’t send your request just now. Please <a href="'+window.BV.mailtoFallback(data,"Med spa quote request")+'">email your details to us</a> or call or text <a href="tel:+19548251009">(954) 825-1009</a>.';
      err.classList.add("show");
    });
  });
  show(1,false);

  /* slider */
  var slider=document.querySelector(".qslider");
  if(slider){
    var slides=slider.querySelectorAll(".qslide"), dots=slider.querySelectorAll(".qs-dots button"), idx=0, timer=null, paused=false;
    var reduce=window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    function go(n){ idx=(n+slides.length)%slides.length;
      slides.forEach(function(s,i){s.classList.toggle("is-active",i===idx);});
      dots.forEach(function(d,i){ if(i===idx) d.setAttribute("aria-current","true"); else d.removeAttribute("aria-current"); }); }
    function play(){ if(reduce) return; clearInterval(timer); timer=setInterval(function(){ if(!paused&&!document.hidden) go(idx+1); },6000); }
    dots.forEach(function(d,i){ d.addEventListener("click",function(){ go(i); play(); }); });
    slider.addEventListener("mouseenter",function(){paused=true;}); slider.addEventListener("mouseleave",function(){paused=false;});
    slider.addEventListener("focusin",function(){paused=true;}); slider.addEventListener("focusout",function(){paused=false;});
    var x0=null, box=slider.querySelector(".qslides");
    box.addEventListener("touchstart",function(e){x0=e.touches[0].clientX;},{passive:true});
    box.addEventListener("touchend",function(e){ if(x0===null) return; var dx=e.changedTouches[0].clientX-x0; if(Math.abs(dx)>40){ go(idx+(dx<0?1:-1)); play(); } x0=null; });
    play();
  }
});
</script>'''.replace("__TOTAL__", str(total))
    page(QUOTE, "Free Med Spa Marketing Quote | BV Consulting",
         "Get a free growth plan and quote for your med spa: AI agents, automated SMS and booking, SEO, website development, and API integrations. Takes 60 seconds.",
         body, schemas=[breadcrumb_ld([("Home", "/"), ("Free Quote", QUOTE)]), faq_ld(faqs)],
         extra_head=QUOTE_STYLE, scripts_after=script, funnel=True, priority="0.9")


def thank_you():
    body = '''
<section class="funnel-hero" style="padding-bottom:60px">
  <div class="container center" style="max-width:760px">
    <div style="width:76px;height:76px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--blue-deep));display:flex;align-items:center;justify-content:center;margin:10px auto 18px;color:#fff">{check}</div>
    <span class="eyebrow">Request received</span>
    <h1>Thank you<span id="ty-name"></span>! Your growth plan is on the way.</h1>
    <p class="lede" style="margin:0 auto 22px">We'll review your practice and reach out within 24 hours on business days to schedule your free strategy call. Keep an eye on your phone and inbox.</p>
    <div class="hero-ctas" style="justify-content:center"><a class="btn btn-primary" href="/blog/">Read Med Spa Growth Guides</a><a class="btn btn-secondary" href="tel:{tel}">{call_btn}</a></div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="next-steps">
      <div class="next-step"><b>We review your practice</b><span>Website, Google profile, reviews, and booking flow.</span></div>
      <div class="next-step"><b>Free strategy call</b><span>We'll confirm your goals, software, and priorities.</span></div>
      <div class="next-step"><b>Your plan &amp; quote</b><span>A written plan with services, tools, timeline, and pricing.</span></div>
    </div>
  </div>
</section>
<canvas id="confetti-canvas" style="position:fixed;inset:0;pointer-events:none;z-index:500"></canvas>
'''.format(call_btn=CALL_BTN, check=ic("check", 40, 2.6), tel=TEL, phone=PHONE)
    script = r'''<script>
document.addEventListener("DOMContentLoaded",function(){
  try{var n=sessionStorage.getItem("bv_lead_name"); if(n){document.getElementById("ty-name").textContent=", "+n;}}catch(e){}
  if(window.BV) window.BV.track("quote_thank_you_view");
  if(window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var c=document.getElementById("confetti-canvas"),x=c.getContext("2d");c.width=innerWidth;c.height=innerHeight;
  var cols=["#2BA0EE","#0f5e93","#c98d7a","#efe3d6","#7cc7f6"],P=[];
  for(var i=0;i<140;i++)P.push({x:Math.random()*c.width,y:-20-Math.random()*c.height*.5,w:6+Math.random()*7,h:8+Math.random()*9,c:cols[i%cols.length],r:Math.random()*3,vr:(Math.random()-.5)*.3,vy:2.4+Math.random()*3,vx:(Math.random()-.5)*2});
  var t0=Date.now();(function f(){x.clearRect(0,0,c.width,c.height);P.forEach(function(p){p.y+=p.vy;p.x+=p.vx;p.r+=p.vr;x.save();x.translate(p.x,p.y);x.rotate(p.r);x.fillStyle=p.c;x.fillRect(-p.w/2,-p.h/2,p.w,p.h);x.restore();});if(Date.now()-t0<4200)requestAnimationFrame(f);else x.clearRect(0,0,c.width,c.height);})();
});
</script>'''
    page("/thank-you/", "Thank You | BV Consulting", "Your med spa growth plan request was received.", body,
         noindex=True, funnel=True, scripts_after=script, sitemap=False)


# ---------------------------------------------------------------- Fort Lauderdale local page
LOCAL_FAQS = [
    ("Do you meet with Fort Lauderdale med spas in person?", "Yes. BV Consulting is based in Fort Lauderdale, and we're happy to meet at your practice in Broward County and nearby South Florida communities. Most ongoing work happens remotely, with video check-ins."),
    ("Do you only work with med spas in Fort Lauderdale?", "No. Fort Lauderdale is our home base, but we work with med spas and aesthetic practices nationwide."),
    ("Can you help my med spa rank in Fort Lauderdale and nearby cities?", "Yes. We optimize your Google Business Profile, build treatment and location pages, and strengthen reviews and local citations so you can compete for searches in Fort Lauderdale and the communities you draw clients from."),
    ("Can you create bilingual content for South Florida clients?", "Yes. Many South Florida practices serve Spanish- and Portuguese-speaking clients. We can build bilingual website pages, AI agent responses, and text templates, reviewed by your team."),
    ("What does it cost?", "Pricing depends on your goals, number of locations, and current software. <a href=\"/quote/\">Request a free quote</a> and we'll send a clear, written proposal."),
]


def local_page():
    areas = "".join("<li>%s</li>" % a for a in BROWARD)
    svc = "\n".join('<a class="svc-card" href="%s"><div class="svc-body"><span class="svc-ic" style="margin-top:0">%s</span><h3>%s</h3><p>%s</p><span class="more">Learn more &rarr;</span></div></a>' % (
        LOCAL_BY_SVC[s["key"]], ic(s["icon"], 20, 1.9), s["name"] + " in Fort Lauderdale", s["short"]) for s in SERVICES)
    body = '''
<section class="hero bg-warm">
  <div class="container">
    {crumbs}
    <div class="hero-grid">
      <div>
        <span class="eyebrow">Fort Lauderdale, FL</span>
        <h1>Med Spa Marketing in Fort Lauderdale, FL</h1>
        <p class="hero-sub">BV Consulting is a Fort Lauderdale-based team helping South Florida med spas book more clients with AI agents, automated SMS and booking, local SEO, websites, and software integrations. We know the market because we work in it.</p>
        <div class="hero-ctas">
          <a class="btn btn-primary" href="{quote}">Get a Free Quote</a>
          <a class="btn btn-secondary" href="tel:{tel}">{call_btn}</a>
        </div>
        <div class="hero-meta"><span><span class="dot"></span>Local, in-person meetings</span><span><span class="dot"></span>Broward, Palm Beach &amp; Miami-Dade</span></div>
      </div>
      <div class="svc-hero-photo">{photo}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:30px">
      <span class="eyebrow">The local market</span>
      <h2>What Makes Marketing a Fort Lauderdale Med Spa Different</h2>
      <p style="max-width:740px;margin:0 auto">South Florida is one of the most competitive aesthetics markets in the country. Winning here takes more than a pretty Instagram feed.</p>
    </div>
    <div class="pains" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">
      <div class="pain"><div class="ic">{i_pin}</div><div><b>Dense local competition</b><span>From Las Olas Boulevard to the Galt Ocean Mile, clients can find several med spas within a short drive. Your Google Maps presence often decides who gets the call.</span></div></div>
      <div class="pain"><div class="ic">{i_cal}</div><div><b>Seasonal swings</b><span>Winter brings seasonal residents and visitors, while summer demand shifts. Automated waitlists, reminders, and reactivation campaigns help keep the calendar steady year-round.</span></div></div>
      <div class="pain"><div class="ic">{i_chat}</div><div><b>A multilingual clientele</b><span>Broward County is home to large Spanish- and Portuguese-speaking communities. Bilingual pages, AI agent replies, and texts can make a real difference.</span></div></div>
      <div class="pain"><div class="ic">{i_zap}</div><div><b>Sun-aware treatment planning</b><span>In a sunny climate, clients often ask about downtime and sun exposure. Clear treatment pages and approved AI answers help set expectations before they book.</span></div></div>
      <div class="pain"><div class="ic">{i_phone}</div><div><b>After-hours inquiries</b><span>Busy professionals and visitors research treatments at night. A 24/7 AI agent can respond when your front desk is closed.</span></div></div>
      <div class="pain"><div class="ic">{i_search}</div><div><b>Neighborhood-level search</b><span>Clients search for treatments near Victoria Park, Wilton Manors, Coral Ridge, Harbor Beach, and beyond. Strong local SEO helps you show up where they are.</span></div></div>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">Services</span><h2>Services for Fort Lauderdale Med Spas</h2></div>
    <div class="svc-grid">{svc}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:26px">
      <span class="eyebrow">Visit or call</span>
      <h2>BV Consulting in Fort Lauderdale</h2>
      <p style="max-width:680px;margin:0 auto">We meet with med spa owners across Broward County and nearby South Florida communities.</p>
    </div>
    <div class="local-grid">
      <div class="map-wrap">
        <!-- After verifying your Google Business Profile, replace this src with your profile's "Embed a map" link so the pin matches your listing. -->
        <iframe src="https://www.google.com/maps?q=Fort%20Lauderdale%2C%20FL&amp;z=12&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map of Fort Lauderdale, Florida"></iframe>
      </div>
      <div class="nap-card">
        <h3>BV Consulting</h3>
        <ul>
          <li>{i_pin2}<span>Fort Lauderdale, FL<br><small style="color:var(--muted)">Service-area business: we meet clients at their practices</small></span></li>
          <li>{i_phone2}<a href="tel:{tel}">{phone}</a></li>
          <li>{i_mail2}<a href="mailto:{email}">{email}</a></li>
          <li>{i_clock2}<span>Monday&ndash;Friday: 8am&ndash;6pm<br>Weekends: by appointment</span></li>
          <li>{i_web2}<a href="/">bvconsulting.live</a></li>
        </ul>
        <a class="btn btn-primary" href="{quote}" style="width:100%;margin-top:18px">Get a Free Quote</a>
      </div>
    </div>
    <div style="margin-top:30px">
      <p class="soft-label center">Serving med spas in and around</p>
      <ul class="area-list">{areas}</ul>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">FAQ</span><h2>Fort Lauderdale Med Spa Marketing FAQ</h2></div>
    <div style="max-width:820px;margin:0 auto">{faqs}</div>
  </div>
</section>

{cta}
'''.format(call_btn=CALL_BTN, crumbs=crumbs([("Home", "/"), ("Fort Lauderdale Med Spa Marketing", LOCAL)]), quote=QUOTE, tel=TEL, phone=PHONE, email=EMAIL,
           photo=picture("med-spa-laser-hair-removal", "Nurse performing laser hair removal at a Fort Lauderdale area med spa", sizes="(min-width: 960px) 45vw, 100vw", eager=True, fallback_icon="pin"),
           i_pin=ic("pin", 20), i_cal=ic("calendar", 20), i_chat=ic("chat", 20), i_zap=ic("zap", 20), i_phone=ic("phone", 20), i_search=ic("search", 20),
           i_pin2=ic("pin", 18, 2), i_phone2=ic("phone", 18, 2), i_mail2=ic("mail", 18, 2), i_clock2=ic("clock", 18, 2), i_web2=ic("web", 18, 2),
           svc=svc, areas=areas, faqs=faq_html(LOCAL_FAQS),
           cta=cta_strip("Grow your Fort Lauderdale med spa", "Get a free quote from a local team that builds AI, SEO, and automation for med spas."))
    local_ld = dict(BUSINESS)
    local_ld = {k: v for k, v in BUSINESS.items() if k not in ("hasOfferCatalog",)}
    local_ld["areaServed"] = [{"@type": "City", "name": c + ", FL"} for c in ["Fort Lauderdale", "Wilton Manors", "Oakland Park", "Plantation", "Davie", "Weston", "Coral Springs", "Pompano Beach", "Hollywood", "Boca Raton"]] + \
                             [{"@type": "AdministrativeArea", "name": n} for n in ["Broward County, FL", "Palm Beach County, FL", "Miami-Dade County, FL"]]
    service_ld = {"@context": "https://schema.org", "@type": "Service", "@id": SITE + LOCAL + "#service",
                  "name": "Med Spa Marketing in Fort Lauderdale, FL", "serviceType": "Med spa marketing",
                  "provider": {"@id": BUSINESS_ID}, "url": SITE + LOCAL, "areaServed": local_ld["areaServed"]}
    page(LOCAL, "Med Spa Marketing in Fort Lauderdale, FL | BV Consulting",
         "Fort Lauderdale med spa marketing from a local team: AI agents, SMS booking automation, local SEO, websites, and integrations for South Florida med spas.",
         body, schemas=[local_ld, service_ld, breadcrumb_ld([("Home", "/"), ("Fort Lauderdale Med Spa Marketing", LOCAL)]), faq_ld(LOCAL_FAQS)],
         priority="0.9", images=["med-spa-laser-hair-removal"])


# ---------------------------------------------------------------- Legal
LEGAL_STYLE = '''<style>
.legal-note{background:var(--blue-soft);border-left:4px solid var(--blue);border-radius:0 12px 12px 0;padding:14px 18px;margin:0 0 24px;font-size:.92rem;color:var(--blue-deep)}
.prose h2{margin-top:1.7em}.updated{color:var(--muted);font-size:.9rem;margin-bottom:6px}
</style>'''
CONTACT_LIST = '''<ul>
        <li>Phone: <a href="tel:%s">%s</a></li>
        <li>Email: <a href="mailto:%s">%s</a></li>
        <li>Location: Fort Lauderdale, FL (serving clients nationwide)</li>
      </ul>''' % (TEL, PHONE, EMAIL, EMAIL)


def legal(path, title, h1, desc, content):
    body = '''
<section class="page-hero"><div class="container"><span class="eyebrow">Legal</span><h1>%s</h1><p class="updated">Last updated: %s</p></div></section>
<section class="section"><div class="container"><div class="prose">
%s
<p style="margin-top:30px"><a class="btn btn-secondary" href="/">&larr; Back to Home</a></p>
</div></div></section>''' % (h1, TODAY_HUMAN, content)
    page(path, title, desc, body, extra_head=LEGAL_STYLE, priority="0.2")


def privacy():
    legal("/privacy/", "Privacy Policy | BV Consulting", "Privacy Policy",
          "BV Consulting's privacy policy: what information we collect, how we use it, and your choices.", '''
<div class="legal-note">This Privacy Policy is provided for general informational purposes and is not legal advice. Please review it with a qualified attorney to make sure it fits your business and the laws that apply to you.</div>
<p>BV Consulting ("BV Consulting," "we," "us," or "our") respects your privacy. This policy explains what information we collect when you visit bvconsulting.live or use our services, how we use it, and your choices.</p>
<h2>1. Information we collect</h2>
<ul>
<li>Contact and practice details you submit, such as your name, practice name, email, phone number, state, city, website, and the services and software you're interested in.</li>
<li>Information you share during a project, including account access needed to build websites, AI agents, automations, or integrations.</li>
<li>Usage data collected automatically, such as IP address, browser, device, and pages visited, through cookies and analytics tools such as Google Analytics.</li>
</ul>
<p><strong>Please do not submit patient or health information through our website forms.</strong></p>
<h2>2. How we use information</h2>
<ul>
<li>Respond to quote requests and questions, and prepare proposals.</li>
<li>Plan, build, and support the services you hire us for.</li>
<li>Communicate with you about your project.</li>
<li>Understand and improve how our website is used.</li>
<li>Comply with legal obligations and protect our rights.</li>
</ul>
<h2>3. How we share information</h2>
<p>We do not sell personal information. We share information with service providers only as needed to operate our business, such as form delivery services (for example, FormSubmit), website hosting, analytics, scheduling, communications, and AI or automation platforms used to deliver client projects. We may disclose information when required by law.</p>
<h2>4. Client and patient data in projects</h2>
<p>When we build AI agents, automations, or integrations for healthcare and aesthetic practices, we may access data stored in client systems. We access only what's needed to deliver the agreed work, use it only for that purpose, and apply reasonable safeguards. Where protected health information (PHI) is involved, we work under an appropriate Business Associate Agreement and use services and configurations that support HIPAA requirements. Clients remain responsible for their own compliance programs.</p>
<h2>5. AI tools</h2>
<p>We use third-party AI services, such as Claude by Anthropic, to build and operate client solutions. We select tools and settings appropriate for business use and the sensitivity of the data involved.</p>
<h2>6. Cookies and analytics</h2>
<p>You can set your browser to refuse cookies and opt out of Google Analytics with Google's browser add-on.</p>
<h2>7. Retention and security</h2>
<p>We keep information only as long as needed for the purposes above and legal requirements, and we use reasonable measures to protect it. No method of transmission or storage is completely secure.</p>
<h2>8. Your choices</h2>
<p>You may ask what information we hold about you, request corrections or deletion (subject to legal requirements), and opt out of marketing messages at any time. Depending on where you live, you may have additional rights under state privacy laws.</p>
<h2>9. Children</h2>
<p>Our website and services are intended for businesses and adults. We do not knowingly collect information from children under 13.</p>
<h2>10. Changes</h2>
<p>We may update this policy and will revise the "Last updated" date when we do.</p>
<h2>11. Contact us</h2>
''' + CONTACT_LIST)


def terms():
    legal("/terms/", "Terms & Conditions | BV Consulting", "Terms &amp; Conditions",
          "The terms that govern use of BV Consulting's website and our AI, automation, SEO, website, and integration services.", '''
<div class="legal-note">These Terms are provided for general informational purposes and are not legal advice. Please have a qualified attorney review them, and use a signed agreement for client projects.</div>
<p>These Terms &amp; Conditions ("Terms") govern your use of bvconsulting.live and the services BV Consulting provides ("Services"). By using our website or Services, you agree to these Terms.</p>
<h2>1. Services</h2>
<p>BV Consulting provides digital services for businesses, including med spas and aesthetic practices: AI agent creation, AI and workflow automation, SMS and booking automation, search engine optimization, website design and development, API integrations, and related consulting and support. Scope, deliverables, timeline, and pricing for each project are defined in a written proposal or agreement.</p>
<h2>2. Proposals and payment</h2>
<p>Quotes are based on the information you provide. Changes in scope may change cost or timeline, and we'll discuss them before doing additional work. Payment terms, including deposits and recurring fees, appear in your proposal or invoice. Third-party subscriptions and usage fees (such as software, SMS, voice, or AI usage) are your responsibility unless agreed otherwise in writing.</p>
<h2>3. Your responsibilities</h2>
<ul>
<li>Provide accurate information, content, approvals, and timely feedback.</li>
<li>Provide access to accounts and confirm you're authorized to grant it.</li>
<li>Review and approve AI agent knowledge, guardrails, and automated messages before launch, including any clinical or treatment-related content, which should be reviewed by your licensed providers.</li>
<li>Maintain your own HIPAA, advertising, and privacy compliance programs, including patient consent for photos and communications.</li>
<li>Comply with laws that apply to texting, calling, and email, including consent and opt-out requirements.</li>
</ul>
<h2>4. AI and third-party platforms</h2>
<p>Our solutions may rely on third-party platforms and AI models, such as Claude by Anthropic, which can change, experience outages, or update their terms and APIs. AI-generated output can be inaccurate. AI agents we build are not designed to provide medical advice, and important or clinical communications should involve human review. We are not responsible for the performance, pricing, or terms of third-party services.</p>
<h2>5. No guaranteed results</h2>
<p>We follow recognized best practices, but we do not guarantee specific rankings, traffic, leads, bookings, or revenue.</p>
<h2>6. Ownership</h2>
<p>Unless your agreement says otherwise, once paid in full you own the final website content and design created specifically for you. Pre-existing tools, code, templates, prompts, and know-how remain ours or our licensors'. We may reference completed work in our portfolio unless you ask us not to.</p>
<h2>7. Disclaimers and limitation of liability</h2>
<p>Services and our website are provided "as is" except as expressly stated in a signed agreement. To the fullest extent permitted by law, BV Consulting is not liable for indirect, incidental, or consequential damages, and our total liability for any claim will not exceed the amount you paid for the specific Service giving rise to the claim.</p>
<h2>8. Website content</h2>
<p>Content on this website belongs to BV Consulting or its licensors. Product names mentioned are trademarks of their respective owners, and their mention does not imply affiliation or endorsement.</p>
<h2>9. Governing law</h2>
<p>These Terms are governed by the laws of the State of Florida. Disputes will be handled in the courts located in Broward County, Florida, unless otherwise required by law.</p>
<h2>10. Contact us</h2>
''' + CONTACT_LIST)


def not_found():
    links = "".join('<li><a href="%s">%s</a></li>' % (s["url"], s["name"]) for s in SERVICES)
    body = '''
<section class="page-hero"><div class="container center">
  <span class="eyebrow">404</span><h1>We couldn't find that page</h1>
  <p class="lede" style="margin:0 auto 20px">The page may have moved. Try one of these instead.</p>
  <div class="hero-ctas" style="justify-content:center"><a class="btn btn-primary" href="/quote/">Get a Free Quote</a><a class="btn btn-secondary" href="/">Go to Home</a></div>
  <ul class="area-list" style="margin-top:22px">%s<li><a href="/blog/">Blog</a></li></ul>
</div></section>''' % links
    page("/404", "Page Not Found | BV Consulting", "The page you were looking for could not be found.", body, noindex=True, sitemap=False)
