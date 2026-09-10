from common import *
from tools import revenue_calc, TOOLS_SCRIPT
from posts_meta import POSTS

HOME_FAQS = [
    ("What does BV Consulting do for med spas?",
     "We build a complete growth system for med spas and aesthetic practices: AI agents that answer and book around the clock, automated SMS and online booking, SEO that helps you rank for the treatments you offer, a high-converting website, and API integrations that connect your booking software, CRM, and payments."),
    ("What is an AI agent for a med spa?",
     "An AI agent is a virtual assistant trained on your treatment menu, pricing guidelines, policies, and brand voice. It can respond to calls, texts, website chats, and social DMs, answer common questions, collect lead details, and book consultations. It hands off to your team for anything clinical or sensitive, and it never gives medical advice. <a href=\"/med-spa-ai-agents/\">Learn about AI agents</a>."),
    ("Which AI tools do you use?",
     "We build with several leading AI tools, including Claude by Anthropic, ChatGPT by OpenAI, and Google Gemini, plus automation platforms like Zapier, Make, and n8n. We pick the right tool for each workflow and your privacy requirements."),
    ("Will it work with my booking software?",
     "Most likely. We regularly plan integrations around popular med spa platforms such as Boulevard, Zenoti, Mangomint, Vagaro, Mindbody, AestheticsPro, Aesthetic Record, and PatientNow, along with CRMs like GoHighLevel and HubSpot. What's possible depends on each platform's API access, which we confirm before any work starts."),
    ("How do you handle HIPAA and patient privacy?",
     "We design every system with patient privacy in mind: we limit protected health information in automations and marketing messages, use vendors and settings that support a Business Associate Agreement (BAA) where PHI is involved, and restrict access to only what each tool needs. Your compliance team or attorney should review your specific setup."),
    ("Do you work with med spas in my state?",
     "Yes. We work with med spas and aesthetic practices nationwide. Websites, SEO, AI agents, automations, and integrations are all delivered remotely, with video calls for strategy and training."),
    ("How much does it cost?",
     "Every practice is different, so we quote after a free consultation. Pricing depends on which services you need, how many locations you have, and your current software. <a href=\"/quote/\">Request a free quote</a> and we'll send a clear, written proposal."),
]

PAINS = [
    ("phone", "Missed calls & after-hours inquiries", "Prospective clients call, text, and DM when your front desk is busy or closed, then book somewhere else."),
    ("calendar", "No-shows & last-minute cancellations", "Empty chairs cost your injectors and aestheticians time you can't get back."),
    ("repeat", "Clients who never rebook", "Treatments like neurotoxins and facials need maintenance, but reminders fall through the cracks."),
    ("search", "Invisible on Google", "People search for lip filler, laser hair removal, or a med spa near me, and find competitors first."),
    ("web", "A website that doesn't convert", "Slow pages, unclear pricing guidance, and buried booking buttons send visitors away."),
    ("edit", "Front desk overload", "Double data entry between booking, CRM, and payments steals time from client care."),
]

TRUST = [
    ("lock", "HIPAA-conscious builds", "PHI minimized, BAA-supported vendors where needed."),
    ("shield", "Provider-safe AI", "No medical advice. Clinical questions go to your team."),
    ("chat", "Your brand voice", "Trained on your menu, policies, and tone."),
    ("flag", "Texting done right", "Consent, opt-outs, and registered business messaging."),
]


