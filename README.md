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
förklarar resten. Ett gym, en bastu, en föreningslokal, sex tvättstugor, tio
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

### Ämnessidor är undantaget från regeln om roller

En ny sida kräver normalt en ny **roll** – barn, bil, cykel, hund, träning – och
inte en ny anläggning. `gardarna.html` är undantaget: *utemiljön* är något varje
köpare bedömer, inte en läsare som känner igen sig i den. "För dig som grillar"
hade varit fel snitt – ingen spekulant identifierar sig som grillare, och ingen
mäklare länkar dit.

Sidan finns för att grillavsnittet hade vuxit ur översikten: 18 procent av
sidans ord och tolv av arton bilder, alltså två tredjedelar av förstasidans
fotografier. Nu ligger grillplatserna, lekplatserna och sportytorna samlade där
de hör hemma, och översikten är nere i sex bilder.

Testet för nästa ämnessida är detsamma: bär den ett ämne som någon utifrån
faktiskt bedömer, och avlastar den översikten? Annars hör innehållet hemma på en
befintlig sida.

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

### Var förråden ligger står inte utskrivet

Sajten ligger öppet på nätet. Att skriva ut exakt var föreningens förråd finns är
därför en upplysning, och frågan är alltid **vem den är till nytta för**:

- **Spekulanten och mäklaren**, som sidorna är skrivna för: ingen nytta alls. De
  har inga däck och inga cyklar stående i föreningens utrymmen. Det som säljer är
  att förvaringen *finns* och är gratis.
- **Den som bor här**: svag nytta, och uppgiften står redan i anslaget i porten,
  som texten kan peka på i stället.
- **Den som vill stjäla ur ett olarmat utrymme**: full nytta. Det är den enda
  läsaren som har konkret användning av en adress.

Är fördelningen sådan, skriv inte ut var det ligger. Skriv att det finns, vad det
kostar och var man får veta resten.

**Det här är inte samma sak som att göra sajten otydlig, och inte ett undantag
från "göm inte" ovan.** Den regeln gäller det obekväma – avgiftshöjningar,
stambytet, sådant en köpare behöver för att bedöma föreningen. En förrådsdörr är
ingen svaghet som göms; det är en driftsdetalj som inte hör till det läsaren ska
bedöma.

Taget bort med detta som skäl, båda 2026-08-17:

- **Vilket garage däcken förvaras i** – ur `dackforvaring` och raden i
  `det-har-ingar`.
- **Vilket hus cykelförrådet ligger i** – ur `cykelforrad-m10` (som också bytte
  rubrik), raden i `det-har-ingar` samt ingressen och sidbeskrivningen på
  `bicycle.html`. En cykel i långtidsförvaring är ett bättre byte än ett däck:
  lätt att bära, lätt att sälja, och ingen tittar till den på flera månader.

Två saker att veta innan någon skriver tillbaka det:

1. **Kommentarerna följer med ut i den byggda HTML-filen.** Uppgiften får alltså
   inte stå i en kommentar som förklarar varför den är borttagen heller – den går
   att läsa i källkoden på sidan.
2. **A–Ö på sjotungan.se skriver ut garaget ändå** (kontrollerat 2026-08-17). Det
   är inget skäl att ta tillbaka det: att uppgiften finns någon annanstans gör den
   inte nyttigare här. Att städa den officiella sajten är styrelsens beslut.

**Barnvagnsrummen är i sin ordning** som de står: *"nedre botten i trapphuset"*
är en sorts plats och inte en adress, och en barnvagn är inget någon bär ut ur
området. Regeln gäller utrymmen som står orörda och innehåller något säljbart,
inte varje mening som nämner var något finns – bastun i M90 och tvättstugorna
står kvar med hus, och ska göra det. De används dagligen.

**Blocknamnen är inte städade.** `cykelforrad-m10` heter fortfarande så i
`src/blocks/`. Blocknamn följer aldrig med ut i den byggda sidan, så de döljer
ingenting – ett byte hade bara rört om i sidorna som hämtar in blocket.

## Sidor

Tabellen står i menyns ordning: det som lockar först, det som kontrolleras sist.

| Fil | Sida i menyn | Vad sidan gör |
| --- | --- | --- |
| [index.html](index.html) | Översikt | Hela argumentet i scrollordning: fotohjälte, sex siffror, området, *Det här finns i föreningen*, tesen om den stora föreningen, rollkorten, grannarna emellan, gemensamt, grillplatserna – och ekonomin sist |
| [laget.html](laget.html) | Läget | Karta, direktbussen till city, tillgänglighet, närområdet, skogen med blåbärsriset och rådjursfilmen |
| [bilder.html](bilder.html) | Bilder | Sajtens alla bilder i ett galleri, samlas in vid bygget |
| [family.html](family.html) | För dig … med barn | Lekplatser, gårdar, fotbollsplan, isbana, förskola och kulturskola |
| [car.html](car.html) | För dig … med bil eller MC | Platser, garage, laddning, MC, däckförvaring |
| [bicycle.html](bicycle.html) | För dig … på cykel | Cykelrum, långtidsförråd, cykelvägarna utanför |
| [dogs.html](dogs.html) | För dig … med hund | Hundrastgården, Wättinge, hundägarnas grupp |
| [fitness.html](fitness.html) | För dig … som tränar | Gym, bastu, utegym, boulebana |
| [ekonomi.html](ekonomi.html) | Ekonomi och underhåll | Nyckeltalen förklarade, stambytet, avgiftsutvecklingen, allt underhåll år för år |
| [fakta.html](fakta.html) | Fakta | Allt i faktarader, i den form uppgifter jämförs i mellan föreningar |

