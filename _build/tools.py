"""Interactive tools: missed revenue calculator, automation timeline, SEO scorecard.
Markup is rendered here; behavior lives in out/tools.js."""
from common import *

TOOLS_SCRIPT = '<script src="/tools.js" defer></script>'


def _head(eyebrow, title, lede):
    return '''<div class="center tool-head">
      <span class="eyebrow">%s</span>
      <h2>%s</h2>
      <p>%s</p>
    </div>''' % (eyebrow, title, lede)


def revenue_calc(bg="bg-soft", title="How Much Revenue Is Your Med Spa Missing?"):
    fields = [
        ("missed", "Calls, texts &amp; DMs that go unanswered each week", 0, 80, 1, 12, "", ""),
        ("book", "Share of those that would have booked", 5, 60, 5, 30, "", "%"),
        ("value", "Average visit value", 100, 2000, 25, 450, "$", ""),
        ("appts", "Appointments per month", 0, 1500, 10, 250, "", ""),
        ("noshow", "No-show &amp; late cancel rate", 0, 30, 1, 8, "", "%"),
    ]
    rows = "".join('''
        <div class="calc-field">
          <div class="calc-label"><label for="calc-{k}">{label}</label><output for="calc-{k}" data-show="{k}">{pre}{val}{suf}</output></div>
          <input type="range" id="calc-{k}" data-in="{k}" min="{mn}" max="{mx}" step="{st}" value="{val}" data-pre="{pre}" data-suf="{suf}" />
        </div>'''.format(k=k, label=label, mn=mn, mx=mx, st=st, val=val, pre=pre, suf=suf) for k, label, mn, mx, st, val, pre, suf in fields)
    return '''<section class="section {bg} tool-section" id="calculator" aria-label="Missed revenue calculator">
  <div class="container">
    {head}
    <div class="calc" data-calc>
      <div class="calc-inputs">{rows}
      </div>
      <div class="calc-results" aria-live="polite">
        <span class="calc-kicker">Estimated revenue slipping away</span>
        <div class="calc-big"><b data-out="month">$0</b><span>/month</span></div>
        <div class="calc-year">About <b data-out="year">$0</b> a year</div>
        <ul class="calc-rows">
          <li><span>{i_phone}Unanswered leads</span><b data-out="leads">$0</b></li>
          <li><span>{i_cal}No-shows &amp; late cancels</span><b data-out="noshows">$0</b></li>
        </ul>
        <div class="calc-recover">
          <span>If automation won back <b>1 in 3</b> missed leads and cut no-shows by <b>25%</b>:</span>
          <strong>+<span data-out="recover">$0</span>/month</strong>
        </div>
        <a class="btn btn-primary calc-cta" href="{quote}">Get a Plan to Recover It</a>
        <p class="calc-note">Illustrative estimate based on your inputs (4.33 weeks per month). Actual results vary by practice.</p>
      </div>
    </div>
  </div>
</section>'''.format(bg=bg, rows=rows, quote=QUOTE, i_phone=ic("phone", 16, 2), i_cal=ic("calendar", 16, 2),
                     head=_head("Free calculator", title, "Move the sliders to match your practice and see what missed calls and no-shows could be costing you every month."))


TL_TRIGGERS = [("lead", "sparkle", "New lead"), ("missed", "phone", "Missed call"), ("booked", "calendar", "Consult booked"),
               ("noshow", "clock", "No-show"), ("rebook", "repeat", "Rebooking"), ("review", "star", "After the visit")]


