/* BV Consulting - shared site interactions
   Scroll reveal animations, animated stat counters, and back-to-top button.
   Loaded on every page. Nav toggle + year are handled inline per page. */
(function () {
  "use strict";

  function ready(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else { fn(); }
  }

  ready(function () {

    /* ---------- 1. Back-to-top button ---------- */
    var btn = document.createElement("button");
    btn.id = "back-to-top";
    btn.setAttribute("aria-label", "Back to top");
    btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>';
    document.body.appendChild(btn);

    window.addEventListener("scroll", function () {
      btn.classList.toggle("visible", window.scrollY > 300);
    }, { passive: true });

    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });

    /* ---------- 2. Scroll reveal animations ---------- */
    var revealTargets = [
      ".hero h1", ".hero-sub", ".hero-ctas", ".hero-meta", ".hero-image",
      ".page-hero .eyebrow", ".page-hero h1", ".page-hero p",
      ".section .center .eyebrow", ".section .center h2", ".section .center p",
      ".card", ".step", ".value", ".quote", ".stat",
      ".post-card", ".ci-item", ".form-card", ".cta-strip",
      ".split > div", ".img-ph", "details.faq-item"
    ];

    var seen = [];
    revealTargets.forEach(function (sel) {
      document.querySelectorAll(sel).forEach(function (el) {
        if (seen.indexOf(el) !== -1) return;
        seen.push(el);
        if (!el.hasAttribute("data-reveal")) el.setAttribute("data-reveal", "");
      });
    });

    /* stagger items that share a parent grid */
    document.querySelectorAll(".cards, .quotes, .process, .values, .stats, .blog-grid").forEach(function (grid) {
      Array.prototype.forEach.call(grid.children, function (child, i) {
        child.setAttribute("data-reveal", "");
        child.dataset.revealDelay = (i * 90);
      });
    });

    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          var delay = parseFloat(el.dataset.revealDelay || 0);
          setTimeout(function () { el.classList.add("revealed"); }, delay);
          io.unobserve(el);
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });

      document.querySelectorAll("[data-reveal]").forEach(function (el) { io.observe(el); });
    } else {
      document.querySelectorAll("[data-reveal]").forEach(function (el) { el.classList.add("revealed"); });
    }

    /* ---------- 3. Animated stat counters ---------- */
    function animateCount(el) {
      var text = el.textContent.trim();
      var m = text.match(/^(\D*)([\d,]*\.?\d+)(\D*)$/);
      if (!m) return;
      var prefix = m[1], numStr = m[2], suffix = m[3];
      var decimals = (numStr.split(".")[1] || "").length;
      var target = parseFloat(numStr.replace(/,/g, ""));
      var duration = 1500, start = performance.now();

      function fmt(v) {
        return prefix + v.toFixed(decimals).replace(/\B(?=(\d{3})+(?!\d))/g, ",") + suffix;
      }
      function step(now) {
        var p = Math.min((now - start) / duration, 1);
        var ease = 1 - Math.pow(1 - p, 3);
        el.textContent = fmt(target * ease);
        if (p < 1) { requestAnimationFrame(step); }
        else { el.textContent = fmt(target); }
      }
      el.textContent = fmt(0);
      requestAnimationFrame(step);
    }

    var counters = document.querySelectorAll(".stat-num");
    if (counters.length) {
      if ("IntersectionObserver" in window) {
        var ioCount = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (!entry.isIntersecting) return;
            animateCount(entry.target);
            ioCount.unobserve(entry.target);
          });
        }, { threshold: 0.5 });
        counters.forEach(function (el) { ioCount.observe(el); });
      } else {
        counters.forEach(animateCount);
      }
    }

  });
})();
