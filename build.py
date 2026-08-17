#!/usr/bin/env python3
"""Bygger de statiska sidorna för brf-sjotungan.

Varje sida finns som ett innehållsfragment i src/pages/. Skriptet lägger på
gemensam <head>, sidhuvud, meny och sidfot och skriver färdiga HTML-filer i
projektroten. Kör:

    python3 build.py

Ändra sidhuvud, meny eller sidfot här – aldrig i de genererade filerna, som
skrivs över vid nästa körning.

Innehållet finns i två lager. En sida i src/pages/ bestämmer ordning och
layout; en anläggning – lekplatsen, gymmet, hundrastgården – beskrivs i ett
eget innehållsblock i src/blocks/ och hämtas in med {{block:namn}}. Samma block
kan ligga på flera sidor, och texten står då bara på ett ställe.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(ROOT, "src", "pages")
BLOCKS = os.path.join(ROOT, "src", "blocks")

SITE_NAME = "BRF Sjötungan"
OFFICIAL_SITE = "https://www.sjotungan.se"

ANNUAL_REPORT_PDF = (
    "https://www.sjotungan.se/public_html/new2016/images/information/"
    "arsmotes_handlingar/2026/stamma2026.pdf"
)

# Menyn. "children" ger en undermeny; "external" länkar utanför sajten.
#
# Menyn är byggd för två besök, inte för två målgrupper. Det är samma person
# båda gångerna:
#
# 1. Första besöket – en spekulant som tittar på många lägenheter, kommer från
#    mäklarens länk, läser tre minuter i mobilen och scrollar. Det besöket rör
#    aldrig menyn. Hela argumentet ligger på index.html i fallande ordning
#    efter hur mycket det påverkar ett köpbeslut.
# 2. Andra besöket – samma person med två, tre lägenheter kvar på listan, som
#    ska försvara några miljoner kronor. Nu är läsaren skeptisk och letar efter
#    det som är fel. Det besöket *navigerar*: man kommer tillbaka för en
#    bestämd fråga.
#
# Menyn följer ändå samma ordning som översikten: det som lockar först, det som
# ska kontrolleras sist. Ekonomi och underhåll låg tidigare direkt efter
# Översikt, med motiveringen att det andra besöket letar efter den. Det var fel
# av två skäl. Menyn syns för *båda* besöken, och en meny som inleds med
# "Ekonomi och underhåll" säger en förstagångsbesökare att sajten handlar om
# föreningens siffror – vilket den inte gör. Och den som återvänder för just
# ekonomin letar aktivt och hittar posten var den än står.
#
# Ekonomi och Fakta står bredvid varandra i slutet, före årsredovisningen: de
# tre hör ihop som det man kontrollerar med, och den som är i det ärendet vill
# ha dem samlade.
#
# Undermenyn "För dig…" är indelad efter vem läsaren är, inte efter vilka
# anläggningar som finns. Den är inte till för att besökaren ska välja profil –
# den sorteringen gör mäklaren, som har träffat köparen och länkar direkt till
# rätt sida. Etiketterna läses ihop med föräldern: "För dig" + "med barn".
NAV = [
    {"href": "index.html", "label": "Översikt"},
    {"href": "laget.html", "label": "Läget"},
    # Ämnessida, inte rollsida: utemiljön är något varje köpare bedömer, inte en
    # läsare som känner igen sig. Den ligger därför här och inte under "För dig…".
    {"href": "gardarna.html", "label": "Gårdarna"},
    {"href": "bilder.html", "label": "Bilder"},
    {
        # Ingen "href": posten är enbart en meny som fälls ut vid klick.
        "label": "För dig…",
        "children": [
            {"href": "family.html", "label": "med barn"},
            {"href": "car.html", "label": "med bil eller MC"},
            {"href": "bicycle.html", "label": "på cykel"},
            {"href": "dogs.html", "label": "med hund"},
            {"href": "fitness.html", "label": "som tränar"},
        ],
    },
    {"href": "ekonomi.html", "label": "Ekonomi och underhåll"},
    {"href": "fakta.html", "label": "Fakta"},
    {"href": ANNUAL_REPORT_PDF, "label": "Årsredovisning 2025", "external": True},
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
    "road": '<path d="M8.5 3.5 6 20.5"/><path d="m15.5 3.5 2.5 17"/><path d="M12 4.5v2.6"/><path d="M12 10.7v2.6"/><path d="M12 16.9v2.6"/>',
    "map": '<path d="M9 4.4 3.5 6.6v13L9 17.4l6 2.2 5.5-2.2v-13L15 6.6z"/><path d="M9 4.4v13"/><path d="M15 6.6v13"/>',
    "bin": '<path d="M6 8h12l-1 11a2 2 0 0 1-2 1.8H9A2 2 0 0 1 7 19z"/><path d="M4.5 8h15"/><path d="M9.5 8V5.5a1.5 1.5 0 0 1 1.5-1.5h2a1.5 1.5 0 0 1 1.5 1.5V8"/>',
    "home2": '<path d="M3.5 20V9.5L12 4l8.5 5.5V20"/><path d="M3.5 20h17"/><path d="M9 20v-5h6v5"/>',
    "kite": '<path d="M12 2.8 4.8 10 12 17.2 19.2 10Z"/><path d="M12 2.8V17.2"/><path d="M4.8 10h14.4"/><path d="M12 17.2v2.3a1.7 1.7 0 0 1-3.4 0"/>',
    "ball": '<circle cx="12" cy="12" r="8.6"/><path d="m12 7.4 3.9 2.8-1.5 4.6H9.6l-1.5-4.6Z"/><path d="M12 3.4v4"/><path d="m4 9.9 4.1.3"/><path d="m20 9.9-4.1.3"/><path d="m7.3 19 2.3-4.2"/><path d="m16.7 19-2.3-4.2"/>',
    "drill": '<rect x="3" y="6.5" width="9.5" height="6" rx="1.6"/><rect x="12.5" y="8" width="3.5" height="3" rx="0.6"/><path d="M16 9.5h4.6"/><path d="M6 12.5v6h3v-6"/>',
    "parcel": '<path d="M3.5 7.6 12 3.5l8.5 4.1v8.8L12 20.5l-8.5-4.1Z"/><path d="m3.5 7.6 8.5 4.1 8.5-4.1"/><path d="M12 11.7v8.8"/><path d="m7.75 5.55 8.5 4.1"/>',
    "tag": '<path d="M4 11.8V4.4h7.4l8.2 8.2a1.6 1.6 0 0 1 0 2.3l-5.1 5.1a1.6 1.6 0 0 1-2.3 0Z"/><path d="M8.2 8.2h.01"/>',
    "leaf": '<path d="M20 4.2c-9.2 0-15.2 3.6-15.2 10.1a4.9 4.9 0 0 0 4.9 4.9c6.5 0 10.3-6 10.3-15Z"/><path d="M4.5 19.8C7 15.3 11 11.8 15.4 9.8"/>',
    "flame": '<path d="M12 3.2c1.1 3.3 3 4.9 4.3 6.5a6.5 6.5 0 0 1 1.7 4.2 6 6 0 0 1-12 0c0-2 .8-3.7 2-5.1.3 1.3.9 2.1 1.7 2.6C10 8.6 10.9 5.9 12 3.2Z"/>',
    "chat": '<path d="M20.5 12.2c0 3.9-3.8 7.1-8.5 7.1-1 0-2-.15-2.9-.4L4 20.5l1.7-3.9a6.8 6.8 0 0 1-2.2-4.4C3.5 8.3 7.3 5.1 12 5.1s8.5 3.2 8.5 7.1Z"/>',
    "chart": '<path d="M4 20V4"/><path d="M4 20h16"/><path d="M8 20v-5.5"/><path d="M12.7 20V9.5"/><path d="M17.3 20v-8"/>',
    "coin": '<ellipse cx="12" cy="6.6" rx="7.5" ry="3.1"/><path d="M4.5 6.6v10.8c0 1.7 3.4 3.1 7.5 3.1s7.5-1.4 7.5-3.1V6.6"/><path d="M4.5 12c0 1.7 3.4 3.1 7.5 3.1s7.5-1.4 7.5-3.1"/>',
    "wrench": '<path d="M15.2 7.4a3.9 3.9 0 0 1 5.1-5.1l-2.9 2.9.6 2.4 2.4.6 2.9-2.9a3.9 3.9 0 0 1-5.1 5.1" transform="translate(-2.2 .6)"/><path d="M14.1 9.9 4.6 19.4a2 2 0 0 0 2.8 2.8l9.5-9.5"/>',
    "lift": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M12 3v18"/><path d="m8.6 9.6 1.4-1.8 1.4 1.8"/><path d="m14.6 14.4 1.4 1.8 1.4-1.8" transform="translate(-1.5)"/>',
    "shield": '<path d="M12 3.2 5 6v5.6c0 4.2 2.8 7.6 7 9.2 4.2-1.6 7-5 7-9.2V6Z"/><path d="m9 12.2 2.1 2.1L15 10.5"/>',
    "wifi": '<path d="M2.8 9.1a14 14 0 0 1 18.4 0"/><path d="M6 12.4a9.2 9.2 0 0 1 12 0"/><path d="M9.2 15.7a4.5 4.5 0 0 1 5.6 0"/><path d="M12 19.2h.01"/>',
    "bus": '<rect x="4" y="4" width="16" height="12.5" rx="2.2"/><path d="M4 10.5h16"/><path d="M7.5 13.6h.01"/><path d="M16.5 13.6h.01"/><path d="M7 16.5v2.3"/><path d="M17 16.5v2.3"/>',
    "pin": '<path d="M12 21c4-4.4 6-7.6 6-10.3A6 6 0 0 0 6 10.7C6 13.4 8 16.6 12 21Z"/><circle cx="12" cy="10.6" r="2.3"/>',
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


# Länkar ut från sajten öppnas i en ny flik. Sajten finns för att någon ska
# stanna kvar och läsa färdigt, och en spekulant som klickar på kartan eller på
# årsredovisningen ska inte behöva hitta tillbaka.
#
# Tre saker följer med automatiskt, och därför sker det här och inte för hand i
# ett femtiotal block:
#
#   target="_blank"   öppnar i ny flik
#   rel="noopener"    hindrar den öppnade sidan från att komma åt window.opener
#                     och styra om vår flik – annars en känd fiskemetod
#   "(öppnas i ny flik)"  läses upp av skärmläsare men syns inte. Utan den vet
#                     den som inte ser skärmen inte varför bakåtknappen slutade
#                     fungera; WCAG förutsätter att det framgår i förväg.
#
# mailto: rörs inte – de öppnar e-postklienten, inte en flik. Relativa länkar
# inom sajten rörs inte heller, och därför inte bildernas länkar till
# originalfilerna: de öppnas i samma flik och stängs med bakåtknappen.
EXTERNAL_LINK_RE = re.compile(
    r'<a\s+([^>]*href="https?://[^"]*"[^>]*)>(.*?)</a>', re.S)

NEW_TAB_NOTE = '<span class="sr-only"> (öppnas i ny flik)</span>'


def open_external_in_new_tab(html):
    def rewrite(m):
        attrs, inner = m.group(1), m.group(2)
        if "target=" in attrs:
            return m.group(0)
        return '<a %s target="_blank" rel="noopener">%s%s</a>' % (
            attrs, inner, NEW_TAB_NOTE)

    return EXTERNAL_LINK_RE.sub(rewrite, html)


def read_fragment(path):
    """Returnerar (metadata, innehåll) för en sida eller ett block.

    Metadata står i en HTML-kommentar överst, en nyckel per rad."""
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


# Innehållsblock. Ett block beskriver en sak i området – lekplatsen, gymmet,
# hundrastgården – som ren text plus en rubrik och en ikon. Inramningen ligger
# inte i blocket utan i varianten, så att samma block kan vara ett kort i ett
# rutnät på en sida och ett helt avsnitt på en annan.
#
# Hämtas in med {{block:namn}} eller {{block:namn:variant}}, ensamt på en rad.
# Raden får den indragning platsen kräver – blocket skrivs in med samma.
BLOCK_RE = re.compile(
    r"^([ \t]*)\{\{block:([a-z0-9-]+)(?::([a-z-]+))?\}\}[ \t]*$", re.M)

# Första stycket i ett block är ingressen: den mening som ensam duger som svar.
# Varianten "section" sätter den i sidhuvudet och resten under.
#
# De inledande kommentarerna räknas inte som text. Uttrycket krävde tidigare att
# kroppen började med <p>, och de fem block som dokumenterar sina val i en
# kommentar överst matchade därför aldrig: ingressen blev liggande kvar i
# kroppen och renderades som brödtext i stället för som ingress. Kommentarerna
# fångas nu i en egen grupp så att de följer med ut i sidan – de är skrivna för
# den som läser källan och ska inte tappas bort på vägen.
LEAD_RE = re.compile(r"\A\s*((?:<!--.*?-->\s*)*)(<p>.*?</p>)(.*)\Z", re.S)


def indent(text, pad):
    return "\n".join(pad + line if line.strip() else line
                     for line in text.splitlines())


def read_block(name):
    path = os.path.join(BLOCKS, name + ".html")
    if not os.path.isfile(path):
        sys.exit("hittar inget block som heter %s (%s)" % (name, path))
    meta, body = read_fragment(path)
    if "title" not in meta:
        sys.exit("blocket %s saknar title i kommentaren överst" % name)
    return meta, body


def split_lead(body):
    """Delar innehållet i ingress (första stycket) och resten.

    Kommentarerna överst hör till resten, inte till ingressen, och ställs
    först i den så att de står kvar ovanför texten de handlar om.
    """
    m = LEAD_RE.match(body)
    if not m:
        return "", body
    notes, lead, rest = m.group(1), m.group(2), m.group(3)
    kvar = [del_ for del_ in (notes.strip(), rest.strip()) if del_]
    return lead, "\n\n".join(kvar)


def card_body(meta, body):
    out = []
    if "icon" in meta:
        out.append('  <span class="card__icon" aria-hidden="true">'
                   "{{icon:%s}}</span>" % meta["icon"])
    out.append("  <h3>%s</h3>" % meta["title"])
    out.append(indent(body, "  "))
    return out


def render_card(meta, body):
    """Ett kort att ställa i ett rutnät: ikon, rubrik och text."""
    return "\n".join(['<article class="card">']
                     + card_body(meta, body) + ["</article>"])


def render_link_card(meta, body):
    """Samma kort, men hela ytan är en länk – för det som ligger utanför sajten."""
    if "href" not in meta:
        sys.exit("blocket %s saknar href och kan inte bli link-card"
                 % meta["title"])
    more = meta.get("more", "Läs mer")
    return "\n".join(
        ['<a class="card card--link" href="%s">' % meta["href"]]
        + card_body(meta, body)
        + ['  <span class="card__more">%s {{icon:arrow}}</span>' % more,
           "</a>"])


def render_section(meta, body):
    """Ett eget avsnitt: rubrik och ingress i ett sidhuvud, resten under."""
    lead, rest = split_lead(body)
    head = ['<div class="section__head">', "  <h2>%s</h2>" % meta["title"]]
    if lead:
        head.append(indent(lead, "  "))
    head.append("</div>")
    head = "\n".join(head)
    return head + "\n\n" + rest if rest else head


def render_prose(meta, body):
    """Rubrik och text utan inramning, att ställa i en .prose eller .split."""
    return "<h2>%s</h2>\n%s" % (meta["title"], body)


def render_subsection(meta, body):
    """Samma sak en nivå ner, under en rubrik som sidan redan satt."""
    return "<h3>%s</h3>\n%s" % (meta["title"], body)


def render_text(meta, body):
    """Bara innehållet – sidan sätter rubriken själv, eller ingen alls."""
    return body


VARIANTS = {
    "card": render_card,
    "link-card": render_link_card,
    "section": render_section,
    "prose": render_prose,
    "subsection": render_subsection,
    "text": render_text,
}


def expand_blocks(html, stack=()):
    def replace(m):
        pad, name, variant = m.group(1), m.group(2), m.group(3) or "card"
        if name in stack:
            sys.exit("blocket %s hämtar in sig självt: %s"
                     % (name, " → ".join(stack + (name,))))
        if variant not in VARIANTS:
            sys.exit("okänd variant %s för blocket %s – finns: %s"
                     % (variant, name, ", ".join(sorted(VARIANTS))))
        meta, body = read_block(name)
        rendered = VARIANTS[variant](meta, body)
        return indent(expand_blocks(rendered, stack + (name,)), pad)

    html = BLOCK_RE.sub(replace, html)
    left = re.search(r"\{\{block:[^}]*\}\}", html)
    if left:
        sys.exit("%s måste stå ensamt på sin rad för att hämtas in"
                 % left.group(0))
    return html


# Bildsidan. Sidan skriver inga bilder själv utan samlar in dem: när blocken
# hämtats in går skriptet igenom de andra sidorna i menyns ordning och plockar
# ut varje <figure>. Bilderna hamnar i ett enda galleri – en uppsättning att
# bläddra igenom, utan avsnitt och rubriker emellan. Bildtexten står kvar på ett
# enda ställe – i blocket eller på sidan där bilden hör hemma – och bildsidan
# fylls på av sig själv när en bild läggs till någon annanstans.
#
# Sidfragmentet markerar platsen med {{gallery}}, ensamt på en rad.
GALLERY_PAGE = "bilder.html"
GALLERY_MARK_RE = re.compile(r"^[ \t]*\{\{gallery\}\}[ \t]*$", re.M)

FIGURE_RE = re.compile(r"^([ \t]*)<figure>.*?</figure>", re.M | re.S)
HREF_RE = re.compile(r'<a href="([^"]+)"')


def dedent_to(text, pad):
    return "\n".join(line[len(pad):] if line.startswith(pad) else line.lstrip()
                     for line in text.splitlines())


def collect_figures(pages, order):
    """Alla bilder på sajten, i den ordning läsaren möter dem.

    Blocken är redan inhämtade, så det spelar ingen roll om en bild står på
    sidan eller i ett block. En bild som står på flera sidor tas med en gång."""
    seen = set()
    figures = []
    for name in order:
        if name == GALLERY_PAGE:
            continue
        for found in FIGURE_RE.finditer(pages[name][1]):
            figure = dedent_to(found.group(0), found.group(1))
            href = HREF_RE.search(figure)
            key = href.group(1) if href else figure
            if key in seen:
                continue
            seen.add(key)
            figures.append(figure)
    return figures


def render_gallery_page(figures):
    """Ett enda galleri: hela sajtens bilder i en följd."""
    return "\n".join(
        ['  <section class="section">',
         '    <div class="container">',
         '      <div class="gallery gallery--all">']
        + [indent(figure, "        ") for figure in figures]
        + ["      </div>",
           "    </div>",
           "  </section>"])


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
    page = """<!DOCTYPE html>
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
    <p class="site-footer__note">
      <a href="{official}">sjotungan.se</a> är föreningens officiella webbplats.
      Den här sidan är inte officiell utan är skapad och underhålls av aktiva
      medlemmar i föreningen.
    </p>
    <p class="site-footer__note">
      Innehållet är sammanställt efter bästa förmåga, men kan innehålla fel och
      hinner bli inaktuellt. Vi tar inget ansvar för felaktiga uppgifter – det
      som formellt gäller står i föreningens stadgar och årsredovisning och på
      den officiella webbplatsen.
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
        official=OFFICIAL_SITE,
    )
    # Sist av allt, på hela dokumentet: då täcks även årsredovisningen i menyn
    # och länken till sjotungan.se i sidfoten, inte bara sidornas eget innehåll.
    return open_external_in_new_tab(page)


