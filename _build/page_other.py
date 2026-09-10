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
.form-success{display:none;background:var(--blue-soft);border:1px solid #d3dbc6;color:var(--blue-deep);border-radius:12px;padding:16px;font-weight:600;margin-top:10px}
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
         "Contact BV Consulting about AI agents, SEO, websites, SMS booking automation, and integrations for your med spa. Call 954-825-1009 or email us.",
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
QUOTE_STYLE = '''<style>
.wizard{max-width:none}
.wiz-card{background:#fff;border:1px solid var(--line);border-radius:20px;box-shadow:0 20px 50px rgba(10,13,18,.12);padding:24px 20px 26px;overflow:hidden}
.wiz-title{font-family:'Poppins',sans-serif;font-weight:700;font-size:1.05rem;color:var(--black);margin:0 0 12px}
.progress-head{margin-bottom:18px}
.progress-meta{display:flex;justify-content:space-between;font-size:.8rem;color:var(--muted);font-weight:600;margin-bottom:8px}
.progress-track{height:8px;border-radius:999px;background:var(--blue-soft);overflow:hidden}
.progress-fill{height:100%;width:0%;background:linear-gradient(90deg,var(--blue),var(--blue-deep));border-radius:999px;transition:width .4s var(--ease)}
.step-panel{display:none;animation:fadeIn .35s var(--ease)}
.step-panel.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.step-q{font-family:'Poppins',sans-serif;font-weight:700;color:var(--black);font-size:1.25rem;margin:0 0 4px;line-height:1.25}
.step-help{color:var(--muted);font-size:.9rem;margin-bottom:16px}
.opt-grid{display:grid;grid-template-columns:1fr;gap:9px}
@media(min-width:560px){.opt-grid{grid-template-columns:1fr 1fr}}
.opt{display:flex;align-items:center;gap:11px;text-align:left;background:#fff;border:2px solid var(--line);border-radius:12px;padding:12px 14px;cursor:pointer;font-size:.95rem;font-weight:600;color:var(--ink);transition:border-color .15s,background .15s;font-family:inherit;width:100%;min-height:var(--tap)}
.opt:hover{border-color:var(--blue);background:var(--blue-50)}
.opt.selected{border-color:var(--blue);background:var(--blue-soft)}
.opt .opt-ic{flex-shrink:0;width:34px;height:34px;border-radius:9px;background:var(--blue-soft);display:flex;align-items:center;justify-content:center;color:var(--blue-dark)}
.opt.selected .opt-ic{background:var(--blue);color:#fff}
.wiz-nav{display:flex;justify-content:space-between;align-items:center;margin-top:18px;gap:12px}
.btn-back{background:transparent;border:0;color:var(--muted);font-weight:600;font-family:inherit;font-size:.95rem;cursor:pointer;padding:8px 4px}
.btn-back:hover{color:var(--ink)}
.btn-back.is-hidden{visibility:hidden}
.summary-box{background:var(--bg-soft);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin-bottom:16px;font-size:.86rem}
.summary-box .srow{display:flex;justify-content:space-between;gap:12px;padding:3px 0;color:var(--ink-2)}
.summary-box .srow b{color:var(--black);font-weight:600;flex-shrink:0}
.summary-box .srow span:last-child{text-align:right;color:var(--blue-dark);font-weight:600}
.funnel-grid{grid-template-areas:"copy" "form" "photo"}
.funnel-copy{grid-area:copy}.funnel-form{grid-area:form}.funnel-photo{grid-area:photo;margin-top:0}
@media(min-width:960px){.funnel-grid{grid-template-areas:"copy form" "photo form";grid-template-rows:auto 1fr}}
.load-overlay{position:fixed;inset:0;background:rgba(255,255,255,.96);display:none;flex-direction:column;align-items:center;justify-content:center;z-index:300;padding:24px;text-align:center}
.load-overlay.show{display:flex}
.spinner{width:46px;height:46px;border:4px solid var(--blue-soft);border-top-color:var(--blue);border-radius:50%;animation:spin 1s linear infinite;margin-bottom:18px}
@keyframes spin{to{transform:rotate(360deg)}}
</style>'''


def quote():
    def opts(items, multi=False):
        out = []
        for i, v in items:
            chk = '<span class="opt-check">%s</span>' % ic("check", 14, 3) if multi else ""
            out.append('<button type="button" class="opt%s" data-value="%s"%s><span class="opt-ic">%s</span>%s%s</button>' % (
                " multi" if multi else "", v, ' aria-pressed="false"' if multi else "", ic(i, 18, 1.7), v, chk))
        return "\n".join(out)

    steps = [
        ("services", "What do you want help with?", "Choose all that apply.", True,
         [("bot", "AI agent / AI receptionist"), ("calendar", "Automated SMS &amp; booking"), ("sparkle", "AI automation workflows"),
          ("search", "Med spa SEO"), ("web", "Website development"), ("nodes", "API &amp; software integrations"), ("layers", "The complete growth system")]),
        ("practice", "What type of practice do you run?", "So we can tailor ideas to your services.", False,
         [("sparkle", "Med spa"), ("syringe", "Injector or aesthetics studio"), ("heart", "Dermatology or plastic surgery"),
          ("zap", "Laser &amp; skin clinic"), ("refresh", "Wellness, IV, or weight loss clinic"), ("dots", "Something else")]),
        ("locations", "How many locations do you have?", "Including any opening soon.", False,
         [("pin", "1 location"), ("layers", "2 to 3 locations"), ("flag", "4 to 10 locations"), ("chart", "More than 10")]),
        ("software", "Which booking or EMR software do you use?", "We'll check integration options before your consultation.", False,
         [("calendar", "Boulevard"), ("calendar", "Zenoti"), ("calendar", "Mangomint"), ("calendar", "Vagaro"), ("calendar", "Mindbody"),
          ("calendar", "AestheticsPro"), ("calendar", "Aesthetic Record"), ("calendar", "PatientNow"), ("dots", "Other software"), ("question", "Not sure / none")]),
        ("challenge", "What's your biggest challenge right now?", "We'll focus your growth plan here.", False,
         [("phone", "Missed calls &amp; slow follow-up"), ("calendar", "No-shows &amp; cancellations"), ("search", "Not showing up on Google"),
          ("web", "Website doesn't convert"), ("edit", "Too much front desk admin"), ("repeat", "Low rebooking &amp; retention")]),
    ]
    panels = []
    for n, (key, q, help_, multi, items) in enumerate(steps):
        cont = '<button type="button" class="btn btn-primary wiz-continue" data-continue disabled>Continue</button>' if multi else ""
        panels.append('''<div class="step-panel%s" data-step="%d" data-key="%s"%s>
              <h2 class="step-q">%s</h2><p class="step-help">%s</p>
              <div class="opt-grid" data-choices>%s</div>%s
            </div>''' % (" active" if n == 0 else "", n + 1, key, ' data-multi="1"' if multi else "", q, help_, opts(items, multi), cont))
    states = "".join('<option%s>%s</option>' % (' value=""' if s == "" else "", s) for s in [""] + US_STATES)

    faqs = [
        ("Is the quote really free?", "Yes. The consultation, growth plan, and quote are free with no obligation."),
        ("How fast will I hear back?", "We typically respond within 24 hours on business days, by phone or email, whichever you prefer."),
        ("Do you work with med spas outside Florida?", "Yes. BV Consulting is based in Fort Lauderdale and works with med spas nationwide."),
        ("Should I include patient information?", "No. Please don't share any patient or health information in this form. We only need details about your practice."),
    ]
    body = '''
<section class="funnel-hero">
  <div class="container">
    <div class="funnel-grid">
      <div class="funnel-copy">
        <span class="eyebrow">Free quote for med spas</span>
        <h1>Get Your Free Med Spa Growth Plan &amp; Quote</h1>
        <p class="lede">Answer 6 quick questions (about 60 seconds). We'll review your practice and send a clear plan and quote for AI agents, automated SMS and booking, SEO, your website, and integrations.</p>
        <ul class="check-list" style="margin-top:14px">
          <li>A review of your website, Google presence, and booking flow</li>
          <li>Specific AI agent and automation opportunities for your practice</li>
          <li>A clear, written quote with no obligation</li>
        </ul>
        <ul class="mini-trust">
          <li>{i_check} Free &amp; no obligation</li><li>{i_check} Reply within 24 hours</li><li>{i_check} Serving med spas nationwide</li>
        </ul>
      </div>
      <div class="funnel-form" id="quote-form-wrap">
        <div class="wiz-card">
          <div class="progress-head">
            <div class="progress-meta"><span id="step-label">Step 1 of 6</span><span id="step-pct">17%</span></div>
            <div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div>
          </div>
          <form id="quote-form" novalidate>
            <input type="text" name="_honey" id="q-honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true" />
            {panels}
            <div class="step-panel" data-step="6" data-key="contact">
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
              <p style="font-size:.78rem;color:var(--muted);margin-top:10px;text-align:center">By submitting, you agree to be contacted by BV Consulting about your request. See our <a href="/privacy/">Privacy Policy</a>.</p>
              <div class="form-error" id="quote-error" role="alert"></div>
            </div>
            <div class="wiz-nav">
              <button type="button" class="btn-back is-hidden" id="btn-back">&larr; Back</button>
              <span style="font-size:.8rem;color:var(--muted)">Free &bull; No obligation</span>
            </div>
          </form>
        </div>
      </div>
      <div class="funnel-photo">{photo}</div>
    </div>
    <div style="margin-top:36px">{carousel}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:28px"><span class="eyebrow">What happens next</span><h2>From Form to Growth Plan in Three Steps</h2></div>
    <div class="next-steps">
      <div class="next-step"><b>We review your practice</b><span>We look at your website, Google profile, reviews, and booking flow before we talk.</span></div>
      <div class="next-step"><b>Free strategy call</b><span>A focused call about your goals, software, and where bookings are slipping away.</span></div>
      <div class="next-step"><b>Your plan &amp; quote</b><span>A written growth plan with recommended services, tools, timeline, and pricing.</span></div>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="split-photo flip">
      <div>
        <span class="eyebrow">What we can build for you</span>
        <h2>One Partner for Your Entire Growth System</h2>
        <ul class="check-list">{svc_list}</ul>
        <p style="margin-top:10px">We build with leading AI tools, including Claude by Anthropic, and integrate with the booking software you already use.</p>
        <p style="margin-top:16px"><a class="btn btn-primary" href="#quote-form-wrap">Start My Free Quote</a></p>
      </div>
      {photo2}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:26px"><span class="eyebrow">FAQ</span><h2>Quick Questions</h2></div>
    <div style="max-width:780px;margin:0 auto">{faqs}</div>
    <div class="center" style="margin-top:26px"><a class="btn btn-primary" href="#quote-form-wrap">Get My Free Quote</a></div>
  </div>
</section>

<div class="load-overlay" id="load-overlay" role="status" aria-live="polite"><div class="spinner"></div><h3>Sending your request&hellip;</h3><p style="color:var(--muted)">This only takes a moment.</p></div>
'''.format(i_check=ic("check", 16, 3), panels="\n            ".join(panels), states=states,
           photo=picture("med-spa-consultation-mirror", "Med spa client reviewing her results in a mirror", sizes="(min-width: 960px) 45vw, 100vw", fallback_icon="sparkle"),
           svc_list="".join('<li><a href="%s"><strong>%s</strong></a>: %s</li>' % (s["url"], s["name"], s["short"]) for s in SERVICES),
           photo2=picture("growth-strategy-session", "Growth strategy session with a presenter and a team on laptops", fallback_icon="users"),
           faqs=faq_html(faqs), carousel=logo_carousel("Built with trusted tools"))

    script = r'''<script>
document.addEventListener("DOMContentLoaded",function(){
  var TOTAL=6, current=1, answers={services:[]};
  var panels=document.querySelectorAll(".step-panel");
  var fill=document.getElementById("progress-fill"), label=document.getElementById("step-label"), pct=document.getElementById("step-pct");
  var back=document.getElementById("btn-back"), wrap=document.getElementById("quote-form-wrap");
  var LABELS={services:"Services",practice:"Practice",locations:"Locations",software:"Software",challenge:"Challenge"};
  var started=false;
  function show(step,scroll){
    current=step;
    panels.forEach(function(p){p.classList.toggle("active", +p.dataset.step===step);});
    var percent=Math.round(step/TOTAL*100);
    fill.style.width=percent+"%"; label.textContent="Step "+step+" of "+TOTAL; pct.textContent=percent+"%";
    back.classList.toggle("is-hidden", step===1);
    if(step===TOTAL) buildSummary();
    if(scroll && wrap.getBoundingClientRect().top<0){ window.scrollTo({top:wrap.getBoundingClientRect().top+window.scrollY-16,behavior:"smooth"}); }
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
          setTimeout(function(){ if(current<TOTAL) show(current+1,true); },200);
        }
      });
    });
    if(cont){ cont.addEventListener("click",function(){ show(current+1,true); }); }
  });
  back.addEventListener("click",function(){ if(current>1) show(current-1,true); });
  function escHtml(s){return String(s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}
  function val(k){return Array.isArray(answers[k])?answers[k].join(", "):(answers[k]||"");}
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
    var data={form:"Med spa quote funnel (/quote)",services:val("services"),practice_type:val("practice"),locations:val("locations"),
      software:val("software"),biggest_challenge:val("challenge"),name:g("q-name"),practice:g("q-business"),email:g("q-email"),
      phone:g("q-phone"),state:g("q-state"),city:g("q-city"),website:g("q-site"),details:g("q-details")};
    var err=document.getElementById("quote-error"), ov=document.getElementById("load-overlay");
    err.classList.remove("show"); ov.classList.add("show");
    window.BV.submitLead(data,"New med spa quote request: "+data.practice+" ("+data.state+")").then(function(){
      try{ sessionStorage.setItem("bv_lead_name", data.name.split(" ")[0]); }catch(x){}
      window.location.href="/thank-you/";
    }).catch(function(){
      ov.classList.remove("show");
      err.innerHTML='We couldn’t send your request just now. Please <a href="'+window.BV.mailtoFallback(data,"Med spa quote request")+'">email your details to us</a> or call <a href="tel:+19548251009">954-825-1009</a>.';
      err.classList.add("show");
    });
  });
  show(1,false);
});
</script>'''
    page(QUOTE, "Free Med Spa Marketing Quote | BV Consulting",
         "Get a free growth plan and quote for your med spa: AI agents, automated SMS and booking, SEO, website development, and API integrations. Takes 60 seconds.",
         body, schemas=[breadcrumb_ld([("Home", "/"), ("Free Quote", QUOTE)]), faq_ld(faqs)],
         extra_head=QUOTE_STYLE, scripts_after=script, funnel=True, priority="0.9", images=["med-spa-consultation-mirror"])


def thank_you():
    body = '''
<section class="funnel-hero" style="padding-bottom:60px">
  <div class="container center" style="max-width:760px">
    <div style="width:76px;height:76px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--blue-deep));display:flex;align-items:center;justify-content:center;margin:10px auto 18px;color:#fff">{check}</div>
    <span class="eyebrow">Request received</span>
    <h1>Thank you<span id="ty-name"></span>! Your growth plan is on the way.</h1>
    <p class="lede" style="margin:0 auto 22px">We'll review your practice and reach out within 24 hours on business days to schedule your free strategy call. Keep an eye on your phone and inbox.</p>
    <div class="hero-ctas" style="justify-content:center"><a class="btn btn-primary" href="/blog/">Read Med Spa Growth Guides</a><a class="btn btn-secondary" href="tel:{tel}">Call {phone}</a></div>
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
'''.format(check=ic("check", 40, 2.6), tel=TEL, phone=PHONE)
    script = r'''<script>
document.addEventListener("DOMContentLoaded",function(){
  try{var n=sessionStorage.getItem("bv_lead_name"); if(n){document.getElementById("ty-name").textContent=", "+n;}}catch(e){}
  if(window.BV) window.BV.track("quote_thank_you_view");
  if(window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var c=document.getElementById("confetti-canvas"),x=c.getContext("2d");c.width=innerWidth;c.height=innerHeight;
  var cols=["#4F5E3D","#2C3622","#c98d7a","#efe3d6","#a9b88e"],P=[];
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
        s["url"], ic(s["icon"], 20, 1.9), s["name"], s["short"]) for s in SERVICES)
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
          <a class="btn btn-secondary" href="tel:{tel}">Call {phone}</a>
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
'''.format(crumbs=crumbs([("Home", "/"), ("Fort Lauderdale Med Spa Marketing", LOCAL)]), quote=QUOTE, tel=TEL, phone=PHONE, email=EMAIL,
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
