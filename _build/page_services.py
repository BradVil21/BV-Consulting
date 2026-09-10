from common import *
from tools import revenue_calc, automation_timeline, seo_scorecard, TOOLS_SCRIPT
from posts_meta import POSTS

LANDING = {
    "agents": {
        "title": "AI Agents for Med Spas | AI Receptionist | BV Consulting",
        "desc": "Custom AI agents for med spas that answer calls, texts, chats, and DMs 24/7 and book consultations. Built with Claude and other leading AI tools.",
        "eyebrow": "AI Agent Creation",
        "h1": "Custom AI Agents That Answer, Qualify, and Book Med Spa Clients 24/7",
        "lede": "Your AI agent works the front desk around the clock. It answers questions about treatments, pricing guidelines, and availability across phone, text, website chat, and social DMs, then books the consultation or hands off to your team. Built on leading AI tools, including Claude, and trained on your practice.",
        "alt": "Med spa client reviewing results in a hand mirror after a consultation",
        "card_title": "Your AI agent can",
        "card": ["Answer calls, texts, chats &amp; Instagram DMs", "Explain treatments and prep instructions you approve", "Qualify leads and book consultations", "Send deposit and intake links", "Escalate clinical questions to your team", "Log every conversation in your CRM"],
        "problems_h": "Why med spas are adding AI agents",
        "problems": [
            ("clock", "Inquiries come in after hours", "Many clients research treatments at night and on weekends, when no one is there to reply."),
            ("phone", "Front desk can't answer everything", "Check-ins, checkouts, and phone calls compete for the same person's attention."),
            ("sms", "DMs sit unanswered", "Instagram and Facebook messages pile up and warm leads go cold."),
            ("repeat", "Same questions all day", "Pricing ranges, downtime, parking, and prep questions eat hours every week."),
        ],
        "deliver_h": "AI agents we build for med spas",
        "deliver": [
            ("phone", "AI voice receptionist", "Answers overflow and after-hours calls in a natural voice, books appointments, and transfers to staff when needed."),
            ("sms", "Text &amp; DM agent", "Replies to SMS, Instagram, and Facebook messages instantly with on-brand answers and booking links."),
            ("chat", "Website chat agent", "Greets visitors, answers treatment FAQs, and captures name, phone, and interest before they leave."),
            ("calendar", "Booking agent", "Checks availability in your booking software and schedules consultations or treatments."),
            ("refresh", "Follow-up agent", "Nudges leads who didn't book, reminds clients about maintenance treatments, and reactivates past clients."),
            ("shield", "Guardrails &amp; handoff", "Clear rules for what the agent can and can't say, with instant handoff to licensed providers for clinical questions."),
        ],
        "steps": [
            ("Discovery", "We learn your treatments, policies, pricing guidelines, tone, and the questions your team hears most."),
            ("Knowledge &amp; guardrails", "We build the agent's knowledge base and define what it should never answer, like medical advice."),
            ("Connect &amp; test", "We connect your phone, website, social inbox, booking software, and CRM, then test real scenarios."),
            ("Launch &amp; improve", "We review conversations, refine answers, and report on inquiries handled and consultations booked."),
        ],
        "extra": "tools",
        "faqs": [
            ("What is an AI agent for a med spa?", "An AI agent is a virtual assistant trained on your practice's information. It communicates with clients by phone, text, chat, or DM, answers common questions, collects details, and books appointments, following rules you approve."),
            ("Which AI do you use to build agents?", "We build with several leading AI tools, including Claude by Anthropic, ChatGPT by OpenAI, and Google Gemini, and choose based on the channel, your budget, and privacy needs. Voice and SMS run on established business communications platforms."),
            ("Will the AI give medical advice?", "No. We configure agents to share only information you approve, such as general treatment descriptions and policies, and to route clinical or medical questions to your licensed team."),
            ("Is an AI agent HIPAA compliant?", "Compliance depends on the full setup, not just the AI. We design agents to minimize protected health information, use services that support a Business Associate Agreement where PHI is involved, and document how data flows so your compliance lead can review it."),
            ("Can clients still reach a real person?", "Always. Clients can ask for a human at any time, and the agent can transfer calls, notify staff, or create a callback task in your CRM."),
        ],
        "posts": ["ai-agents-for-med-spas", "med-spa-missed-calls-no-shows"],
    },
    "sms": {
        "title": "Med Spa SMS & Booking Automation | BV Consulting",
        "desc": "Automated SMS and online booking for med spas: confirmations, reminders, deposits, waitlist fills, rebooking texts, and two-way texting that reduce no-shows.",
        "eyebrow": "Automated SMS &amp; Bookings",
        "h1": "Automated SMS &amp; Online Booking That Keeps Your Med Spa Calendar Full",
        "lede": "Make booking effortless and no-shows rare. We set up online booking, deposit collection, and automated text workflows for confirmations, reminders, waitlists, and rebooking, all connected to your booking software and written in your voice.",
        "alt": "Med spa client in a robe relaxing with tea before her treatment",
        "card_title": "Automations we set up",
        "card": ["Instant booking confirmations", "Reminders before every appointment", "Deposit &amp; card-on-file requests", "Waitlist texts for open slots", "Rebooking nudges timed to each treatment", "Two-way texting in one shared inbox"],
        "problems_h": "Sound familiar?",
        "problems": [
            ("calendar", "No-shows and late cancellations", "Empty appointment slots waste provider time and hurt monthly revenue."),
            ("repeat", "Clients forget to rebook", "Maintenance treatments slip because no one reminds clients at the right time."),
            ("phone", "Phone tag to schedule", "Clients want to book in a few taps, not wait for a callback."),
            ("edit", "Manual reminder calls", "Your team spends hours calling and texting clients one by one."),
        ],
        "deliver_h": "What's included",
        "deliver": [
            ("calendar", "Online booking setup", "A clean booking flow on your website and Google Business Profile, connected to your booking software."),
            ("sms", "Confirmation &amp; reminder texts", "Friendly confirmations and reminders with easy confirm or reschedule options."),
            ("dollar", "Deposits &amp; no-show protection", "Deposit or card-on-file requests for high-value appointments, based on your policy."),
            ("zap", "Waitlist &amp; gap fillers", "When a slot opens, the next client on the waitlist gets a text to grab it."),
            ("repeat", "Rebooking &amp; maintenance reminders", "Timed nudges based on the treatment, like a follow-up for neurotoxin maintenance."),
            ("flag", "Compliant business texting", "Registered business messaging, consent capture, opt-out handling, and PHI-light message templates."),
        ],
        "steps": [
            ("Audit your booking flow", "We map how clients book today and where they drop off or no-show."),
            ("Write the messages", "We draft every text in your brand voice, keeping treatment details out of messages where appropriate."),
            ("Connect &amp; register", "We connect your booking software and complete business texting registration."),
            ("Launch &amp; measure", "We track confirmation rates, no-shows, and rebookings, then fine-tune timing."),
        ],
        "extra": "compliance",
        "faqs": [
            ("Can automated texts reduce no-shows?", "Reminders give clients an easy way to confirm or reschedule, which helps practices recover slots they would otherwise lose. Combined with a clear deposit or cancellation policy, they're one of the most practical ways to protect your schedule."),
            ("Will this work with my booking software?", "Most med spa booking platforms offer built-in reminders, integrations, or an API. We review your platform, use native features where they're strong, and add automations where they're not."),
            ("What is business texting registration?", "U.S. carriers require businesses that send texts through software from local numbers to register their brand and message use (often called A2P 10DLC). Registration helps your texts get delivered instead of filtered."),
            ("Can we text marketing promotions?", "Yes, with the right consent. Promotional texts require clear opt-in and easy opt-out, and federal and state rules apply. We build consent capture into your forms and booking flow, and recommend legal review of your policy."),
            ("Do texts include treatment details?", "We keep messages minimal by default, such as your practice name, date, and time, to protect client privacy. Any more detailed messaging is set up deliberately with your compliance guidance."),
        ],
        "posts": ["med-spa-sms-booking-automation", "med-spa-missed-calls-no-shows"],
    },
    "automation": {
        "title": "AI Automation for Med Spas | BV Consulting",
        "desc": "AI automation for med spas: instant lead follow-up, review requests, reactivation campaigns, membership renewals, and workflows that save hours.",
        "eyebrow": "AI Automation",
        "h1": "AI Automation That Handles Your Med Spa's Busywork",
        "lede": "From the moment a lead comes in to the review request after their treatment, automation keeps every step moving. We use AI and workflow tools to follow up instantly, nurture leads, bring past clients back, and eliminate repetitive admin.",
        "alt": "Injector performing a dermal filler treatment at a med spa",
        "card_title": "Popular automations",
        "card": ["Speed-to-lead replies for ads &amp; forms", "Consultation no-book follow-ups", "Google review requests after visits", "Past-client reactivation campaigns", "Membership &amp; package renewals", "Weekly performance summaries"],
        "problems_h": "Where time and revenue slip away",
        "problems": [
            ("clock", "Slow lead follow-up", "Leads from ads and your website wait hours for a reply and book elsewhere."),
            ("users", "Consults that never convert", "Clients come in for a consultation, then go quiet without a follow-up plan."),
            ("star", "Not enough reviews", "Happy clients leave without being asked, so your Google profile undersells your results."),
            ("chart", "No clear numbers", "It's hard to see which campaigns and providers drive real bookings."),
        ],
        "deliver_h": "Automation workflows we build",
        "deliver": [
            ("zap", "Speed-to-lead", "New leads from Meta ads, Google, and your website get an instant, personal text and email and land in your CRM."),
            ("users", "Consult-to-treatment nurture", "Thoughtful follow-ups after consultations with answers to common hesitations and easy booking."),
            ("star", "Review generation", "Automatic Google review requests after completed visits, following Google's review policies."),
            ("gift", "Reactivation &amp; memberships", "Win back lapsed clients and remind members about renewals, credits, and packages."),
            ("sparkle", "AI content assist", "AI-drafted blog outlines, social captions, and Google Business Profile posts for your team to review."),
            ("chart", "Reporting", "Automated weekly summaries of leads, bookings, and revenue by source and location."),
        ],
        "steps": [
            ("Map the client journey", "We trace every touchpoint from first inquiry to rebooking."),
            ("Prioritize quick wins", "We start with the automations most likely to recover bookings or save staff time."),
            ("Build with your tools", "We build on your CRM and booking platform, adding AI and workflow tools where they help."),
            ("Review &amp; refine", "Monthly reviews of results, message performance, and new opportunities."),
        ],
        "extra": "tools",
        "faqs": [
            ("What's the difference between AI automation and an AI agent?", "An AI agent has conversations with clients. AI automation covers the workflows behind the scenes, like sending follow-ups, requesting reviews, updating your CRM, and generating reports. Most practices benefit from both."),
            ("Do I need a CRM?", "A CRM makes automation far more powerful because every lead and client lives in one place. If you don't have one, we'll recommend options that integrate well with your booking software."),
            ("Are review request automations allowed?", "Yes, asking for reviews is allowed. Google's policies prohibit offering incentives for reviews and discourage selectively asking only happy clients, so we set up requests that go to every eligible client."),
            ("How long does it take to set up?", "Simple automations can launch quickly once access is in place. Multi-step journeys across several tools take longer. Your proposal will include a clear timeline."),
            ("Can you automate across multiple locations?", "Yes. We build workflows that route leads, messages, and reporting by location so each team sees its own clients."),
        ],
        "posts": ["med-spa-missed-calls-no-shows", "ai-agents-for-med-spas"],
    },
    "seo": {
        "title": "Med Spa SEO Services | Rank on Google Maps | BV Consulting",
        "desc": "SEO for med spas: Google Business Profile optimization, treatment pages, local SEO for every location, and content that ranks for injectables and laser.",
        "eyebrow": "Med Spa SEO",
        "h1": "Med Spa SEO That Gets You Found for the Treatments You Offer",
        "lede": "When someone searches for lip filler, laser hair removal, or a med spa near them, you should be one of the first practices they see. We build the local SEO, treatment content, and technical foundation that helps med spas rank on Google and Google Maps.",
        "alt": "Registered nurse performing laser hair removal treatment at a med spa",
        "card_title": "Every SEO plan includes",
        "card": ["Google Business Profile optimization", "Keyword research by treatment &amp; city", "Treatment &amp; location page strategy", "Technical SEO &amp; schema markup", "Review strategy &amp; local citations", "Monthly ranking &amp; lead reporting"],
        "problems_h": "Is search working for your practice?",
        "problems": [
            ("search", "Competitors outrank you", "Nearby practices show up first for the treatments you're known for."),
            ("pin", "Weak Google Maps presence", "An incomplete profile, few recent reviews, or wrong categories hold you back."),
            ("web", "Thin treatment pages", "One generic services page can't rank for dozens of specific treatment searches."),
            ("chart", "No idea what's working", "You can't connect rankings and traffic to actual consultations."),
        ],
        "deliver_h": "Med spa SEO services",
        "deliver": [
            ("pin", "Google Business Profile", "Categories, services, photos, posts, and review strategy for every location."),
            ("layers", "Treatment pages", "In-depth pages for injectables, lasers, facials, body contouring, and wellness services that answer real client questions."),
            ("flag", "Multi-location SEO", "Unique location pages and profiles for practices with more than one clinic."),
            ("code", "Technical SEO", "Speed, mobile experience, crawlability, and structured data so search engines understand your practice."),
            ("edit", "Content &amp; blog", "Educational articles that build trust and rank for the questions clients ask before booking."),
            ("chart", "Tracking &amp; reporting", "Search Console, analytics, and call tracking that tie SEO to booked consultations."),
        ],
        "steps": [
            ("SEO audit", "We review your rankings, Google profile, website, and competitors in your market."),
            ("Strategy", "We map target treatments and locations to pages and profile updates."),
            ("Optimize &amp; publish", "We fix technical issues, build and improve pages, and strengthen your local presence."),
            ("Report &amp; grow", "Monthly reporting on rankings, traffic, calls, and consultations, plus next priorities."),
        ],
        "extra": "compliance-seo",
        "faqs": [
            ("How long does med spa SEO take?", "Some improvements, like fixing your Google Business Profile, can help relatively quickly. Competitive treatment keywords usually take several months of consistent work on content, reviews, and authority."),
            ("Do you guarantee first-page rankings?", "No honest SEO provider can guarantee rankings, because search engines control results. We focus on the proven factors Google describes, like relevance, distance, and prominence, and report transparently on progress."),
            ("Can you do SEO for multiple locations or states?", "Yes. We build a unique location page and Google Business Profile strategy for each clinic, wherever you operate in the U.S."),
            ("Can you write about treatments like Botox or fillers?", "Yes. We write educational, accurate content and follow advertising best practices, such as avoiding guaranteed results and using brand names correctly. Your medical director should review clinical content before it's published."),
            ("Does SEO include before-and-after photos?", "Before-and-after galleries can help, but they require documented patient consent. We help you present them properly and optimize images for search."),
        ],
        "posts": ["med-spa-seo-checklist", "med-spa-website-cost"],
    },
    "web": {
        "title": "Med Spa Website Design & Development | BV Consulting",
        "desc": "Custom med spa website design and development: fast, elegant, mobile-first sites with online booking, treatment pages, SEO, and AI chat built in.",
        "eyebrow": "Website Development",
        "h1": "Med Spa Websites Designed to Turn Visitors Into Booked Consultations",
        "lede": "Your website should feel as polished as your treatment rooms. We design and develop fast, elegant, mobile-first med spa websites with clear treatment pages, easy online booking, and the SEO and AI features that turn browsers into clients.",
        "alt": "Modern med spa lounge with treatment beds, plants, and relaxation chairs",
        "card_title": "Every website includes",
        "card": ["Custom, luxury-feel design", "Treatment &amp; pricing guidance pages", "Online booking &amp; tap-to-call everywhere", "SEO &amp; schema built in", "AI chat &amp; lead capture ready", "Analytics &amp; conversion tracking"],
        "problems_h": "Is your website costing you clients?",
        "problems": [
            ("mobile", "Clunky on mobile", "Most clients browse on their phones, and slow, cramped pages send them away."),
            ("calendar", "Booking is buried", "If booking takes more than a few taps, many visitors won't finish."),
            ("layers", "Treatments are hard to understand", "Vague descriptions and missing FAQs leave clients with unanswered questions."),
            ("search", "Not built for search", "Pretty sites without SEO structure rarely show up on Google."),
        ],
        "deliver_h": "What we build",
        "deliver": [
            ("web", "Custom design", "A refined look that reflects your brand, whether it's clinical, luxury, or boutique."),
            ("layers", "Treatment pages", "Clear pages for each service with benefits, what to expect, FAQs, and booking calls to action."),
            ("calendar", "Booking integration", "Your booking software embedded or linked cleanly, plus deposit and intake flows."),
            ("gift", "Memberships &amp; offers", "Pages for memberships, packages, gift cards, and seasonal promotions."),
            ("zap", "Speed &amp; accessibility", "Lightweight, fast-loading pages built with accessibility best practices."),
            ("bot", "AI-ready", "AI chat, lead capture, and tracking that plug into your automations and CRM."),
        ],
        "steps": [
            ("Discovery", "We learn your brand, providers, treatments, and ideal clients."),
            ("Design", "You review a custom design and site plan before development starts."),
            ("Develop &amp; optimize", "We build the site, polish copy, add SEO, booking, tracking, and integrations."),
            ("Launch &amp; support", "We launch, submit to Google, and provide ongoing updates and improvements."),
        ],
        "extra": None,
        "faqs": [
            ("How much does a med spa website cost?", "It depends on the number of treatment pages, locations, features, and integrations. We provide a clear, written quote after a free consultation. Our <a href=\"/blog/med-spa-website-cost/\">med spa website cost guide</a> covers typical market ranges."),
            ("Can you redesign my existing site?", "Yes. We can refresh or rebuild your site while preserving the pages and URLs that already bring in search traffic."),
            ("Which platform do you build on?", "We build fast custom sites and also work with platforms like WordPress, Webflow, Squarespace, and Wix when they're a better fit for your team."),
            ("Will I be able to update the website myself?", "Yes. We set things up so your team can update offers, team bios, and blog posts, and we can handle changes for you on a care plan."),
            ("Can you integrate my booking software?", "Yes. We integrate platforms like Boulevard, Zenoti, Mangomint, Vagaro, and Mindbody through embeds, booking links, or APIs, depending on what each platform supports."),
        ],
        "posts": ["med-spa-website-cost", "med-spa-seo-checklist"],
    },
    "api": {
        "title": "Med Spa API Integrations & Software Sync | BV Consulting",
        "desc": "API integrations for med spas: connect Boulevard, Zenoti, Vagaro, Mindbody, and more to your CRM, payments, and ads. HIPAA-conscious builds.",
        "eyebrow": "API Integrations",
        "h1": "API Integrations That Connect Your Med Spa's Software",
        "lede": "Your booking system, EMR, CRM, payment processor, and marketing tools should share information automatically. We design and build API integrations that eliminate double entry, keep client records in sync, and give you a clear view of your business.",
        "alt": "Payment terminal at a med spa connected to booking and accounting software",
        "card_title": "Common integrations",
        "card": ["Booking software &rarr; CRM", "Website &amp; ad leads &rarr; CRM &amp; AI agent", "Payments &rarr; accounting", "Completed visits &rarr; review requests", "Bookings &rarr; ad conversion tracking", "All locations &rarr; one dashboard"],
        "problems_h": "Signs your software isn't talking",
        "problems": [
            ("edit", "Double data entry", "Staff copy client details between booking, CRM, and spreadsheets."),
            ("database", "Conflicting records", "Client info, memberships, and payments don't match across systems."),
            ("chart", "Marketing flies blind", "Ad platforms can't see which leads actually booked and paid."),
            ("clock", "Workflows stall", "Follow-ups and tasks wait until someone manually moves them forward."),
        ],
        "deliver_h": "Integration services",
        "deliver": [
            ("nodes", "Booking &amp; EMR connections", "Integrations with platforms such as Boulevard, Zenoti, Mangomint, Vagaro, Mindbody, AestheticsPro, and Aesthetic Record, based on available APIs."),
            ("users", "CRM sync", "Keep GoHighLevel, HubSpot, or your CRM updated with leads, bookings, and client status."),
            ("dollar", "Payments &amp; accounting", "Connect Stripe, Square, and your POS to accounting and reporting."),
            ("chart", "Ad conversion tracking", "Send booked and completed appointments back to Google and Meta so campaigns optimize for real clients."),
            ("code", "Custom APIs &amp; webhooks", "Custom integrations when no ready-made connector exists."),
            ("lock", "Secure, documented builds", "Least-privilege access, error monitoring, and plain-English documentation."),
        ],
        "steps": [
            ("Software audit", "We list your tools, what data each holds, and what each API allows."),
            ("Integration design", "We decide the source of truth for each data type and map every flow, including failure handling."),
            ("Build &amp; test", "We build with official APIs and trusted connectors and test with realistic scenarios."),
            ("Monitor &amp; support", "Alerts, documentation, and ongoing support as platforms change."),
        ],
        "extra": "compliance",
        "faqs": [
            ("Can you integrate with my med spa software?", "Most modern med spa platforms offer some integration options, but API access varies by vendor and plan. We confirm exactly what's available for your software before recommending an approach."),
            ("Do you use Zapier or custom code?", "Both. Tools like Zapier, Make, and n8n are great for many workflows. Custom integrations make sense for higher volume, advanced logic, or connections that don't exist yet."),
            ("How do you protect patient data in integrations?", "We move only the data each workflow needs, use secure authentication and least-privilege access, choose services that support a BAA when PHI is involved, and avoid sending health details to marketing platforms."),
            ("Can you connect Claude or other AI to my systems?", "Yes. We integrate AI tools, including Claude by Anthropic, with your CRM, booking software, and messaging platforms so AI agents and automations can work with real-time availability and client context, within the privacy limits you set."),
            ("What happens if an integration breaks?", "We build in error alerts and retry logic, and on a support plan we fix issues and update integrations as software vendors change their APIs."),
        ],
        "posts": ["med-spa-software-integrations", "med-spa-sms-booking-automation"],
    },
}