def page_order(names):
    """Sidorna i menyns ordning – den ordning läsaren möter dem i."""
    wanted = []
    for item in NAV:
        if item.get("external"):
            continue
        for entry in [item] + item.get("children", []):
            if "href" in entry and entry["href"] in names:
                wanted.append(entry["href"])
    return wanted + [n for n in sorted(names) if n not in wanted]


def main():
    if not os.path.isdir(PAGES):
        sys.exit("hittar inte %s" % PAGES)

    names = [n for n in os.listdir(PAGES) if n.endswith(".html")]
    pages = {}
    for name in names:
        meta, content = read_fragment(os.path.join(PAGES, name))
        pages[name] = (meta, expand_blocks(content))

    order = page_order(names)
    if GALLERY_PAGE in pages:
        figures = collect_figures(pages, order)
        meta, content = pages[GALLERY_PAGE]
        if not GALLERY_MARK_RE.search(content):
            sys.exit("%s saknar {{gallery}} på egen rad" % GALLERY_PAGE)
        pages[GALLERY_PAGE] = (
            meta,
            # Funktionen som ersättning: innehållet skrivs in som det står.
            GALLERY_MARK_RE.sub(lambda m: render_gallery_page(figures), content),
        )
        print("bildsidan: %d bilder" % len(figures))

    for name in order:
        meta, content = pages[name]
        html = render(meta, content, name)
        open(os.path.join(ROOT, name), "w", encoding="utf-8").write(html)
        print("skrev %-24s %6d bytes" % (name, len(html)))
    print("%d sidor" % len(order))


if __name__ == "__main__":
    main()
