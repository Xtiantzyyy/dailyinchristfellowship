/* ==========================================================================
   Daily In Christ Fellowship — interactions
   Vanilla JS, no dependencies.
   ========================================================================== */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------ sticky header state -- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 24);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ------------------------------------------------------- mobile menu -- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector("#primary-nav");

  function closeNav() {
    document.body.classList.remove("nav-open");
    if (toggle) toggle.setAttribute("aria-expanded", "false");
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) closeNav();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeNav();
    });
  }

  /* ----------------------------------------------------- scroll reveal -- */
  var revealEls = Array.prototype.slice.call(document.querySelectorAll(".reveal"));

  if (revealEls.length) {
    if (!("IntersectionObserver" in window) || reduceMotion) {
      revealEls.forEach(function (el) { el.classList.add("is-visible"); });
    } else {
      var revealObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
          }
        });
      }, { rootMargin: "0px 0px -12% 0px", threshold: 0.08 });
      revealEls.forEach(function (el) { revealObserver.observe(el); });
    }
  }

  /* -------------------------------------------------------- stat count -- */
  var stats = Array.prototype.slice.call(document.querySelectorAll("[data-count]"));

  function animateStat(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    if (isNaN(target)) return;
    if (reduceMotion) { el.textContent = target.toLocaleString() + suffix; return; }

    var duration = 1400;
    var start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString() + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  if (stats.length && "IntersectionObserver" in window) {
    var statObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateStat(entry.target);
          statObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    stats.forEach(function (el) { statObserver.observe(el); });
  }

  /* ------------------------------------------------------- video modal -- */
  var modal = document.querySelector("#video-modal");

  if (modal) {
    var modalFrame = modal.querySelector(".modal__frame");
    var modalNote = modal.querySelector(".modal__note");
    var lastFocus = null;

    function openModal(label) {
      lastFocus = document.activeElement;
      modal.classList.add("is-open");
      modal.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
      if (modalNote) {
        modalNote.textContent = label
          ? "“" + label + "” — the sermon video will be embedded here."
          : "The sermon video will be embedded here.";
      }
      var closeBtn = modal.querySelector(".modal__close");
      if (closeBtn) closeBtn.focus();
    }

    function closeModal() {
      modal.classList.remove("is-open");
      modal.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
      if (lastFocus) lastFocus.focus();
    }

    document.addEventListener("click", function (e) {
      var trigger = e.target.closest("[data-sermon]");
      if (trigger) {
        e.preventDefault();
        openModal(trigger.getAttribute("data-sermon"));
      }
      if (e.target.closest(".modal__close") || e.target.classList.contains("modal__backdrop")) {
        closeModal();
      }
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && modal.classList.contains("is-open")) closeModal();
    });
  }

  /* -------------------------------------------------- fake form submit -- */
  document.querySelectorAll("form[data-demo]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form__status");
      var ok = true;
      form.querySelectorAll("[required]").forEach(function (field) {
        if (!field.value.trim() || (field.type === "email" && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(field.value))) {
          ok = false;
          field.setAttribute("aria-invalid", "true");
          field.style.borderColor = "#B4463F";
        } else {
          field.removeAttribute("aria-invalid");
          field.style.borderColor = "";
        }
      });
      if (!ok) {
        if (status) {
          status.textContent = "Please check the highlighted fields and try again.";
          status.classList.add("is-visible");
        }
        return;
      }
      if (status) {
        status.textContent =
          "Thank you! Your message is ready to send — connect this form to your email service (see README) to receive it.";
        status.classList.add("is-visible");
      }
      form.reset();
      form.querySelectorAll("input, textarea, select").forEach(function (f) {
        f.style.borderColor = "";
        f.removeAttribute("aria-invalid");
      });
    });
  });

  /* ------------------------------------------------------ amount chips -- */
  document.querySelectorAll("[data-amounts]").forEach(function (group) {
    group.addEventListener("click", function (e) {
      var btn = e.target.closest(".amount");
      if (!btn) return;
      group.querySelectorAll(".amount").forEach(function (b) { b.classList.remove("is-active"); });
      btn.classList.add("is-active");
    });
  });

  /* ---------------------------------------------------- sermon filters -- */
  var filterBar = document.querySelector("[data-filters]");
  if (filterBar) {
    filterBar.addEventListener("click", function (e) {
      var chip = e.target.closest("[data-filter]");
      if (!chip) return;
      var value = chip.getAttribute("data-filter");
      filterBar.querySelectorAll("[data-filter]").forEach(function (c) {
        c.classList.toggle("is-active", c === chip);
      });
      document.querySelectorAll("[data-series]").forEach(function (item) {
        var series = item.getAttribute("data-series");
        item.hidden = !(value === "all" || series === value);
      });
    });
  }

  /* ------------------------------------------------- sprite-safe year -- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ------------------------------------------- section nav highlight -- */
  var jumpNav = document.querySelector("[data-jumplinks]");
  if (jumpNav && "IntersectionObserver" in window) {
    var targets = Array.prototype.slice.call(jumpNav.querySelectorAll("a")).map(function (a) {
      return document.querySelector(a.getAttribute("href"));
    }).filter(Boolean);

    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        jumpNav.querySelectorAll("a").forEach(function (a) {
          a.classList.toggle("is-active", a.getAttribute("href") === "#" + entry.target.id);
        });
      });
    }, { rootMargin: "-25% 0px -65% 0px" });

    targets.forEach(function (t) { spy.observe(t); });
  }
})();
