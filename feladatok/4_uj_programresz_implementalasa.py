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
	# TODO: valósítsd meg
	raise NotImplementedError("A függvény még nincs implementálva.")


def hallgato_atlag(hallgato):
	# TODO: valósítsd meg
	raise NotImplementedError("A függvény még nincs implementálva.")


def legjobb_hallgato(hallgatok):
	# TODO: valósítsd meg
	raise NotImplementedError("A függvény még nincs implementálva.")


def mentes_osszefoglalo_json(hallgatok, fajlnev):
	# TODO: valósítsd meg
	raise NotImplementedError("A függvény még nincs implementálva.")


if __name__ == "__main__":
	minta_hallgatok = [
		{"nev": "Anna", "zh1": 78, "zh2": 82, "beadando": 91},
		{"nev": "Bela", "zh1": 55, "zh2": 49, "beadando": 60},
		{"nev": "Csilla", "zh1": 95, "zh2": 88, "beadando": 93},
	]

	# A TODO-k megoldása után ezek használhatók tesztelésre:
	# print("Anna átlaga:", hallgato_atlag(minta_hallgatok[0]))
	# print("Legjobb hallgató:", legjobb_hallgato(minta_hallgatok))
	# mentes_osszefoglalo_json(minta_hallgatok, "osszefoglalo.json")

