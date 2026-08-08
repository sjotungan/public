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

- [ ] **Är uthyrningen fortfarande pausad?** A–Ö säger att både köavgiften och
      uthyrandet pausats under stambytet. Raden lovar i dag inget om
      inflyttning – men om pausen är hävd är det en mycket starkare rad
- [ ] **Hyran** för en ungdomslägenhet – fortfarande okänd
- [ ] Flytta upp gruppen *Att låna, boka och hyra* först i listan när raderna är
      klara – grupperna står i fallande ordning efter hur ovanliga de är, och
      nio egna lägenheter slår ett gym

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

## Klart, uppgift från medlem 2026-08-07

Ingen av de här kostar något. Raderna i `det-har-ingar` står därför kvar utan
kostnad, vilket är precis vad ingressen säger att de ska göra – inget att ändra.

- [x] **Däckförvaring** – gratis. Skrivet med ord i `dackforvaring`-blocket
      också, eftersom rollsidorna inte lyder under ingressens regel och de
      flesta föreningar tar betalt för det här
- [x] **Tvättstugor** – gratis
- [x] **Borrmaskin** – gratis, ingen deposition
- [x] **Cykelrum** i husen – gratis
