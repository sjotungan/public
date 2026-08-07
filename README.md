# BRF Sjötungan – webbplats

Målet med webbplatsen är att visa vad föreningen är värd att bo i, för
spekulanter och mäklare. Statisk HTML och CSS, inga externa beroenden – sidorna
fungerar även offline. `python3 build.py` bygger om dem.

Den tidigare versionen ligger kvar i [old_version/](old_version/) som arkiv, med
sina egna designnoteringar och sin källförteckning. Den byggs inte.

## Strukturen är byggd för två besök, inte två målgrupper

Det är samma person båda gångerna, och besöken ställer motsatta krav:

1. **Första besöket.** En spekulant som tittar på många lägenheter, kommer från
   mäklarens länk, läser tre minuter i mobilen och scrollar. Det besöket rör
   aldrig menyn. Därför bär `index.html` hela argumentet, i fallande ordning
   efter hur mycket varje sak påverkar ett köpbeslut.
2. **Andra besöket.** Samma person med två eller tre lägenheter kvar på listan,
   som ska försvara några miljoner kronor. Nu är läsaren skeptisk och letar
   efter det som är fel. Det besöket *navigerar* – man kommer tillbaka för en
   bestämd fråga – men den letar aktivt och hittar sidan var den än står i
   menyn.

### Ekonomin är ett hygienkrav, inte ett säljargument

Översikten låg först med ekonomin näst högst upp. Det var fel. Nyckeltalen är
normala snarare än anmärkningsvärda: skuldsättningen är medelmåttig,
soliditeten måttlig, och årsavgiften – knappt 7 000 kronor i månaden för en
snittlägenhet på 83 kvm – har stigit 30 procent på tre år. Sådana tal får ingen
att *välja* Sjötungan. De gör bara att inget diskvalificerar föreningen.

Det som faktiskt lockar är ytan, skötseln och allt det gemensamma. Därför står
det först både på översikten och i menyn, och ekonomin sist på båda ställena –
som avslutande lugnande besked.

Menyn syns för **båda** besöken, och en meny som inleds med *Ekonomi och
underhåll* säger en förstagångsbesökare att sajten handlar om föreningens
siffror. Den som återvänder just för ekonomin letar aktivt och hittar posten
ändå. `ekonomi.html` och `fakta.html` står därför bredvid varandra i slutet,
precis före årsredovisningen: de tre hör ihop som det man kontrollerar med.

### Tesen: allt det här finns för att föreningen är stor

Blocket `stor-forening` är sajtens egentliga argument, och det enda som
förklarar resten. Ett gym, en bastu, en föreningslokal, sex tvättstugor, elva
grillplatser och en borrmaskin kostar nästan ingenting per hushåll när 604
lägenheter delar på dem – i en förening med fyrtio går de inte att ha alls.
Marken likaså: 192 kvm per lägenhet, drygt dubbla bostadsytan.

Det gör dessutom **avgiften begriplig**, vilket ingen siffra i ekonomiavsnittet
klarar: den innehåller värme, vatten, bredband, TV och driften av allt det
gemensamma, och ska jämföras mot vad den täcker. Invändningen mot en stor
förening är att den blir opersonlig – och *Grannarna emellan* är motbeviset.
Låt de två avsnitten stå kvar i den ordningen.

Det som följer av det:

- **Universellt innehåll före uppdelat.** Läget, ekonomin, skicket och vad som
  ingår gäller alla som läser. Rollerna – barn, bil, cykel, hund, träning –
  gäller en del av läsarna och ligger som kort med en rad var, så att den som
  inte har hund hoppar över hunden på en halv sekund.
- **Sajten ber aldrig läsaren välja profil.** Den sorteringen gör mäklaren, som
  har träffat köparen och länkar direkt till rätt sida. Rollsidorna finns för
  att vara länkmål, inte för att vara en meny man klickar sig igenom.
- **Varje sida ska fungera som första sida.** Mäklare djuplänkar.

## Ekonomisidan bryter regeln om minsta möjliga innehåll

Den gamla regeln – *finns uppgiften i årsredovisningen räcker en länk* – är rätt
för det första besöket och fel för det andra. En årsredovisning på 63 sidor är
inte läsbar för en normal spekulant, och "jag kunde inte bedöma ekonomin" landar
som misstanke, inte som neutralt. `ekonomi.html` återger därför årsredovisningen
i läsbar form. Det är ett medvetet undantag för **ett** ämne, inte en öppning
för fler.

### Framhäv inte, men göm inte

Sajten ska sälja, och översikten leder därför aldrig med sitt sämsta tal.
Avgiftshöjningen står inte som nyckeltal på översikten – den hör hemma i
avgiftsavsnittet på `ekonomi.html`, där den läsare som söker den finns.

