# Copilot Használat Dokumentációja – ZH II. Gyakorlati rész

## Projekt áttekintés

Ez a dokumentáció rögzíti a GitHub Copilot felhasználásának részleteit a "II. Zárthelyi dolgozat – Gyakorlati rész" Python feladatsorának elkészítésében.

---

## Prompt 1: Git .idea mappa figyelmen kívül hagyása

**Cél:** Ellenőrizni, hogy az `.idea` mappa megfelelően ki van zárva a Git verziókezelésből.

**Prompt:**
```
exclude .idea folder from git
```

**Válasz:** 
- Az `.idea` mappa már ki volt zárva a `.gitignore` fájlban (sorok: 1-3)
- Javasolt szemplifikáció: csak egy sor szükséges: `.idea/`

**Tanulság:** A projekt már előzetesen megfelelően konfigurálva volt.

---

## Prompt 2: Feladatcsomag meghatározása és témakörök

**Cél:** Létrehozni 4 különböző típusú Python gyakorlóprobléma szövegezetét és kódsablonját.

**Prompt:**
```
Generálj TODO szekciókat és kódrészleteket a feladatok mappa 4 fájljába a megadott módon.

1. Szintaktikai hibás kód javítása
2. Logikai / szemantikai hibás kód javítása
3. Meglévő program kiegészítése új funkcióval
4. Új programrész implementálása

A feladatok harmadéves egyetemi hallgatók számára készülnek python programozás alapjai kurzusra.

Az alábbi témák lettek az órákon feldolgozva:

1. Alapvető utasítások és szintaxis, beépített adattípusok, operátorok
2. Adattípusok és adatszerkezetek
3. UML diagram, Python függvények (szintaktika, paraméterek, visszatérési érték, hatóköre), rekurzió, type, isinstancek
4. Modulok, Fájlkezelés, Fájlformátumok (CSV, JSON), HTTP hívások
5. Python OOP (Osztályok, Példányok, Metódusok, Öröklődés)
6. Python lista kifejezések, generátorok és lambda függvények
7. Kivétel- és Hibakezelés (Kivételek, Try / Except / Finally), Aszinkron programozás
8. Logging és Debugging
```

**Kimenet:** Négy sablon feladatfájl:
- `1_szintaktikai_hiba_javitas.py` – szándékosan szintaktikai hibás kóddal
- `2_szemantikai_hiba_javitas.py` – futtatható, de logikailag hibás programmal
- `3_kod_kiegeszites_uj_funkcioval.py` – OOP alapú, bővítendő struktura
- `4_uj_programresz_implementalasa.py` – CSV/JSON feldolgozás sablonnal

**Tanulság:** Egységes, progresszív nehézségi szint és didaktikai célok.

---

## Prompt 3: Beírási mód aktiválása

**Cél:** Áttérés az olvasási módból az írási módba a fájlok feltöltésére.

**Prompt:**
```
oké, mostmár írási módban vagy, beírnád?
```

**Válasz:** Megerősítés, hogy a fájlok feltöltésre kerülnek.

**Tanulság:** Explicit megerősítés szükséges az írási műveletek elvégzéséhez.

---

## Prompt 4: Megoldások implementálása új branchben

**Cél:** Az összes feladat kész megoldásának elkészítése, mintha egy hallgató oldaná meg azokat.

**Prompt:**
```
2. új ágra váltottam, implementálhatod ebbe, mintha most oldanád meg
```

**Megvalósított lépések:**

### 1. feladat – Szintaktikai hibák javítása
- **Hiba 1:** Hiányzó vessző szótár literálban (19. sor)
- **Hiba 2:** Hiányzó kettőspont függvénydefinícióban (24. sor)
- **Hiba 3:** Hiányzó bezáró zárójel listakomprehenzióban (31. sor)
- **Kimenet:** 
  ```
  Sikeres hallgatók: ['Anna', 'Csilla', 'David']
  Átlagpontszám: 71.5
  ```

