import os, re, glob

# Project root — this script lives in <project>/_dicf-shots, so the project is one level up.
# Override with the DICF_ROOT environment variable if the project ever moves elsewhere.
root = os.environ.get("DICF_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pat = re.compile(
    r'(?P<ind>[ ]*)<a class="brand" href="index\.html" aria-label="Daily In [Cc]hrist Fellowship, home">.*?</a>',
    re.S,
)


def repl(m):
    i = m.group("ind")
    return (
        f'{i}<a class="brand" href="index.html" aria-label="Daily in Christ Fellowship, home">\n'
        f'{i}  <span class="brand__mark" aria-hidden="true"></span>\n'
        f'{i}  <span class="brand__text">\n'
        f'{i}    <span class="brand__name">Daily in Christ Fellowship</span>\n'
        f'{i}    <span class="brand__tag">Quezon City</span>\n'
        f'{i}  </span>\n'
        f'{i}</a>'
    )


for p in sorted(glob.glob(os.path.join(root, "*.html"))):
    s = open(p, encoding="utf-8").read()
    before = s
    s, n = pat.subn(repl, s)
    s = s.replace(
        '<span class="brand__mark"><img src="assets/images/logo.png" alt="" width="46" height="46"></span>',
        "",
    )
    s = s.replace(
        '<span class="fb-card__avatar"><img src="assets/images/logo.png" alt="" width="44" height="44"></span>',
        '<span class="fb-card__avatar"><img src="assets/images/logo-mark.png" alt="" width="44" height="44"></span>',
    )
    if s != before:
        open(p, "w", encoding="utf-8", newline="").write(s)
        print(os.path.basename(p), "brand blocks:", n)