**Stambytet är ett undantag, för att det inte är en svaghet.** Varje hus från
1968 har ett stambyte framför sig, och den som jämför tre sådana föreningar
jämför tre som alla har det. Skillnaden är att här är det beslutat på stämma,
upphandlat och finansierat med lånelöften – hos de andra ligger det kvar som en
oprissatt post i framtiden. Formulerad så är uppgiften ett skäl att köpa. Skriv
den som *finansierat och planerat*, aldrig som ett förbehåll, och ta inte bort
den: en mäklare som blir överraskad av frågan på en visning slutar använda
sajten, och uppgiften är väsentlig nog att den bör vara känd i en
försäljningsprocess.

Regeln blir alltså: **framhäv inte det obekväma, men göm det inte heller.**
Översikten är säljande, `ekonomi.html` är fullständig. Det är samma
uppdelning i två besök som resten av strukturen bygger på.

### Skriv möjligheten, inte förbudet

Den gamla sajten var skriven för medlemmar, och då är regler själva poängen. För
en spekulant läses samma mening tvärtom: *"Det är inte tillåtet att köra bil
inne i området"* låter som en inskränkning, medan *"Det går inga gator mellan
husen, så barnen kan cykla på gårdarna"* är exakt samma sak formulerad som det
skäl att flytta hit den faktiskt är. Gå igenom varje ny text med den frågan.

Av samma skäl togs det här bort ur sidorna – blocken ligger kvar i
`src/blocks/`, de hör hemma på sjotungan.se:

- **Ordningsregler**: kopplingstvång, plocka upp, parkera på sin plats,
  uppställningstider, körning i området, varför reglerna ser ut som de gör.
- **Handhavande**: hyra eller säga upp en plats, teckna laddavtal, laddkabel.
- **Parkeringsövervakning.** En spekulant läser ett bevakningsbolags
  telefonnummer som en varning, inte som en upplysning.

**Inga synliga "Innehåll kommer".** På en säljande sajt läses en sådan rad som
att sidan är övergiven. Luckor står som HTML-kommentar i blocket och i listan
nedan – aldrig i texten besökaren ser. Skriv hellre en kortare färdig mening än
en längre med ett hål i.

## Sidor

Tabellen står i menyns ordning: det som lockar först, det som kontrolleras sist.

| Fil | Sida i menyn | Vad sidan gör |
| --- | --- | --- |
| [index.html](index.html) | Översikt | Hela argumentet i scrollordning: fotohjälte, sex siffror, området, *Det här ingår i boendet*, tesen om den stora föreningen, rollkorten, grannarna emellan, gemensamt, grillplatserna – och ekonomin sist |
| [laget.html](laget.html) | Läget | Karta, direktbussen till city, tillgänglighet, närområdet, rådjursfilmen |
| [bilder.html](bilder.html) | Bilder | Sajtens alla bilder i ett galleri, samlas in vid bygget |
| [family.html](family.html) | För dig … med barn | Lekplatser, gårdar, fotbollsplan, isbana, förskola och kulturskola |
| [car.html](car.html) | För dig … med bil eller MC | Platser, garage, laddning, MC, däckförvaring |
| [bicycle.html](bicycle.html) | För dig … på cykel | Cykelrum, långtidsförråd, cykelvägarna utanför |
| [dogs.html](dogs.html) | För dig … med hund | Hundrastgården, Wättinge, hundägarnas grupp |
| [fitness.html](fitness.html) | För dig … som tränar | Gym, bastu, utegym, boulebana |
| [ekonomi.html](ekonomi.html) | Ekonomi och underhåll | Nyckeltalen förklarade, stambytet, avgiftsutvecklingen, allt underhåll år för år |
| [fakta.html](fakta.html) | Fakta | Allt i faktarader, i den form uppgifter jämförs i mellan föreningar |

*Det här ingår i boendet* på översikten är ett register över allt föreningen
har, en rad per sak. Det finns för att **varken spekulanten eller mäklaren vet
vad som ingår** – en gästlägenhet, en ungdomslägenhet, ett gym för 50 kronor i
månaden, en bastu, en föreningslokal utan kostnad och en borrmaskin att låna
står inte i annonsen och går inte att läsa sig till någon annanstans. Håll
listan uppdaterad; den är sajtens tydligaste skäl att finnas.

Listan är ordnad efter hur ovanliga sakerna är, och **lägenheterna är det
ovanligaste föreningen har**: en gästlägenhet och åtta ungdomslägenheter utöver
de 604 är inget en spekulant har sett i någon av de andra föreningarna på
listan, och det är tesen i `stor-forening` i två rader. De ligger tills vidare i
*Att låna, boka och hyra* som står som andra grupp – flytta upp den när
ungdomslägenheternas status är avgjord.

## Vad som fortfarande saknas