### 2. feladat – Logikai hibák javítása
- **Hiba 1:** `atlag()` számít helyesen, de `len(pontok) - 1` helyett `len(pontok)` kell
- **Hiba 2:** `atment_e()` feltétele: `>` helyett `>=` kell
- **Hiba 3:** `sikeresek_szama()` logikája invertált (not hozzáadása)
- **Hiba 4:** `legjobb_hallgato()` összehasonlítása fordított (`<` helyett `>`)
- **Kimenet:**
  ```
  Sikeres hallgatók száma: 3
  Legjobb hallgató: Csilla
  ```

### 3. feladat – Program kiegészítése új funkcióval
- **Megvalósítások:**
  - `keres_szerzo_szerint()` – szerzőalapú szűrés listakomprehenzióval
  - `elerheto_konyvek_szama()` – generator expression és sum() használatával
  - `mentes_json_fajlba()` – JSON export UTF-8 kódolással
- **Kimenet:**
  ```
  Jokai Mor könyvei: ['Az arany ember', 'A koszivu ember fiai']
  Elérhető könyvek száma: 2
  ```

### 4. feladat – Új programrész implementálása
- **Megvalósítások:**
  - `beolvas_eredmenyek()` – CSV beolvasás `csv.DictReader`-rel, validáció (0–100 pont)
  - `hallgato_atlag()` – átlagszámítás hármas oszlopból
  - `legjobb_hallgato()` – max() és lambda key-vel
  - `mentes_osszefoglalo_json()` – összefoglaló JSON exportálása
- **Tesztadatok:** `eredmenyek.csv` fájl létrehozva
- **Kimenet:**
  ```json
  {
    "hallgatok_szama": 3,
    "atlagok": {
      "Anna": 83.66666666666667,
      "Bela": 54.666666666666664,
      "Csilla": 92.0
    },
    "legjobb_hallgato": "Csilla"
  }
  ```

**Tanulság:** Teljes feladat-ökoszisztéma tesztelésre kerülve, mind a 4 feladat működőképes.

---

## Prompt 5: COPILOT.md generálása

**Cél:** A beszélgetés dokumentációs fájlként való rögzítése.

**Prompt:**
```
"Generálj egy COPILOT.md nevű fájlt, melybe a jelenlegi beszélgetés tartalma, elsősorban a promptok kerüljenek rögzítésre."
```

**Kimenet:** Ez a fájl (COPILOT.md).

---

## Felhasznált Python modulok és technikák

| Modul/Technika | Feladat | Célja |
|---|---|---|
| `csv.DictReader` | 4. | CSV fájlok olvasása szótári formátumban |
| `json.dump()` | 3., 4. | Szerializáció JSON-be |
| List comprehension | 1., 2., 3. | Adatszűrés és transzformáció |
| Generator expression | 3. | Memória-hatékony számlálás |
| Lambda funkció | 4. | Inline key-függvény a max()-hoz |
| Exception handling | 4. | Validációs hibák kezelése |
| File I/O | 3., 4. | CSV és JSON fájlkezelés |

---

## Technikai tanulságok

1. **Szintaxis vs. szemantika:** Az 1. és 2. feladat jól szemlélteti a különbséget
2. **OOP alapok:** A 3. feladat osztálymódszerek bővítésének gyakorlásához
3. **Adatformátumok:** CSV és JSON párhuzamosítása a 4. feladatban
4. **Hibakezelés:** ValueError kivételek használata validációhoz
5. **Testing:** Mindegyik feladat futási eredménye empirikusan ellenőrzött

---

## Összesítés

- **Létrehozott fájlok:** 4 feladat Python fájl + 1 CSV teszt + 1 JSON kimenet
- **Összes szintaktikai hiba javítva:** 3 hiba
- **Összes logikai hiba javítva:** 4 hiba  
- **Új funkció implementálva:** 7 függvény/metódus
- **Teljes teszt lefuttatva:** ✅ Mind a 4 feladat működőképes

---

## Beadási követelmények (README szerint)

✅ Feladatok elkészültek a `/feladatok` mappában  
✅ AI eszköz használata dokumentálva (ez a fájl)  
✅ Összes megoldás működőképes és tesztelt  
⚠️ Még szükséges: AI_REFERENCES.md feltöltése a tanári útmutatáson kívül  

**Készült:** 2026. április 29.  
**Copilot verzió:** GitHub Copilot (2026)  
**Projekt:** II. Zárthelyi dolgozat – Gyakorlati rész (Python alapok kurzus)