COMPLIANCE = '''<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:26px"><span class="eyebrow">Privacy &amp; compliance</span><h2>Built With Patient Privacy in Mind</h2>
    <p style="max-width:720px;margin:0 auto">Med spas handle sensitive client information. Our builds follow practical safeguards, and we recommend your compliance lead or attorney review your final setup.</p></div>
    <div class="trust-row">
      <div class="trust"><div class="ic">%s</div><div><b>PHI minimized</b><span>Messages and marketing tools get only the data they need.</span></div></div>
      <div class="trust"><div class="ic">%s</div><div><b>BAA-supported services</b><span>Used wherever protected health information is involved.</span></div></div>
      <div class="trust"><div class="ic">%s</div><div><b>Consent &amp; opt-outs</b><span>Clear opt-in capture and STOP handling for texts.</span></div></div>
      <div class="trust"><div class="ic">%s</div><div><b>Documented flows</b><span>Plain-English records of what connects to what.</span></div></div>
    </div>
  </div>
</section>''' % (ic("lock", 20), ic("shield", 20), ic("flag", 20), ic("edit", 20))

SEO_NOTE = '''<section class="section bg-soft">
  <div class="container">
    <div class="split-photo">
      <div>
        <span class="eyebrow">Local &amp; nationwide</span>
        <h2>SEO for Med Spas in Every Market</h2>
        <p>Whether you run one clinic or locations across several states, local search works the same way: Google looks at relevance, distance, and prominence. We build a separate, genuinely useful presence for each location, from Google Business Profile to location pages, so every clinic can compete in its own market.</p>
        <p>Based in South Florida? See our <a href="/med-spa-marketing-fort-lauderdale/">Fort Lauderdale med spa marketing</a> page.</p>
      </div>
      %s
    </div>
  </div>
</section>''' % picture("med-spa-consultation-mirror", "Med spa client checking treatment results in a mirror", fallback_icon="search")


