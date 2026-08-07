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
   bestämd fråga – och därför ligger `ekonomi.html` först i menyn.

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

| Fil | Sida i menyn | Vad sidan gör |
| --- | --- | --- |
| [index.html](index.html) | Översikt | Hela argumentet i scrollordning: fotohjälte, sex siffror, ekonomin i korthet, *Det här ingår i boendet*, området, rollkorten, grannarna emellan, gemensamt, grillplatserna |
| [ekonomi.html](ekonomi.html) | Ekonomi och underhåll | Nyckeltalen förklarade, stambytet, avgiftsutvecklingen, allt underhåll år för år |
| [laget.html](laget.html) | Läget | Karta, kommunikationer, tillgänglighet, närområdet, rådjursfilmen |
| [fakta.html](fakta.html) | Fakta | Allt i faktarader, i den form uppgifter jämförs i mellan föreningar |
| [bilder.html](bilder.html) | Bilder | Sajtens alla bilder i ett galleri, samlas in vid bygget |
| [family.html](family.html) | För dig … med barn | Lekplatser, gårdar, fotbollsplan, isbana, förskola och kulturskola |
| [car.html](car.html) | För dig … med bil eller MC | Platser, garage, laddning, MC, däckförvaring |
| [bicycle.html](bicycle.html) | För dig … på cykel | Cykelrum, långtidsförråd, cykelvägarna utanför |
| [dogs.html](dogs.html) | För dig … med hund | Hundrastgården, Wättinge, hundägarnas grupp |
| [fitness.html](fitness.html) | För dig … som tränar | Gym, bastu, utegym, boulebana |

*Det här ingår i boendet* på översikten är ett register över allt föreningen
har, en rad per sak. Det finns för att **varken spekulanten eller mäklaren vet
vad som ingår** – ett gym för 50 kronor i månaden, en bastu, en föreningslokal
utan kostnad och en borrmaskin att låna står inte i annonsen och går inte att
läsa sig till någon annanstans. Håll listan uppdaterad; den är sajtens
tydligaste skäl att finnas.

## Vad som fortfarande saknas

Luckorna är markerade med "Innehåll kommer" i sidorna. Skriv inte in gissningar.

- **Kommunikationer** (`laget.html`) – busslinjer från Myggdalsvägen, restid till
  Gullmarsplan och Slussen, gångavstånd till hållplats och till Tyresö centrum.
  Det är den vanligaste frågan från någon som väger adresser mot varandra.
- **Hiss per hus** (`tillganglighet`-blocket) – vilka av de 24 husen som har
  hiss. Att samtliga hissar renoverades 2023 är belagt; fördelningen är det
  inte. Viktigt för den som säljer villa och söker sig till lägenhet.
- **Bredbandsleverantör och hastighet** (`bredband`-blocket) – att bredband och
  TV ingår i avgiften är belagt, men inte vilken leverantör eller vilken
  hastighet.

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