def build():
    cards = []
    for s in SERVICES:
        cards.append('''<a class="svc-card" href="{url}">
        {photo}
        <div class="svc-body">
          <span class="svc-ic">{icon}</span>
          <h3>{name}</h3>
          <p>{short}</p>
          <span class="more">Explore {name} &rarr;</span>
        </div>
      </a>'''.format(url=s["url"], photo=picture(s["img"], s["long"], sizes="(min-width: 960px) 33vw, (min-width: 640px) 50vw, 100vw", fallback_icon=s["icon"]),
                     icon=ic(s["icon"], 20, 1.9), name=s["name"], short=s["short"]))
    pains = "\n".join('<div class="pain"><div class="ic">%s</div><div><b>%s</b><span>%s</span></div></div>' % (ic(i, 20), h, t) for i, h, t in PAINS)
    trust = "\n".join('<div class="trust"><div class="ic">%s</div><div><b>%s</b><span>%s</span></div></div>' % (ic(i, 20), h, t) for i, h, t in TRUST)
    posts = "\n".join(post_card(p) for p in POSTS[:3])

    body = '''
<section class="hero bg-warm">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="eyebrow">AI, SEO &amp; automation for med spas</span>
        <h1>Fill Your Med Spa's Calendar With <span>AI Agents, SEO &amp; Automated Booking</span></h1>
        <p class="hero-sub">BV Consulting builds med spas a growth system that works around the clock: AI agents that answer every inquiry and book consultations, automated SMS reminders that cut no-shows, SEO that gets you found for the treatments you offer, and integrations that connect it all.</p>
        <div class="hero-ctas">
          <a class="btn btn-primary" href="{quote}">Get a Free Quote</a>
          <a href="/services/" class="btn btn-secondary">See How It Works</a>
        </div>
        <div class="hero-meta">
          <span><span class="dot"></span>Built for aesthetic practices</span>
          <span><span class="dot"></span>Works with your booking software</span>
          <span><span class="dot"></span>Free consultation</span>
        </div>
      </div>
      <div class="hero-photo-wrap">
        {hero_photo}
        <div class="float-card fc-2"><span class="fc-ic">{i_bot}</span><div><b>AI agent replied</b>Answered a lip filler question and offered consult times</div></div>
        <div class="float-card green fc-1"><span class="fc-ic">{i_cal}</span><div><b>Consultation booked</b>Synced to your calendar &amp; CRM</div></div>
        <div class="float-card fc-3"><span class="fc-ic">{i_sms}</span><div><b>Reminder sent</b>24 hours before the appointment</div></div>
      </div>
    </div>
    {carousel}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:30px">
      <span class="eyebrow">The problem</span>
      <h2>Where Med Spas Lose Bookings (and Revenue)</h2>
      <p style="max-width:700px;margin:0 auto">Great providers and beautiful treatment rooms aren't enough if inquiries go unanswered and clients forget to come back. These are the leaks we fix first.</p>
    </div>
    <div class="pains">{pains}</div>
  </div>
</section>

{demo}

{calc}

<section class="section" id="services">
  <div class="container">
    <div class="center" style="margin-bottom:30px">
      <span class="eyebrow">What we build</span>
      <h2>Six Services. One Med Spa Growth System.</h2>
      <p style="max-width:720px;margin:0 auto">Start with the piece you need most, or let us build the whole system so your marketing, front desk, and software finally work together.</p>
    </div>
    <div class="svc-grid">
      {cards}
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="split-photo">
      <div>
        <span class="eyebrow">Made for aesthetics</span>
        <h2>Technology That Respects Your Clients and Your Clinical Standards</h2>
        <p>Med spas aren't like other small businesses. Your clients share personal details, your providers are licensed professionals, and your reputation depends on trust. We build every AI agent, text message, and integration around that.</p>
        <ul class="check-list">
          <li>AI agents answer booking and pricing questions, then route anything clinical to your licensed team</li>
          <li>Messages written in your voice, from warm consult reminders to post-treatment check-ins</li>
          <li>Patient data kept to the minimum each tool needs, with BAA-supported services where required</li>
          <li>Clear reporting on leads, bookings, and rebooking rates across every location</li>
        </ul>
        <p style="margin-top:16px"><a class="btn btn-primary" href="{quote}">Get a Free Quote</a></p>
      </div>
      {laser_photo}
    </div>
    <div class="trust-row" style="margin-top:34px">{trust}</div>
  </div>
</section>

{ai_tools}

<section class="section bg-soft">
  <div class="container">
    <div class="split-photo flip">
      <div>
        <span class="eyebrow">Booking, deposits &amp; payments</span>
        <h2>From First Text to Checkout, Everything Stays in Sync</h2>
        <p>A new lead books online, pays a deposit, gets a reminder, checks out at the front desk, and receives a rebooking text a few weeks later. With the right integrations, your booking software, CRM, payment processor, and ad platforms all see the same information automatically.</p>
        <ul class="check-list">
          <li><a href="{u_sms}">Automated SMS &amp; booking</a>: confirmations, reminders, waitlists, and rebooking</li>
          <li><a href="{u_api}">API integrations</a>: Boulevard, Zenoti, Vagaro, Stripe, Square, GoHighLevel, and more</li>
          <li><a href="{u_auto}">AI automation</a>: review requests, reactivation, and membership renewals</li>
        </ul>
        {software}
      </div>
      {pos_photo}
    </div>
  </div>
</section>

<section class="section bg-dark">
  <div class="container">
    <div class="center" style="margin-bottom:40px">
      <span class="eyebrow">How it works</span>
      <h2>Your Growth System in Four Steps</h2>
      <p style="max-width:640px;margin:0 auto">A clear path from free consultation to a system that books clients while you focus on treatments.</p>
    </div>
    <div class="process">
      <div class="step"><div class="n">1</div><h3>Free consultation</h3><p>We review your website, Google presence, booking flow, and software to find where bookings slip away.</p></div>
      <div class="step"><div class="n">2</div><h3>Growth plan &amp; quote</h3><p>You get a written plan and quote showing what we'll build, which tools we'll use, and why.</p></div>
      <div class="step"><div class="n">3</div><h3>Build &amp; integrate</h3><p>We build your AI agent, automations, website, and SEO foundation, and connect your software.</p></div>
      <div class="step"><div class="n">4</div><h3>Launch &amp; optimize</h3><p>We monitor conversations, bookings, and rankings, and keep refining the system every month.</p></div>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:30px">
      <span class="eyebrow">Med spa growth guides</span>
      <h2>Learn What's Working for Med Spas</h2>
    </div>
    <div class="blog-grid">{posts}</div>
    <div class="center" style="margin-top:26px"><a class="btn btn-secondary" href="/blog/">Read all articles</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">FAQ</span><h2>Questions Med Spa Owners Ask</h2></div>
    <div style="max-width:820px;margin:0 auto">{faqs}</div>
  </div>
</section>

{cta}
'''.format(quote=QUOTE,
           hero_photo=picture("med-spa-lip-filler-treatment", "Injector performing a dermal filler treatment on a client at a med spa", sizes="(min-width: 960px) 45vw, 100vw", eager=True, fallback_icon="syringe"),
           i_bot=ic("bot", 18), i_cal=ic("calendar", 18), i_sms=ic("sms", 18), carousel=logo_carousel(), software=software_strip("Plus the med spa software you already use").replace('class="soft-strip"', 'class="soft-strip left"'),
           pains=pains, cards="\n      ".join(cards),
           laser_photo=picture("med-spa-laser-hair-removal", "Registered nurse performing laser hair removal at a med spa", fallback_icon="zap"),
           trust=trust, ai_tools=ai_tools_section("", carousel=False), demo=sms_demo(), calc=revenue_calc("bg-warm"),
           u_sms=SVC["sms"]["url"], u_api=SVC["api"]["url"], u_auto=SVC["automation"]["url"],
           pos_photo=picture("med-spa-payment-terminal-booking", "Payment terminal at a med spa front desk connected to booking software", fallback_icon="dollar"),
           posts=posts, faqs=faq_html(HOME_FAQS),
           cta=cta_strip("Ready to fill your med spa's calendar?", "Get a free quote and a clear, written growth plan for your practice."))

    page("/", "Med Spa Marketing, AI Agents & Automation | BV Consulting",
         "BV Consulting helps med spas book more clients with AI agents, automated SMS and booking, SEO, high-converting websites, and API integrations. Free quote.",
         body, schemas=[BUSINESS, WEBSITE, faq_ld(HOME_FAQS)], active="/", priority="1.0",
         images=["med-spa-lip-filler-treatment"], scripts_after=DEMO_SCRIPT + TOOLS_SCRIPT)
