---
name: bilder
description: Lägg in nya foton och filmer på sajten. Använd när det ligger kameraoriginal i repots rot (IMG_*.HEIC/.heic/.MOV/.PNG) som ska bli webbilder, eller när användaren säger "jag har lagt till några bilder", "lägg in de nya fotona", "ta hand om bilderna i roten". Går igenom en bild i taget tillsammans med användaren, beslutar sida och bildtext, bygger om sajten och tar bort originalen till sist.
---

# Nya bilder till sajten

Kameraoriginal hamnar i repots rot. Den här färdigheten tar dem därifrån till
färdiga webbilder på rätt sida, med rätt bildtext, och städar upp efter sig.

**Arbeta en bild i taget.** Användaren vill besluta varje bild tillsammans med
dig, inte godkänna en färdig lista. Visa vad du ser, föreslå en placering med
skäl, ställ de frågor bilden kräver – och gå vidare först när den är på plats.

## 1. Hitta originalen

```sh
ls -la IMG_*.HEIC IMG_*.heic IMG_*.MOV IMG_*.PNG 2>/dev/null
```

Ta reda på vilka som redan är använda innan du frågar användaren om något:

```sh
for n in 2638 2721; do
  echo "$n: $(find assets -iname "*$n*" | tr '\n' ' ')"
done
```

## 2. Titta på bilderna

Du måste se dem för att kunna föreslå något. `sips` läser HEIC, Read visar JPEG:

```sh
OUT="$CLAUDE_SCRATCHPAD/preview"; mkdir -p "$OUT"
for f in IMG_*.HEIC IMG_*.heic; do
  b=$(basename "$f" | sed 's/\.[Hh][Ee][Ii][Cc]$//')
  sips -s format jpeg -Z 900 "$f" --out "$OUT/$b.jpg" >/dev/null 2>&1
done
```

För film: `ffmpeg -ss <sek> -i fil.MOV -frames:v 1 -vf scale=700:-1 ut.jpg`.
Ta flera bildrutor spridda över klippet – den första säger sällre något om
resten. Zooma in på det som kan vara intressant med `crop` innan du dömer ut
det.

Läs sedan igenom hela högen och skaffa dig en uppfattning, men **besluta inte
allt på en gång** – användaren vill ta dem en och en.

## 3. Konvertera

Kör `scripts/mkweb.py` i den här mappen:

```sh
python3 .claude/skills/bilder/scripts/mkweb.py IMG_2638.HEIC assets/images/lakes/img_2638.jpg
```

**Använd inte `sips -Z` rakt av.** `sips` skalar rå pixelbuffert och lämnar kvar
EXIF-orientationen, så ett stående foto blir en liggande fil som ligger ner i
vissa lägen. Sajtens övriga filer är fysiskt roterade (1200×1600 för stående).
`mkweb.py` bakar in roteringen med `ImageOps.exif_transpose`.

Namn och mapp: `assets/images/<ämne>/img_NNNN.jpg`, alltid gemener. Ämnesmappar
som finns i dag: `courtyards`, `grill`, `playground`, `nature`, `lakes`,
`buildings`, `sport`, `boulebana`, `outdoor-gym`, `gym`, `laundry`, `dogs`,
`car`, `bicycle`, `transit`, `parcel`, `tools`, `cycle-routes`. Skapa en ny bara
när ingen befintlig passar.

## 4. Bestäm var bilden hör hemma

Sajtens regel: **ett foto står under det påstående det bevisar.** Det är den
regeln som håller nere antalet bilder. Fråga alltid först: vilket påstående på
sajten blir starkare av den här bilden? Finns inget sådant är bilden inte
sämre – den hör bara hemma någon annanstans.

Två utfall:

**A. Bilden bär ett påstående** → in på ämnessidan, intill texten den styrker.
Leta upp blocket eller avsnittet först (`grep -rn` i `src/`) så att bildtexten
och brödtexten säger samma sak.

