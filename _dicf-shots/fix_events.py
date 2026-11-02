import re, os

# Project root — this script lives in <project>/_dicf-shots, so the project is one level up.
# Override with the DICF_ROOT environment variable if the project ever moves elsewhere.
ROOT = os.environ.get("DICF_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(ROOT, "events.html")
s = open(p, encoding="utf-8").read()

new = '''<div class="grid grid--3">
        <article class="card card--stack reveal">
          <p class="eyebrow" style="margin-bottom:12px">Sunday</p>
          <h3>Sunday Gatherings</h3>
          <p>AM Service · 9:30 AM<br>Sunday School · 9:30 AM<br>Youth Service · 2:30 PM</p>
          <p style="margin-top:14px; font-size:.85rem; color:var(--muted)">Main Sanctuary &amp; livestream.</p>
        </article>
        <article class="card card--stack reveal" style="--delay:70ms">
          <p class="eyebrow" style="margin-bottom:12px">2nd &amp; 4th Wednesday</p>
          <h3>Midweek Prayer Night</h3>
          <p>7:00 PM<br>Prayer Chapel</p>
          <p style="margin-top:14px; font-size:.85rem; color:var(--muted)">One hour of unhurried prayer.</p>
        </article>
        <article class="card card--stack reveal" style="--delay:140ms">
          <p class="eyebrow" style="margin-bottom:12px">Small groups</p>
          <h3>Weekday Groups</h3>
          <p>In homes across the city<br>Times vary</p>
          <p style="margin-top:14px; font-size:.85rem; color:var(--muted)">Ask us for a group near you.</p>
        </article>
      </div>'''

start = s.find('<div class="grid grid--4">')
end = s.find("\n      </div>", start)
assert start > 0 and end > start, "block not found"
s = s[:start] + new + s[end + len("\n      </div>"):]
open(p, "w", encoding="utf-8", newline="").write(s)
print("events cards rebuilt (3 columns)")