def build():
    for key, L in LANDING.items():
        s = SVC[key]
        related = [p for p in POSTS if p["slug"] in L["posts"]]
        problems = "\n".join('<div class="pain"><div class="ic">%s</div><div><b>%s</b><span>%s</span></div></div>' % (ic(i, 20), h, t) for i, h, t in L["problems"])
        deliver = "\n".join('<div class="card"><div class="card-body"><div class="ic">%s</div><h3>%s</h3><p>%s</p></div></div>' % (ic(i, 24), h, t) for i, h, t in L["deliver"])
        steps = "\n".join('<div class="step"><div class="n">%d</div><h3>%s</h3><p>%s</p></div>' % (n + 1, h, t) for n, (h, t) in enumerate(L["steps"]))
        others = [x for x in SERVICES if x["key"] != key]
        other_html = "\n".join('<a class="svc-card" href="%s"><div class="svc-body"><span class="svc-ic" style="margin-top:0">%s</span><h3>%s</h3><p>%s</p><span class="more">Learn more &rarr;</span></div></a>'
                               % (x["url"], ic(x["icon"], 20, 1.9), x["name"], x["short"]) for x in others)
        TOOLS = {"sms": revenue_calc(""), "automation": automation_timeline("bg-warm"), "api": automation_timeline("bg-warm"),
                 "seo": seo_scorecard("bg-warm"), "web": seo_scorecard("bg-warm", "Is Your Website Helping Your Local SEO?"), "agents": ""}
        extra = {"tools": ai_tools_section("bg-soft"), "compliance": COMPLIANCE, "compliance-seo": SEO_NOTE, None: ""}[L["extra"]]
        body = '''
<section class="hero bg-warm">
  <div class="container">
    {crumbs}
    <div class="hero-grid">
      <div>
        <span class="eyebrow">{eyebrow} &middot; For med spas</span>
        <h1>{h1}</h1>
        <p class="hero-sub">{lede}</p>
        <div class="hero-ctas">
          <a class="btn btn-primary" href="{quote}">Get a Free Quote</a>
          <a class="btn btn-secondary" href="tel:{tel}">{call_btn}</a>
        </div>
        <p class="local-callout">{pin_sm}<span>South Florida practice? <a href="{local_url}">{svc_name} in Fort Lauderdale</a></span></p>
      </div>
      <div class="svc-hero-photo">
        {photo}
        <div class="sys-card">
          <div class="sys-head"><span class="sys-title">{card_title}</span></div>
          <ul class="check-list">{card}</ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">The challenge</span><h2>{problems_h}</h2></div>
    <div class="pains" style="grid-template-columns:repeat(auto-fit,minmax(250px,1fr))">{problems}</div>
  </div>
</section>

{demo}

{tool}

<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">What you get</span><h2>{deliver_h}</h2></div>
    <div class="cards">{deliver}</div>
    <div class="center" style="margin-top:28px"><a class="btn btn-primary" href="{quote}">Get a Free Quote</a></div>
  </div>
</section>

<section class="section bg-dark">
  <div class="container">
    <div class="center" style="margin-bottom:40px"><span class="eyebrow">Our process</span><h2>How It Works</h2></div>
    <div class="process">{steps}</div>
  </div>
</section>

{extra}

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">FAQ</span><h2>{long}: Frequently Asked Questions</h2></div>
    <div style="max-width:820px;margin:0 auto">{faqs}</div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">Learn more</span><h2>Related Guides</h2></div>
    <div class="blog-grid" style="max-width:820px;margin:0 auto;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{related}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">Complete the system</span><h2>Works Even Better Together</h2></div>
    <div class="svc-grid">{others}</div>
  </div>
</section>

{cta}
'''.format(call_btn=CALL_BTN, pin_sm=ic("pin", 16, 2), local_url=LOCAL_BY_SVC[key], svc_name=s["name"].replace("&", "&amp;"), tool=TOOLS[key], crumbs=crumbs([("Home", "/"), ("Services", "/services/"), (s["name"], s["url"])]), eyebrow=L["eyebrow"],
           h1=L["h1"], lede=L["lede"], quote=QUOTE, tel=TEL, phone=PHONE,
           photo=picture(s["img"], L["alt"], sizes="(min-width: 960px) 45vw, 100vw", eager=True, fallback_icon=s["icon"]),
           card_title=L["card_title"], card="".join("<li>%s</li>" % c for c in L["card"]), problems_h=L["problems_h"],
           problems=problems, deliver_h=L["deliver_h"], deliver=deliver, steps=steps, extra=extra, long=s["long"],
           demo=(sms_demo("sms-demo", "bg-warm", "Live demo", "Text the Demo AI Agent Right Now") if key == "agents" else
                 sms_demo("sms-demo", "bg-warm", "Live demo", "See Automated Med Spa Texting in Action",
                          "Try a missed-call text back, an appointment reminder, or a rebooking nudge. Reply the way a real client would and watch the automation respond.", start="missed") if key == "sms" else ""),
           faqs=faq_html(L["faqs"]), related="\n".join(post_card(p) for p in related), others=other_html,
           cta=cta_strip("Ready to see what %s can do for your practice?" % s["name"].replace("Med Spa ", ""),
                         "Get a free quote and a clear plan tailored to your med spa."))
        service_ld = {"@context": "https://schema.org", "@type": "Service", "@id": SITE + s["url"] + "#service",
                      "name": strip(s["long"]), "serviceType": strip(s["name"]), "description": L["desc"],
                      "url": SITE + s["url"], "provider": {"@id": BUSINESS_ID},
                      "areaServed": {"@type": "Country", "name": "United States"},
                      "audience": {"@type": "BusinessAudience", "audienceType": "Med spas and aesthetic practices"}}
        page(s["url"], L["title"], L["desc"], body,
             schemas=[service_ld, breadcrumb_ld([("Home", "/"), ("Services", "/services/"), (s["name"], s["url"])]), faq_ld(L["faqs"])],
             active="/services/", priority="0.9", images=[s["img"]], scripts_after=(DEMO_SCRIPT if key in ("agents", "sms") else "") + (TOOLS_SCRIPT if key != "agents" else ""))


