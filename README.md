# BRF Sjötungan – webbplats

Statisk webbplats för HSB Bostadsrättsförening Sjötungan i Tyresö. Ren HTML och
CSS, inga externa beroenden – sidorna fungerar även offline.

## Sidor

| Fil | Sida i menyn | Vad sidan samlar |
| --- | --- | --- |
| [index.html](index.html) | Översikt | Föreningen, ekonomin, styrelsen, det gemensamma |
| [family.html](family.html) | För dig … med barn | Gårdarna, lekplatser, fotbollsplan, isbana |
| [car.html](car.html) | För dig … med bil eller MC | P-platser, garage, laddplatser, MC och moped, körning i området |
| [bicycle.html](bicycle.html) | För dig … på cykel | Cykelrum i husen, långtidsförrådet |
| [dogs.html](dogs.html) | För dig … med hund | Kopplingstvång, hundrastgården, katter |
| [fitness.html](fitness.html) | För dig … som tränar | Gymmet med bilder och video, bastun, utegym, boulebana |

Menyvalet **Årsredovisning 2025** är ingen sida utan en direktlänk till PDF:en
hos sjotungan.se. Ekonomin behöver ingen egen sida så länge dokumentet finns.

### Indelningen följer läsaren, inte anläggningarna

Sidorna är indelade efter **vem läsaren är** – med barn, med bil, på cykel, med
hund, som tränar – inte efter vilka anläggningar föreningen råkar äga. Det är
så en spekulant läser: man letar efter om det finns någonstans att göra av
cykeln eller om barnen kan vara ute själva, inte efter en förteckning över
gemensamma utrymmen.

Det får några konsekvenser att hålla fast vid:

- **En anläggning kan förekomma på flera sidor.** Hundrastgården ligger vid
  idrottsplatsen och nämns därför både under hund och under barn. Bilförbudet i
  området hör lika mycket hemma på barnsidan som på bilsidan. Upprepa det korta
  och länka till sidan som har detaljerna.
- **Anläggningar utan läsare får ingen sida.** Tvättstugor, grillplatser,
  gästlägenheten och miljöhusen är sådant alla har, inte en roll man känner
  igen sig i. De ligger som korta punkter under *Gemensamt för alla* på
  översikten.
- **En ny sida kräver en ny roll**, inte en ny anläggning. Frågan att ställa är
  ”vem är det som söker det här?”. Finns rollen inte redan i menyn, och är den
  inte tillräckligt vanlig för att bära en egen sida, hör uppgiften hemma på en
  befintlig sida eller ingenstans.

Sidorna för barn och träning innehåller stycken märkta ”Innehåll kommer” där
uppgifter saknas – lekplatsernas läge och utrustning, när isbanan är i bruk,
samt utegymmets och boulebanans läge. Det som står i övrigt är belagt i
källorna längre ned. Skriv inte in gissningar i luckorna.

Filnamn, id:n och CSS-klasser är på engelska; all text som besökaren ser är på
svenska.

## Målgrupp: allmänheten, inte i första hand medlemmarna

