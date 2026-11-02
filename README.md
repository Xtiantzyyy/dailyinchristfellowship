# Daily in Christ Fellowship — Website

A complete church website in the colors taken from your logo, built around your tagline:
**“Sharing the Gospel, Sharing our Lives” — 1 Thess. 2:8.**

Pure HTML, CSS, and a little vanilla JavaScript — no build step, no framework, no dependencies.

---

## Open it

Double-click **index.html**, or drag it into any browser. Everything works offline
except the web fonts, which fall back to system serif/sans if there is no internet.

---

## Pages

| File | What it is |
|---|---|
| `index.html` | Home — hero with the tagline, service times, welcome, story, tagline section, ministries, sermons, events, Facebook pinned post, verse, giving CTA |
| `about.html` | About — story, what our name means, mission/values, statement of faith, how we are led, next steps |
| `ministries.html` | Eight ministries — Praise and Worship, Multimedia, Outreach & Missions, Kids for Christ (K4C), Young and Adult Fusion, Men in Bonding (MIB), Women of Worth (WOW), and Small Groups (cell groups) |
| `sermons.html` | Featured message, filterable archive, listening platforms |
| `events.html` | Weekly rhythm, upcoming events, volunteer sign-up, calendar links |
| `give.html` | Three ways to give, stewardship commitments, scripture, FAQ |
| `contact.html` | Address, phone, email, Facebook, contact form, map panel, first-visit guidance |

Every page shares the same header, navigation, and footer, and highlights the
current page in the menu automatically.

---

## The tagline

“Sharing the Gospel, Sharing our Lives” now appears in four places:

1. **Hero** — under the headline, with the `1 Thess. 2:8` reference in a pill.
2. **Home tagline section** — the two halves of the ministry, plus the full verse.
3. **About → “Our name”** — Daily / In Christ / Fellowship, tied back to 1 Thess. 2:8.
4. **Footer** — on every page, above the description.

To change the wording, search for `Sharing the Gospel` inside the HTML files.

---

## Your Facebook page

- Every Facebook link points to <https://www.facebook.com/DailyInChristFellowship>.
- Messenger buttons use <https://m.me/DailyInChristFellowship> — replace the username if the page handle ever changes.
- The home page has a **“From our Facebook page”** section with a pinned-post card
  (`<article class="fb-card">` in `index.html`). The card currently quotes the tagline.

### Updating the pinned post

Facebook blocks public reading of page posts from outside a logged-in session, so the
pinned post itself has **not** been copied into the site. Once you paste its text into
the card, it will read like an embedded post.

In `index.html`, find:

```html
<p class="fb-card__body">&ldquo;Sharing the Gospel, Sharing our Lives.&rdquo;</p>
<p class="fb-card__sub">Our announcements, prayer requests ...</p>
```

Replace the first paragraph with the headline of the pinned post and the second with the
body text. Keep both short — roughly 2 lines for the headline and 3 for the body.

---

## Brand palette (sampled from your logo)

| Color | Hex | Used for |
|---|---|---|
| Brand indigo | `#26255E` | Buttons, links, accents — the logo's deep blue |
| Deep navy | `#15143A` → `#0F0E2B` | Hero and footer gradients |
| Iris | `#7C79D6` | Eyebrows, small accents, hover states |
| Ivory | `#F5F6F9` | Alternating section backgrounds |
| Silver | `#DEDFE8` | Borders and dividers |
| White | `#FFFFFF` | Cards and surfaces |

All of these live as CSS variables at the top of `assets/css/styles.css` — change a
value there and the whole site updates.

---

## What is real and what is placeholder

**Confirmed with you:** the church name, the tagline and its verse, Quezon City, the weekly
rhythm — Sunday School 9:30 AM, Sunday AM Service 9:30 AM, Youth Service 2:30 PM, Midweek
Prayer Night on the 2nd and 4th Wednesday at 7:00 PM, and Night of Worship on the 3rd
Wednesday of every other month at 7:00 PM — the mission and vision statements, and the seven
core values: passionate spirituality, evangelism, discipleship, strong family, leadership
development, voluntary service, and excellence. All of it is used word for word on the home
page and on About, and the weekly rhythm drives the generated calendar.

**Sample content to replace** (written so the design can be judged, not as facts):

| Where | What to change |
|---|---|
| Contact + footer | Street address — only the city is filled in. Phone and email are confirmed and live |
| Sermons | Nine sample messages, their titles, dates and lengths |
| Events | Five one-off events (November–December 2026) in `assets/js/schedule.js` — the weekly services around them are generated from rules, not typed |
| Ministry photos | Eight banner photos in `assets/images/ministries/`, plus `church-members.jpg` for the story header |
| Staff | Leadership is described by role only (no names) — add names and photos when you are ready |
| Testimonies | Removed — add real member stories when you have them, with permission |

No founding year, member count, giving percentage, or staff name has been invented on
the live pages; those sections were rewritten so nothing false is published.

---

## What to edit first

1. **Service times** — the hero strip, footer (“Gatherings”), `contact.html`, and the
   generated calendar in `assets/js/schedule.js`.
2. **The upcoming calendar** — every Sunday service, prayer night, and Night of Worship is
   generated from rules in `assets/js/schedule.js` (see “The upcoming calendar” below).
3. **Street address** — `contact.html` and the footer of every page (phone and email are already filled in).
4. **Pinned post card** — see above.
5. **Sermons and one-off events** — sermons use `data-sermon` on `sermons.html`; one-off
   events are listed in `SPECIAL` inside `assets/js/schedule.js`.
6. **Instagram / YouTube links** — the footer icons currently point to `#`. Facebook and TikTok are live and confirmed.

---

## The upcoming calendar

