/* BV Consulting interactive tools: missed revenue calculator, automation timeline, SEO scorecard.
   Everything runs in the browser. Nothing you enter is sent anywhere. */
(function () {
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function track(name, params) { if (window.BV && window.BV.track) window.BV.track(name, params || {}); }
  function money(n) { return "$" + Math.round(n).toLocaleString("en-US"); }
  function ready(fn) { if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", fn); else fn(); }

  /* ---------------- Missed revenue calculator ---------------- */
  function initCalc(root) {
    var inputs = root.querySelectorAll("[data-in]"), used = false;
    function v(k) { return parseFloat(root.querySelector('[data-in="' + k + '"]').value) || 0; }
    function out(k, text) { var el = root.querySelector('[data-out="' + k + '"]'); if (el) el.textContent = text; }
    function update() {
      inputs.forEach(function (i) {
        var pct = (i.value - i.min) / (i.max - i.min) * 100;
        i.style.setProperty("--pct", pct + "%");
        var show = root.querySelector('[data-show="' + i.dataset.in + '"]');
        var label = i.dataset.pre + Number(i.value).toLocaleString("en-US") + i.dataset.suf;
        if (show) show.textContent = label;
        i.setAttribute("aria-valuetext", label);
      });
      var leads = v("missed") * 4.33 * (v("book") / 100) * v("value");
      var noshows = v("appts") * (v("noshow") / 100) * v("value");
      var total = leads + noshows;
      out("month", money(total)); out("year", money(total * 12));
      out("leads", money(leads)); out("noshows", money(noshows));
      out("recover", money(leads / 3 + noshows * 0.25));
      out("sticky", money(total));
    }
    inputs.forEach(function (i) {
      i.addEventListener("input", function () { update(); if (!used) { used = true; track("tool_calculator_use"); } });
    });
    update();
    var sticky = root.querySelector("[data-calc-sticky]"), results = root.querySelector(".calc-big"), inBox = root.querySelector(".calc-inputs");
    if (sticky && "IntersectionObserver" in window) {
      var inputsOn = false, resultsOn = false;
      var sync = function () { var on = inputsOn && !resultsOn; sticky.classList.toggle("show", on); document.body.classList.toggle("calc-sticky-on", on); };
      new IntersectionObserver(function (e) { inputsOn = e[0].isIntersecting; sync(); }, { threshold: 0.15 }).observe(inBox);
      new IntersectionObserver(function (e) { resultsOn = e[0].intersectionRatio > 0.9; sync(); }, { threshold: [0, 0.9, 1] }).observe(results);
    }
  }

  /* ---------------- Automation timeline ---------------- */
  var P = {
    sms: '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    cal: '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    user: '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    bell: '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9M13.7 21a2 2 0 0 1-3.4 0"/>',
    star: '<path d="M12 2l3 6 6 1-4.5 4 1 6-5.5-3-5.5 3 1-6L3 9l6-1z"/>',
    mail: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    check: '<path d="M20 6L9 17l-5-5"/>',
    phone: '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    card: '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
    chart: '<path d="M3 3v18h18M7 14l4-4 3 3 5-6"/>',
    alert: '<path d="M12 9v4M12 17h.01M10.3 3.9L1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/>'
  };
  function svg(k, s) { return '<svg width="' + (s || 16) + '" height="' + (s || 16) + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + P[k] + "</svg>"; }

  var FLOWS = {
    lead: { title: "New lead comes in", stack: ["Website form", "Instagram ads", "CRM", "AI agent", "Booking software"], steps: [
      ["0:00", "user", "Lead captured", "Maria fills out your lip filler form. A CRM contact is created and tagged by treatment and source.", "CRM"],
      ["+30 sec", "sms", "Instant text reply", "“Hi Maria! Thanks for your interest in lip filler at Your Med Spa. Want me to find you a consultation time?”", "AI agent"],
      ["+2 min", "cal", "Consultation booked", "Maria picks Thursday at 1:15 PM. The appointment lands in your booking software with a confirmation text.", "Booking software"],
      ["+3 min", "mail", "Intake forms sent", "Digital intake and consent forms go out so check-in takes seconds.", "Forms"],
      ["If no reply in 1 hr", "bell", "Gentle follow-up", "A friendly nudge with your openings this week and a link to your treatment page.", "AI agent"],
      ["Day 2", "check", "Team task created", "Still unbooked? Your front desk gets a call task with the full conversation attached.", "CRM"]
    ]},
    missed: { title: "A call goes unanswered", stack: ["Phone system", "AI agent", "Booking software", "CRM"], steps: [
      ["0:00", "phone", "Missed call detected", "Your front desk is with a client when a new caller rings in.", "Phone system"],
      ["+10 sec", "sms", "Text back", "“Sorry we missed your call! This is Your Med Spa. How can we help? You can text us right here.”", "AI agent"],
      ["+1 min", "sms", "AI answers questions", "The caller asks about Botox pricing and downtime. The agent replies with your approved answers.", "AI agent"],
      ["+3 min", "cal", "Appointment booked", "The client books a consultation by text. It syncs to your calendar automatically.", "Booking software"],
      ["+4 min", "user", "Logged in your CRM", "Call source, conversation, and booking are saved to the client's record.", "CRM"]
    ]},
    booked: { title: "A consultation is booked", stack: ["Booking software", "SMS", "Payments", "Forms"], steps: [
      ["0:00", "check", "Confirmation", "Instant text and email confirmation with date, time, address, and parking tips.", "SMS"],
      ["+1 min", "card", "Deposit link", "For longer appointments, a secure deposit or card-on-file link goes out based on your policy.", "Payments"],
      ["48 hrs before", "mail", "Prep instructions", "Treatment-specific prep, like avoiding certain supplements, as written by your providers.", "Forms"],
      ["24 hrs before", "sms", "Confirm or reschedule", "“Reply C to confirm or R to reschedule.” Replies update the calendar on their own.", "SMS"],
      ["2 hrs before", "bell", "See you soon", "A short reminder with directions, so fewer clients show up late.", "SMS"]
    ]},
    noshow: { title: "A client doesn't show up", stack: ["Booking software", "SMS", "CRM", "Reports"], steps: [
      ["+15 min", "alert", "Marked as no-show", "The appointment is flagged in your booking software.", "Booking software"],
      ["+20 min", "sms", "We missed you text", "“We missed you today! Life happens. Want to grab another time this week?”", "SMS"],
      ["+1 day", "cal", "Next openings", "A second message shares your next few openings with one-tap booking.", "SMS"],
      ["+1 day", "user", "Tagged in CRM", "The client is tagged so your team can apply your cancellation policy consistently.", "CRM"],
      ["Weekly", "chart", "No-show report", "Owners see no-show rates by provider and service, so patterns are easy to spot.", "Reports"]
    ]},
    rebook: { title: "Time for a maintenance visit", stack: ["Booking software", "SMS", "AI agent", "Email"], steps: [
      ["Visit day", "check", "Treatment logged", "The client's neurotoxin visit is recorded with their provider.", "Booking software"],
      ["Week 11", "sms", "Rebooking text", "“Hi Jess! It's about time for your next Botox touch-up. Want your usual Tuesday afternoon with Dr. Lee?”", "SMS"],
      ["+1 min", "cal", "Booked in a reply", "Jess replies yes, and the agent books the next opening with her provider.", "AI agent"],
      ["Week 13", "mail", "Membership offer", "If she hasn't booked, an email shares your membership perks for regular treatments.", "Email"]
    ]},
    review: { title: "After the visit", stack: ["Booking software", "SMS", "Google reviews", "Team alerts"], steps: [
      ["+2 hrs", "sms", "Thank you and aftercare", "Aftercare instructions for today's treatment, plus how to reach the team with questions.", "SMS"],
      ["+1 day", "star", "Review request", "Every client gets a link to leave a Google review. No review gating, per Google's policies.", "Google reviews"],
      ["+1 day", "bell", "Concerns go to a person", "If a client replies with a concern, your manager is alerted right away to follow up personally.", "Team alerts"],
      ["+2 weeks", "sms", "Check-in", "A friendly check-in to see how they're loving their results.", "SMS"]
    ]}
  };

  function initTimeline(root) {
    var list = root.querySelector("[data-tl-steps]"), title = root.querySelector("[data-tl-title]"), stack = root.querySelector("[data-tl-stack]");
    var btns = root.querySelectorAll("[data-trigger]"), timers = [], current = "lead", seen = false;
    function clear() { timers.forEach(clearTimeout); timers = []; }
    function play(key) {
      clear(); current = key;
      var f = FLOWS[key];
      btns.forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.trigger === key ? "true" : "false"); });
      title.textContent = f.title;
      stack.innerHTML = f.stack.map(function (s) { return "<span>" + s + "</span>"; }).join("");
      list.innerHTML = f.steps.map(function (s) {
        return '<li class="tl-step"><span class="tl-dot">' + svg(s[1], 16) + '</span><div class="tl-body"><div class="tl-meta"><span class="tl-time">' + s[0] +
          '</span><span class="tl-tag">' + s[4] + '</span></div><b>' + s[2] + "</b><p>" + s[3] + "</p></div></li>";
      }).join("");
      var items = list.querySelectorAll(".tl-step");
      if (reduce) { items.forEach(function (li) { li.classList.add("on"); }); return; }
      items.forEach(function (li, i) { timers.push(setTimeout(function () { li.classList.add("on"); }, 250 + i * 650)); });
    }
    btns.forEach(function (b) { b.addEventListener("click", function () { play(b.dataset.trigger); track("tool_timeline_trigger", { trigger: b.dataset.trigger }); }); });
    root.querySelector("[data-tl-replay]").addEventListener("click", function () { play(current); });
    if ("IntersectionObserver" in window && !reduce) {
      list.innerHTML = "";
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting && !seen) { seen = true; play(current); io.disconnect(); } });
      }, { threshold: 0.25 });
      io.observe(root);
    } else { play(current); }
  }

  /* ---------------- SEO scorecard ---------------- */
  function initScorecard(root) {
    var qs = root.querySelectorAll(".sc-q"), ring = root.querySelector("[data-sc-ring]"), C = 2 * Math.PI * 52;
    var scoreEl = root.querySelector("[data-sc-score]"), grade = root.querySelector("[data-sc-grade]"), prog = root.querySelector("[data-sc-progress]");
    var fixes = root.querySelector("[data-sc-fixes]"), list = root.querySelector("[data-sc-list]"), done = false;
    ring.style.strokeDasharray = C; ring.style.strokeDashoffset = C;
    function update() {
      var score = 0, answered = 0, misses = [];
      qs.forEach(function (q) {
        var a = q.dataset.answer, w = +q.dataset.weight;
        if (!a) return;
        answered++;
        if (a === "yes") score += w; else misses.push({ w: w + (a === "no" ? 0.5 : 0), fix: q.dataset.fix });
      });
      scoreEl.textContent = score;
      ring.style.strokeDashoffset = C * (1 - score / 100);
      root.classList.toggle("sc-low", score < 50); root.classList.toggle("sc-mid", score >= 50 && score < 80); root.classList.toggle("sc-high", score >= 80);
      prog.textContent = answered + " of " + qs.length + " answered";
      if (!answered) { grade.textContent = "Answer the questions"; }
      else if (answered < qs.length) { grade.textContent = "Keep going…"; }
      else if (score >= 80) { grade.textContent = "Strong foundation"; }
      else if (score >= 50) { grade.textContent = "Room to grow"; }
      else { grade.textContent = "Big opportunity"; }
      misses.sort(function (a, b) { return b.w - a.w; });
      list.innerHTML = misses.slice(0, 3).map(function (m) { return "<li>" + m.fix + "</li>"; }).join("");
      fixes.hidden = !misses.length;
      if (answered === qs.length && !done) { done = true; track("tool_seo_scorecard_complete", { score: score }); }
    }
    qs.forEach(function (q) {
      q.querySelectorAll("[data-a]").forEach(function (b) {
        b.addEventListener("click", function () {
          q.dataset.answer = b.dataset.a;
          q.querySelectorAll("[data-a]").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
          q.classList.add("answered");
          update();
        });
      });
    });
    update();
  }

  ready(function () {
    document.querySelectorAll("[data-calc]").forEach(initCalc);
    document.querySelectorAll("[data-timeline]").forEach(initTimeline);
    document.querySelectorAll("[data-scorecard]").forEach(initScorecard);
  });
})();
