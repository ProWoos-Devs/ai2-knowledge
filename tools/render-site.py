#!/usr/bin/env python3
"""Write the catalog's web page, _site/index.html, from catalog/community.yml
and catalog/categories.yml.

The page is for people who do not read YAML or use GitHub: a teacher, a
volunteer preparing donated laptops, a reviewer. It is generated, never edited
by hand, so it always says what the catalog says. The pages workflow runs this
script and publishes the result on every change to main.

One self-contained file: no fonts, scripts or images from elsewhere, so it can
be saved and opened on a machine with no connection.

  python3 tools/render-site.py            write _site/index.html
  python3 tools/render-site.py OUT_DIR    write OUT_DIR/index.html
"""
import html
import os
import sys

import yaml

REPO = "https://github.com/ProWoos-Devs/ai2-knowledge"
AI2 = "https://github.com/ProWoos-Devs/ai-2"
LANGUAGES = {"en": "English", "es": "Spanish", "de": "German", "fr": "French", "pt": "Portuguese", "pl": "Polish"}


def e(text) -> str:
    return html.escape(str(text), quote=True)


def size(n: int) -> str:
    return f"{n / 1_048_576:.1f} MB" if n >= 1_048_576 else f"{max(1, n // 1024)} KB"


def card(p: dict, names: dict, ages: dict) -> str:
    cats = [str(c) for c in p.get("categories") or []]
    subjects = ", ".join(names.get(c, c) for c in cats)
    who = "Everyone"
    if p.get("audience") == "children":
        who = "Children: " + "; ".join(ages.get(a, a) for a in p.get("ages") or [])
    langs = ", ".join(LANGUAGES.get(l, l) for l in p["languages"])
    recipe = f'<a href="{REPO}/tree/main/recipes/{e(p["id"])}">How it was made</a>' if os.path.isdir(f"recipes/{p['id']}") else ""
    search = " ".join([p["id"], p["title"], p.get("description") or "", subjects, who, langs, p["contact"]]).lower()
    return f"""<article class="pack" data-search="{e(search)}" data-lang="{e(' '.join(p['languages']))}" data-audience="{e(p.get('audience') or 'general')}">
<h3>{e(p['title'])}</h3>
<p class="desc">{e(p.get('description') or '')}</p>
<dl>
<dt>Subject</dt><dd>{e(subjects)}</dd>
<dt>For</dt><dd>{e(who)}</dd>
<dt>Language</dt><dd>{e(langs)}</dd>
<dt>Made by</dt><dd><a href="https://github.com/{e(p['contact'])}">{e(p['contact'])}</a></dd>
<dt>Version</dt><dd>{e(p['version'])}, revision {e(p.get('revision', 1))}</dd>
<dt>Contents</dt><dd>{e(p['documents'])} documents, {e(size(int(p['size_bytes'])))}</dd>
<dt>License</dt><dd>{e(p['license'])}</dd>
</dl>
<p class="install">On AI-2: <code>ai-2 knowledge install {e(p['id'])}</code></p>
<p class="links"><a href="{e(p['url'])}">Download the file</a>{' · ' + recipe if recipe else ''}</p>
</article>"""


def page(packs: list, cats: list, ages_list: list) -> str:
    names = {str(c["code"]): str(c["en"]) for c in cats}
    ages = {a["id"]: a["en"] for a in ages_list}
    groups: dict[str, list] = {}
    for p in sorted(packs, key=lambda p: (str((p.get("categories") or [""])[0]), p["title"].lower())):
        top = str((p.get("categories") or [""])[0]).split(".")[0]
        groups.setdefault(top, []).append(p)
    sections = "\n".join(
        f'<section class="group"><h2>{e(names.get(top, top))}</h2>\n<div class="grid">\n'
        + "\n".join(card(p, names, ages) for p in items) + "\n</div></section>"
        for top, items in sorted(groups.items()))
    langs = sorted({l for p in packs for l in p["languages"]})
    lang_opts = "".join(f'<option value="{e(l)}">{e(LANGUAGES.get(l, l))}</option>' for l in langs)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI-2 Knowledge Packs</title>
