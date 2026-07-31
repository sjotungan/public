#!/usr/bin/env python3
"""Bygger de statiska sidorna för brf-sjotungan.

Varje sida finns som ett innehållsfragment i src/pages/. Skriptet lägger på
gemensam <head>, sidhuvud, meny och sidfot och skriver färdiga HTML-filer i
projektroten. Kör:

    python3 build.py

Ändra sidhuvud, meny eller sidfot här – aldrig i de genererade filerna, som
skrivs över vid nästa körning.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(ROOT, "src", "pages")

SITE_NAME = "BRF Sjötungan"
LEGAL_NAME = "HSB Brf Sjötungan i Tyresö"
ADDRESS = "Myggdalsvägen 102, 135 43 Tyresö"
EMAIL = "info@sjotungan.se"
OFFICIAL_SITE = "https://www.sjotungan.se"

ANNUAL_REPORT_PDF = (
    "https://www.sjotungan.se/public_html/new2016/images/information/"
    "arsmotes_handlingar/2026/stamma2026.pdf"
)

# Menyn. "children" ger en undermeny; "external" länkar utanför sajten.
NAV = [
    {"href": "index.html", "label": "Översikt"},
    {"href": ANNUAL_REPORT_PDF, "label": "Årsredovisning 2025", "external": True},
    {
        # Ingen "href": posten är enbart en meny som fälls ut vid klick.
        "label": "Bekvämligheter",
        "children": [
            {"href": "parking.html", "label": "Parkering"},
            {"href": "bicycle-storage.html", "label": "Cykelförråd"},
            {"href": "playground.html", "label": "Lekplats"},
            {"href": "gym.html", "label": "Gym"},
            {"href": "outdoor-gym.html", "label": "Utegym"},
            {"href": "sauna.html", "label": "Bastu"},
            {"href": "boule.html", "label": "Boulebana"},
            {"href": "ice-rink.html", "label": "Isbana"},
            {"href": "football-field.html", "label": "Fotbollsplan"},
            {"href": "barbecue.html", "label": "Grillplatser"},
            {"href": "dogs.html", "label": "Hundägare"},
            {"href": "laundry.html", "label": "Tvättstugor"},
        ],
    },
]

# Ikoner används i sidfragmenten som {{icon:namn}}.
ICONS = {
    "house": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.6V21h14V9.6"/><path d="M9.5 21v-6h5v6"/>',
    "menu": '<path d="M4 7h16"/><path d="M4 12h16"/><path d="M4 17h16"/>',
    "chevron": '<path d="m6 9 6 6 6-6"/>',
    "arrow": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11.5V16"/><path d="M12 8h.01"/>',
    "warn": '<path d="M12 4 3.2 19.5h17.6z"/><path d="M12 10v4.5"/><path d="M12 17.5h.01"/>',
    "doc": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6"/><path d="M9 17h4"/>',
    "download": '<path d="M12 3v12"/><path d="m7.5 11 4.5 4.5 4.5-4.5"/><path d="M5 20h14"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 7.5 8.5 5.8 8.5-5.8"/>',
    "car": '<path d="m3 13.5 1.9-5.6A2 2 0 0 1 6.8 6.5h10.4a2 2 0 0 1 1.9 1.4L21 13.5"/><path d="M3 13.5h18V18h-3v-1.5H6V18H3z"/><path d="M6.5 16h.01"/><path d="M17.5 16h.01"/>',
    "paw": '<circle cx="6.8" cy="9" r="1.9"/><circle cx="12" cy="6.9" r="1.9"/><circle cx="17.2" cy="9" r="1.9"/><path d="M12 11.4c2.5 0 4.6 2 4.6 4.4 0 1.6-1.2 2.6-2.7 2.6-.9 0-1.4-.4-1.9-.4s-1 .4-1.9.4c-1.5 0-2.7-1-2.7-2.6 0-2.4 2.1-4.4 4.6-4.4Z"/>',
    "spark": '<path d="M11 3.5 12.8 8l4.5 1.8L12.8 11.6 11 16.1 9.2 11.6 4.7 9.8 9.2 8Z"/><path d="m18.2 14.6.9 2.3 2.3.9-2.3.9-.9 2.3-.9-2.3-2.3-.9 2.3-.9Z"/>',
    "wash": '<rect x="4" y="3" width="16" height="18" rx="2.5"/><circle cx="12" cy="14" r="4"/><path d="M8 6.5h.01"/><path d="M11 6.5h.01"/>',
    "sauna": '<path d="M8 14c-2-2.2-2-4.5 0-6.7 1.3-1.4 1.6-2.5 1-3.3"/><path d="M15 14c-2-2.2-2-4.5 0-6.7 1.3-1.4 1.6-2.5 1-3.3"/><path d="M4 17.5h16"/><path d="M4 20.5h16"/>',
    "gym": '<path d="M4 9v6"/><path d="M20 9v6"/><path d="M7 6.5v11"/><path d="M17 6.5v11"/><path d="M7 12h10"/>',
    "bike": '<circle cx="5.8" cy="16" r="3.2"/><circle cx="18.2" cy="16" r="3.2"/><path d="M8.5 8.5h3.5l2.8 7.5"/><path d="m9.5 16 3.5-6"/><path d="M15 8.5h2.5"/>',
    "bin": '<path d="M6 8h12l-1 11a2 2 0 0 1-2 1.8H9A2 2 0 0 1 7 19z"/><path d="M4.5 8h15"/><path d="M9.5 8V5.5a1.5 1.5 0 0 1 1.5-1.5h2a1.5 1.5 0 0 1 1.5 1.5V8"/>',
    "home2": '<path d="M3.5 20V9.5L12 4l8.5 5.5V20"/><path d="M3.5 20h17"/><path d="M9 20v-5h6v5"/>',
}

FAVICON = (
    "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
    "<rect width='100' height='100' rx='22' fill='%230f5c4a'/>"
    "<path d='M22 52 50 28l28 24' fill='none' stroke='white' stroke-width='8' "
    "stroke-linecap='round' stroke-linejoin='round'/>"
    "<path d='M30 48v26h40V48' fill='none' stroke='white' stroke-width='8' "
    "stroke-linecap='round' stroke-linejoin='round'/></svg>"
)


def icon(name, width="1.8", extra=' aria-hidden="true"'):
    return (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="%s" stroke-linecap="round" stroke-linejoin="round"%s>%s</svg>'
        % (width, extra, ICONS[name])
    )


def expand_icons(html):
    return re.sub(r"\{\{icon:([a-z0-9]+)\}\}",
                  lambda m: icon(m.group(1)), html)


def read_page(path):
    """Returnerar (metadata, innehåll) för ett sidfragment."""
    raw = open(path, encoding="utf-8").read()
    meta = {}
    m = re.match(r"\s*<!--(.*?)-->\s*", raw, re.S)
    if m:
        for line in m.group(1).strip().splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip()
        raw = raw[m.end():]
    return meta, raw.strip()


def nav_link(item, current):
    aria = ' aria-current="page"' if item["href"] == current else ""
    return '<a href="%s"%s>%s</a>' % (item["href"], aria, item["label"])


def render_nav(current):
    """Menyn. En post med "children" är ingen länk utan en knapp som fäller ut
    undermenyn – ett klick på etiketten öppnar alltså menyn i stället för att
    leda till en egen sida."""
    out = []
    for item in NAV:
        children = item.get("children", [])
        if not children:
            out.append("        <li>%s</li>" % nav_link(item, current))
            continue

        # Föräldern markeras som aktiv när någon av undersidorna visas.
        in_branch = current in [c["href"] for c in children]
        cls = " nav__sub-button is-active" if in_branch else " nav__sub-button"
        subs = "\n".join(
            "            <li>%s</li>" % nav_link(c, current) for c in children
        )
        out.append(
            '        <li class="nav__has-sub">\n'
            '          <button class="%s" type="button" aria-expanded="false">\n'
            "            %s\n"
            "            %s\n"
            "          </button>\n"
            '          <ul class="nav__sub">\n%s\n          </ul>\n'
            "        </li>"
            % (cls.strip(), item["label"], icon("chevron", width="2"), subs)
        )
    return "\n".join(out)


def render(meta, content, current):
    title = meta.get("title", SITE_NAME)
    description = meta.get("description", "")
    return """<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – {site}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="assets/css/style.css">
