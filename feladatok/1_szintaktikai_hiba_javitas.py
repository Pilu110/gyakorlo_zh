"""
1. feladat – Szintaktikai hibás kód javítása

TODO:
- Javítsd ki a szintaktikai hibákat úgy, hogy a program futtatható legyen.
- A program célja:
	1. kiszámolja a hallgatók átlagpontszámát,
	2. kilistázza a sikeres hallgatókat.
- A sikeresség feltétele: legalább 60 pont.
- A program logikáját ne írd át jelentősen, csak a szintaktikai hibákat javítsd.

Elvárt működés a javítás után:
- A `sikeres_hallgatok_listaja()` adja vissza azoknak a nevét, akik legalább 60 pontot értek el.
- Az `atlag_pontszam()` adja vissza az összes hallgató pontszámának átlagát.
"""

hallgatok = [
	{"nev": "Anna", "pont": 78},
	{"nev": "Bela", "pont": 54}
	{"nev": "Csilla", "pont": 91},
	{"nev": "David", "pont": 63},
]

def atlag_pontszam(adatok)
	osszeg = 0
	for elem in adatok:
		osszeg += elem["pont"]
	return osszeg / len(adatok)

def sikeres_hallgatok_listaja(adatok):
	return [elem["nev"] for elem in adatok if elem["pont"] >= 60

if __name__ == "__main__":
	sikeres_hallgatok = sikeres_hallgatok_listaja(hallgatok)
	print("Sikeres hallgatók:", sikeres_hallgatok)
	print("Átlagpontszám:", atlag_pontszam(hallgatok))