The “Upcoming” lists on `index.html` and `events.html` are **generated, not typed by hand**,
so they never go stale. Everything lives at the top of `assets/js/schedule.js`:

```js
var RECURRING = [
  { title: "Sunday AM Service", time: "9:30 AM", hour: 9, minute: 30, weekday: 0 },
  { title: "Youth Service", time: "2:30 PM", hour: 14, minute: 30, weekday: 0 },
  { title: "Midweek Prayer Night", time: "7:00 PM", hour: 19, minute: 0,
    weekday: 3, weeks: [2, 4] },
  { title: "Night of Worship", time: "7:00 PM", hour: 19, minute: 0,
    weekday: 3, weeks: [3], months: "odd", note: "…" }
];
```

- `weekday` — `0` is Sunday, `1` Monday, `3` Wednesday … `6` Saturday.
- `weeks` — which weeks of the month it falls in (`[2, 4]` = second and fourth).
- `months` — `"odd"` or `"even"` to run every other month; leave it out to run monthly.
- `note` — an optional sentence shown under the time. Only Night of Worship has one, naming
  the Praise and Worship and Multimedia ministries.

One-off events sit in the `SPECIAL` array just below it. Each has an `id` that matches the
anchor on `events.html`, plus a date and time. **Once a date passes it drops off the list on
its own**, so nothing needs deleting.

How many entries each page shows is one attribute in the HTML: `data-schedule-limit="6"` on
the home page and `"14"` on the events page. With JavaScript off, the original hand-written
list stays on the page as a fallback.

---

## Replacing the logo

The logo is **embedded in the stylesheet**, not loaded as a file — so it can never
appear as an empty circle, even offline or in a preview that blocks images.
Three embedded copies live in assets/css/styles.css:

| Variable | Size | Where it appears |
|---|---|---|
| --logo-mark | 200×200 | Header, footer, Facebook card avatar |
| --logo-lg | 300×300 | Hero seal, About page seal |

Plus two files for the browser chrome:

| File | Size | Where it appears |
|---|---|---|
| favicon.png | 64×64 (navy badge) | Browser tab |
| logo-192.png | 192×192 (navy badge) | Phone home-screen icon |

logo.png and logo-mark.png are still in assets/images/ — they are the source
files used to build the embedded copies and the icons.

**If you change the artwork:**

1. Save the new emblem as a square PNG (at least 300×300).
2. Base64-encode it and swap the string after data:image/png;base64, in the
   --logo-mark / --logo-lg rules in assets/css/styles.css.
3. Regenerate favicon.png and logo-192.png from the new artwork.

---

## Connecting the contact form

The form validates and shows a friendly confirmation, but does not send anywhere yet.
Choose one:

- **Formspree** — set `<form class="form" action="https://formspree.io/f/YOUR_ID" method="POST">` and delete the `data-demo` attribute.
- **Netlify Forms** — add `netlify` and `name="contact"` to the `<form>` tag, then deploy to Netlify.
- **Your own endpoint** — point `action` at it and remove `data-demo`.

Without `data-demo`, the browser submits the form normally.

---

## Adding a real map

On `contact.html`, replace the decorative `<div class="map"> … </div>` with a Google Maps embed:

```html
<iframe
  src="https://www.google.com/maps/embed?pb=YOUR_EMBED_CODE"
  width="100%" height="380" style="border:0;border-radius:26px"
  loading="lazy" referrerpolicy="no-referrer-when-downgrade"
  title="Map to Daily in Christ Fellowship"></iframe>
```

Get the embed code from Google Maps → Share → Embed a map.

---

## Sermon videos

Play buttons open a lightbox showing a placeholder note. Easiest path: link each play
button straight to the video and delete `data-sermon`. To embed instead, inject your
iframe into `.modal__frame` inside `openModal()` in `assets/js/main.js`.

---

## Giving

All three mailto links on the site (general, finance, media) point to the one church address, `dailyinchristfellowship1999@gmail.com` — split them if you set up separate inboxes.

Giving is deliberately **in person, or by mail and bank transfer only** — there is no online
giving form on the site. The two cards live in `give.html`:

- **In person** — offering boxes at the rear of the sanctuary during the Sunday service.
- **By mail or transfer** — checks payable to the church, posted to the office; bank
  transfer details are sent on request.

The card beside the giving breakdown is **Mission Pledges** — it explains that the fund is
used for upcoming mission trips. Update that copy in `give.html` as trips are added.

---

## Structure

```
Daily in Christ Fellowship/
├── index.html
├── about.html
├── ministries.html
├── sermons.html
├── events.html
├── give.html
├── contact.html
├── assets/
│   ├── css/styles.css      ← all styling, color tokens at the top
│   ├── js/main.js          ← nav, scroll effects, filters, form, lightbox
│   ├── js/schedule.js      ← generates the upcoming calendar from weekly rules
│   └── images/             ← logo, favicon, app icon, ministry banner photos
├── _dicf-shots/            ← build screenshots and one-off patch scripts (not part of the site)
├── _ministries-banner/     ← the original ministry photos you supplied (source files)
└── README.md
```

---

## Publishing

Any static host works — nothing needs compiling:

- **GitHub Pages** — push the folder, enable Pages on the branch
- **Netlify / Vercel** — drag the folder into the dashboard
- **Your existing host** — upload via FTP to `public_html`

---

## Good to know

- **Responsive** — tested from 390 px phones up to large desktops; the mobile menu is a full-height panel.
- **Accessible** — semantic landmarks, skip link, focus rings, labelled form fields,
  `aria-current` on the active nav item, reduced-motion support, and print styles.
- **Fast** — one CSS file, one small JS file, two Google Fonts families, no libraries.
- **Fonts** — Playfair Display (headings) + Inter (body), loaded from Google Fonts with
  graceful system fallbacks.
