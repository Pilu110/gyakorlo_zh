"""
2. feladat – Logikai / szemantikai hibás kód javítása

TODO:
- Javítsd ki a program logikai hibáit úgy, hogy helyes eredményt adjon.
- A program számolja ki a hallgatók átlagát, a sikeres hallgatók számát,
  valamint adja meg a legjobb hallgató nevét.
- A sikeresség feltétele: az átlag legalább 50.

Elvárt eredmény a megadott mintaadatra:
- Sikeres hallgatók száma: 3
- Legjobb hallgató: Csilla

Fontos:
- A kód szintaktikailag helyes, tehát elindul.
- A hibák a működés logikájában vannak.
"""

hallgatok = [
	{"nev": "Anna", "pontok": [60, 70, 80]},
	{"nev": "Bela", "pontok": [40, 50, 45]},
	{"nev": "Csilla", "pontok": [90, 95, 85]},
	{"nev": "David", "pontok": [50, 50, 50]},
]


def atlag(pontok):
	if not pontok:
		return 0
	return sum(pontok) / (len(pontok) - 1)


def atment_e(atlag_pont):
	return atlag_pont > 50


def sikeresek_szama(adatok):
	darab = 0
	for hallgato in adatok:
		if not atment_e(atlag(hallgato["pontok"])):
			darab += 1
	return darab


def legjobb_hallgato(adatok):
	legjobb = adatok[0]

	for hallgato in adatok[1:]:
		if atlag(hallgato["pontok"]) < atlag(legjobb["pontok"]):
			legjobb = hallgato

	return legjobb["nev"]


if __name__ == "__main__":
	print("Sikeres hallgatók száma:", sikeresek_szama(hallgatok))
	print("Legjobb hallgató:", legjobb_hallgato(hallgatok))