*Det här finns i föreningen* på översikten är ett register över allt föreningen
har, en rad per sak. Det finns för att **varken spekulanten eller mäklaren vet
vad föreningen har** – en gästlägenhet, en ungdomslägenhet, ett gym för 50 kronor i
månaden, en bastu, en föreningslokal utan kostnad och en borrmaskin att låna
står inte i annonsen och går inte att läsa sig till någon annanstans. Håll
listan uppdaterad; den är sajtens tydligaste skäl att finnas.

**Raderna är länkar in i resten av sajten**, 27 av 29. Registret påstod förut 29
saker utan att ge något sätt att kontrollera dem, trots att gymmet, bastun,
grillplatserna och resten stod beskrivna med foton en bit bort – och den som
läste uppifrån och ner hittade rollkorten först två avsnitt längre ner. En
granne som gick igenom sajten upptäckte bilderna först vid andra genomläsningen,
och det var beviset: hittar inte den som letar, hittar ingen. Länkarna kopplar
ihop påstående och underlag utan att översikten växer en rad.

Skriv därför aldrig en ny rad i registret utan att fråga vart den ska peka. Finns
det inget mål är det raden som saknar innehåll, inte länken som saknas – och då
hör den hemma i [TODO.md](TODO.md). Gästlägenheten och ungdomslägenheterna är de
två som står så i dag.

Listan är ordnad efter hur ovanliga sakerna är, och **lägenheterna är det
ovanligaste föreningen har**: en gästlägenhet och åtta ungdomslägenheter utöver
de 604 är inget en spekulant har sett i någon av de andra föreningarna på
listan, och det är tesen i `stor-forening` i två rader. De ligger i *Att låna,
boka och hyra* som står som andra grupp, och där står de kvar: uthyrningen av
ungdomslägenheterna är pausad under stambytet, beräknat klart 2030 (A–Ö
2026-08-17). Åtta lägenheter som ingen kan hyra på flera år bär ingen
förstaplacering. Flytta upp gruppen när pausen är hävd.

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
- **Bredband och TV** (`bredband`-blocket) – **Telenor 250/250 Mbit/s** sedan
  2021-08-01, uttaget i hallen, och **TV från Tele2**, tidigare Com Hem, med det
  digitala grundutbudet på 16 kanaler sedan 2020-09-08. Kontrollerat 2026-08-08
  mot A–Ö, som är enda källan – årsredovisningen nämner varken leverantör eller
  hastighet.

  **Att det är två olika bolag skrivs ut med flit.** "Bredband och TV ingår"
  läses annars som ett avtal hos en leverantör, och den som ringer fel bolag om
  TV-kanalerna får svaret att han inte är kund. Skriv inte ihop dem igen.
