"""Standalone tool pages."""
from common import *
from tools import revenue_calc, TOOLS_SCRIPT, CALC_URL


def calculator_page():
    formulas = [
        ("Unanswered lead revenue", "Missed inquiries per week &times; 4.33 weeks &times; share that would book &times; average visit value",
         "Every call, text, or DM that goes unanswered is a potential client who may book somewhere else. 4.33 is the average number of weeks in a month."),
        ("No-show revenue", "Appointments per month &times; no-show &amp; late cancel rate &times; average visit value",
         "Once an appointment time passes, that chair can't be resold, so each no-show or late cancel is revenue the day can't get back."),
        ("Recovery scenario", "(Unanswered lead revenue &divide; 3) + (No-show revenue &times; 25%)",
         "A conservative what-if, not a guarantee: winning back one in three missed leads with instant replies and cutting no-shows by a quarter with reminders."),
        ("Yearly estimate", "Monthly total &times; 12",
         "Seasonal swings change the real number, so treat the yearly figure as a rough picture of what's at stake."),
    ]
    formula_html = "".join('<div class="formula-card"><h3>%s</h3><code>%s</code><p>%s</p></div>' % f for f in formulas)
    guide = [
        ("Calls, texts &amp; DMs that go unanswered", "Check your phone system's missed call log, after-hours voicemails, and unread Instagram and Facebook messages for a typical week."),
        ("Share that would have booked", "Think about how often your front desk books a new inquiry when they do reach the person. If you're not sure, start with the default and adjust."),
        ("Average visit value", "Use the average ticket or revenue per appointment report in your booking software."),
        ("Appointments per month", "Count booked appointments across all providers in a typical month."),
        ("No-show &amp; late cancel rate", "Most booking platforms report no-shows and late cancellations. Divide them by total appointments for the month."),
    ]
    guide_html = "".join("<div><b>%s</b><span>%s</span></div>" % g for g in guide)
    recover = [SVC["sms"], SVC["agents"], SVC["automation"]]
    recover_why = {"sms": "Confirmations, reminders, deposits, and waitlist texts that cut no-shows and refill openings.",
                   "agents": "A 24/7 AI receptionist that answers calls, texts, and DMs in seconds and books the consultation.",
                   "automation": "Instant lead follow-up, missed call text back, and rebooking campaigns that run on their own."}
    recover_html = "\n".join('<a class="svc-card" href="%s"><div class="svc-body"><span class="svc-ic" style="margin-top:0">%s</span><h3>%s</h3><p>%s</p><span class="more">Learn more &rarr;</span></div></a>'
                             % (s["url"], ic(s["icon"], 20, 1.9), s["name"].replace("&", "&amp;"), recover_why[s["key"]]) for s in recover)
    faqs = [
        ("Is this calculator free?", "Yes. It runs entirely in your browser, and nothing you enter is saved or sent anywhere."),
        ("How accurate is the estimate?", "It's an illustrative estimate based on the numbers you enter. Real results depend on your services, pricing, policies, and how quickly your team follows up with new inquiries."),
        ("What counts as a late cancellation?", "Most practices count any cancellation inside their cancellation policy window, often 24 to 48 hours before the appointment, because that time is hard to refill."),
        ("How can a med spa lower its no-show rate?", "Confirmation texts with a simple reply to confirm or reschedule, reminders a day or two ahead, deposits for longer appointments, and waitlist texts that refill openings all help. See our <a href=\"/med-spa-sms-booking-automation/\">SMS and booking automation</a> service."),
    ]
    crumb_items = [("Home", "/"), ("Revenue Calculator", CALC_URL)]
    body = '''
<section class="section bg-warm calc-hero">
  <div class="container">
    {crumbs}
    <span class="eyebrow">Free tool for med spa owners</span>
    <h1>Med Spa Missed Revenue Calculator</h1>
    <p class="hero-sub">See what missed calls, unanswered texts, and no-shows could be costing your practice every month. Adjust five sliders. No email required.</p>
  </div>
</section>

{calc}

<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:28px"><span class="eyebrow">The math</span><h2>How the Calculator Works</h2>
      <p style="max-width:680px;margin:0 auto">No hidden assumptions. Here's exactly how each number is calculated.</p></div>
    <div class="formula">{formulas}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:28px"><span class="eyebrow">Get accurate inputs</span><h2>Where to Find Your Numbers</h2></div>
    <div class="input-guide">{guide}</div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:28px"><span class="eyebrow">Recover it</span><h2>How Med Spas Win That Revenue Back</h2></div>
    <div class="svc-grid">{recover}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:28px"><span class="eyebrow">FAQ</span><h2>Revenue Calculator FAQ</h2></div>
    <div style="max-width:820px;margin:0 auto">{faqs}</div>
  </div>
</section>

{cta}
'''.format(crumbs=crumbs(crumb_items), calc=revenue_calc("calc-page-tool", show_head=False, full_link=False),
           formulas=formula_html, guide=guide_html, recover=recover_html, faqs=faq_html(faqs),
           cta=cta_strip("Ready to stop losing bookings?", "Get a free plan to recover missed calls and no-shows. It takes about a minute."))
    app_ld = {"@context": "https://schema.org", "@type": "WebApplication", "@id": SITE + CALC_URL + "#app",
              "name": "Med Spa Missed Revenue Calculator", "url": SITE + CALC_URL,
              "description": "Estimate the monthly revenue a med spa loses to unanswered calls, texts, DMs, and no-shows.",
              "applicationCategory": "BusinessApplication", "operatingSystem": "Any", "browserRequirements": "Requires JavaScript",
              "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
              "publisher": {"@id": BUSINESS_ID}}
    page(CALC_URL, "Med Spa No-Show & Missed Call Calculator | BV Consulting",
         "Free calculator for med spa owners: see what missed calls, unanswered texts, and no-shows cost your practice each month and how much you could recover.",
         body, schemas=[app_ld, breadcrumb_ld(crumb_items), faq_ld([(q, strip(a)) for q, a in faqs])],
         scripts_after=TOOLS_SCRIPT, priority="0.8")