def automation_timeline(bg="bg-soft", title="Watch a Med Spa Automation Run"):
    btns = "".join('<button type="button" class="tl-trigger" data-trigger="%s" aria-pressed="%s">%s<span>%s</span></button>'
                   % (k, "true" if n == 0 else "false", ic(i, 16, 2), name) for n, (k, i, name) in enumerate(TL_TRIGGERS))
    return '''<section class="section {bg} tool-section" id="automation-timeline" aria-label="Automation timeline example">
  <div class="container">
    {head}
    <div class="tl" data-timeline>
      <div class="tl-triggers" role="group" aria-label="Choose a trigger">{btns}</div>
      <div class="tl-panel">
        <div class="tl-top">
          <div><span class="tl-kicker">When this happens</span><b class="tl-title" data-tl-title>New lead comes in</b></div>
          <button type="button" class="tl-replay" data-tl-replay>{i_rep}<span>Replay</span></button>
        </div>
        <ol class="tl-steps" data-tl-steps></ol>
        <div class="tl-stack"><span>Connected in this workflow:</span><div data-tl-stack></div></div>
      </div>
    </div>
    <p class="tool-note center">Example workflow. Timing, messages, and tools are customized for your practice and policies.</p>
  </div>
</section>'''.format(bg=bg, btns=btns, i_rep=ic("repeat", 15, 2),
                     head=_head("Interactive example", title, "Pick a moment in the client journey and watch what happens automatically, across your texts, calendar, CRM, and team."))


SEO_QS = [
    ("Is your Google Business Profile claimed and fully filled out, with your services, hours, and photos?", 16,
     "Complete your Google Business Profile: primary category, every service, hours, photos, and weekly posts."),
    ("Do you have a separate page on your website for each main treatment (Botox, filler, laser, facials)?", 14,
     "Build a dedicated page for each core treatment with pricing guidance, FAQs, and a booking button."),
    ("Are you getting new Google reviews every month?", 14,
     "Automate review requests to every client after their visit so fresh reviews keep coming in."),
    ("Are your business name, address, and phone number identical on your website, Google, Yelp, and Apple Maps?", 12,
     "Clean up your listings so your name, address, and phone match everywhere Google looks."),
    ("Does your website load quickly and look great on a phone?", 12,
     "Speed up your mobile site with compressed images and a lighter layout. Most clients browse on phones."),
    ("Do your page titles mention the treatment and your city (for example, &ldquo;Lip Filler in Fort Lauderdale&rdquo;)?", 10,
     "Rewrite page titles and descriptions to include each treatment and your city."),
    ("Can visitors book online from every page of your site?", 10,
     "Add a clear Book Now button to every page so search traffic turns into appointments."),
    ("Do you publish helpful content, like FAQs, guides, or before-and-afters (with consent), at least monthly?", 12,
     "Publish one helpful treatment guide or FAQ update each month to build authority."),
]


def seo_scorecard(bg="bg-soft", title="How Strong Is Your Med Spa's Local SEO?"):
    qs = "".join('''
        <li class="sc-q" data-weight="{w}" data-fix="{fix}">
          <p id="sc-q{n}">{q}</p>
          <div class="sc-opts" role="group" aria-labelledby="sc-q{n}">
            <button type="button" data-a="yes" aria-pressed="false">Yes</button><button type="button" data-a="unsure" aria-pressed="false">Not sure</button><button type="button" data-a="no" aria-pressed="false">No</button>
          </div>
        </li>'''.format(n=n + 1, q=q, w=w, fix=fix.replace('"', "&quot;")) for n, (q, w, fix) in enumerate(SEO_QS))
    return '''<section class="section {bg} tool-section" id="seo-scorecard" aria-label="Med spa SEO scorecard">
  <div class="container">
    {head}
    <div class="sc" data-scorecard>
      <ol class="sc-qs">{qs}
      </ol>
      <div class="sc-result" aria-live="polite">
        <div class="sc-ring">
          <svg viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="52" class="sc-track"/><circle cx="60" cy="60" r="52" class="sc-fill" data-sc-ring/></svg>
          <div class="sc-num"><b data-sc-score>0</b><span>/100</span></div>
        </div>
        <b class="sc-grade" data-sc-grade>Answer the questions</b>
        <p class="sc-progress" data-sc-progress>0 of {total} answered</p>
        <div class="sc-fixes" data-sc-fixes hidden>
          <span>Your top fixes</span>
          <ol data-sc-list></ol>
        </div>
        <a class="btn btn-primary sc-cta" href="{quote}">Get a Free SEO Review</a>
      </div>
    </div>
  </div>
</section>'''.format(bg=bg, qs=qs, total=len(SEO_QS), quote=QUOTE,
                     head=_head("Free SEO scorecard", title, "Answer 8 quick questions to see where your practice stands on Google and which fixes will move the needle most."))
