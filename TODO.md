# Att ta reda på

Öppna frågor, en rad var. **Varför** en uppgift saknas och hur den ska skrivas
när den finns står i [README.md](README.md#vad-som-fortfarande-saknas) – här
står bara vad som ska fram och av vem.

Skriv aldrig in en gissning. En kortare färdig mening är bättre än en längre med
ett hål i.

## Först: gympriset kan vara fel på sex ställen

Sajten påstår **"ett gym för 50 kronor i månaden"** i `gym`-blocket,
`kort-traning`, `det-har-ingar`, ingressen på översikten och två gånger i
README. Föreningens egen A–Ö säger något annat:

- bastun kostar **"50 kr per hushåll per månad"**
- gymmet beskrivs bara som **"för en låg kostnad"**, utan belopp

Femtiolappen ser alltså ut att vara bastuns avgift som vandrat över till gymmet.
Det är sajtens mest upprepade enskilda påstående, och det står i ingressen på
förstasidan.

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

## Blockerar: ingressen i `det-har-ingar` lovar för hela listan

Ingressen säger *"Allt ingår i avgiften, utom det som står med en kostnad."*
Varje rad utan kostnad påstår alltså att den är gratis. Kvar att belägga:

- [ ] **Cykelförrådet i M10** – husens cykelrum är gratis, men gäller det även
      långtidsförrådet, eller finns kö eller avgift dit?
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

## Ska M10 stå utskrivet?

Garaget med däckförvaringen är avidentifierat, se *Var förråden ligger står inte
utskrivet* i [README.md](README.md). Cykelförrådet är det inte: `cykelforrad-m10`
heter *"Långtidsförvaring i M10"* och raden i `det-har-ingar` säger samma sak. En
cykel i långtidsförvaring är ett bättre byte än ett däck.

- [ ] **Avgör om regeln gäller cykelförrådet också.** Ja betyder ny rubrik på
      blocket, ändrad rad i `det-har-ingar` och en genomgång av `bicycle.html`,
      som hämtar in blocket. Nej betyder att raden om däckgaraget bör omprövas –
      det ena eller det andra, inte båda
- [ ] Fråga samtidigt om cykelförrådet är **larmat eller låst med egen nyckel**.
      Är det det, faller hela invändningen och båda uppgifterna kan stå kvar

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

Ingen av de här kostar något. Raderna i `det-har-ingar` står därför kvar utan
kostnad, vilket är precis vad ingressen säger att de ska göra – inget att ändra.

- [x] **Däckförvaring** – gratis. Skrivet med ord i `dackforvaring`-blocket
      också, eftersom rollsidorna inte lyder under ingressens regel och de
      flesta föreningar tar betalt för det här
- [x] **Tvättstugor** – gratis
- [x] **Borrmaskin** – gratis, ingen deposition
- [x] **Cykelrum** i husen – gratis
