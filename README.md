# Daily in Christ Fellowship — Website

A complete church website in the colours taken from your logo, built around your tagline:
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
| `ministries.html` | Eight ministries with meeting times, serving opportunities, small groups |
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

| Colour | Hex | Used for |
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
Prayer Night on the 2nd and 4th Wednesday at 7:00 PM — and the mission and vision statements
(used word for word on the home page and on About).

**Sample content to replace** (written so the design can be judged, not as facts):

| Where | What to change |
|---|---|
| Contact + footer | Street address (city only is filled in), phone `+63 917 000 0000`, email `hello@dailyinchrist.org` |
| Sermons | Nine sample messages, their titles, dates and lengths |
| Events | Six sample events, November–December 2026 |
| Staff | Leadership is described by role only (no names) — add names and photos when you are ready |
| Testimonies | Removed — add real member stories when you have them, with permission |

No founding year, member count, giving percentage, or staff name has been invented on
the live pages; those sections were rewritten so nothing false is published.

---

## What to edit first

1. **Service times** — hero strip, footer (“Gatherings”), `contact.html`, `events.html`.
2. **Address, phone, email** — `contact.html` and the footer of every page.
3. **Pinned post card** — see above.
4. **Sermons and events** — sample entries with `data-sermon` and event rows.
5. **Instagram / YouTube links** — the footer icons currently point to `#`.

---

## Replacing the logo

The logo is **embedded in the stylesheet**, not loaded as a file — so it can never
appear as an empty circle, even offline or in a preview that blocks images.
Three embedded copies live in ssets/css/styles.css:

| Variable | Size | Where it appears |
|---|---|---|
| --logo-mark | 200×200 | Header, footer, Facebook card avatar |
| --logo-lg | 300×300 | Hero seal, About page seal |

Plus two files for the browser chrome:

| File | Size | Where it appears |
|---|---|---|
| avicon.png | 64×64 (navy badge) | Browser tab |
| logo-192.png | 192×192 (navy badge) | Phone home-screen icon |

logo.png and logo-mark.png are still in ssets/images/ — they are the source
files used to build the embedded copies and the icons.

**If you change the artwork:**

1. Save the new emblem as a square PNG (at least 300×300).
2. Base64-encode it and swap the string after data:image/png;base64, in the
   --logo-mark / --logo-lg rules in ssets/css/styles.css.
3. Regenerate avicon.png and logo-192.png from the new artwork.

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

“Give online” currently points to `#`. Replace it with your processor's link
(Tithe.ly, Pushpay, Stripe, PayPal, Givelify, or your bank's giving page) in
`give.html` — and update the matching button on the home page CTA if desired.

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
│   ├── css/styles.css      ← all styling, colour tokens at the top
│   ├── js/main.js          ← nav, scroll effects, filters, form, lightbox
│   └── images/             ← logo, favicon, app icon
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