<link rel="icon" href="{favicon}">
</head>
<body>
<a class="skip-link" href="#main">Hoppa till innehållet</a>

<header class="site-header">
  <div class="container site-header__inner">
    <a class="brand" href="index.html">
      <span class="brand__mark" aria-hidden="true">{brandmark}</span>
      {site}
    </a>

    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
      {menuicon}
      Meny
    </button>

    <nav class="nav" id="site-nav" aria-label="Huvudmeny">
      <ul class="nav__list">
{nav}
      </ul>
    </nav>
  </div>
</header>

{content}

<footer class="site-footer">
  <div class="container site-footer__inner">
    <p class="site-footer__name">{legal}</p>
    <p>{address}</p>
    <p>
      <a href="mailto:{email}">{email}</a>
      <span class="site-footer__sep" aria-hidden="true">·</span>
      <a href="{official}">sjotungan.se</a>
    </p>
  </div>
</footer>

<script src="assets/js/site.js"></script>
</body>
</html>
""".format(
        title=title,
        site=SITE_NAME,
        description=description,
        favicon=FAVICON,
        brandmark=icon("house", width="1.9", extra=""),
        menuicon=icon("menu", width="2"),
        nav=render_nav(current),
        content=expand_icons(content),
        legal=LEGAL_NAME,
        address=ADDRESS,
        email=EMAIL,
        official=OFFICIAL_SITE,
    )


def main():
    if not os.path.isdir(PAGES):
        sys.exit("hittar inte %s" % PAGES)
    written = 0
    for name in sorted(os.listdir(PAGES)):
        if not name.endswith(".html"):
            continue
        meta, content = read_page(os.path.join(PAGES, name))
        html = render(meta, content, name)
        open(os.path.join(ROOT, name), "w", encoding="utf-8").write(html)
        print("skrev %-24s %6d bytes" % (name, len(html)))
        written += 1
    print("%d sidor" % written)


if __name__ == "__main__":
    main()
