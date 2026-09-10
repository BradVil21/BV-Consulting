"""Fort Lauderdale service pages (service x city). Each page has unique local copy, a tool, FAQs, and schema."""
from common import *
from tools import revenue_calc, automation_timeline, seo_scorecard, TOOLS_SCRIPT

CENSUS = '<a href="https://www.census.gov/quickfacts/fact/table/browardcountyflorida/PST045225" rel="noopener" target="_blank">U.S. Census Bureau</a>'

LOCAL_PAGES = [
    {"key": "seo", "slug": "/med-spa-seo-fort-lauderdale/", "short": "SEO",
     "title": "Med Spa SEO in Fort Lauderdale, FL | BV Consulting",
     "desc": "Local SEO for Fort Lauderdale med spas. Rank in Google Maps for Botox, filler, and laser searches across Las Olas, Wilton Manors, and all of Broward.",
     "h1": "Med Spa SEO in Fort Lauderdale, FL",
     "lede": "Show up when people in Fort Lauderdale search for Botox, lip filler, laser hair removal, and facials near them. We handle your Google Business Profile, treatment pages, reviews, and local listings, built around how South Florida clients actually search.",
     "img": "med-spa-laser-hair-removal", "alt": "Laser hair removal treatment at a Fort Lauderdale area med spa",
     "local_h": "What Ranking a Fort Lauderdale Med Spa Really Takes",
     "local": [
         ("pin", "The Map Pack decides most calls", "Search &ldquo;Botox near me&rdquo; from Las Olas or Flagler Village and Google shows a handful of nearby practices above everything else. Proximity, reviews, and a complete Google Business Profile decide who makes that list."),
         ("chat", "Clients search in more than English", "43.8% of Broward County residents age 5 and up speak a language other than English at home, according to the " + CENSUS + ". Spanish and Portuguese treatment pages can reach clients your competitors miss."),
         ("calendar", "Demand shifts with the season", "Search interest rises and falls as seasonal residents and visitors come and go. We plan treatment content and Google posts ahead of your busy months, not during them."),
         ("search", "Neighborhood-level intent", "Clients search by area: Victoria Park, Coral Ridge, Harbor Beach, Wilton Manors, Plantation. Helpful, specific content makes your practice relevant beyond your exact street."),
     ],
     "deliver": ["Google Business Profile optimization: categories, services, photos, and weekly posts",
                 "A dedicated page for every treatment you offer, written for Fort Lauderdale searches",
                 "Review requests sent to every client after their visit (no review gating)",
                 "Matching name, address, and phone across Apple Maps, Yelp, Bing, and health directories",
                 "Spanish-language pages for your top treatments",
                 "Monthly ranking, traffic, and call reports"],
     "tool": "seo",
     "areas_intro": "Google weighs distance heavily in Maps results, so we focus your visibility on the neighborhoods closest to your practice, then grow outward with content.",
     "faqs": [
         ("How long does SEO take for a Fort Lauderdale med spa?", "Most practices see Google Business Profile improvements in the first two to three months. Competitive treatment keywords in Fort Lauderdale usually take four to six months or longer, depending on your reviews, website, and how many nearby competitors invest in SEO."),
         ("Can I rank in areas where I don't have an office?", "Google Maps favors practices close to the person searching, so ranking in the Map Pack far from your address is difficult. Your website can still rank in regular search results for nearby areas with helpful, specific content, and that's the approach we take."),
         ("Do you create Spanish-language pages?", "Yes. For practices that serve Spanish- or Portuguese-speaking clients, we build translated treatment pages reviewed for natural wording, with the right language tags so Google shows each version to the right people."),
         ("Is it OK to only ask happy clients for Google reviews?", "No. Google's policies prohibit selectively asking for positive reviews, often called review gating. Our review automation sends requests to every client and routes any concerns to your team separately."),
     ]},
    {"key": "web", "slug": "/med-spa-website-design-fort-lauderdale/", "short": "Website Design",
     "title": "Med Spa Website Design in Fort Lauderdale | BV Consulting",
     "desc": "Fort Lauderdale med spa website design: fast, mobile-first, bilingual-ready sites with online booking, treatment pages, and local SEO built in.",
     "h1": "Med Spa Website Design in Fort Lauderdale",
     "lede": "A website that feels as polished as your treatment rooms and books consultations from any phone. We design and build fast, mobile-first med spa websites for Fort Lauderdale practices, with online booking, treatment pages, and local SEO from day one.",
     "img": "med-spa-consultation-mirror", "alt": "Med spa client reviewing her results in a hand mirror",
     "local_h": "Built for How Fort Lauderdale Clients Browse and Book",
     "local": [
         ("mobile", "Designed for phones first", "Most med spa visitors browse on a phone, between errands, after work, or on a weekend at the beach. Every page is built to load fast and book in a few taps."),
         ("chat", "Bilingual-ready from the start", "With 43.8% of Broward residents speaking a language other than English at home (" + CENSUS + "), your site is structured so Spanish or Portuguese pages can be added cleanly."),
         ("shield", "Accessible and privacy-minded", "We follow WCAG accessibility guidelines, add clear consent language to forms, and keep patient health information off public website forms."),
         ("zap", "Ready for storm season", "Hurricane season runs June 1 through November 30. Your site includes an easy-to-update alert banner for closures and rescheduling, so clients are never guessing."),
     ],
     "deliver": ["Custom design that matches your brand and treatment menu",
                 "Online booking connected to Boulevard, Zenoti, Vagaro, and more",
                 "Treatment pages with pricing guidance, FAQs, and before-and-after galleries (with client consent)",
                 "Local business schema, a Google Maps embed, and consistent contact details",
                 "Speed tuning with compressed modern image formats",
                 "Lead forms that deliver to your inbox and CRM"],
     "tool": "seo",
     "areas_intro": "We meet with practice owners across Broward County to plan the site, review designs, and walk through launch.",
     "faqs": [
         ("How much does a med spa website cost in Fort Lauderdale?", "It depends on the number of treatment pages, languages, and integrations. We give a clear, fixed quote after a free consultation. Our guide on <a href=\"/blog/med-spa-website-cost/\">med spa website costs</a> explains what drives the price."),
         ("Can you redesign my site without losing my Google rankings?", "Yes. We map every existing URL, set up redirects, and carry over page titles, content, and schema to protect your rankings through the move."),
         ("Do you meet in person?", "Yes. We're based in Fort Lauderdale and can meet at your practice in Broward County to review the plan and designs."),
         ("Will the site work with my booking software?", "In most cases, yes. We connect platforms like Boulevard, Zenoti, Mangomint, and Vagaro through booking widgets, links, or integrations, then test the full booking flow on mobile before launch."),
     ]},
    {"key": "agents", "slug": "/med-spa-ai-agents-fort-lauderdale/", "short": "AI Agents",
     "title": "AI Agents for Med Spas in Fort Lauderdale | BV Consulting",
     "desc": "AI receptionists for Fort Lauderdale med spas that answer calls, texts, and DMs 24/7 in English or Spanish and book consultations while you're closed.",
     "h1": "AI Agents for Fort Lauderdale Med Spas",
     "lede": "An AI receptionist that answers every call, text, and Instagram DM, day or night, in English or Spanish. It books consultations, answers the questions you approve, and hands clinical questions to your licensed team.",
     "img": "med-spa-consultation-mirror", "alt": "Med spa client smiling at her results after a consultation",
     "local_h": "Why Fort Lauderdale Practices Are Adding AI Agents",
     "local": [
         ("clock", "Late-night and out-of-town inquiries", "Visitors and seasonal residents often message late at night or from other time zones. Your agent replies in seconds instead of the next business day."),
         ("chat", "English, Spanish, and Portuguese", "Your agent can reply in the language a client writes in, using answers your team has reviewed. That matters in a county where 43.8% of residents speak another language at home."),
         ("zap", "Storm-day messaging", "During hurricane season, update one set of instructions and your agent tells every client about closures and helps them reschedule."),
         ("shield", "Guardrails for a medical setting", "No medical advice from AI. Clinical questions, reactions, and urgent concerns are flagged for your provider right away."),
     ],
     "deliver": ["24/7 text, website chat, and Instagram and Facebook DM agent",
                 "AI voice receptionist for overflow and after-hours calls",
                 "Bilingual replies reviewed by your team",
                 "Consultation booking inside your booking software",
                 "Lead details logged in your CRM automatically",
                 "Monthly conversation reviews to keep improving answers"],
     "tool": "demo",
     "areas_intro": "Your AI agent covers every client, wherever they text from, while our team supports practices across Broward County in person.",
     "faqs": [
         ("Can the AI agent reply in Spanish?", "Yes. We set up the agent to recognize the language a client writes in and reply with translated answers your team has approved."),
         ("What happens when someone asks a medical question?", "The agent does not give medical advice. It lets the client know a licensed provider will follow up and alerts your team with the conversation details."),
         ("Will it work with my current phone number?", "Usually, yes. We can connect texting and voice to your existing business number or add a new registered line, depending on your phone provider."),
         ("Is texting clients allowed in Florida?", "Yes, with proper consent. Florida's Telephone Solicitation Act covers marketing texts, and its 2023 amendment centers on honoring STOP requests. We build consent capture and opt-out handling into every agent. This isn't legal advice, so confirm your campaigns with your attorney."),
     ]},
    {"key": "sms", "slug": "/med-spa-sms-booking-automation-fort-lauderdale/", "short": "SMS &amp; Booking",
     "title": "Med Spa SMS Booking Automation Fort Lauderdale | BV Consulting",
     "desc": "Automated reminders, confirmations, waitlists, and rebooking texts for Fort Lauderdale med spas, with Florida texting consent and opt-out rules built in.",
     "h1": "Automated SMS &amp; Booking for Fort Lauderdale Med Spas",
     "lede": "Confirmations, reminders, waitlist fills, and rebooking texts that run on their own and sync with your booking software, set up with the consent and opt-out handling Florida texting requires.",
     "img": "med-spa-payment-terminal-booking", "alt": "Client paying at the front desk of a med spa after booking her next visit",
     "local_h": "Texting and Booking Challenges Unique to South Florida",
     "local": [
         ("calendar", "Busy seasons fill fast", "When winter calendars are packed, a cancellation is revenue you can still save. Waitlist texts offer the opening to the next client in minutes."),
         ("shield", "Florida texting rules", "Florida's Telephone Solicitation Act applies to marketing texts, and its 2023 update put STOP replies front and center. Consent capture and opt-out handling are built into every workflow."),
         ("zap", "Hurricane rescheduling", "When a storm closes your doors, one message lets affected clients pick a new time, without your front desk calling everyone one by one."),
         ("repeat", "Rebooking on schedule", "Maintenance treatments work best on a schedule. Rebooking texts go out at the right interval for each service you offer."),
     ],
     "deliver": ["Booking confirmations with intake forms and prep instructions",
                 "Reminder texts with C to confirm and R to reschedule",
                 "Waitlist and cancellation-fill texts",
                 "Deposit and card-on-file links for longer appointments",
                 "Rebooking and reactivation campaigns by treatment",
                 "Registered business texting (A2P 10DLC) for better delivery"],
     "tool": "calc",
     "areas_intro": "Reminders and rebooking texts work for every client on your books, whether they live in Victoria Park or visit every winter.",
     "faqs": [
         ("How much can reminder texts reduce no-shows?", "Results vary by practice, deposit policy, and how far ahead clients book. Reminders that let clients confirm or reschedule with a one-letter reply are one of the most reliable ways to cut no-shows. Use the calculator above to see what that could be worth for you."),
         ("Do I need to register my business texting number?", "Yes. U.S. carriers require A2P 10DLC registration for business texting from standard local numbers. We handle registration so your messages are less likely to be filtered."),
         ("Which booking systems do you connect?", "We commonly work with Boulevard, Zenoti, Mangomint, Vagaro, Mindbody, AestheticsPro, Aesthetic Record, and PatientNow, along with CRMs like HighLevel and HubSpot."),
         ("Can reminders go out in Spanish?", "Yes. We can store each client's preferred language and send reminders and campaigns in English or Spanish."),
     ]},
    {"key": "automation", "slug": "/med-spa-ai-automation-fort-lauderdale/", "short": "AI Automation",
     "title": "AI Automation for Med Spas in Fort Lauderdale | BV Consulting",
     "desc": "AI automation for Fort Lauderdale med spas: instant lead follow-up, review requests, membership renewals, and win-back campaigns that run on autopilot.",
     "h1": "AI Automation for Fort Lauderdale Med Spas",
     "lede": "Hand the repetitive work to automation: lead follow-up in seconds, intake and aftercare messages, review requests, and win-back campaigns. Your team gets time back for the clients in the room.",
     "img": "med-spa-lip-filler-treatment", "alt": "Provider performing a lip filler treatment at a med spa",
     "local_h": "Where Automation Pays Off for Fort Lauderdale Practices",
     "local": [
         ("users", "Consistency through staff changes", "Front desk turnover is a familiar challenge for busy practices. Automated follow-up keeps working the same way no matter who is on shift."),
         ("layers", "Practices across the tri-county area", "Many groups operate in Broward, Palm Beach, and Miami-Dade. One set of workflows can route leads and reports to the right location."),
         ("star", "Reviews that keep coming", "In a crowded market, recent reviews matter. Automated requests go to every client after their visit, never only the happy ones."),
         ("refresh", "Win back seasonal clients", "Send welcome-back offers when seasonal residents return, and check in with clients who haven't booked in a while."),
     ],
     "deliver": ["Instant lead follow-up by text and email",
                 "Intake, prep, and aftercare messages by treatment",
                 "Post-visit review requests to every client",
                 "Membership renewal and failed payment follow-ups",
                 "Win-back campaigns for lapsed clients",
                 "Weekly lead and revenue reports by location"],
     "tool": "timeline",
     "areas_intro": "We build automations for single-location med spas and multi-location groups across Broward County and South Florida.",
     "faqs": [
         ("What should a Fort Lauderdale med spa automate first?", "Start with what costs you bookings: new lead follow-up, missed call text back, and appointment reminders. Most practices add review requests and rebooking next."),
         ("Which tools do you build automations with?", "We use platforms like Zapier, Make, and HighLevel together with AI tools such as Claude and ChatGPT, connected to your booking software and CRM."),
         ("Will automated messages feel robotic?", "Not when they're done well. We write in your brand voice, personalize each message with the client's name and treatment, and keep a person in the loop for anything sensitive."),
         ("Do you only work with Fort Lauderdale practices?", "No. We're based in Fort Lauderdale and work with med spas across South Florida and nationwide."),
     ]},
    {"key": "api", "slug": "/med-spa-api-integrations-fort-lauderdale/", "short": "API Integrations",
     "title": "Med Spa API Integrations in Fort Lauderdale | BV Consulting",
     "desc": "Connect your Fort Lauderdale med spa's booking software, CRM, payments, ads, and phone system so every lead and appointment syncs without double entry.",
     "h1": "Med Spa Software Integrations in Fort Lauderdale",
     "lede": "Your booking software, CRM, forms, payments, ads, and phone system, finally talking to each other. We connect the tools your Fort Lauderdale practice already uses so data moves on its own.",
     "img": "med-spa-payment-terminal-booking", "alt": "Med spa front desk payment terminal connected to booking software",
     "local_h": "Integration Problems We Solve for South Florida Practices",
     "local": [
         ("layers", "One view across locations", "Practices with locations in more than one South Florida county get a single view of leads, bookings, and revenue."),
         ("chart", "Know which ads book clients", "Connect Meta and Google Ads to your booking software to see which campaigns turn into paid appointments, not just clicks."),
         ("database", "No more double entry", "New leads, appointments, and payments sync between systems, so your team stops copying details from one screen to another."),
         ("shield", "Privacy-minded data flows", "We keep patient health information out of tools that aren't meant for it and use vendors that sign a Business Associate Agreement where needed."),
     ],
     "deliver": ["Booking software to CRM sync (Boulevard, Zenoti, Vagaro, and more)",
                 "Website forms and chat connected to your CRM",
                 "Ad conversion tracking tied to real bookings",
                 "Payments and membership data connected to client records",
                 "Call tracking that logs lead source and outcome",
                 "Custom API work when no ready-made connector exists"],
     "tool": "timeline",
     "areas_intro": "Integration work happens remotely, but we're happy to meet at your Broward County practice to map out your systems.",
     "faqs": [
         ("What if my booking software doesn't have an open API?", "Some platforms limit API access. We check what your system supports, then use official integrations, automation platforms, or scheduled exports to connect it as reliably as possible."),
         ("Is patient data safe when systems are connected?", "We design integrations to share only the data each tool needs, keep health information in HIPAA-appropriate systems, and use vendors that sign a Business Associate Agreement where required."),
         ("How long does an integration project take?", "Simple connections can be live within a couple of weeks. Multi-system or custom API projects usually take several weeks, and your quote includes a timeline."),
         ("Can you fix integrations someone else set up?", "Yes. We audit existing Zaps, workflows, and API connections, fix what's broken, and document how everything works for your team."),
     ]},
]
LOCAL_BY_KEY = {p["key"]: p for p in LOCAL_PAGES}


