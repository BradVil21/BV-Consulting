/* BV Consulting: shared site script (loaded on every page)
   ------------------------------------------------------------------
   SETTINGS: edit these values in one place.
   ------------------------------------------------------------------ */
var BV_CONFIG = {
  // Every form submission is emailed here (via FormSubmit.co, free).
  // The FIRST submission sends an activation email to this inbox. Click
  // "Activate Form" in that email once and all future leads arrive.
  email: "BVConsultings@outlook.com",
  formEndpoint: "https://formsubmit.co/ajax/BVConsultings@outlook.com",

  // Optional: also log every lead to a Google Sheet.
  // See GOOGLE-SHEET-SETUP.md, then paste your Apps Script /exec URL here.
  googleSheetUrl: "",

  // Optional: Google Analytics 4 measurement ID, e.g. "G-XXXXXXXXXX".
  // Leave blank until you create your GA4 property.
  gaId: ""
};

(function () {
  "use strict";

  /* ---------- Google Analytics 4 (only loads when gaId is set) ---------- */
  if (BV_CONFIG.gaId) {
    var ga = document.createElement("script");
    ga.async = true;
    ga.src = "https://www.googletagmanager.com/gtag/js?id=" + BV_CONFIG.gaId;
    document.head.appendChild(ga);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", BV_CONFIG.gaId);
  }
  function track(name, params) {
    if (typeof window.gtag === "function") { window.gtag("event", name, params || {}); }
  }

  /* ---------- Lead submission shared by the quote + contact forms ---------- */
  window.BV = window.BV || {};
  window.BV.track = track;
  window.BV.submitLead = function (data, subject) {
    var payload = {};
    Object.keys(data).forEach(function (k) { payload[k] = data[k]; });
    payload._subject = subject || "New lead from bvconsulting.live";
    payload._template = "table";
    payload._captcha = "false";
    if (payload.email) { payload._replyto = payload.email; }
    payload.page = window.location.href;

    if (BV_CONFIG.googleSheetUrl) {
      try {
        var fd = new FormData();
        Object.keys(payload).forEach(function (k) { if (k.charAt(0) !== "_") fd.append(k, payload[k]); });
        fetch(BV_CONFIG.googleSheetUrl, { method: "POST", mode: "no-cors", body: fd });
      } catch (e) { /* sheet logging is optional */ }
    }

    return fetch(BV_CONFIG.formEndpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(payload)
    }).then(function (res) {
      if (!res.ok) { throw new Error("Form service returned " + res.status); }
      track("generate_lead", { form: payload.form || "unknown" });
      return res;
    });
  };
  window.BV.mailtoFallback = function (data, subject) {
    var body = Object.keys(data).map(function (k) { return k + ": " + data[k]; }).join("\n");
    return "mailto:" + BV_CONFIG.email + "?subject=" + encodeURIComponent(subject || "Website inquiry") + "&body=" + encodeURIComponent(body);
  };

  function ready(fn) {
    if (document.readyState === "loading") { document.addEventListener("DOMContentLoaded", fn); } else { fn(); }
  }

  ready(function () {

    /* ---------- Mobile nav + footer year ---------- */
    var toggle = document.querySelector(".menu-toggle"), links = document.getElementById("nav-links");
    if (toggle && links) {
      toggle.addEventListener("click", function () {
        var open = links.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
      links.querySelectorAll("a").forEach(function (a) {
        a.addEventListener("click", function () { links.classList.remove("open"); toggle.setAttribute("aria-expanded", "false"); });
      });
    }
    var y = document.getElementById("year"); if (y) { y.textContent = new Date().getFullYear(); }

    /* ---------- Track phone + email clicks (GA4) ---------- */
    document.querySelectorAll('a[href^="tel:"]').forEach(function (a) { a.addEventListener("click", function () { track("click_to_call"); }); });
    document.querySelectorAll('a[href^="mailto:"]').forEach(function (a) { a.addEventListener("click", function () { track("click_email"); }); });

    /* ---------- Back-to-top button ---------- */
    var btn = document.createElement("button");
    btn.id = "back-to-top";
    btn.setAttribute("aria-label", "Back to top");
    btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>';
    document.body.appendChild(btn);
    window.addEventListener("scroll", function () { btn.classList.toggle("visible", window.scrollY > 300); }, { passive: true });
    btn.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });

    /* ---------- Scroll reveal animations ---------- */
    var revealTargets = [
      ".hero h1", ".hero-sub", ".hero-ctas", ".hero-meta", ".sys-card",
      ".page-hero .eyebrow", ".page-hero h1", ".page-hero p",
      ".section .center .eyebrow", ".section .center h2", ".section .center p",
      ".card", ".step", ".value", ".pillar", ".industry", ".promise",
      ".post-card", ".ci-item", ".form-card", ".cta-strip",
      ".split > div", "details.faq-item"
    ];
    var seen = [];
    revealTargets.forEach(function (sel) {
      document.querySelectorAll(sel).forEach(function (el) {
        if (seen.indexOf(el) !== -1) return;
        seen.push(el);
        if (!el.hasAttribute("data-reveal")) el.setAttribute("data-reveal", "");
      });
    });
    document.querySelectorAll(".cards, .process, .values, .pillars, .industries, .promises, .blog-grid, .deliverables").forEach(function (grid) {
      Array.prototype.forEach.call(grid.children, function (child, i) {
        child.setAttribute("data-reveal", "");
        child.dataset.revealDelay = (i * 80);
      });
    });
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          setTimeout(function () { el.classList.add("revealed"); }, parseFloat(el.dataset.revealDelay || 0));
          io.unobserve(el);
        });
      }, { threshold: 0.1, rootMargin: "0px 0px -30px 0px" });
      document.querySelectorAll("[data-reveal]").forEach(function (el) { io.observe(el); });
    } else {
      document.querySelectorAll("[data-reveal]").forEach(function (el) { el.classList.add("revealed"); });
    }

    /* ---------- Blog category filter ---------- */
    var filters = document.querySelectorAll(".filter");
    if (filters.length) {
      filters.forEach(function (f) {
        f.addEventListener("click", function () {
          filters.forEach(function (x) { x.classList.remove("active"); x.setAttribute("aria-pressed", "false"); });
          f.classList.add("active"); f.setAttribute("aria-pressed", "true");
          var cat = f.getAttribute("data-filter");
          document.querySelectorAll(".blog-grid .post-card").forEach(function (card) {
            card.hidden = !(cat === "all" || card.getAttribute("data-cat") === cat);
          });
        });
      });
    }

    /* ---------- Contact form ---------- */
    var cform = document.getElementById("contact-form");
    if (cform) {
      cform.addEventListener("submit", function (e) {
        e.preventDefault();
        if (!cform.checkValidity()) { cform.reportValidity(); return; }
        if (cform.elements["_honey"] && cform.elements["_honey"].value) { return; }
        var v = function (n) { var el = cform.elements[n]; return el ? String(el.value).trim() : ""; };
        var data = {
          form: "Contact page",
          name: v("name"),
          business: v("business"),
          phone: v("phone"),
          email: v("email"),
          interest: v("interest"),
          message: v("message")
        };
        var sub = cform.querySelector("button[type=submit]");
        var ok = document.getElementById("contact-success"), err = document.getElementById("contact-error");
        sub.disabled = true; sub.textContent = "Sending…"; err.classList.remove("show");
        window.BV.submitLead(data, "New message from " + data.name + " (bvconsulting.live)").then(function () {
          ok.classList.add("show"); cform.reset(); sub.textContent = "Message sent";
        }).catch(function () {
          err.innerHTML = 'Something went wrong sending your message. Please <a href="' + window.BV.mailtoFallback(data, "Website inquiry") + '">email us directly</a> or call <a href="tel:+19548251009">954-825-1009</a>.';
          err.classList.add("show"); sub.disabled = false; sub.textContent = "Send Message";
        });
      });
    }
  });
})();