Den här webbplatsen vänder sig i huvudsak till **allmänheten** – spekulanter,
mäklare, blivande grannar och andra som vill bilda sig en uppfattning om
föreningen. Den ersätter inte [sjotungan.se](https://www.sjotungan.se), som är
de boendes kanal med felanmälan, bokning och intern information.

### Det viktigaste målet

Sidan ska ge någon som **inte** bor här en bild av hur det skulle vara att
flytta hit. Vad får man tillgång till, hur ser föreningen ut, vad kan man
räkna med?

Det ska aldrig stå uttryckligen på sidan – ingen text riktad till ”dig som
funderar på att flytta hit”, inga säljande formuleringar. Det är en ton, inte
ett budskap. Innehållet skrivs som saklig information om föreningen, och läsaren
får själv dra slutsatserna.

I praktiken styr det vad som tas med:

- **Skriv om möjligheterna.** Att det finns ett gym med löpband och fria vikter,
  en bastu, en gästlägenhet, laddplatser i garaget, en hundrastgård. Det är
  sådant som gör skillnad för någon som väger olika föreningar mot varandra.
- **Utelämna handhavandet.** Hur man bokar tvättstugan, hur nyckelbrickan
  uppdateras, vilken blankett som ska lämnas i vilken brevlåda. Det säger
  ingenting om hur det är att bo här och hör hemma på sjotungan.se.
- **Behåll siffrorna.** Ekonomi, avgifter och nyckeltal är precis vad en
  spekulant eller mäklare letar efter, och de talar för sig själva.

### Så lite innehåll som möjligt

Grundregeln för hela sajten: **exponera minsta möjliga mängd innehåll.** Varje
sida, stycke och uppgift ska kunna motiveras med varför någon utifrån behöver
den. Finns inget svar tas den bort.

- Lägg inte till uppgifter ”för att de är bra att ha”. Utan ett skäl hör de inte
  hemma här.
- Finns informationen redan i ett dokument – som årsredovisningen – räcker en
  länk. Bygg ingen sida som återger den.
- Färre sidor är bättre än fler. En ny sida ska bära ett eget ämne som någon
  utifrån faktiskt letar efter.
- Vid tveksamhet: ta bort. Det går alltid att lägga tillbaka.

Det betyder att en del av innehållet som finns här i dag egentligen är riktat
till medlemmar och kan tas bort eller kortas ned. Sådant att gå igenom innan
publicering:

- **Namngivna styrelseledamöter och deras e-postadresser** på översiktssidan.
  Överväg att bara ha en funktionsadress, `info@sjotungan.se`.
- **Telefonnumret till gästlägenheten** och andra direktnummer till enskilda
  förtroendevalda.
- **Journummer och förvaltarens direktnummer** – behövs av boende, inte av
  allmänheten.
- **Praktiska instruktioner** som bara är relevanta när man redan bor här: hur
  nyckelbrickan uppdateras, hur man bokar tvättstugan, var miljöhusen är låsta
  och när, hur laddavtalet tecknas.
- **Bilderna och videon från gymmet** visar interiörer i låsta utrymmen. Det är
  knappast känsligt, men det är ett medvetet val att ha dem öppet på nätet.

Det som däremot hör hemma på en publik sida är föreningens storlek och historia,
ekonomin och nyckeltalen, avgiftsnivåer, vilka gemensamma utrymmen som finns och
vad som gäller för husdjur och parkering.

## Struktur och bygge

Sidhuvud, meny och sidfot finns på **ett** ställe. `build.py` sätter ihop dem med
innehållet från `src/pages/` och skriver färdiga HTML-filer i projektroten.

```text
build.py                bygger sajten – här bor meny, sidhuvud, sidfot och ikoner
src/pages/*.html        innehållet, ett <main> per sida
*.html                  genererade filer (checkas in, skrivs över vid bygge)
assets/css/style.css    designsystem (färger, typografi, komponenter)
assets/js/site.js       enda skriptet: mobilmeny och undermenyer
assets/images/gym/      bilder till gymavsnittet på fitness.html (JPEG) + posterbild
assets/video/           gym-tour.mp4
```

```sh
python3 build.py
```

Inga beroenden utöver Python 3. De genererade filerna checkas in, så GitHub
Pages kan servera dem rakt av utan byggsteg.

> **Redigera aldrig `index.html` och de andra filerna i roten.** De skrivs över
> vid nästa bygge. Innehåll ändras i `src/pages/`, allt gemensamt i `build.py`.

### Lägga till en sida

1. Skapa `src/pages/min-sida.html` med en kommentar överst och sidans `<main>`:

   ```html
   <!--
   title: Rubrik i webbläsarfliken
   description: Metabeskrivning för sökmotorer.
   -->

   <main id="main"> … </main>
   ```

2. Lägg in den i `NAV` i `build.py`. En undersida läggs som `children` till sin
   förälder – då hamnar den i undermenyn:

   ```python
   {"label": "För dig…", "children": [
       {"href": "family.html", "label": "med barn"},
   ]},
   ```

   Etiketterna i rollmenyn är skrivna för att läsas ihop med föräldern –
   ”För dig” + ”med barn” – och börjar därför med liten bokstav. Föräldern har
   ingen `href`: den är bara en knapp som fäller ut undermenyn.
   `"external": True` markerar en länk som pekar utanför sajten.

3. Kör `python3 build.py`.

Menyn räknar själv ut vilken post som är aktuell sida, och markerar föräldern
när en undersida visas.

### Ikoner

Ikonerna ligger som SVG-banor i `ICONS` i `build.py` och används i fragmenten
som `{{icon:namn}}` – till exempel `{{icon:arrow}}`. Ändra en ikon på ett ställe
och den uppdateras på alla sidor.

### Bilderna och videon från gymmet

Originalen kommer från en iPhone. De ligger inte i repot – `.gitignore` håller
`IMG_*.HEIC` och `IMG_*.MOV` utanför, och det är webbversionerna under `assets/`
som sidan använder. Behöver bilderna göras om från original tas de fram så här,
med verktyg som redan finns i macOS:

```sh
# HEIC -> JPEG, max 1600 px
sips -s format jpeg -s formatOptions 72 -Z 1600 IMG_2546.HEIC --out img_2546.jpg

# HEVC-video -> H.264 i 540x960, utan ljudspår (AVFoundation via swift)
swift strip.swift IMG_2556.MOV assets/video/gym-tour.mp4
```

Två fallgropar om bilderna behöver göras om:

- `sips -r` roterar bildpunkterna men lämnar kvar EXIF-taggen `Orientation`, så
  webbläsaren roterar en gång till. Taggen måste nollställas till `1` efteråt.
- Kontrollera alltid resultatet i en **webbläsare**. Flera bildvisare roterar
  utifrån EXIF-taggen och visar därför något annat än vad sidan kommer att visa.

## Kör lokalt

Öppna `index.html` direkt i webbläsaren, eller starta en enkel server:

```sh
python3 -m http.server 8000
# http://localhost:8000
```

## Var uppgifterna kommer ifrån

Allt sakinnehåll är hämtat från föreningens egna publicerade källor. Sidorna
innehåller inga påhittade uppgifter.

| Innehåll | Källa |
| --- | --- |
| Ekonomi, nyckeltal, innehav, styrelse, underhållsplan | [Årsmöteshandlingar 2026 med årsredovisning 2025](https://www.sjotungan.se/public_html/new2016/images/information/arsmotes_handlingar/2026/stamma2026.pdf) (PDF) |
| Parkering, hundar, tvättstugor, bastu, gym, sopor | [Sjötungan A–Ö](https://www.sjotungan.se/public_html/new2016/a-o/a-o.html) |
| Adresser, org.nr, e-post, styrelsens roller | [Kontakt](https://www.sjotungan.se/public_html/new2016/kontakt/kontakt.html) |
| Felanmälan och journummer | [Felanmälan](https://www.sjotungan.se/public_html/new2016/forvaltning/felanmalan.html) |
| Gymavgiften, 50 kr per medlem och månad | Uppgift från styrelsen – står inte på sjotungan.se |
| Cykelrum i nästan alla hus, långtidsförråd i M10 | Uppgift från styrelsen – A–Ö anger M6, se nedan |

Ett par saker att känna till innan sidorna publiceras:

- **Avgifter och tider** på A–Ö-sidan var senast uppdaterade 2024-06. Stäm av
  att de fortfarande gäller.
- **Journumret** anges olika på två ställen på sjotungan.se: `08–657 64 50` på
  Felanmälan-sidan och i A–Ö, `010–550 21 65` på Förvaltning-sidan. Här används
  det förstnämnda, eftersom det står på två av tre ställen.
- **Årsredovisningen 2025** fastställs på stämman den 2 juni 2026. Siffrorna här
  är hämtade ur handlingarna till den stämman.
- **Styrelsen** som listas är den som valdes för 2026–2027. Uppdatera efter
  nästa stämma.
- **Gymavsnittet** på `fitness.html` bygger på bilder tagna i lokalen i juli
  2026 plus uppgifterna om öppettider, åldersgräns och medlemskap från A–Ö.
- **Lekplatser, fotbollsplan, isbana, utegym och boulebana** finns belagda som
  anläggningar, men A–Ö säger inget om läge, utrustning eller säsong. Därför står
  bara att de finns. Uppgifterna behöver hämtas från styrelsen innan styckena
  ”Innehåll kommer” kan ersättas.
- **Cykelförrådet.** A–Ö skriver att långtidsförvaringen finns i miljöhuset vid
  **M6** och rymmer ett tjugotal cyklar. Sidan anger **M10** enligt uppgift från
  styrelsen. Stäm av vilket som gäller, och rätta antingen sidan eller A–Ö.
- **Länkarna till årsredovisningen** – i menyn och på översiktssidan – pekar på
  PDF:en hos sjotungan.se. Sökvägen innehåller årtalet `2026`, så den måste
  bytas när nästa års handlingar publiceras. Den står på ett ställe i koden:
  `ANNUAL_REPORT_PDF` i `build.py`.

## Publicera

Vilken statisk webbhotellstjänst som helst fungerar. Med GitHub Pages: pusha
till `main` och slå på Pages med `main` / `/ (root)` under *Settings → Pages*.

## Designnoteringar

- Färger, radier och skuggor ligger som CSS-variabler överst i `style.css` –
  ändra `--accent` för att byta profilfärg på hela sajten.
- Mörkt läge följer operativsystemets inställning via `prefers-color-scheme`.
- Layouten är responsiv utan brytpunktshopp: kortrutnät använder `auto-fit`,
  menyn fälls ihop till en hamburgermeny under 860 px och breda tabeller
  scrollar i sin egen behållare.
