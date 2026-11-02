/* Daily in Christ Fellowship — upcoming calendar
   ---------------------------------------------------------------------------
   The list of upcoming dates is generated from the rules below, so it never
   goes stale. To change the rhythm of the church, edit RECURRING. To add a
   one-off event, add it to SPECIAL — events drop off the list automatically
   once their date has passed.

   weekday: 0 = Sunday, 1 = Monday, 3 = Wednesday … 6 = Saturday
   weeks:   which weeks of the month the event falls in (1 = first week)
   months:  "odd" or "even" to run every other month, otherwise omit
   --------------------------------------------------------------------------- */
(function () {
  "use strict";

  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  var DOW = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  var HORIZON_DAYS = 200;
  var ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"' +
    ' stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
    '<path d="M9 6l6 6-6 6"/></svg>';

  /* --------------------------------------------------------- recurring ---- */
  var RECURRING = [
    { title: "Sunday AM Service", time: "9:30 AM", hour: 9, minute: 30, weekday: 0 },
    { title: "Youth Service", time: "2:30 PM", hour: 14, minute: 30, weekday: 0 },
    { title: "Midweek Prayer Night", time: "7:00 PM", hour: 19, minute: 0,
      weekday: 3, weeks: [2, 4] },
    { title: "Night of Worship", time: "7:00 PM", hour: 19, minute: 0,
      weekday: 3, weeks: [3], months: "odd",
      note: "Led by the Praise and Worship team, with the Multimedia ministry " +
            "running sound, lyrics, and the livestream." }
  ];

  /* ------------------------------------------------------------- one-off -- */
  var SPECIAL = [
    { id: "baptism", title: "Water Baptism Sunday", date: "2026-11-22",
      time: "9:30 AM", hour: 9, minute: 30 },
    { id: "members", title: "Quarterly Members' Meeting", date: "2026-11-29",
      time: "1:00 PM", hour: 13, minute: 0 },
    { id: "carols", title: "Christmas Carol Service", date: "2026-12-06",
      time: "6:00 PM", hour: 18, minute: 0 },
    { id: "camp", title: "Youth Winter Camp", date: "2026-12-12",
      time: "12-14 December", hour: 9, minute: 0 },
    { id: "eve", title: "Christmas Eve Candlelight Service", date: "2026-12-24",
      time: "8:00 PM", hour: 20, minute: 0 }
  ];

  /* ------------------------------------------------------------ helpers --- */
  function weekOfMonth(d) {
    return Math.floor((d.getDate() - 1) / 7) + 1;
  }

  function pad(n) {
    return n < 10 ? "0" + n : "" + n;
  }

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function matchesRule(rule, d) {
    if (d.getDay() !== rule.weekday) return false;
    if (rule.weeks && rule.weeks.indexOf(weekOfMonth(d)) === -1) return false;
    var month = d.getMonth() + 1;
    if (rule.months === "odd" && month % 2 === 0) return false;
    if (rule.months === "even" && month % 2 === 1) return false;
    return true;
  }

  function collect(now) {
    var items = [];
    var i, j;

    for (i = 0; i <= HORIZON_DAYS; i++) {
      var d = new Date(now.getFullYear(), now.getMonth(), now.getDate() + i);
      for (j = 0; j < RECURRING.length; j++) {
        var rule = RECURRING[j];
        if (!matchesRule(rule, d)) continue;
        var when = new Date(d.getFullYear(), d.getMonth(), d.getDate(), rule.hour, rule.minute);
        if (when.getTime() < now.getTime()) continue;   /* already started today */
        items.push({ when: when, title: rule.title, time: rule.time,
                     note: rule.note || "", id: "" });
      }
    }

    for (i = 0; i < SPECIAL.length; i++) {
      var s = SPECIAL[i];
      var p = s.date.split("-");
      var at = new Date(+p[0], +p[1] - 1, +p[2], s.hour || 0, s.minute || 0);
      if (at.getTime() < now.getTime()) continue;       /* past events drop off */
      items.push({ when: at, title: s.title, time: s.time,
                   note: s.note || "", id: s.id });
    }

    items.sort(function (a, b) { return a.when - b.when; });
    return items;
  }

  function rowFor(item) {
    var onThisPage = item.id && document.getElementById(item.id);
    var tag = item.id ? "a" : "div";
    var el = document.createElement(tag);
    el.className = "event-row" + (item.id ? "" : " event-row--plain");
    if (item.id) {
      el.id = item.id;
      el.setAttribute("href", onThisPage ? "#" + item.id : "events.html#" + item.id);
    }
    var d = item.when;
    el.innerHTML =
      '<span class="event-date">' +
        '<span class="event-date__month">' + MONTHS[d.getMonth()] + '</span>' +
        '<span class="event-date__day">' + pad(d.getDate()) + '</span>' +
        '<span class="event-date__dow">' + DOW[d.getDay()] + '</span>' +
      '</span>' +
      '<span>' +
        '<span class="event-row__title">' + esc(item.title) + '</span>' +
        '<span class="event-row__meta"><span>' + esc(item.time) + '</span></span>' +
        (item.note ? '<span class="event-row__note">' + esc(item.note) + '</span>' : '') +
      '</span>' +
      (item.id ? '<span class="event-row__cta">' + ARROW + '</span>' : '');
    return el;
  }

  /* --------------------------------------------------------------- render -- */
  function render() {
    var targets = document.querySelectorAll("[data-schedule]");
    if (!targets.length) return;

    var now = new Date();
    var items = collect(now);
    var i, j;

    for (i = 0; i < targets.length; i++) {
      var box = targets[i];
      var limit = parseInt(box.getAttribute("data-schedule-limit") || "8", 10);
      box.innerHTML = "";
      for (j = 0; j < items.length && j < limit; j++) {
        box.appendChild(rowFor(items[j]));
      }
    }

    /* keep deep links into the events page working after the list is rebuilt */
    if (location.hash.length > 1) {
      var target = document.getElementById(location.hash.slice(1));
      if (target && target.classList.contains("event-row")) {
        target.scrollIntoView({ block: "center" });
      }
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render);
  } else {
    render();
  }
})();
