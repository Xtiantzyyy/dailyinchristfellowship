import os

# Project root — this script lives in <project>/_dicf-shots, so the project is one level up.
# Override with the DICF_ROOT environment variable if the project ever moves elsewhere.
ROOT = os.environ.get("DICF_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(ROOT, "contact.html")
lines = open(p, encoding="utf-8").read().split("\n")

# lines 81..97 (1-based) hold the mangled block; replace with two clean list items
start, end = 80, 97  # 0-based slice [80:97] == lines 81..97

new_block = '''          <li>
            <span class="info-list__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 11h18"/></svg></span>
            <div>
              <p class="info-list__label">Service times</p>
              <p class="info-list__value">Sunday School &amp; AM Service 9:30 AM · Youth 2:30 PM<br>Prayer Night · 2nd &amp; 4th Wednesday, 7:00 PM</p>
            </div>
          </li>
          <li>
            <span class="info-list__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6.5 3.5h3l1.5 4-2 1.5a11 11 0 0 0 5 5l1.5-2 4 1.5v3a2 2 0 0 1-2 2A16 16 0 0 1 4.5 5.5a2 2 0 0 1 2-2Z"/></svg></span>
            <div>
              <p class="info-list__label">Phone</p>
              <p class="info-list__value"><a href="tel:+639170000000">+63 917 000 0000</a></p>
            </div>
          </li>'''.split("\n")

assert "<li>" in lines[start + 3], lines[start:start + 4]
print("replacing:", lines[start].strip()[:40], "->", lines[end - 1].strip())

lines[start:end] = new_block
open(p, "w", encoding="utf-8", newline="").write("\n".join(lines))
print("fixed")