**B. Bilden bär inget påstående** → skriv den som en vanlig figur i
`src/pages/bilder.html`, mellan sidhuvudet och gallerimarkören. `build.py`
lyfter ut den och lägger den sist i galleriet. Se README, avsnittet
"Bilder utan sida".

Fråga användaren när du inte kan avgöra det själv – och du kan sällan avgöra
**fakta**: vilken sjö det är, vad en byggnad används till, om något ligger på
föreningens mark eller utanför. Gissa aldrig sådant, och skriv aldrig in en
uppgift i en bildtext som du inte har fått bekräftad.

## 5. Skriv figuren

```html
<figure>
  <a href="assets/images/lakes/img_2638.jpg">
    <img src="assets/images/lakes/img_2638.jpg" alt="..." loading="lazy" decoding="async">
  </a>
  <figcaption>...</figcaption>
</figure>
```

Regler som går att göra fel på:

- **Aldrig `width`/`height` på ett fotografi.** Bara kartor och skärmbilder har
  dem. Galleriet beskär till 4:3 med `aspect-ratio`, och ett `height`-attribut
  vinner över beskärningen och gör miniatyren till en smal remsa.
- **`alt` beskriver bilden utförligt** på svenska: vad som syns, färger,
  material, vad som står i bakgrunden. Jämför längden med befintliga alt-texter.
- **`figcaption` säger vad bilden bevisar.** För en bild utan sida måste den
  dessutom bära sig själv – den står aldrig under en rubrik som säger var den är
  tagen. "En av gårdarna" duger inte.
- **Namnge inga växter, trädslag eller byggnader du inte kan se säkert.**
  Beskriv i stället: "gula blommor över mörkt purpurfärgade blad". Sätt en
  kommentar om vad som återstår att kontrollera.
- **Inga människor i bild.** Sajten är öppen och riktar sig till spekulanter.
- **Skriv aldrig `<figure>` bokstavligt i en HTML-kommentar.** Figurregexen är
  lat och plockar då ut en bit som börjar inne i kommentaren och slutar i nästa
  riktiga figur; kommentartexten hamnar synlig i galleriet. `find_figures()`
  hoppar numera över kommentarer, men skriv "figur" i löptext ändå.

Kommentera i koden **varför** bilden ligger där den ligger, i samma ton som
resten av repot – det är så sajten är dokumenterad.

## 6. Bygg och kontrollera

```sh
python3 build.py
```

Bygget skriver `bildsidan: N bilder, varav M egna`. Kontrollera sedan:

```sh
# Bilder som ingen sida använder
comm -23 \
  <(find assets/images -type f | sed 's|^|/|' | sort) \
  <(grep -oh 'assets/images/[^"]*' *.html | sed 's|^|/|' | sort -u)
```

```sh
# Att ingen kommentartext läckt ut i sidan
python3 - <<'PY'
import glob, re
for f in sorted(glob.glob('*.html')):
    s = open(f, encoding='utf-8').read()
    if s.count('<!--') != s.count('-->'):
        print("OBALANS:", f)
    if '-->' in re.sub(r'<!--.*?-->', '', s, flags=re.S):
        print("LÖS -->:", f)
PY
```

Be användaren titta på sidan i webbläsaren innan originalen tas bort.

## 7. Städa upp

Originalen är ~8 MB styck och ska inte ligga kvar. **Fråga först** – borttagning
går inte att ångra, och de ligger utanför git (`.gitignore`), så de finns inte i
någon historik att hämta tillbaka dem ur.

```sh
rm IMG_2638.HEIC IMG_2721.HEIC   # bara de som blivit webbilder
```

Ta bara bort dem du faktiskt har konverterat. Bilder ni beslutat att hoppa över
är fortfarande original – fråga om de ska bort eller ligga kvar.

Om ett nytt filnamnsmönster dykt upp (annan ändelse, annat prefix), lägg till
det i `.gitignore`. Både gemener och versaler behövs som egna rader: macOS har
`core.ignorecase=true` och döljer felet lokalt, men på ett skiftlägeskänsligt
filsystem följer originalen med in i git.
