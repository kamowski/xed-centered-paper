# Centered Paper pre Xed

Malý doplnok pre Xed, ktorý zmení editor na jednoduchý, vycentrovaný „hárok papiera“.

Okolo textovej plochy vytvorí široké sivé okraje a uprostred ponechá bielu plochu pripomínajúcu papier.

Doplnok je určený najmä na pohodlné písanie bez zbytočného rozptyľovania.

## Funkcie

biely papier vycentrovaný v editore, približne 80 znakov široký

sivá plocha po oboch stranách

tenký okraj papiera

automatické prispôsobenie veľkosti okna

automatické prispôsobenie zmenám fontu

F10 zapína a vypína režim centered paper

nemení obsah dokumentu

nezasahuje do ukladania ani exportu

nemá vplyv na Pandoc ani iné nástroje pracujúce s dokumentom

## Klávesová skratka
Kláves	Funkcia
F10	    Zapnúť/vypnúť centered paper

Ostatné klávesové skratky poskytuje samotný Xed.

Napríklad príjemná zostava na písanie:

F9 — bočný panel / tagy

F10 — centered paper

F11 — celá obrazovka

## Inštalácia

1. Vytvor adresár doplnku:

mkdir -p ~/.local/share/xed/plugins/centered-paper


2. Doň skopíruj tieto dva súbory:

centered-paper/
├── centered-paper.plugin
└── centered_paper.py


Súbor centered-paper.plugin má obsahovať:

[Plugin]
Loader=python3
Module=centered_paper


3. Potom doplnok zapni v:

Xed → Nastavenia → Moduly

Xed reštartuj.

## Kontrola Python súboru

Pred spustením Xedu možno skontrolovať syntax:

python3 -m py_compile ~/.local/share/xed/plugins/centered-paper/centered_paper.py


Ak príkaz nič nevypíše, syntax Python súboru je v poriadku.

Testované s

Xed 3.8.9

GTK 3

GtkSourceView 4

Python 3

Doplnok môže fungovať aj s inými verziami Xedu, kompatibilita s budúcimi verziami však nie je zaručená.

## Poznámka

Doplnok mení iba vizuálne zobrazenie editora.

„Papier“ nie je súčasťou dokumentu. Kreslí ho samotný doplnok, takže nemá žiadny vplyv na:

Markdown

HTML

LaTeX

obyčajný text

Pandoc

tlač alebo export

Obsah dokumentu zostáva nezmenený.

## Údržba

Ide o malý doplnok vytvorený pôvodne pre osobné použitie a zverejnený preto, že môže byť užitočný aj pre ďalších používateľov Xedu.

Bol vytvorený a testovaný pre Xed 3.8.9.

Budúce verzie Xedu môžu zmeniť API doplnkov alebo spôsob integrácie GTK, takže doplnok môže v budúcnosti vyžadovať úpravy.

Ak prestane fungovať v novšej verzii Xedu, pokojne ho forknite a opravte.

Stav údržby: funguje u mňa. 🙂

##Licencia

Copyright © 2026

Tento projekt je vydaný pod licenciou MIT.
