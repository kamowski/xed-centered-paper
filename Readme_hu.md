# Centered Paper Xedhez

Egy apró bővítmény az Xed
 szövegszerkesztőhöz, amely az editort egyszerű, középre igazított „papírlappá” alakítja.

Az írási terület két oldalán széles szürke sávokat jelenít meg, középen pedig egy fehér, papírlaphoz hasonló területet hagy.

A bővítmény elsősorban kényelmes, zavaró tényezőktől mentes íráshoz készült.

## Funkciók

középre igazított, körülbelül 80 karakter széles fehér papírlap

szürke terület a papír két oldalán

vékony szegély a papír két oldalán

automatikus alkalmazkodás az ablak méretéhez

automatikus alkalmazkodás a betűtípus változásához

F10 — a centered paper mód be- és kikapcsolása

nem módosítja a dokumentum tartalmát

nincs hatással a mentésre vagy az exportálásra

nincs hatással a Pandocra vagy más, a dokumentummal dolgozó eszközökre

## Gyorsbillentyű
Billentyű	Funkció
F10	        A centered paper be-/kikapcsolása

A többi gyorsbillentyűt maga az Xed biztosítja.

Például egy kényelmes írási összeállítás:

F3 — osztott nézet

F9 — oldalsáv / címkék

F10 — centered paper

F11 — teljes képernyő

## Telepítés

1. Hozd létre a bővítmény könyvtárát:

mkdir -p ~/.local/share/xed/plugins/centered-paper


2. Másold bele ezt a két fájlt:

centered-paper/
├── centered-paper.plugin
└── centered_paper.py


A centered-paper.plugin fájl tartalma:

[Plugin]
Loader=python3
Module=centered_paper


3. Ezután engedélyezd a bővítményt itt:

Xed → Beállítások → Bővítmények

Indítsd újra az Xedet.

## A Python fájl ellenőrzése

A Python fájl szintaxisa a következő paranccsal ellenőrizhető:

python3 -m py_compile ~/.local/share/xed/plugins/centered-paper/centered_paper.py


Ha a parancs nem ír ki semmit, a Python fájl szintaktikailag rendben van.

Tesztelve

Xed 3.8.9

GTK 3

GtkSourceView 4

Python 3

A bővítmény más Xed-verziókkal is működhet, de a jövőbeli verziókkal való kompatibilitás nem garantált.

## Megjegyzés

A bővítmény csak az editor megjelenését módosítja.

A „papír” nem része a dokumentumnak. A bővítmény rajzolja ki, ezért nincs hatással:

Markdownra

HTML-re

LaTeX-re

egyszerű szövegre

Pandocra

nyomtatásra vagy exportra

A dokumentum tartalma változatlan marad.

## Karbantartás

Ez egy kis bővítmény, amely eredetileg személyes használatra készült, és azért került közzétételre, mert más Xed-felhasználók számára is hasznos lehet.

A bővítmény Xed 3.8.9 alatt készült és lett tesztelve.

Az Xed jövőbeli verziói megváltoztathatják a bővítmények API-ját vagy a GTK-integrációt, ezért előfordulhat, hogy a bővítmény később módosításra szorul.

Ha egy újabb Xed-verzióval már nem működik, nyugodtan forkold és javítsd.

Karbantartási állapot: nálam működik. 🙂

## Licenc

Copyright © 2026

A projekt MIT licenc alatt kerül kiadásra.
