# Att ta reda på

Öppna frågor, en rad var. **Varför** en uppgift saknas och hur den ska skrivas
när den finns står i [README.md](README.md#vad-som-fortfarande-saknas) – här
står bara vad som ska fram och av vem.

Skriv aldrig in en gissning. En kortare färdig mening är bättre än en längre med
ett hål i.

## Först: gympriset kan vara fel på fem ställen

Sajten påstår **"ett gym för 50 kronor i månaden"** i `gym`-blockets text och i
dess faktaruta, i `kort-traning`, på raden i `det-har-ingar` och i README.
Föreningens egen A–Ö säger något annat:

- bastun kostar **"50 kr per hushåll per månad"**
- gymmet beskrivs bara som **"för en låg kostnad"**, utan belopp

Femtiolappen ser alltså ut att vara bastuns avgift som vandrat över till gymmet.
Det är sajtens mest upprepade enskilda påstående. (Det stod tidigare även i
ingressen på översikten – den är borta sedan 2026-08-17, men talet står kvar i
`kort-traning`, som ligger på samma sida.)

Omkontrollerat mot A–Ö 2026-08-17: oförändrat. Gymmet står fortfarande utan
belopp och femtiolappen sitter fortfarande på bastun. A–Ö kommer alltså inte att
lösa det här – frågan måste till någon som har en avi.

- [ ] **Vad kostar gymmedlemskapet?** Kontrollera mot en avgiftsavi från
      Fastighetsägarna, inte mot A–Ö. Rätta i så fall alla sex ställena samtidigt
- [ ] Betalar man **båda** avgifterna separat om man har gym och bastu?

## Avgjort: laddplatsen kostar 445 kr/mån plus 69 kr för appen

Sajten sa båda talen samtidigt, på sidor som en mäklare läser bredvid varandra.
**445 kr/mån är rätt** – A–Ö:s 425 kr är gammalt. Till det kommer 69 kr/mån för
mobilappen som styr laddningen, plus elförbrukningen. Källa: faktura från Ladda
Tillsammans för juli 2026 och deras support, båda via medlem 2026-08-07. Det är
den som tar betalt, så frågan är stängd.

- [x] `det-har-ingar` rättad från 425 till 445 kr/mån, med appavgiften utskriven
- [x] `parkeringsavgifter` (car.html) och `fakta.html` stod redan rätt
- [x] `parkeringsavgifter` sa att hela tabellen debiteras på avgiftsavin från
      Fastighetsägarna – laddningen faktureras av Ladda Tillsammans. Rättat där
      och i `elbilsladdning`

Kvar: A–Ö visade sig kunna vara inaktuell. Det gör den till en bra men inte
sista källa – de andra A–Ö-priserna i `det-har-ingar` bör vid tillfälle stämmas
av mot en avgiftsavi.

## Bilder

- [x] Grillplatsernas elva foton – samlade i `grillplatser-bilder`, nu på
      `gardarna.html`
- [ ] **Tvättstugornas tolv foton är oanvända.** De låg i blocken
      `tvattstuga-m52`, `tvattstuga-m64` och `grovtvattstuga-m64`, som inte
      hämtas in av någon sida längre. Sex tvättstugor med grov- och snabbtvätt
      är en riktig förmån och står i registret, men tolv bilder av tvättstugor
      är dokumentation snarare än säljande. Förslag: två eller tre
      representativa i ett `tvattstugor-bilder`-block under *Gemensamt för
      alla*, på samma sätt som `grillplatser-bilder`. Beslut behövs om det ska
      bli några alls
- [ ] **`car/img_2587.jpg`** ligger kvar oanvänd. Den hör till `laddkabel`, som
      togs bort som handhavande – ta bort filen eller låt den ligga

**Kontrollera alltid bilderna när ett block slutar användas.** Bildsidan samlar
in figurer från de sidor som byggs, så ett block som ingen sida hämtar in tar
sina foton med sig ut ur hela sajten, galleriet inkluderat. Så försvann alla
elva grillbilderna en gång. Kommandot som visar oanvända bilder står i
[README.md](README.md#vad-som-fortfarande-saknas).

## Vad kostar cykelförrådet, barnvagnsrummet och föreningslokalen?

Blockerade tidigare hela blocket: ingressen sa *"Allt ingår i avgiften, utom det
som står med en kostnad"*, och då påstod varje tyst rad att den var gratis.
Ingressen är borta sedan 2026-08-17, så raderna påstår ingenting längre och
frågan blockerar inte prodsättning.

Den är däremot inte mindre värd att svara på – **tystnad är inte ett svar till
läsaren, bara ett ärligt icke-svar.** Tre rader kan bli säljande av ett besked:

- [ ] **Cykelförrådet** – husens cykelrum är gratis, men gäller det även
      långtidsförrådet, eller finns kö eller avgift dit? Samma svar behövs för
      hur man får plats eller nyckel, se avsnittet om cykelförrådet ovan
- [ ] **Barnvagnsrum** – fritt för alla i huset?
- [ ] **Föreningslokalen** står som "bokas utan kostnad" – A–Ö bekräftar inte
      det, priset ligger på en undersida. Verifiera påståendet

## Ungdomslägenheterna

Åtta stycken, 18–27 år, kategori A är boende i föreningen eller barn till
boende, kategori B är HSB-föreningar i Tyresö. Administrativ köavgift 100 kr/år.

- [x] **Är uthyrningen fortfarande pausad?** Ja, kontrollerat mot A–Ö
      2026-08-17: *"Under stambytet har vi pausat köavgiften för och uthyrandet
      av ungdomslägenheterna."* Stambytet är beräknat klart 2030. Raden sa
      "efter kötid", vilket lovade en kötid som inte finns, och säger nu
      "uthyrningen pausad under stambytet" i stället
- [ ] **Hyran** för en ungdomslägenhet – fortfarande okänd
- [ ] Flytta upp gruppen *Att låna, boka och hyra* först i listan **när pausen är
      hävd** – grupperna står i fallande ordning efter hur ovanliga de är, och nio
      egna lägenheter slår ett gym. Men åtta av de nio går inte att hyra förrän
      stambytet är klart, och då bär de ingen förstaplacering. Väntar på att
      uthyrningen öppnar igen, inte på att raden skrivs om

## Cykelförrådet: huset borttaget, men hur får man plats?

Huset är avidentifierat sedan 2026-08-17, samma regel som däckgaraget – se *Var
förråden ligger står inte utskrivet* i [README.md](README.md).

Det lämnade en lucka som däcktexten inte har. Den kan säga "står i anslaget i
porten", för A–Ö säger att öppettiderna anslås där. För cykelförrådet vet vi
ingenting motsvarande, så texten säger nu bara att förrådet finns.

- [ ] **Hur får en medlem plats eller nyckel till cykelförrådet?** Med det svaret
      kan blocket peka vidare i stället för att sluta i tomma intet, precis som
      däcktexten gör
- [ ] **Är förrådet larmat eller låst med egen nyckel?** Är det det, faller
      invändningen och husbeteckningen kan stå kvar igen – både här och,
      beroende på svaret för garaget, för däcken

## Gästlägenheten och ungdomslägenheterna har inget innehåll alls

De två enda raderna i registret som inte kan länkas vidare: det finns inget block,
ingen sida och inget foto om någon av dem. Alla andra 27 rader leder numera till
ett avsnitt som beskriver saken med bild.

Det är sajtens största innehållslucka, och den sitter på fel rader – README:s tes
är att de nio egna lägenheterna är det ovanligaste föreningen har.

- [ ] **Bilder på gästlägenheten.** Två rum, sex bäddar, pentry och WC med dusch,
      på Myggdalsvägen 28. Ingen bild finns
- [ ] **Ett block om gästlägenheten** – vad den kostar, hur den bokas, vad som
      ingår. Priset är belagt (400 kr/dygn), resten inte
- [ ] **Ungdomslägenheterna** – kan vänta tills pausen är hävd, men hyran och
      kötiden behövs innan raden kan bära en egen sida

## Övriga luckor

- [ ] **Hemresan från city på eftermiddagen** – aldrig kontrollerad. SL:s
      reseplanerare är en JS-app; kör den i en riktig webbläsare
- [ ] **Linjer vid hållplatsen på Myggdalsvägen** och **gångavståndet dit**
- [ ] **Hiss per hus** – vilka av de 24 husen som har hiss. Att alla hissar
      renoverades 2023 är belagt, fördelningen inte. Viktig för den som säljer
      villa

## Klart, hämtat ur A–Ö 2026-08-07

Källa: <https://www.sjotungan.se/public_html/new2016/a-o/a-o.html>

- [x] Gästlägenheten – 400 kr/dygn, en (1) lägenhet på Myggdalsvägen 28, två rum,
      sex bäddar, pentry och WC med dusch. Bara övernattning, inga fester
- [x] Bastun – 50 kr per hushåll och månad, dras på avgiftsavin
- [x] Elbilsladdning – A–Ö säger 425 kr/mån för laddplatsen utöver
      garageavgiften på 6 000 kr/år, men det talet är gammalt: rätt pris är
      445 kr/mån plus 69 kr/mån för appen och elförbrukningen. Utökat från 8
      till 34 platser i Garage B
- [x] Gästparkering – fyra platser, avgiftsbelagda, betalas i app. Parkit sköter
      övervakningen sedan 2024-04-01
- [x] Paketboxen – gratis, på gaveln vid M64, öppen dygnet runt
- [x] Ungdomslägenheterna – åtta stycken, 18–27 år, kötid och kategori

## Klart, hämtat ur A–Ö 2026-08-08

Källa: <https://www.sjotungan.se/public_html/new2016/a-o/a-o.html>

- [x] Bredbandsleverantör och hastighet – Telenor 250/250 Mbit/s ingår i
      avgiften sedan 2021-08-01, uttaget sitter i hallen. TV är en **annan**
      leverantör: Tele2, tidigare Com Hem, med det digitala grundutbudet på
      16 kanaler sedan 2020-09-08. Com Hems bredband finns att teckna vid sidan
      av. Årsredovisningen säger inget om detta – A–Ö är enda källan

## Klart, hämtat ur A–Ö 2026-08-17

Källa: <https://www.sjotungan.se/public_html/new2016/a-o/a-o.html>

- [x] **Ungdomslägenheterna är fortfarande pausade** – se avsnittet ovan. Raden i
      `det-har-ingar` är omskriven efter det
- [x] **A–Ö namnger själv garaget** för däckförvaringen. Vi har tagit bort
      bokstaven ur den här sajten på inrådan från en granne, men uppgiften ligger
      kvar öppet på föreningens officiella sajt. Att ändra det är styrelsens
      beslut, inte vårt – tipsa dem gärna.

      Det är däremot inget skäl att ta tillbaka bokstaven här. Vår borttagning
      står på egna ben: uppgiften är värdelös för spekulanten och mäklaren som
      sidan är skriven för, den finns redan i porten för den som bor här, och den
      enda som har konkret nytta av den är en tjuv. Se kommentaren i
      `dackforvaring`
- [x] **A–Ö säger fortfarande 425 kr/mån för laddplatsen.** Rätt pris är 445 kr
      plus 69 kr för appen, belagt mot faktura. Sidan behöver inte ändras – det
      här är bara ännu en bekräftelse på att A–Ö kan vara gammal
- [x] **Gästparkeringen** – ingen prisuppgift, men Parkit sköter övervakningen
      sedan 2024-04-01 och betalning sker via Easypark, Parkster eller SMS.
      Raden "betalas i app" stämmer

A–Ö svarar **inte** på priset för cykelförrådet, barnvagnsrummen, tvättstugorna,
borrmaskinen, paketboxen eller föreningslokalen. De raderna vilar alltså
fortfarande bara på uppgiften från en medlem nedan, och de tre som står kvar
under *Blockerar* ovan är fortfarande obelagda.

## Klart, uppgift från medlem 2026-08-07

Ingen av de här kostar något. Sedan ingressen togs bort 2026-08-17 skriver de
fyra raderna ut "utan kostnad" själva i `det-har-ingar`, tillsammans med
paketboxen ur A–Ö – de fem är listans enda belagda kostnadsuppgifter.

- [x] **Däckförvaring** – gratis. Skrivet med ord i `dackforvaring`-blocket
      också, eftersom de flesta föreningar tar betalt för det här
- [x] **Tvättstugor** – gratis
- [x] **Borrmaskin** – gratis, ingen deposition
- [x] **Cykelrum** i husen – gratis
