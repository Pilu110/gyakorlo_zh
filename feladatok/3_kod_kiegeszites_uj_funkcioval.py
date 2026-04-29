"""
3. feladat – Meglévő program kiegészítése új funkcióval

TODO:
Egészítsd ki a meglévő könyvtárkezelő programot az alábbi funkciókkal:

1. `keres_szerzo_szerint(szerzo)`
   - Adja vissza az adott szerzőhöz tartozó könyveket listában.

2. `elerheto_konyvek_szama()`
   - Adja vissza, hogy hány kölcsönözhető könyv van jelenleg.

3. `mentes_json_fajlba(fajlnev)`
   - Mentse el a könyvek adatait JSON formátumban a megadott fájlba.

Követelmények:
- A meglévő kódot ne írd át feleslegesen.
- Használj listát, ciklust, feltételt és fájlkezelést.
- A JSON fájl minden könyvről tartalmazza:
	- cím
	- szerző
	- kölcsönözhető-e
"""

import json


class Konyv:
	def __init__(self, cim, szerzo, kolcsonozheto=True):
		self.cim = cim
		self.szerzo = szerzo
		self.kolcsonozheto = kolcsonozheto

	def __repr__(self):
		return f"Konyv(cim='{self.cim}', szerzo='{self.szerzo}', kolcsonozheto={self.kolcsonozheto})"


class Konyvtar:
	def __init__(self):
		self.konyvek = []

	def hozzaad_konyv(self, konyv):
		self.konyvek.append(konyv)

	def listaz_cimek(self):
		return [konyv.cim for konyv in self.konyvek]

	def kolcsonozheto_konyvek(self):
		return [konyv.cim for konyv in self.konyvek if konyv.kolcsonozheto]

	def keres_szerzo_szerint(self, szerzo):
		# TODO: valósítsd meg
		pass

	def elerheto_konyvek_szama(self):
		# TODO: valósítsd meg
		pass

	def mentes_json_fajlba(self, fajlnev):
		# TODO: valósítsd meg
		pass


if __name__ == "__main__":
	konyvtar = Konyvtar()
	konyvtar.hozzaad_konyv(Konyv("Az arany ember", "Jokai Mor", True))
	konyvtar.hozzaad_konyv(Konyv("Egri csillagok", "Gardonyi Geza", False))
	konyvtar.hozzaad_konyv(Konyv("A koszivu ember fiai", "Jokai Mor", True))

	print("Minden cím:", konyvtar.listaz_cimek())
	print("Kölcsönözhető könyvek:", konyvtar.kolcsonozheto_konyvek())

	# A TODO-k elkészítése után ezeknek is működniük kell:
	print("Jokai Mor könyvei:", konyvtar.keres_szerzo_szerint("Jokai Mor"))
	print("Elérhető könyvek száma:", konyvtar.elerheto_konyvek_szama())

	# Opcionális teszt:
	# konyvtar.mentes_json_fajlba("konyvek.json")