<meta name="description" content="Knowledge Packs that an AI-2 computer searches with no Internet: what each one covers, who made it, and how to install it.">
<style>
:root {{ --bg:#f7f8f6; --card:#ffffff; --text:#1d231f; --muted:#56605a; --line:#d8ddd9; --accent:#1f7a45; --code:#eef2ef; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#111513; --card:#1a201c; --text:#e6ebe7; --muted:#a3ada6; --line:#2e3631; --accent:#5fd08c; --code:#232a26; }} }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--text); font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; }}
main, header, footer {{ max-width:1100px; margin:0 auto; padding:0 16px; }}
header {{ padding-top:40px; }}
h1 {{ font-size:2rem; margin:0 0 8px; }}
h2 {{ font-size:1.25rem; margin:36px 0 12px; border-bottom:1px solid var(--line); padding-bottom:6px; }}
h3 {{ font-size:1.1rem; margin:0 0 6px; }}
a {{ color:var(--accent); }}
.lead {{ font-size:1.1rem; max-width:760px; }}
.muted {{ color:var(--muted); }}
code {{ background:var(--code); padding:2px 6px; border-radius:4px; font-size:.92em; overflow-wrap:anywhere; }}
.filters {{ display:flex; flex-wrap:wrap; gap:12px; margin:24px 0 0; }}
.filters input, .filters select {{ font:inherit; padding:8px 10px; border:1px solid var(--line); border-radius:6px; background:var(--card); color:var(--text); }}
.filters input {{ flex:1 1 260px; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:16px; }}
.pack {{ background:var(--card); border:1px solid var(--line); border-radius:8px; padding:16px; display:flex; flex-direction:column; }}
.desc {{ margin:0 0 12px; }}
dl {{ display:grid; grid-template-columns:auto 1fr; gap:2px 12px; margin:0 0 12px; font-size:.92rem; }}
dt {{ color:var(--muted); }}
dd {{ margin:0; }}
.install {{ margin:auto 0 8px; font-size:.92rem; }}
.install code {{ display:block; margin-top:4px; padding:6px 8px; }}
.links {{ margin:0; font-size:.92rem; }}
.hidden {{ display:none; }}
footer {{ padding:40px 16px; font-size:.92rem; }}
</style>
</head>
<body>
<header>
<h1>AI-2 Knowledge Packs</h1>
<p class="lead">A Knowledge Pack is a set of documents that an <a href="{AI2}">AI-2</a> computer can search with no Internet at all. It answers with the passage the authors wrote and names where it came from, instead of making up an answer.</p>
<p class="muted">Install a pack once while you have a connection, or from a file someone hands you on a USB stick. From then on it works offline. This page lists every pack in the <a href="{REPO}">community catalog</a>: {len(packs)} today.</p>
<div class="filters" role="search">
<input id="q" type="search" placeholder="Search the packs, for example water, children or Spanish" aria-label="Search the packs">
<select id="lang" aria-label="Language"><option value="">Any language</option>{lang_opts}</select>
<select id="aud" aria-label="Audience"><option value="">Everyone and children</option><option value="general">For everyone</option><option value="children">For children</option></select>
</div>
<p id="none" class="muted hidden">No pack matches.</p>
</header>
<main>
{sections}
</main>
<footer class="muted">
<p>Each pack's maker answers for its contents. The catalog checks that each file is the one its entry describes and that AI-2 installs it. Read a pack's description to see who has reviewed it.</p>
<p><a href="{REPO}/blob/main/CONTRIBUTING.md">Make and share a pack</a> · <a href="{REPO}/blob/main/REVIEWING.md">Review a pack</a> · <a href="{REPO}/issues">Report a mistake</a> · <a href="{AI2}">Get AI-2</a></p>
<p>Generated from the catalog in <a href="{REPO}">ProWoos-Devs/ai2-knowledge</a>.</p>
</footer>
<script>
(function () {{
  var q = document.getElementById('q'), lang = document.getElementById('lang'), aud = document.getElementById('aud');
  function apply() {{
    var words = q.value.toLowerCase().split(/\\s+/).filter(Boolean), shown = 0;
    document.querySelectorAll('.group').forEach(function (g) {{
      var any = false;
      g.querySelectorAll('.pack').forEach(function (p) {{
        var ok = words.every(function (w) {{ return p.dataset.search.indexOf(w) !== -1; }})
          && (!lang.value || p.dataset.lang.split(' ').indexOf(lang.value) !== -1)
          && (!aud.value || p.dataset.audience === aud.value);
        p.classList.toggle('hidden', !ok); if (ok) {{ any = true; shown++; }}
      }});
      g.classList.toggle('hidden', !any);
    }});
    document.getElementById('none').classList.toggle('hidden', shown > 0);
  }}
  [q, lang, aud].forEach(function (el) {{ el.addEventListener('input', apply); }});
}})();
</script>
</body>
</html>
"""


def main() -> int:
    out = sys.argv[1] if len(sys.argv) > 1 else "_site"
    packs = (yaml.safe_load(open("catalog/community.yml", encoding="utf-8")) or {}).get("packs") or []
    cats_doc = yaml.safe_load(open("catalog/categories.yml", encoding="utf-8")) or {}
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(page(packs, cats_doc.get("categories") or [], cats_doc.get("ages") or []))
    print(f"{out}/index.html written with {len(packs)} pack(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