def build_hub():
    blocks = []
    for n, s in enumerate(SERVICES):
        L = LANDING[s["key"]]
        text = '''<div><span class="eyebrow">%s</span><h2>%s</h2><p>%s</p><ul class="check-list">%s</ul>
<p style="margin-top:16px"><a class="btn btn-primary" href="%s">Explore %s</a></p></div>''' % (
            s["name"], L["h1"], s["short"], "".join("<li>%s</li>" % c for c in L["card"][:4]), s["url"], s["name"])
        blocks.append('<section class="section%s" id="%s"><div class="container"><div class="split-photo%s">%s%s</div></div></section>' % (
            " bg-soft" if n % 2 else "", s["key"], " flip" if n % 2 else "", text,
            picture(s["img"], L["alt"], fallback_icon=s["icon"])))
    faqs = [
        ("Which service should my med spa start with?", "If inquiries go unanswered, start with an AI agent or automated SMS. If you're not getting found, start with SEO and your website. If your team juggles disconnected software, start with integrations. We'll recommend a first step on your free consultation."),
        ("Can I combine services?", "Yes, and that's where results compound: SEO and your website bring in leads, AI agents and SMS convert them, and integrations keep every system in sync."),
        ("Do you work with multi-location practices?", "Yes. We build location-specific SEO, routing, and reporting for groups with clinics in one or several states."),
    ]
    body = '''
<section class="page-hero bg-warm">
  <div class="container">
    {crumbs}
    <span class="eyebrow">Services for med spas</span>
    <h1>Med Spa Marketing &amp; Automation Services</h1>
    <p class="lede">AI agent creation, automated SMS and booking, AI automation, SEO, website development, and API integrations, built specifically for med spas and aesthetic practices nationwide.</p>
    <div class="hero-ctas" style="margin-top:18px"><a class="btn btn-primary" href="{quote}">Get a Free Quote</a><a class="btn btn-secondary" href="tel:{tel}">{call_btn}</a></div>
  </div>
</section>
{blocks}
{tools}
<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:30px"><span class="eyebrow">FAQ</span><h2>Questions About Our Services</h2></div>
    <div style="max-width:820px;margin:0 auto">{faqs}</div>
  </div>
</section>
{cta}
'''.format(call_btn=CALL_BTN, crumbs=crumbs([("Home", "/"), ("Services", "/services/")]), quote=QUOTE, tel=TEL, phone=PHONE,
           blocks="\n".join(blocks), tools=ai_tools_section(""), faqs=faq_html(faqs),
           cta=cta_strip("Not sure where to start?", "Tell us about your practice and we'll recommend the right first step."))
    page("/services/", "Med Spa Marketing & Automation Services | BV Consulting",
         "Services for med spas: AI agents, automated SMS and booking, AI automation, SEO, website development, and API integrations. Get a free quote.",
         body, schemas=[breadcrumb_ld([("Home", "/"), ("Services", "/services/")]), faq_ld(faqs)],
         active="/services/", priority="0.9", images=[SERVICES[0]["img"]])
