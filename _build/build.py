import os, re, shutil
from common import *
from posts_meta import POSTS
import posts_a, posts_b, page_home, page_services, page_other, page_local
from tools import revenue_calc, automation_timeline, seo_scorecard, TOOLS_SCRIPT

CONTENT = {}
CONTENT.update(posts_a.CONTENT)
CONTENT.update(posts_b.CONTENT)


POST_TOOLS = {
    "med-spa-seo-checklist": seo_scorecard("bg-warm", "Score Your Med Spa SEO Checklist"),
    "med-spa-website-cost": seo_scorecard("bg-warm", "Is Your Website Helping Your Local SEO?"),
    "med-spa-missed-calls-no-shows": revenue_calc("bg-warm", "What Are Missed Calls and No-Shows Costing You?"),
    "med-spa-sms-booking-automation": revenue_calc("bg-warm"),
    "med-spa-software-integrations": automation_timeline("bg-warm", "See Connected Med Spa Software in Action"),
    "ai-agents-for-med-spas": automation_timeline("bg-warm", "See What an AI Agent Automates"),
}


def build_post(p):
    c = CONTENT[p["slug"]]
    svc = SVC[p["service"]]
    toc = "".join('<li><a href="#%s">%s</a></li>' % (sid, strip(h)) for sid, h, _ in c["sections"]) + '<li><a href="#faq">Frequently asked questions</a></li>'
    secs = []
    for n, (sid, h, html_) in enumerate(c["sections"]):
        secs.append('<h2 id="%s">%s</h2>\n%s' % (sid, h, html_))
        if n + 1 == c["cta_after"]:
            secs.append('''<aside class="lead-inline">
  <h3>Want this built for your med spa?</h3>
  <p>BV Consulting sets up %s for med spas nationwide. Get a free growth plan and quote.</p>
  <a class="btn" href="%s">Get a Free Quote</a> <a class="btn" href="%s" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.7)">See %s</a>
</aside>''' % ({"agents": "custom AI agents", "sms": "automated SMS and booking", "automation": "AI automation", "seo": "SEO", "web": "high-converting websites", "api": "API integrations"}[p["service"]], QUOTE, svc["url"], svc["name"]))
    faqs = "\n".join('<h3>%s</h3>\n<p>%s</p>' % (q, a) for q, a in c["faqs"])
    related = [x for x in POSTS if x["slug"] != p["slug"]]
    related = sorted(related, key=lambda x: (x["cat_key"] != p["cat_key"]))[:3]
    if p.get("img") in IMG:
        hero = picture(p["img"], p["img_alt"], sizes="(min-width: 800px) 760px, 100vw", eager=True)
    else:
        hero = '<div class="pc-art %s">%s<span class="pc-art-label">%s</span></div>' % (p["art"], ic(p["icon"], 60, 1.4), p["cat"])
    body = '''
<article class="section">
  <div class="container">
    <header class="article-head">
      {crumbs}
      <span class="eyebrow">{cat}</span>
      <h1>{title}</h1>
      <div class="article-meta"><span>By BV Consulting</span><span>&bull;</span><time datetime="{date}">{date_h}</time><span>&bull;</span><span>{mins} min read</span></div>
    </header>
    <div class="article-hero">{hero}</div>
    <div class="prose">
      {intro}
      <div class="takeaways"><h2>Key takeaways</h2><ul class="check-list">{takeaways}</ul></div>
      <nav class="toc" aria-label="Table of contents"><h2>In this article</h2><ol>{toc}</ol></nav>
      {sections}
      <h2 id="faq">Frequently asked questions</h2>
      {faqs}
      <div class="author-box"><span class="brand-badge" style="width:46px;height:46px;flex-shrink:0">BV</span><p><strong>BV Consulting</strong> builds <a href="/med-spa-ai-agents/">AI agents</a>, <a href="/med-spa-sms-booking-automation/">SMS &amp; booking automation</a>, <a href="/med-spa-seo/">SEO</a>, <a href="/med-spa-website-design/">websites</a>, and <a href="/med-spa-api-integrations/">integrations</a> for med spas. Based in Fort Lauderdale, FL, serving med spas nationwide.</p></div>
      <p style="margin-top:26px"><a class="btn btn-secondary" href="/blog/">&larr; Back to Blog</a></p>
    </div>
  </div>
</article>
{tool}
<section class="section bg-soft">
  <div class="container">
    <div class="center" style="margin-bottom:26px"><span class="eyebrow">Keep reading</span><h2>Related Articles</h2></div>
    <div class="blog-grid">{related}</div>
  </div>
</section>
{cta}
'''.format(crumbs=crumbs([("Home", "/"), ("Blog", "/blog/"), (p["cat"].replace("&", "&amp;"), p["url"])]),
           cat=p["cat"].replace("&", "&amp;"), title=p["title"], date=p["date"], date_h=TODAY_HUMAN, mins=p["mins"],
           hero=hero, intro=c["intro"], takeaways="".join("<li>%s</li>" % t for t in c["takeaways"]), toc=toc,
           sections="\n".join(secs), faqs=faqs, related="\n".join(post_card(x) for x in related),
           tool=POST_TOOLS.get(p["slug"], ""),
           cta=cta_strip("Ready to put this to work at your med spa?", "Get a free growth plan and quote. It takes about 60 seconds."))
    words = len(strip(c["intro"] + " ".join(s[2] for s in c["sections"]) + " ".join(q + a for q, a in c["faqs"])).split())
    post_ld = {"@context": "https://schema.org", "@type": "BlogPosting", "@id": SITE + p["url"] + "#article",
               "headline": p["title"], "description": p["desc"], "image": img_url(p["img"]),
               "datePublished": p["date"], "dateModified": p["date"], "inLanguage": "en-US",
               "author": {"@type": "Organization", "@id": BUSINESS_ID, "name": "BV Consulting", "url": SITE + "/"},
               "publisher": {"@type": "Organization", "@id": BUSINESS_ID, "name": "BV Consulting", "logo": {"@type": "ImageObject", "url": SITE + "/logo.png"}},
               "mainEntityOfPage": SITE + p["url"], "articleSection": p["cat"], "keywords": p["keywords"], "wordCount": words,
               "isPartOf": {"@id": SITE + "/blog/#blog"}, "about": {"@type": "Thing", "name": strip(svc["long"])}}
    page(p["url"], p["seo_title"], p["desc"], body,
         schemas=[post_ld, breadcrumb_ld([("Home", "/"), ("Blog", "/blog/"), (p["title"], p["url"])]), faq_ld(c["faqs"])],
         og_type="article", active="/blog/", priority="0.7", images=[p["img"]],
         extra_head='<meta property="article:published_time" content="%sT09:00:00-04:00" />' % p["date"],
         scripts_after=TOOLS_SCRIPT if p["slug"] in POST_TOOLS else "")
    return words


