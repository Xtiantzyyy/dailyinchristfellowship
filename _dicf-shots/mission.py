import os, re

# Project root — this script lives in <project>/_dicf-shots, so the project is one level up.
# Override with the DICF_ROOT environment variable if the project ever moves elsewhere.
ROOT = os.environ.get("DICF_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MISSION = ("To worship the living God as our highest service; commission every member to disciple "
           "the fruits of evangelism, commits to study the Word and to pray; and to establish cell "
           "groups in various locations.")
VISION = ("We will win souls and make disciples by sharing the Gospel through evangelism, sharing "
          "the transformed lives through discipleship, and ultimately train Spirit-filled leaders.")

# ------------------------------------------------------------------ index ----
p = f"{ROOT}/index.html"
s = open(p, encoding="utf-8").read()

s = s.replace(
    '<p class="eyebrow">Our name &amp; our mission</p>',
    '<p class="eyebrow">Our mission &amp; vision</p>',
)
s = s.replace(
    '<p class="lead">Two halves of one calling. We do not only hand people words about Jesus — '
    'we open our homes, our tables, and our lives beside them. That is the pattern Paul described, '
    'and it is the pattern we are still learning.</p>',
    '<p class="lead">Our name is a promise. Our mission and vision are how we keep it — in worship, '
    'in discipleship, and in cell groups across the city.</p>',
)

start = s.index('<div class="grid grid--2" style="max-width:920px; margin:0 auto">')
end = s.index('<figure class="tagline-verse reveal">')
new_block = f'''<div class="grid grid--2" style="max-width:980px; margin:0 auto">
        <article class="pillar reveal">
          <div class="icon-box">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v18M7 8h10"/></svg>
          </div>
          <h3>Our mission</h3>
          <p>{MISSION}</p>
        </article>

        <article class="pillar reveal" style="--delay:80ms">
          <div class="icon-box">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"/></svg>
          </div>
          <h3>Our vision</h3>
          <p>{VISION}</p>
        </article>
      </div>

      '''
s = s[:start] + new_block + s[end:]
open(p, "w", encoding="utf-8", newline="").write(s)
print("index mission/vision replaced")

# ------------------------------------------------------------------ about ----
p = f"{ROOT}/about.html"
s = open(p, encoding="utf-8").read()

old_start = s.index('<section class="section" aria-labelledby="mission-title">')
old_end = s.index("</section>", old_start) + len("</section>")
new_section = f'''<section class="section" aria-labelledby="mission-title">
    <div class="wrap">
      <div class="section-head section-head--center reveal">
        <p class="eyebrow">Mission &amp; vision</p>
        <h2 id="mission-title">Why we exist</h2>
        <p class="lead">Two statements, one direction — worship, evangelism, discipleship, and leaders raised up in cell groups across the city.</p>
      </div>
      <div class="grid grid--2">
        <article class="card reveal">
          <div class="icon-box">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v18M7 8h10"/></svg>
          </div>
          <h3>Our mission</h3>
          <p>{MISSION}</p>
        </article>
        <article class="card reveal" style="--delay:80ms">
          <div class="icon-box">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 0 18M12 3a15 15 0 0 0 0 18"/></svg>
          </div>
          <h3>Our vision</h3>
          <p>{VISION}</p>
        </article>
      </div>
    </div>
  </section>'''
s = s[:old_start] + new_section + s[old_end:]
open(p, "w", encoding="utf-8", newline="").write(s)
print("about mission/vision replaced")