- **Vad som kostar extra** (`det-har-ingar`-blocket) – varje rad bär sin egen
  kostnadsuppgift, eller ingen alls. Blocket hade tidigare en ingress som slutade
  *"Allt ingår i avgiften, utom det som står med en kostnad"*, och då betydde en
  tyst rad att den ingick. Ingressen togs bort inför prodsättning 2026-08-17 och
  regeln försvann med den.

  Kvar står: rader med pris (gym, p-plats, garage, MC-garage, laddplats,
  gästlägenhet), fem rader med utskrivet "utan kostnad" som är kontrollerade
  (däckförvaring, tvättstugor, borrmaskin, cykelrum, paketbox) – och resten
  tysta, vilket nu inte påstår någonting. **Det är en förbättring, inte en
  lucka:** ett tjugotal rader vilade förut på en enda mening, och sex av dem var
  aldrig kontrollerade.

  Kvar att belägga: cykelförrådet, barnvagnsrummen och föreningslokalens "bokas
  utan kostnad" – den sista är den enda rad som fortfarande påstår något
  obelagt.

  Priserna kontrollerades 2026-08-07 mot **föreningens egen A–Ö på
  sjotungan.se**, som visade sig svara på det mesta: gästlägenheten 400 kr/dygn,
  bastun 50 kr per hushåll och månad, gästparkeringen avgiftsbelagd, paketboxen
  gratis och ungdomslägenheterna åtta stycken för 18–27-åringar. A–Ö är
  förstahandskällan för allt sådant här – gå dit före styrelsen.

  **Laddplatsen är undantaget som visar att A–Ö kan vara gammal.** Där står
  425 kr/mån; rätt pris är 445 kr/mån utöver garageavgiften plus 69 kr/mån för
  mobilappen som styr laddningen. Källan är starkare än A–Ö: en faktura från
  Ladda Tillsammans för juli 2026 och deras support, båda via medlem
  2026-08-07 – den som tar betalt säger själv vad det kostar. Talen står numera
  lika i `det-har-ingar` och `parkeringsavgifter`, alltså på översikten,
  car.html och fakta.html.

  Fakturan avslöjade också ett fel bredvid priset: `parkeringsavgifter` sa att
  hela tabellen debiteras på avgiftsavin från Fastighetsägarna, men laddningen
  faktureras av Ladda Tillsammans. Två avsändare, inte en.

  **Gympriset var misstänkt men rätt.** Sajten skriver "50 kr i månaden" om
  gymmet på fem ställen, och A–Ö sätter samma belopp på *bastun* men säger bara
  "för en låg kostnad" om gymmet. Det såg ut som att femtiolappen vandrat mellan
  dem. Uppgift från granne 2026-08-19: båda kostar 50 kr i månaden. Det var
  likheten som såg ut som ett fel, och inget behövde rättas.

  Lärdomen är värd att behålla: **A–Ö kan sakna en uppgift utan att motsäga den.**
  Att beloppet stod på bastun och inte på gymmet var inget bevis för att gymmet
  var fel – bara för att A–Ö inte svarade. Skilj "obelagt" från "motsagt" innan du
  river upp en text.

  **Priser läses som fynd, inte som förbehåll.** Femtio kronor för ett gym är ett
  argument, och det är därför prissatta rader hör hit i stället för att gömmas.
  Men en lista där *varje* rad bär ett pris säger tvärtom att avgiften köper
  lägenheten och inget annat. Skriv därför pris där det finns ett, och skriv
  ingenting där det inte är kontrollerat – aldrig en gissning i någon riktning.

  Ett pris som visar sig på visningen i stället för på sidan är precis det som
  får en mäklare att sluta använda sajten. Det var det starkaste skälet att ta
  bort ingressens löfte om hela listan: sidan lovade gratis för sex rader som
  ingen hade kontrollerat.

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
någonstans: beskrivningarna av de tio grillplatserna var för sig och av de
enskilda tvättstugorna. De är detaljer snarare än beslutsunderlag och togs ur
översikten när den kortades. Blocken är kvar för den som vill lägga dem på en
egen sida.

**Kontrollera bilderna när ett block plockas bort.** Bildsidan samlar in figurer
från de sidor som faktiskt byggs, så ett block som ingen sida hämtar in tar sina
foton med sig ut ur hela sajten – också ur galleriet. När grillplatsernas egna
avsnitt togs bort försvann därför alla elva grillbilderna, och kvar stod ett
påstående om tio grillplatser utan en enda bild. De ligger nu samlade i
`grillplatser-bilder`, med adressen i varje bildtext eftersom bilden i galleriet
inte längre står under en rubrik som säger vilken plats det är.

### Bilder utan sida

Regeln är att varje foto står under ett påstående det styrker. Det är den regeln
som håller nere antalet bilder, och den gäller fortfarande. Men ett foto kan
vara värt att visa utan att bevisa något, och tvingar man in ett sådant på en
ämnessida får den sidan bära en bild som inte hör till dess ärende.

Sådana bilder skrivs som vanliga `<figure>` direkt i `src/pages/bilder.html`,
mellan sidhuvudet och `{{gallery}}`. `build.py` lyfter ut dem ur sidan och
lägger dem **sist** i galleriet – de står alltså inte kvar där de skrevs, och
sidan har ett enda galleri, inte två. Bygget skriver ut hur många de är:

```text
bildsidan: 65 bilder, varav 0 egna
```

**Bildtexten måste bära sig själv.** En sådan bild står aldrig under en rubrik
som säger var den är tagen – den har ingen sida att stå på. Det är samma problem
som grillbilderna fick när de hamnade i galleriet, fast permanent: skriv ut plats
och sammanhang i `figcaption`, inte "en av gårdarna". `alt` och `figcaption`
följer med bilden in i galleriet, eftersom det är hela `<figure>` som flyttas.

Kommandot som visar vilka bilder som blivit oanvända:

```sh
comm -23 \
  <(find assets/images -type f | sed 's|^|/|' | sort) \
  <(grep -oh 'assets/images/[^"]*' *.html | sed 's|^|/|' | sort -u)
```

Filnamn, id:n och CSS-klasser är på engelska; all text som besökaren ser är på
svenska.

## Kör lokalt

```sh
python3 build.py
python3 -m http.server 8000
# http://localhost:8000
```