def extras():
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for path, pr in PAGES:
        imgs = "".join("<image:image><image:loc>%s/images/%s-1200.jpg</image:loc></image:image>" % (SITE, k)
                       for k in dict.fromkeys(PAGE_IMAGES.get(path, [])))
        sm.append("  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority>%s</url>" % (SITE, path, TODAY, pr, imgs))
    sm.append("</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    open(os.path.join(OUT, "robots.txt"), "w").write("User-agent: *\nAllow: /\nDisallow: /thank-you/\n\nSitemap: %s/sitemap.xml\n" % SITE)
    open(os.path.join(OUT, "CNAME"), "w").write("bvconsulting.live\n")


if __name__ == "__main__":
    # clean generated html (keep images, static assets)
    # remove previously generated pages (never touches .git, _build, or images)
    for root, dirs, files in os.walk(OUT):
        dirs[:] = [d for d in dirs if not d.startswith((".", "_")) and d != "images"]
        for f in files:
            if f.endswith(".html"):
                os.remove(os.path.join(root, f))
    page_home.build()
    page_services.build()
    page_services.build_hub()
    page_other.local_page()
    page_local.build()
    page_other.about()
    page_other.contact()
    page_other.quote()
    page_other.thank_you()
    page_other.blog_index()
    for p in POSTS:
        print(p["url"], build_post(p), "words")
    page_other.privacy()
    page_other.terms()
    page_other.not_found()
    extras()
    open(os.path.join(OUT, "_config.yml"), "w").write("# GitHub Pages (Jekyll) settings: keep docs and build source off the public site\nexclude:\n  - README.md\n  - GOOGLE-SHEET-SETUP.md\n  - SEO-LAUNCH-CHECKLIST.md\n  - _build\n")
    open(os.path.join(OUT, "styles.css"), "w").write(open(os.path.join(HERE, "base.css")).read() + open(os.path.join(HERE, "add.css")).read() + open(os.path.join(HERE, "add2.css")).read() + open(os.path.join(HERE, "add3.css")).read() + open(os.path.join(HERE, "add4.css")).read())
    print(len(PAGES), "indexable pages")
