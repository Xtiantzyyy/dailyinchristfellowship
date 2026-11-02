import os, re

# Project root — this script lives in <project>/_dicf-shots, so the project is one level up.
# Override with the DICF_ROOT environment variable if the project ever moves elsewhere.
ROOT = os.environ.get("DICF_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(f):
    return open(os.path.join(ROOT, f), encoding="utf-8").read()


def write(f, s):
    open(os.path.join(ROOT, f), "w", encoding="utf-8", newline="").write(s)


def sub(f, pairs):
    s = read(f)
    for a, b in pairs:
        if a not in s:
            print("  MISS", f, "->", a[:70])
        s = s.replace(a, b)
    write(f, s)


FOOTER_OLD = (
    '<div><span>Sunday worship</span><span>9:00 &amp; 11:00 AM</span></div>\n'
    '          <div><span>Wednesday prayer</span><span>7:00 PM</span></div>\n'
    '          <div><span>Friday youth</span><span>6:30 PM</span></div>'
)
FOOTER_NEW = (
    '<div><span>Sunday School</span><span>9:30 AM</span></div>\n'
    '          <div><span>Sunday service</span><span>9:30 AM</span></div>\n'
    '          <div><span>Youth service</span><span>2:30 PM</span></div>\n'
    '          <div><span>Prayer night</span><span>2nd/4th Wed 7 PM</span></div>'
)

# ---------------------------------------------------------------- footer ----
for f in ["index.html", "about.html", "ministries.html", "sermons.html",
          "events.html", "give.html", "contact.html"]:
    s = read(f)
    if FOOTER_OLD in s:
        s = s.replace(FOOTER_OLD, FOOTER_NEW)
        write(f, s)
        print("footer updated:", f)
    else:
        print("footer pattern not found in", f)

# ----------------------------------------------------------------- index ----
sub("index.html", [
    ("Join us Sundays at 9:00 &amp; 11:00 AM.", "Join us Sundays at 9:30 AM."),
    ('<span><strong>Sunday</strong> · 9:00 &amp; 11:00 AM</span>',
     '<span><strong>Sunday</strong> · 9:30 AM</span>'),
    ('<strong>Next gathering</strong>Sunday · 9:00 AM',
     '<strong>Next gathering</strong>Sunday · 9:30 AM'),
    ("during both Sunday gatherings", "during the Sunday service"),
    ("Doors open at 8:30 AM.", "Doors open at 9:00 AM."),
    ("Grades 7–12 gathering every Friday for worship, honest conversation, and real friendship.",
     "Grades 7–12 gathering Sunday afternoons at 2:30 PM for worship, honest conversation, and real friendship."),
    ("Wednesday nights, early-morning intercession, and a team ready to pray with you this week.",
     "Midweek Prayer Night on the 2nd and 4th Wednesday, and a team ready to pray with you this week."),
])

# hero service strip -> four real gatherings
hero_new = '''<div class="hero__services">
        <div class="service-card">
          <span class="service-card__icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v18M7 8h10"/></svg>
          </span>
          <div>
            <p class="service-card__day">Sunday</p>
            <p class="service-card__title">Sunday AM Service</p>
            <p class="service-card__note">9:30 AM · Main Sanctuary</p>
          </div>
        </div>
        <div class="service-card">
          <span class="service-card__icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 6.5C10 5 7 4.5 3.5 5v13c3.5-.5 6.5 0 8.5 1.5 2-1.5 5-2 8.5-1.5V5C17 4.5 14 5 12 6.5Z"/><path d="M12 6.5v13"/></svg>
          </span>
          <div>
            <p class="service-card__day">Sunday</p>
            <p class="service-card__title">Sunday School</p>
            <p class="service-card__note">9:30 AM · Classes for all ages</p>
          </div>
        </div>
        <div class="service-card">
          <span class="service-card__icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3s5 4.2 5 9a5 5 0 0 1-10 0c0-2 1-3.4 2-4.6.4 2 1.2 3 2.4 3.6C12.6 9 12 6 12 3Z"/></svg>
          </span>
          <div>
            <p class="service-card__day">Sunday</p>
            <p class="service-card__title">Youth Service</p>
            <p class="service-card__note">2:30 PM · The Loft</p>
          </div>
        </div>
        <div class="service-card">
          <span class="service-card__icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v3M5.5 8.5l2 2M18.5 8.5l-2 2M3 18h18"/><path d="M6 18a6 6 0 0 1 12 0"/></svg>
          </span>
          <div>
            <p class="service-card__day">Wednesday</p>
            <p class="service-card__title">Midweek Prayer Night</p>
            <p class="service-card__note">2nd &amp; 4th Wednesday · 7:00 PM</p>
          </div>
        </div>
      </div>'''

s = read("index.html")
m = re.search(r'<div class="hero__services">.*?\n      </div>', s, re.S)
if m:
    s = s[:m.start()] + hero_new + s[m.end():]
    write("index.html", s)
    print("hero services replaced")
else:
    print("hero services NOT found")

# ---------------------------------------------------------------- events ----
events_cards = '''<div class="grid grid--4">
        <article class="card card--stack reveal">
          <p class="eyebrow" style="margin-bottom:12px">Sunday</p>
          <h3>Sunday AM Service</h3>
          <p>9:30 AM<br>Main Sanctuary &amp; livestream</p>
          <p style="margin-top:14px; font-size:.85rem; color:var(--muted)">Sunday School for all ages at 9:30 AM.</p>
        </article>
        <article class="card card--stack reveal" style="--delay:70ms">
          <p class="eyebrow" style="margin-bottom:12px">Sunday</p>
          <h3>Youth Service</h3>
          <p>2:30 PM<br>The Loft</p>
          <p style="margin-top:14px; font-size:.85rem; color:var(--muted)">Grades 7–12 and young adults.</p>
        </article>
        <article class="card card--stack reveal" style="--delay:140ms">
          <p class="eyebrow" style="margin-bottom:12px">2nd &amp; 4th Wednesday</p>
          <h3>Midweek Prayer Night</h3>
          <p>7:00 PM<br>Prayer Chapel</p>
          <p style="margin-top:14px; font-size:.85rem; color:var(--muted)">One hour of unhurried prayer.</p>
        </article>
        <article class="card card--stack reveal" style="--delay:210ms">
          <p class="eyebrow" style="margin-bottom:12px">Small groups</p>
          <h3>Weekday Groups</h3>
          <p>In homes across the city<br>Times vary</p>
          <p style="margin-top:14px; font-size:.85rem; color:var(--muted)">Ask us for a group near you.</p>
        </article>
      </div>'''

s = read("events.html")
start = s.find('<div class="grid grid--3">')
end = s.find('\n      </div>', start)
if start > 0 and end > start:
    s = s[:start] + events_cards + s[end + len('\n      </div>'):]
    write("events.html", s)
    print("events weekly cards replaced")
else:
    print("events cards NOT found")

sub("events.html", [("<span>11:00 AM</span>", "<span>9:30 AM</span>")])

# --------------------------------------------------------------- sermons ----
sub("sermons.html", [
    ("livestreamed at 11:00 AM every Sunday", "livestreamed at 9:30 AM every Sunday"),
    ("<p>9:00 &amp; 11:00 AM. Coffee from 8:30. Bring your questions.</p>",
     "<p>9:30 AM. Coffee from 9:00. Bring your questions.</p>"),
])

# ----------------------------------------------------------------- about ----
sub("about.html", [
    ("Coffee from 8:30, a seat with your name on it", "Coffee from 9:00, a seat with your name on it"),
    ("Join us this Sunday at 9:00 or 11:00 AM.", "Join us this Sunday at 9:30 AM."),
])

# ------------------------------------------------------------- ministries ----
sub("ministries.html", [
    ("Nursery (0–3), Preschool (4–5), and Kids Church (Grades 1–6) run during both Sunday gatherings.",
     "Nursery (0–3), Preschool (4–5), and Kids Church (Grades 1–6) run during the Sunday service."),
    ("<p class=\"mini-meta\">Sundays · 9:00 &amp; 11:00 AM · Kids Wing</p>",
     "<p class=\"mini-meta\">Sundays · 9:30 AM · Sunday School &amp; Kids Church</p>"),
    ("Grades 7–12 meet Friday nights for worship, teaching, and small groups — plus summer camp, mission trips, and a lot of shared meals.",
     "Grades 7–12 meet Sunday afternoons for worship, teaching, and small groups — plus summer camp, mission trips, and a lot of shared meals."),
    ("<p class=\"mini-meta\">Fridays · 6:30 PM · The Loft</p>",
     "<p class=\"mini-meta\">Sundays · 2:30 PM · The Loft</p>"),
    ("<p class=\"mini-meta\">1st &amp; 3rd Thursday · 7:00 PM</p>",
     "<p class=\"mini-meta\">Meeting times on request</p>"),
    ("Bible study, prayer, and honest friendship — Tuesday mornings with childcare, and an evening circle for those who work.",
     "Bible study, prayer, and honest friendship — a morning study with childcare, and an evening circle for those who work."),
    ("<p class=\"mini-meta\">Tuesdays · 9:30 AM &amp; 7:00 PM</p>",
     "<p class=\"mini-meta\">Meeting times on request</p>"),
    ("Saturday breakfasts, a study through the gospels, and practical service projects around the city. Come hungry; leave known.",
     "Breakfast gatherings, a study through the gospels, and practical service projects around the city. Come hungry; leave known."),
    ("<p class=\"mini-meta\">Saturdays · 7:30 AM</p>",
     "<p class=\"mini-meta\">Meeting times on request</p>"),
    ("<p class=\"mini-meta\">Rehearsals Thursdays · 7:30 PM</p>",
     "<p class=\"mini-meta\">Rehearsal times on request</p>"),
    ("<p class=\"mini-meta\">Serving Saturdays · 8:00 AM</p>",
     "<p class=\"mini-meta\">Serving days posted monthly</p>"),
    ("Wednesday corporate prayer, a 6:00 AM intercession call on Fridays, and a team available after every service to pray with you.",
     "Midweek Prayer Night on the 2nd and 4th Wednesday, and a team available after every service to pray with you."),
    ("<p class=\"mini-meta\">Wednesdays · 7:00 PM · Prayer Chapel</p>",
     "<p class=\"mini-meta\">2nd &amp; 4th Wednesdays · 7:00 PM · Prayer Chapel</p>"),
])

# ------------------------------------------------------------------ give ----
sub("give.html", [
    ("Offering boxes are at the rear of the sanctuary during both Sunday gatherings.",
     "Offering boxes are at the rear of the sanctuary during our Sunday service."),
])

# --------------------------------------------------------------- contact ----
sub("contact.html", [
    ("<h3>Arrive from 8:30</h3>", "<h3>Arrive from 9:00</h3>"),
    ("Doors open thirty minutes before each service.",
     "Doors open at 9:00, thirty minutes before the service."),
])

print("done")