Här står **varför** en uppgift saknas och hur den ska skrivas när den finns.
Själva att-göra-listan står i [TODO.md](TODO.md), en rad per fråga – håll de två
i takt när något fylls i.

Luckor står som HTML-kommentar i blocket, aldrig som synlig text på sidan. Skriv
inte in gissningar.

- **Kommunikationer** (`kommunikationer`-blocket) – i huvudsak ifyllt och
  kontrollerat mot SL:s reseplanerare 2026-08-07: avgång 08:01 från Tyresö
  centrum är framme på Vattugatan 08:34, 33 minuter utan byte. Direktbussarna
  går **bara i pendlingstid på morgonen**; övrig tid reser man via
  Gullmarsplan.

  Avgången går med **buss 813C mot Stockholm C**, har **två hållplatser** på
  vägen och SL anger **"Sittplatser finns"** – man reser in sittande. Bevis:
  `assets/images/transit/sl-813c.jpg`, en skärmbild ur reseplaneraren som ligger
  på sidan med källhänvisning, på samma sätt som Google-kartan på `laget.html`.

  **Skriv ändå inte ut ett linjenummer** som *den* direktbussen. En tidigare
  version påstod att 812C gick direkt hela vägen på vardagar – 812C är i själva
  verket andra sträckan i en resa med byte. 813C står som den avgång
  uppslagningen gällde, inte som den enda; C-linjerna varierar mellan turer.

  Kvarstår: **hemresan från city på eftermiddagen** (aldrig kontrollerad),
  **vilka linjer som stannar vid hållplatsen på Myggdalsvägen** och
  **gångavståndet dit** från området.

  Båda uppslagningarna är länkade från sidan, så en skeptisk läsare kan göra om
  dem själv: sökningen på sl.se och bilrutten i Google Maps.

  SL:s reseplanerare är en JS-applikation och går inte att läsa med en vanlig
  hämtning – kör den i en riktig webbläsare när uppgifterna ska kontrolleras.

- **Bilvägen** (`bil-till-stan`-blocket) – 18,3 km och typiskt 18–30 minuter
  till T-Centralen enligt Google Maps, uppslaget 2026-08-07 med avfärd 07:59.
  Skriv Googles "typiskt"-intervall, inte dagsvärdet: uppslagningen gjordes en
  fredagmorgon i augusti, då trafiken är lättare än normalt.

  **Cykeltiden skrivs medvetet inte ut någonstans.** Google Maps anger 1 tim
  5 min till T-Centralen, och det är ingen pendling någon flyttar hit för – att
  redovisa den vore att sälja in ett dåligt alternativ. Cykelsidan handlar om
  cykeln i vardagen, inte om att ta sig till stan.
- **Hiss per hus** (`tillganglighet`-blocket) – vilka av de 24 husen som har
  hiss. Att samtliga hissar renoverades 2023 är belagt; fördelningen är det
  inte. Viktigt för den som säljer villa och söker sig till lägenhet.
- **Bredbandsleverantör och hastighet** (`bredband`-blocket) – att bredband och
  TV ingår i avgiften är belagt, men inte vilken leverantör eller vilken
  hastighet.
- **Vad som kostar extra** (`det-har-ingar`-blocket) – ingressen säger nu att
  allt ingår i avgiften utom det som står med en kostnad. Fyra rader har pris
  (gym, p-plats, garage, MC-garage) och en är uttryckligen kostnadsfri
  (föreningslokalen). Tio rader är aldrig kontrollerade: bastu, borrmaskin,
  tvättstugor, paketbox, elbilsladdning, gästparkering, cykelrum, cykelförråd,
  barnvagnsrum och däckförvaring.

  Priserna kontrollerades 2026-08-07 mot **föreningens egen A–Ö på
  sjotungan.se**, som visade sig svara på det mesta: gästlägenheten 400 kr/dygn,
  bastun 50 kr per hushåll och månad, laddplatsen 425 kr/mån utöver
  garageavgiften, gästparkeringen avgiftsbelagd, paketboxen gratis och
  ungdomslägenheterna åtta stycken för 18–27-åringar. A–Ö är förstahandskällan
  för allt sådant här – gå dit före styrelsen.

  **Gympriset är däremot troligen fel.** Sajten skriver "50 kr i månaden" om
  gymmet på sex ställen, men A–Ö sätter det beloppet på *bastun* och säger bara
  "för en låg kostnad" om gymmet. Femtiolappen ser ut att ha vandrat från bastun
  till gymmet någon gång i skrivandet. Det är sajtens mest upprepade påstående
  och står i ingressen på översikten, så det ska avgöras mot en avgiftsavi och
  rättas på alla sex ställena samtidigt – inte lappas på ett.

  Regeln i ingressen är formulerad så för att ett pris ska läsas som ett
  fynd i stället för som ett förbehåll – femtio kronor för ett gym är ett
  argument – och för att den sätter upp tesen i `stor-forening`, som står
  direkt efter. En lista där varje rad bär ett pris säger tvärtom att avgiften
  köper lägenheten och inget annat.

  Det gör också meningen till ett löfte om hela listan. Kontrollera de tio
  innan blocket ligger uppe; störst risk är däckförvaring och gästparkering,
  som tas betalt för i de flesta föreningar, och laddningen, där strömmen
  alltid mäts. Ett pris som visar sig på visningen i stället för på sidan är
  precis det som får en mäklare att sluta använda sajten.

