from common import TODAY

CATS = {"ai": ("AI Agents & Automation", ""), "growth": ("SEO & Websites", "web"), "ops": ("Booking & Integrations", "api")}


def _p(slug, cat_key, icon, img, img_alt, title, seo_title, desc, excerpt, mins, service, keywords):
    return {"slug": slug, "url": "/blog/%s/" % slug, "cat_key": cat_key, "cat": CATS[cat_key][0], "art": CATS[cat_key][1],
            "icon": icon, "img": img, "img_alt": img_alt, "title": title, "seo_title": seo_title, "desc": desc,
            "excerpt": excerpt, "mins": mins, "date": TODAY, "service": service, "keywords": keywords}


POSTS = [
    _p("ai-agents-for-med-spas", "ai", "bot", "med-spa-consultation-mirror",
       "Med spa client reviewing her results in a hand mirror after a consultation",
       "AI Agents for Med Spas: 7 Ways to Book More Consultations on Autopilot",
       "AI Agents for Med Spas: 7 Ways to Book More Consults",
       "How med spas use AI agents to answer calls, texts, chats, and DMs 24/7, qualify leads, book consultations, and follow up, without adding front desk staff.",
       "Your front desk can't answer every call, DM, and after-hours inquiry. An AI agent can. Here are seven ways med spas put AI agents to work.",
       4, "agents", "AI agents for med spas, AI receptionist med spa, med spa chatbot"),
    _p("med-spa-seo-checklist", "growth", "search", "med-spa-laser-hair-removal",
       "Registered nurse performing laser hair removal on a client's arm at a med spa",
       "Med Spa SEO Checklist: How to Rank on Google Maps for the Treatments You Offer",
       "Med Spa SEO Checklist: Rank on Google Maps in 2026",
       "A step-by-step med spa SEO checklist: Google Business Profile, treatment pages, reviews, citations, and content that ranks for injectables, laser, and more.",
       "When someone nearby searches for lip filler or laser hair removal, will they find you? Work through this checklist to climb Google Maps.",
       4, "seo", "med spa SEO, medical spa SEO, med spa Google Maps ranking"),
    _p("med-spa-software-integrations", "ops", "nodes", "med-spa-payment-terminal-booking",
       "Card payment terminal at a med spa front desk showing a checkout total",
       "Med Spa Software Integrations: How APIs Connect Your Booking System, CRM, and Payments",
       "Med Spa Software Integrations & APIs, Explained",
       "A plain-English guide to med spa API integrations: connect booking software like Boulevard or Zenoti to your CRM, payments, and ads, with HIPAA in mind.",
       "Your booking system, CRM, payments, and ads should work as one. Here's how API integrations connect med spa software, in plain English.",
       4, "api", "med spa software integration, med spa API integration, Boulevard integration"),
    _p("med-spa-sms-booking-automation", "ops", "calendar", "med-spa-payment-terminal-booking",
       "Med spa checkout terminal used for deposits and appointment payments",
       "Med Spa SMS & Booking Automation: 6 Workflows That Keep Your Calendar Full",
       "Med Spa SMS & Booking Automation: 6 Workflows",
       "Six SMS and booking automations for med spas: confirmations, reminders, deposits, waitlist fills, rebooking nudges, and renewals, plus texting rules.",
       "Reminders, deposits, waitlists, and rebooking texts can run themselves. These six workflows keep your med spa's calendar full.",
       3, "sms", "med spa SMS marketing, med spa booking automation, med spa text reminders"),
    _p("med-spa-missed-calls-no-shows", "ai", "phone", "med-spa-lip-filler-treatment",
       "Injector performing a dermal filler treatment at a med spa",
       "Missed Calls and No-Shows Are Costing Your Med Spa: How AI Follow-Up Wins Them Back",
       "Med Spa Missed Calls & No-Shows: How AI Fixes Both",
       "Missed calls and no-shows quietly drain med spa revenue. Learn how missed-call text back, AI follow-up, and smart reminders recover bookings.",
       "Every unanswered call and empty chair is lost revenue. Here's how AI text back and smarter reminders help med spas win it back.",
       3, "automation", "med spa missed calls, med spa no-shows, missed call text back med spa"),
    _p("med-spa-website-cost", "growth", "dollar", "med-spa-consultation-mirror",
       "Client admiring her aesthetic treatment results in a mirror",
       "How Much Does a Med Spa Website Cost in 2026?",
       "How Much Does a Med Spa Website Cost? (2026 Guide)",
       "What does a med spa website cost in 2026? Compare DIY, freelancer, and agency pricing, ongoing costs, and the features a med spa site needs to convert.",
       "DIY, freelancer, or agency? A clear breakdown of 2026 website costs and the must-have features that turn med spa visitors into bookings.",
       4, "web", "med spa website cost, med spa website design, medical spa website"),
]
BY_SLUG = {p["slug"]: p for p in POSTS}
