# BRF Sjötungan – webbplats

Statisk webbplats för HSB Bostadsrättsförening Sjötungan i Tyresö. Ren HTML och
CSS, inga externa beroenden – sidorna fungerar även offline.

## Sidor

| Fil | Sida i menyn | Vad sidan samlar |
| --- | --- | --- |
| [index.html](index.html) | Översikt | Ansvarsfriskrivning, fem siffror om föreningen, och det som väger tyngst för en köpare: skötseln av området, parkeringsavgiften och grillplatserna |
| [family.html](family.html) | För dig … med barn | Gårdarna, de fyra lekplatserna med bilder och kartlänkar, fotbollsplan, isbana, förskola och kulturskola i närområdet |
| [car.html](car.html) | För dig … med bil eller MC | P-platser, garage, laddplatser, MC och moped, körning i området |
| [bicycle.html](bicycle.html) | För dig … på cykel | Cykelrum i husen, långtidsförrådet, cykelvägarna utanför |
| [dogs.html](dogs.html) | För dig … med hund | Kopplingstvång, hundrastgården med karta, katter |
| [fitness.html](fitness.html) | För dig … som tränar | Gymmet med bilder och video, bastun, utegymmet med bilder, boulebana |

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

Översikten och sidorna för barn och träning innehåller stycken märkta ”Innehåll
kommer” där uppgifter saknas – när isbanan är i bruk, vad som står på
lekplatserna vid Myggdalsvägen 40 och 110, var i området utegymmet och
boulebanan ligger, samt var de övriga grillplatserna ligger. Det som står i
övrigt är belagt i källorna längre ned. Skriv inte in gissningar i luckorna.

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

**Målet är inte att redovisa vad föreningen består av.** Sajten är ingen
förteckning över föreningens tillgångar, utan en bild av hur livet ser ut för
den som flyttar hit. Det är skillnaden mellan att svara på ”vad äger
föreningen?” och ”hur blir min vardag?”.

Därför är **ägandeskapet ointressant för urvalet**. En förskola granne med
området, en kulturskola fem minuter bort och kommunens stadslekplats påverkar
vardagen lika mycket som föreningens egen lekplats – ibland mer. Att de inte
ägs av föreningen är ett skäl att formulera dem korrekt, aldrig ett skäl att
utelämna dem eller gömma dem i en fotnot. Sådant samlas under *I närområdet* på
den sida vars läsare berörs.

Gränsen går vid vad som faktiskt formar vardagen inom räckhåll. Allt som råkar
finnas i kommunen hör inte hit – frågan är om läsaren skulle märka skillnaden
från just den här adressen.

I praktiken styr det vad som tas med:

- **Skriv om möjligheterna.** Att det finns ett gym med löpband och fria vikter,
  en bastu, en gästlägenhet, laddplatser i garaget, en hundrastgård. Det är
  sådant som gör skillnad för någon som väger olika föreningar mot varandra.
- **Ta med närområdet på samma villkor.** Förskola, skola, kulturskola,
  lekplatser och kommunikationer inom gångavstånd väger tungt för den som
  jämför adresser. Skriv vad det är, hur långt bort och länka till den som
  faktiskt äger uppgiften – kommunen, inte föreningen.
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

- **Praktiska instruktioner** som bara är relevanta när man redan bor här: hur
  nyckelbrickan uppdateras, hur man bokar tvättstugan, var miljöhusen är låsta
  och när, hur laddavtalet tecknas.
- **Bilderna och videon från gymmet** visar interiörer i låsta utrymmen. Det är
  knappast känsligt, men det är ett medvetet val att ha dem öppet på nätet.

Det som däremot hör hemma på en publik sida är föreningens storlek och historia,
ekonomin och nyckeltalen, avgiftsnivåer, vilka gemensamma utrymmen som finns och
vad som gäller för husdjur och parkering.

### Kontaktytan ligger inte här