## Var uppgifterna kommer ifrån

Ekonomi, ytor och underhållshistorik kommer ur **årsredovisningen för 2025**
(räkenskapsåret 2025-01-01–2025-12-31, beslutad av styrelsen 2026-06-02), länkad
i menyn.

**Stambytets etapper och tidplan** kommer däremot ur föreningens egen
[projektsida för stambytet](https://www.sjotungan.se/public_html/new2016/aktuellt/aktuellaArbeten-stambyte.html),
hämtad i mars 2026. De två källorna säger olika saker och ska hållas isär:

| | Årsredovisningen 2025 | Projektsidan |
| --- | --- | --- |
| Period | 2026–2035 i underhållsplanen, för posten inkl. trapphusupprustning | 2026–2030 för stambytet |
| Slutår | anges inte för stambytet | 2030 |
| Etapper | nämns inte | fem huvudetapper, en i taget |

Sajten skriver **2030**, för att det är föreningens aktuella uppgift om själva
stambytet, och nämner underhållsplanens 2026–2035 i underhållstidslinjen så att
den som slår upp årsredovisningen inte tror att sidan har fel.

**Etappuppgifterna åldras.** De är daterade i texten och länkade till
projektsidan. Gå igenom dem när en ny etapp annonseras – en spekulant som möter
en gammal uppgift slutar tro på resten av sajten. Sifferuppgifter som inte står
i någon av de två källorna ska inte stå här.

Två fel har rättats under arbetet och är värda att inte upprepa: skuldsättningen
per kvm **steg** 2022–2024 och sjönk först 2025 (inte "sjunkit två år i rad"),
och 2035 är underhållsplanens periodslut för hela posten – inte stambytets
slutår. Kontrollera varje trend mot flerårsöversikten innan den skrivs ut.

Övriga uppgifter – anläggningarna i området, avgifterna för parkering, det
grannarna ordnar – har källförteckningen i
[old_version/README.md](old_version/README.md).

## Länkar ut från sajten

`build.py` går igenom det färdiga dokumentet och ger **varje länk till en annan
webbplats** `target="_blank"`, `rel="noopener"` och en dold text
`(öppnas i ny flik)`. Skriv alltså aldrig in attributen för hand – det sker på
ett ställe för ett femtiotal länkar, inklusive årsredovisningen i menyn och
sjotungan.se i sidfoten.

Skälen till de tre delarna:

- **Ny flik**, för att sajten finns för att någon ska läsa färdigt. Den som
  klickar på en karta eller på årsredovisningen ska inte behöva hitta tillbaka.
- **`rel="noopener"`**, för att den öppnade sidan annars kan nå `window.opener`
  och styra om vår flik till en annan adress.
- **Den dolda texten**, för att den som inte ser skärmen annars bara märker att
  bakåtknappen slutat fungera. Den ligger i `.sr-only`, som måste förbli
  1 × 1 px och synlig för webbläsaren – `display: none` eller nollstorlek tar
  bort texten ur tillgänglighetsträdet och då läses den inte upp alls.

`mailto:` rörs inte, och inte heller relativa länkar – bildernas länkar till
originalfilerna öppnas i samma flik och stängs med bakåtknappen.

## Innehållsblock

`build.py` sätter ihop sidhuvud, meny och sidfot; sidorna ligger som fragment i
`src/pages/` och hämtar in innehållsblock från `src/blocks/` med
`{{block:namn}}` eller `{{block:namn:variant}}`, ensamt på en rad. Varianter:
`card`, `link-card`, `section`, `prose`, `subsection`, `text`.

Ett antal block från den gamla sajten ligger kvar utan att vara inhämtade
någonstans: beskrivningarna av de elva grillplatserna var för sig och av de
enskilda tvättstugorna. De är detaljer snarare än beslutsunderlag och togs ur
översikten när den kortades. Blocken är kvar för den som vill lägga dem på en
egen sida.

Filnamn, id:n och CSS-klasser är på engelska; all text som besökaren ser är på
svenska.

## Kör lokalt

```sh
python3 build.py
python3 -m http.server 8000
# http://localhost:8000
```
