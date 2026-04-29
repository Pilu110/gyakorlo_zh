"""
4. feladat – Új programrész implementálása

TODO:
Készíts egy egyszerű eredményfeldolgozó programrészt CSV és JSON használatával.

Feladat:
- Egy CSV fájlból hallgatói eredményeket kell beolvasni.
- Minden hallgatóhoz tartozik:
	- nev
	- zh1
	- zh2
	- beadando
- A program számolja ki az átlagokat,
  keresse meg a legjobb hallgatót,
  majd mentse el az összefoglalót JSON fájlba.

A CSV formátuma:
nev,zh1,zh2,beadando
Anna,78,82,91
Bela,55,49,60
Csilla,95,88,93

Követelmények:
1. Implementáld a `beolvas_eredmenyek(fajlnev)` függvényt.
   - Térjen vissza listával, amely szótárakat tartalmaz.

2. Implementáld a `hallgato_atlag(hallgato)` függvényt.
   - Számolja ki egy hallgató átlagát.

3. Implementáld a `legjobb_hallgato(hallgatok)` függvényt.
   - Adja vissza a legnagyobb átlagú hallgató teljes adatszerkezetét.

4. Implementáld a `mentes_osszefoglalo_json(hallgatok, fajlnev)` függvényt.
   - Mentse el JSON-be:
	   - hallgatok_szama
	   - atlagok
	   - legjobb_hallgato

5. Hibakezelés:
   - Hibás pontszám esetén dobj `ValueError` kivételt.
   - A pontszám csak 0 és 100 közötti egész szám lehet.
"""

import csv
import json


def beolvas_eredmenyek(fajlnev):
    hallgatok = []
    with open(fajlnev, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hallgato = {
                "nev": row["nev"],
                "zh1": int(row["zh1"]),
                "zh2": int(row["zh2"]),
                "beadando": int(row["beadando"])
            }
            # Validálás
            for pont in [hallgato["zh1"], hallgato["zh2"], hallgato["beadando"]]:
                if not (0 <= pont <= 100):
                    raise ValueError(f"Érvénytelen pontszám: {pont}. 0 és 100 között kell lennie.")
            hallgatok.append(hallgato)
    return hallgatok


def hallgato_atlag(hallgato):
    pontok = [hallgato["zh1"], hallgato["zh2"], hallgato["beadando"]]
    return sum(pontok) / len(pontok)


def legjobb_hallgato(hallgatok):
    if not hallgatok:
        return None
    return max(hallgatok, key=lambda h: hallgato_atlag(h))


def mentes_osszefoglalo_json(hallgatok, fajlnev):
    atlagok = {hallgato["nev"]: hallgato_atlag(hallgato) for hallgato in hallgatok}
    legjobb = legjobb_hallgato(hallgatok)
    
    osszefoglalo = {
        "hallgatok_szama": len(hallgatok),
        "atlagok": atlagok,
        "legjobb_hallgato": legjobb["nev"] if legjobb else None
    }
    
    with open(fajlnev, 'w', encoding='utf-8') as f:
        json.dump(osszefoglalo, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    minta_hallgatok = [
        {"nev": "Anna", "zh1": 78, "zh2": 82, "beadando": 91},
        {"nev": "Bela", "zh1": 55, "zh2": 49, "beadando": 60},
        {"nev": "Csilla", "zh1": 95, "zh2": 88, "beadando": 93},
    ]

    # A TODO-k megoldása után ezek használhatók tesztelésre:
    print("Anna átlaga:", hallgato_atlag(minta_hallgatok[0]))
    print("Legjobb hallgató:", legjobb_hallgato(minta_hallgatok)["nev"])
    mentes_osszefoglalo_json(minta_hallgatok, "osszefoglalo.json")