Sajten har ingen kontaktsektion och ingen ”Kontakta styrelsen”-knapp. Den
namnger inga ledamöter, listar inga rolladresser och innehåller inga
direktnummer till förtroendevalda. Enda adressen är funktionsadressen i
sidfoten, som `build.py` sätter. Den som behöver nå en enskild roll hänvisas
till [kontaktsidan på sjotungan.se](https://www.sjotungan.se/public_html/new2016/kontakt/kontakt.html),
som föreningen ändå håller uppdaterad – då slipper den här sajten bli fel efter
varje stämma. Lägg inte tillbaka namn eller personliga adresser.

### Översikten är avsiktligt nästan tom

`index.html` innehåller fyra saker och ingenting annat:

1. **Rubrik och ansvarsfriskrivning.** Att sajten inte är styrelsens, med länk
   till sjotungan.se. Det står överst för att ingen ska tro att de läser
   föreningens officiella information.
2. **Fem siffror** om föreningen – lägenheter, hus, byggår, markyta,
   medlemsantal. Inget mer.
3. **Tre saker som faktiskt påverkar ett köpbeslut**: att området sköts om
   (med bilder), att en bilplats kostar 250 kronor i månaden, och de nya
   grillplatserna.
4. Sidfoten från `build.py`.

Det som låg här tidigare – korten till rollsidorna, *Om föreningen* med
org.nr och fastighetsbeteckningar, *Bra att veta*, innehavstabellen, *Aktuellt*
och styrelseavsnittet – är borttaget. Rollsidorna nås via menyn, och resten
finns i årsredovisningen som menyn länkar till. Lägg inte tillbaka något av det
utan att först svara på vem utifrån som letar efter det.

## Struktur och bygge

Sidhuvud, meny och sidfot finns på **ett** ställe. `build.py` sätter ihop dem med
innehållet från `src/pages/` och skriver färdiga HTML-filer i projektroten.

Innehållet ligger i två lager. En **sida** bestämmer ordning och layout. Ett
**innehållsblock** beskriver en sak i området – lekplatsen, gymmet,
hundrastgården – och hämtas in på de sidor där den hör hemma. Texten om en
anläggning står därmed på ett ställe även när den syns på flera sidor.

```text
build.py                bygger sajten – här bor meny, sidhuvud, sidfot och ikoner
src/pages/*.html        sidorna, ett <main> per sida: ordning och layout
src/blocks/*.html       innehållsblocken, en anläggning per fil
*.html                  genererade filer (checkas in, skrivs över vid bygge)
assets/css/style.css    designsystem (färger, typografi, komponenter)
assets/js/site.js       enda skriptet: mobilmeny och undermenyer
assets/images/courtyards/   bilder på gårdarna till index.html (JPEG): lusthuset
                        och äppelträdet
assets/images/grill/    bilder på grillplatserna (JPEG), en fil per plats:
                        img_2602.jpg vid Myggdalsvägen 16, img_2603.jpg vid 26
                        img_2604.jpg är en ännu oidentifierad plats och visas
                        i galleriet över gårdarna på index.html
assets/images/car/       bild på laddboxen till car.html (JPEG)
assets/images/gym/      bilder till gymavsnittet på fitness.html (JPEG) + posterbild
assets/images/outdoor-gym/  bilder till utegymmet på fitness.html (JPEG)
assets/images/playground/   bilder till lekplatserna på family.html (JPEG),
                        en mapp per lekplats: m10/, m62/ – m40 och m110 saknar bilder
                        m62/img_2583.jpg visas även i galleriet på index.html
                        karta.jpg är översiktskartan (Googles material, se nedan)
assets/images/dogs/     bild på hundrastgårdens grind till dogs.html (JPEG),
                        karta.jpg är samma översiktskarta med rastgården markerad,
                        whatsapp.jpg är en maskad skärmbild ur hundgruppen (se nedan)
assets/images/bicycle/   bild på cykelställen utanför porten till bicycle.html (JPEG)
assets/images/cycle-routes/ kommunens avståndskartor på bicycle.html (JPEG, ej egna)
assets/video/           gym-tour.mp4
```

```sh
python3 build.py
```

Inga beroenden utöver Python 3. De genererade filerna checkas in, så GitHub
Pages kan servera dem rakt av utan byggsteg.

> **Redigera aldrig `index.html` och de andra filerna i roten.** De skrivs över
> vid nästa bygge. Innehåll ändras i `src/blocks/` och `src/pages/`, allt
> gemensamt i `build.py`.

### Innehållsblock

Ett block är en fil i `src/blocks/`, döpt efter saken den beskriver –
`lekplatser.html`, `gardarna.html`. Filen innehåller rubrik, ikon och text, men
ingen inramning:

```html
<!--
title: Lekplatser
icon: kite
-->

<p>Fyra lekplatser ligger utspridda på gårdarna – vid Myggdalsvägen 10, 40, 62 och 110 …</p>
```

En sida hämtar in blocket med `{{block:namn}}`, ensamt på en rad. Raden får den
indragning som platsen kräver, och blocket skrivs in med samma:

```html
<div class="grid grid--2">
  {{block:lekplatser}}
  {{block:fotbollsplan}}
</div>
```

Inramningen väljs av sidan, inte av blocket, med `{{block:namn:variant}}`:

| Variant | Ger | Används när |
| --- | --- | --- |
| `card` (standard) | `<article class="card">` med ikon och `h3` | blocket står i ett rutnät bland andra |
| `link-card` | samma kort, men hela ytan är en länk | blocket pekar ut ur sajten – kräver `href` och `more` i metadatan |
| `section` | `<div class="section__head">` med `h2` och ingress, resten under | blocket är ett helt avsnitt med egen rubrikdel |
| `prose` | `h2` och innehållet | blocket ligger i en `.prose` eller `.split` |
| `subsection` | `h3` och innehållet | sidan har redan satt en `h2` över |
| `text` | bara innehållet | sidan sätter rubriken själv, eller ingen alls |

`section` delar innehållet: **första stycket blir ingressen** i sidhuvudet och
resten hamnar under. Skriv därför blocket med den mening som ensam duger som
svar först, och detaljerna – tabellen, faktarutan, bildraden – efter.

Därför ska ett block innehålla text och länkar – aldrig `<article class="card">`
eller något annat som låser fast hur det ser ut. Det är det som gör att samma
block kan vara ett kort på en sida och ett helt avsnitt på en annan. Marginaler
mellan block hör också till sidan: sätt `<div class="mt-md">` runt inhämtningen
i stället för att lägga klassen i blocket.

**Vad som blir ett block:** en namngiven sak i eller kring området – en
anläggning, en regel, en plats i närheten – eller ett avsnitt som kan behövas på
mer än en sida. Sidorna behåller sitt eget: `page-head`, rutnät och `section`,
bildrader med sidegna bildtexter, och text som bara hör hemma där.

Bygget avbryter med ett felmeddelande om ett block saknas, om varianten inte
finns, om ett block hämtar in sig självt eller om `{{block:…}}` står mitt i en
rad i stället för ensamt på sin.

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

### Bilderna och videon

Originalen till gymmet, utegymmet och lekplatserna kommer från en iPhone. De ligger inte i
repot – `.gitignore` håller
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

#### Kartbilderna är inte våra

`assets/images/cycle-routes/` är det enda undantaget: fyra JPEG-filer hämtade
rakt av från Tyresö kommuns sida *Cykelvägar i Tyresö*. De är kommunens
material, inte föreningens, och används oförändrade med källhänvisning under
bilderna. Se förbehållet under *Var uppgifterna kommer ifrån*.

De har egen CSS – `.gallery--map` i `style.css` – eftersom fotogalleriet
beskär till 4:3 och zoomar vid hover. Kartorna har teckenförklaringen i nedre
vänstra hörnet och skulle förlora den vid beskärning. Bilderna har dessutom
`width`/`height` i HTML, och utan `height: auto` sätter `height`-attributet
höjden till 460 px så att `object-fit` lägger tomma fält över och under kartan.

## Kör lokalt

Öppna `index.html` direkt i webbläsaren, eller starta en enkel server:

```sh
python3 -m http.server 8000
# http://localhost:8000
```

## Var uppgifterna kommer ifrån

Allt sakinnehåll är hämtat från föreningens egna publicerade källor, plus
Tyresö kommun för det som ligger utanför föreningens mark. Sidorna innehåller
inga påhittade uppgifter.

| Innehåll | Källa |
| --- | --- |
| Ekonomi, nyckeltal, innehav, styrelse, underhållsplan | [Årsmöteshandlingar 2026 med årsredovisning 2025](https://www.sjotungan.se/public_html/new2016/images/information/arsmotes_handlingar/2026/stamma2026.pdf) (PDF) |
| Parkering, hundar, tvättstugor, bastu, gym, sopor | [Sjötungan A–Ö](https://www.sjotungan.se/public_html/new2016/a-o/a-o.html) |
| Adresser, org.nr, e-post, styrelsens roller | [Kontakt](https://www.sjotungan.se/public_html/new2016/kontakt/kontakt.html) |
| Felanmälan och journummer | [Felanmälan](https://www.sjotungan.se/public_html/new2016/forvaltning/felanmalan.html) |
| Gymavgiften, 50 kr per medlem och månad | Uppgift från styrelsen – står inte på sjotungan.se |
| Cykelrum i nästan alla hus, långtidsförråd i M10 | Uppgift från styrelsen – A–Ö anger M6, se nedan |
| Att grillplatserna är upprustade | Uppgift från styrelsen – står inte på sjotungan.se, se nedan |
| Bilderna på gårdarna, grillplatserna, lekplatsen och äppelträdet på översikten | Egna bilder tagna på plats i juli–augusti 2026 |
| Att grillplatserna i avsnittet ligger vid Myggdalsvägen 16 och 26 | Lokal uppgift – står inte i någon källa, se nedan |
| Koordinaterna bakom ”Visa på karta” vid grillplatserna | Platsdata ur originalbilderna, se nedan |
| Vad som står på grillplatserna: grill, bänkar, bänkbord och pergola | Framgår av bilderna |
| Att lekplatserna är fyra, vid Myggdalsvägen 10, 40, 62 och 110 | Lokal uppgift – A–Ö säger inget om läge eller antal, se nedan |
| Koordinaterna bakom ”Visa på karta” vid varje lekplats | Lokal uppgift – stämmer mot översiktskartan, se nedan |
| `assets/images/playground/karta.jpg` | Utsnitt ur Google Maps satellitvy – Googles material, tillstånd saknas, se nedan |
| `assets/images/dogs/karta.jpg` | Samma utsnitt, med hundrastgården markerad – Googles material, tillstånd saknas, se nedan |
| Var hundrastgården ligger på kartan | Lokal uppgift – A–Ö anger bara att rastgården finns, inte var, se nedan |
| Koordinaterna bakom ”Visa på karta” vid hundrastgården | Lokal uppgift – stämmer mot bildens platsdata, se nedan |
| Bilden på hundrastgården | Egen bild tagen på plats i augusti 2026 |
| WhatsApp-gruppen ”Hundarna på Myggan” | Uppgift från medlem |
| `assets/images/dogs/whatsapp.jpg` | Skärmbild ur gruppen, maskad – kvar att inhämta: deltagarnas ja, se nedan |
| Att rastgården är inhägnad med nätstängsel och grind | Framgår av bilden |
| Bilderna på lekplatsen vid Myggdalsvägen 10 | Egna bilder tagna på plats i augusti 2026 |
| Kulturskolans ämnen, åldrar 5–19 och läge i Kvarnhjulet | [Tyresö kulturskola](https://www.tyreso.se/tyreso-kulturskola.html) |
| Förskolan Gunghästen, stadslekplatsen, gångavstånden | Uppgift från styrelsen – ej belagt i källa, se nedan |
| Kommunens cykelnät och cykelkarta | [Cykelvägar i Tyresö](https://www.tyreso.se/boende--miljo/trafik/cykel/cykelvagar-i-tyreso.html) och [cykelkartan](https://mkartan.tyreso.se/cykelkartan), Tyresö kommun |
| Cykelväg längs Myggdalsvägen | Lokal uppgift – kommunens sida namnger inga gator, se nedan |
| Cykelställen utanför porten | Egen bild tagen på plats i augusti 2026, se nedan |
| Avstånden bil/cykel för Öringe, Krusboda, Trollbäcken och Tyresö strand | Avläsning ur kommunens fyra kartbilder, se nedan |
| Kartbilderna i `assets/images/cycle-routes/` | Tyresö kommuns egna bilder, kopierade – tillstånd saknas, se nedan |

Ett par saker att känna till innan sidorna publiceras:

- **Avgifter och tider** på A–Ö-sidan var senast uppdaterade 2024-06. Stäm av
  att de fortfarande gäller.
- **Närområdet.** ”Ungefär fem minuters promenad” till kulturskolan och
  stadslekplatsen är en uppgift från styrelsen och inte kontrollerad mot karta.
  Stadslekplatsen har ingen sida hos kommunen – länken går till Google Maps och
  beskrivningen är därför kortare än föreningens egna lekplatser. Kulturskolans
  terminsavgift står inte på kommunens landningssida och är utelämnad. Kontrollera
  avstånden innan publicering; en spekulant som går sträckan märker om det är fel.
- **Journumret** anges olika på två ställen på sjotungan.se: `08–657 64 50` på
  Felanmälan-sidan och i A–Ö, `010–550 21 65` på Förvaltning-sidan. Här används
  det förstnämnda, eftersom det står på två av tre ställen.
- **Årsredovisningen 2025** fastställs på stämman den 2 juni 2026. Siffrorna här
  är hämtade ur handlingarna till den stämman.
- **Styrelsen** namnges inte på sajten, så sidorna behöver inte uppdateras efter
  varje stämma.
- **Grillplatserna.** Att de är upprustade är en uppgift från styrelsen och står
  varken i A–Ö eller i årsredovisningen. Stäm av den. Grillplatserna är flera
  och tas en och en, på samma sätt som lekplatserna: ett block per plats med
  bild och kartlänk. Hittills finns **Myggdalsvägen 16** och **26**. Att de
  ligger just där är en lokal uppgift som inte står i någon källa – vad som står
  på platserna framgår däremot av bilderna.
  **Koordinaterna** i ”Visa på karta” – 59.243267, 18.233162 vid nummer 16 och
  59.242695, 18.232795 vid nummer 26 – är platsdata ur originalbilderna, alltså
  var kameran stod, inte en inmätning av grillarna. Jämförda med lekplatsernas
  koordinater stöder de adresserna olika väl. Sträckan från lekplatsen vid
  nummer 10 till den vid nummer 40 går knappt 90 meter söderut och drygt 30
  österut; grillplatsen vid 26 ligger ungefär två tredjedelar av vägen längs den
  sträckan, vilket är precis vad numret säger. Grillplatsen vid 16 ligger
  däremot på tiondelens breddgrad, 30 meter rakt österut, och ligger alltså
  *öster* om den vid 26 trots det lägre numret. Numren växer med andra ord inte
  entydigt åt något håll här, så koordinaterna bekräftar inte adresserna – de
  motsäger dem inte heller, eftersom en grillplats hör till gården och kan ligga
  en bit från den port den döps efter. Det är **ingen oberoende kontroll**: båda
  adresserna behöver någon som känner området bekräfta.
  De övriga grillplatserna har bara ett ”Innehåll kommer”. En av dem syns i
  galleriet över gårdarna (`grill/img_2604.jpg`) – en murad grillplats av
  kullersten, till skillnad från de runda stålgrillarna vid 16 och 26 – men var
  den ligger är inte belagt.
- **Gymavsnittet** på `fitness.html` bygger på bilder tagna i lokalen i juli
  2026 plus uppgifterna om öppettider, åldersgräns och medlemskap från A–Ö.
- **Utegymmet.** Beskrivningen av redskapen bygger på bilder tagna på plats i
  juli 2026 – A–Ö säger inget om utrustningen. Vilket hus utegymmet står vid
  framgår inte av bilderna, så sidan säger bara ”intill ett av husen”.
- **Lekplatserna.** Utrustningen som räknas upp – gungor, rutschkana,
  klätternät, fjädergungor, karusell, balansbana och sandlådor – bygger på
  bilder tagna på plats i juli och augusti 2026. A–Ö säger inget om
  utrustningen. Att lekplatserna är fyra och ligger vid Myggdalsvägen 10, 40,
  62 och 110 framgår inte av bilderna utan är en lokal uppgift, se tabellen
  ovan. Lekplatserna vid Myggdalsvägen 40 och 110 är ännu inte fotograferade
  och har därför bara ett ”Innehåll kommer”.
- **Koordinaterna i kartlänkarna.** Varje lekplatsblock har en ”Visa på
  karta”-länk till Google Maps med lekplatsens koordinater, i samma form som
  länken till stadslekplatsen. De fyra punkterna har jämförts med de gula
  markeringarna i `karta.jpg`: de sammanfaller på cirka tre meter när, och
  ordningen väster–öster är densamma som gatunumrens. Koordinaterna och kartan
  är alltså inbördes konsekventa. Båda kommer däremot från samma håll, så det är
  **ingen oberoende kontroll** av att en lekplats verkligen finns på var och en
  av punkterna – det behöver någon som känner området bekräfta. Ingen karta
  bäddas in: länken är en vanlig länk ut, så sidan hämtar fortfarande ingenting
  från andra servrar och behöver ingen cookie-ruta.
- **Hundrastgårdens läge.** A–Ö säger att föreningen har en hundrastgård, men
  inte var den ligger. Den gula markeringen i `assets/images/dogs/karta.jpg`
  och koordinaterna 59.241586, 18.233730 i ”Visa på karta” är lokala uppgifter
  och står inte i någon källa. Tre saker stämmer däremot inbördes. Räknar man om
  lekplatsernas fyra koordinater till bildpunkter – kartutsnittet är detsamma –
  hamnar de på sina gula markeringar med ett par meters fel, och samma räkning
  lägger hundkoordinaten cirka 6 meter från mitten av den gula markeringen,
  alltså väl innanför den. Bilden på grinden är tagen på plats och bär
  platsdata 59.241837, 18.233620, knappt 30 meter därifrån och strax utanför
  markeringens kant – rimligt för någon som står utanför staketet. Det är
  fortfarande **ingen oberoende kontroll**: allt kommer från samma håll. Kartan
  är samma utsnitt som lekplatskartan, så måtten och rotationen nedan gäller
  även den.
- **Skärmbilden ur WhatsApp-gruppen.** `assets/images/dogs/whatsapp.jpg` är en
  maskad kopia av `IMG_2613.PNG`. Övertäckt med heltäckande rutor är: de tre
  raderna med avsändarnamn, mobilnumret i den mittersta bubblan,
  deltagarraden under gruppnamnet i sidhuvudet och de tre profilbilderna, varav
  två visar ett ansikte. Rutorna är ifyllda, inte suddade – suddad eller
  pixlad text går ibland att räkna tillbaka, en ifylld ruta gör det inte.
  Originalet är ignorerat i `.gitignore` så att klartexten inte hamnar i
  historiken.
  **Två saker är kvar och kan inte lösas med maskning.** Bilden i det översta
  meddelandet är tagen inne i någons kök, och samtalet är hämtat ur en privat
  chatt: i en förening där alla känner varandra vet man vem som skrev vad även
  utan namnen. Innan sidan publiceras behöver de tre som syns i tråden säga ja
  till att just den här skärmbilden ligger ute. Vill man slippa frågan går
  avsnittet lika bra att illustrera med fotot från rastgården, eller utan bild.
- **Ingen inbjudningslänk till gruppen** står på sidan: en sådan länk fungerar
  för vem som helst som hittar den, alltså också för folk utanför föreningen.
  Hur man går med är i stället formulerat som ”fråga en granne med hund” – stäm
  av att det är den väg gruppen själv vill ha.
- **Bilden på hundrastgården.** `assets/images/dogs/img_2611.jpg` är egen, tagen
  på plats 2026-08-01. Att rastgården är inhägnad med nätstängsel, har en grind
  och består av skogsmark med berg i dagen syns i bilden – A–Ö säger inget om
  någotdera. Att bänkbordet en bit in står innanför staketet är däremot en
  tolkning av bilden, inte något som säkert går att se. Platsdata följde inte med
  in i webbversionen, till skillnad från de tidigare bilderna på lekplatser och
  gym, som fortfarande har sina koordinater kvar i filen.
- **Översiktskartorna `karta.jpg` är inte våra.** De två – lekplatserna och
  hundrastgården – är utsnitt ur Google Maps satellitvy med gula markeringar
  inlagda; lekplatskartan har fyra, hundkartan en. Google Maps-innehåll får
  återges med korrekt källhänvisning, men **något tillstånd är inte inhämtat**,
  och skärmbilderna är beskurna så att Googles egen attributionsrad längst ned
  inte följde med. Sidorna anger källan i en `credit`-rad under bilden. Vill man
  stå helt rätt bör bilderna tas om med attributionsraden kvar i bild, eller
  ersättas med en egen ritad karta – se förbehållet om kommunens kartbilder
  ovan, det är samma sak en gång till. Bilden är ungefär 439 × 175 meter mark,
  roterad cirka 39 grader, så norr ligger snett upp åt vänster.
- **Fotbollsplan, isbana, utegym och boulebana** finns belagda som
  anläggningar, men A–Ö säger inget om läge eller säsong. Därför står bara att
  de finns. Uppgifterna behöver hämtas från styrelsen innan styckena
  ”Innehåll kommer” kan ersättas.
- **Cykelförrådet.** A–Ö skriver att långtidsförvaringen finns i miljöhuset vid
  **M6** och rymmer ett tjugotal cyklar. Sidan anger **M10** enligt uppgift från
  styrelsen. Stäm av vilket som gäller, och rätta antingen sidan eller A–Ö.
- **Cykelvägen längs Myggdalsvägen.** Kommunens sida *Cykelvägar i Tyresö*
  beskriver cykelnätet men namnger inga gator – vilka sträckor som har cykelväg
  syns bara i [cykelkartan](https://mkartan.tyreso.se/cykelkartan). Att just
  Myggdalsvägen har cykelväg är därför en lokal uppgift. Stäm av den mot kartan,
  och notera att `bicycle.html` inte säger något om cykelvägens sträckning eller
  standard, eftersom det inte går att belägga.
- **Cykelställen utanför porten.** Bilden visar **en** entré, och A–Ö säger
  inget om utomhusställ. Sidan skriver därför ”utanför porten” och inte ”vid
  entréerna” – att alla portar har ställ är inte belagt. Fråga styrelsen innan
  det formuleras om till något som gäller hela området. Husnumret **50** syns på
  skylten i bild; stäm av att adressen hör till föreningen om numret ska nämnas
  i texten.
- **Kartbilderna på `bicycle.html` är kommunens, inte våra.** De fyra bilderna
  under *Cykelavstånd i Tyresö* är kopierade från kommunens sida och ligger nu i
  `assets/images/cycle-routes/`. Sidan anger källan under bilderna, men **något
  tillstånd är inte inhämtat** – bilderna har ingen angiven licens. Fråga
  `karta@tyreso.se`, som står som avsändare på kommunens sida, innan sajten
  publiceras. Blir svaret nej tas avsnittet bort; texten omkring det står på
  egna ben.
- **Ingen av de fyra kartorna visar Sjötungan.** De jämför bil och cykel från
  Öringe, Krusboda, Trollbäcken och Tyresö strand *till* Tyresö centrum, och
  föreningen ligger i den änden sträckorna slutar. Därför säger rubrikstycket
  uttryckligen att ingen sträcka utgår härifrån – skriv inte om det till något
  som antyder att det är föreningens cykelavstånd som visas.
- **Kilometer- och minutsiffrorna i bildtexterna** är avlästa ur bilderna, som
  är daterade 2024 i filnamnet (`-24`). Kommunen anger inget mätdatum. Stäm av
  om bilderna byts ut.
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