def local_links(exclude=None, heading=True):
    items = "".join('<a class="local-link" href="%s"><span class="svc-ic">%s</span><span>%s<small>Fort Lauderdale, FL</small></span></a>'
                    % (p["slug"], ic(SVC[p["key"]]["icon"], 20, 1.9), strip(p["h1"]).replace(" in Fort Lauderdale, FL", "").replace(" in Fort Lauderdale", "").replace(" for Fort Lauderdale Med Spas", " for Med Spas"))
                    for p in LOCAL_PAGES if p["key"] != exclude)
    return '<div class="local-links">%s</div>' % items


def build():
    for p in LOCAL_PAGES:
        s = SVC[p["key"]]
        cards = "\n".join('<div class="pain"><div class="ic">%s</div><div><b>%s</b><span>%s</span></div></div>' % (ic(i, 20), h, t) for i, h, t in p["local"])
        deliver = "".join("<li>%s</li>" % d for d in p["deliver"])
        areas = "".join("<li>%s</li>" % a for a in BROWARD)
        scripts = TOOLS_SCRIPT
        if p["tool"] == "seo":
            tool = seo_scorecard("bg-warm", "Score Your Med Spa's Local SEO in 60 Seconds")
        elif p["tool"] == "calc":
            tool = revenue_calc("bg-warm", "What Are No-Shows Costing Your Fort Lauderdale Med Spa?")
        elif p["tool"] == "timeline":
            tool = automation_timeline("bg-warm")
        else:
            tool = sms_demo("sms-demo", "bg-warm", "Live demo", "Text Our Demo AI Agent Right Now")
            scripts = DEMO_SCRIPT
        crumb_items = [("Home", "/"), ("Fort Lauderdale", LOCAL), (strip(p["short"]), p["slug"])]
        body = '''
<section class="hero bg-warm">
  <div class="container">
    {crumbs}
    <div class="hero-grid">
      <div>
        <span class="eyebrow">{pin_sm} Fort Lauderdale, FL</span>
        <h1>{h1}</h1>
        <p class="hero-sub">{lede}</p>
        <div class="hero-ctas">
          <a class="btn btn-primary" href="{quote}">Get a Free Quote</a>
          <a class="btn btn-secondary" href="tel:{tel}">{call_btn}</a>
        </div>
        <div class="hero-meta"><span><span class="dot"></span>Based in Fort Lauderdale</span><span><span class="dot"></span>In-person meetings in Broward</span></div>
      </div>
      <div class="svc-hero-photo">{photo}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">The local market</span><h2>{local_h}</h2></div>
    <div class="pains" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">{cards}</div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:26px"><span class="eyebrow">What's included</span><h2>What You Get</h2>
      <p class="local-intro">Everything below is part of our <a href="{svc_url}">{svc_long}</a> service, tailored to your Fort Lauderdale practice.</p></div>
    <ul class="check-list deliver-list">{deliver}</ul>
    <div class="center" style="margin-top:26px"><a class="btn btn-primary" href="{quote}">Get a Free Quote</a></div>
  </div>
</section>

{tool}

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:22px"><span class="eyebrow">Areas we serve</span><h2>Serving Fort Lauderdale and Broward County</h2>
      <p class="local-intro">{areas_intro}</p></div>
    <ul class="area-list">{areas}</ul>
    <p class="center" style="margin-top:18px"><a href="{local}">See all Fort Lauderdale med spa marketing services &rarr;</a></p>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">FAQ</span><h2>{short} for Fort Lauderdale Med Spas: FAQ</h2></div>
    <div style="max-width:820px;margin:0 auto">{faqs}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:26px"><span class="eyebrow">More in Fort Lauderdale</span><h2>Other Services for Local Med Spas</h2></div>
    {links}
  </div>
</section>

{cta}
'''.format(call_btn=CALL_BTN, crumbs=crumbs(crumb_items), pin_sm=ic("pin", 13, 2.2), h1=p["h1"], lede=p["lede"], quote=QUOTE, tel=TEL,
           photo=picture(p["img"], p["alt"], sizes="(min-width: 960px) 45vw, 100vw", eager=True, fallback_icon=s["icon"]),
           local_h=p["local_h"], cards=cards, svc_url=s["url"], svc_long=s["long"], deliver=deliver, tool=tool,
           areas_intro=p["areas_intro"], areas=areas, local=LOCAL, short=p["short"], faqs=faq_html(p["faqs"]),
           links=local_links(p["key"]),
           cta=cta_strip("Grow your Fort Lauderdale med spa", "Get a free quote from a local team. It takes about a minute."))
        area = [{"@type": "City", "name": "Fort Lauderdale", "containedInPlace": {"@type": "AdministrativeArea", "name": "Broward County, FL"}},
                {"@type": "AdministrativeArea", "name": "Broward County, FL"}]
        service_ld = {"@context": "https://schema.org", "@type": "Service", "@id": SITE + p["slug"] + "#service",
                      "name": strip(p["h1"]), "serviceType": strip(s["long"]), "description": p["desc"], "url": SITE + p["slug"],
                      "provider": {"@id": BUSINESS_ID}, "areaServed": area,
                      "audience": {"@type": "BusinessAudience", "audienceType": "Med spas and aesthetic practices"}}
        page(p["slug"], p["title"], p["desc"], body,
             schemas=[service_ld, breadcrumb_ld(crumb_items), faq_ld([(q, strip(a)) for q, a in p["faqs"]])],
             active="/services/", scripts_after=scripts, priority="0.8", images=[p["img"]])
