# Simulationen zu den Kepler'schen Gesetze

![IMAGE](./README.image.png)

---

## Inhalt

* [Ziel](#ziel-der-simulation)
* [Modell](#mathematisches-modell)
* [Nutzung](#nutzung-der-simulation)
* [Dateien](#enthaltene-dateien)
* [Kepler'sche Gesetze](#keplersche-gesetze)
* [Quellen](#quellen)
* Website: [https://ballandt.github.io/p/PhyKep](#https://ballandt.github.io/p/PhyKep)

---

## Ziel der Simulation

Die Programme zeigen grafisch den Zusammenhang zwischen dem **Newton'schen Gravitationsgesetz**
und den [**Kepler'schen Gesetzen**](#keplersche-gesetze). Dargestellt wird die Bewegung der Erde um die
Sonne durch eine *matplotlib*-Animation. Ein Erdkreis bewegt sich dabei zur simulierten Zeit
um die Sonne.

Dabei soll die erste Simulation die sich einstellende **Kreis- bzw. Ellipsenform**
des Erdorbits zeigen. Die zweite Simulation demonstriert die Gültigkeit des [zweiten
Kepler'schen Gesetzes](#kepler-ii) in dem die **überzogenen Flächen**
berechnet werden.

## Mathematisches Modell

Das Programm simuliert ein Zweikörpersystem **Erde-Sonne** bei
dem lediglich die Erdbewegung betrachtet wird. Die Berechnung der
Erdposition erfolgt durch **Linearisierung** der Bewegung mit der folgende
Gleichungen entstehen



<i>
<b>F</b> = G &centerdot; <sup> m<sub>1</sub> m<sub>2</sub> </sup> / <sub> d<sup>3</sup> </sub> &centerdot; <b>d</b>

<b>a</b> = <sup><b>F</b></sup>/<sub>m</sub>

<b>v</b> = <b>a</b> &centerdot; &Delta;t

<b>d</b> = <b>v</b> &centerdot; &Delta;t
</i>

<sub>(Fett geschriebene Formelzeichen stellen vektorielle Größen dar.)</sub>

> ⚠️Die Genauigkeit der Simulation verschlechtert sich bei sehr ausgeprägter Ellipsenform und hohen Geschwindigkeiten bei großer Richtungsänderung.



---
## Nutzung der Simulation

### Pythonumgebung

Für die Ausführung der Simulation muss auf dem System eine **Python3-Umgebung**
installiert sein. Für fortgeschrittene Pythonnutzer ist die [**Conda**](https://anaconda.com/)
mit dem für den Release beschriebenen Environment zu empfehlen. **Für Anfänger ist
eine [Installation des Pythoninterpreters](https://python.org/) ausreichend**. In diesem
Fall müssen die benötigten Packages
* numpy
* shapely
* matplotlib

über den Paketmanager der IDE oder den [Python-Paketmanager](https://pip.pypa.io/en/stable/) mit `pip install` hinzugefügt werden.

### Ausführung

Mit der eingerichteten Umgebung können die Dateien einfach über die IDE oder mit dem 
Kommandozeilenbefehl 

```commandline
python gravitation_newton.py
python kepler_2.py
```
ausgeführt werden.

---

## Enthaltene Dateien

1. `gravitation_newton.py`
   1. Nachweis [Kepler I](#kepler-i)
   2. Bewegungsberechnung als Grundlage für 2.
2. `kepler_2.py`
   1. Nachweis [Kepler 2](#kepler-ii)
   2. Flächen konstant
   1. Schneller in Sonnennähe
   2. Gravitationsmodell von 1. übernehmen

---
## Kepler'sche Gesetze

### Kepler I

> Alle Planeten bewegen sich auf elliptischen Bahnen. In einem der Brennpunkte steht die Sonne


### Kepler II

> Der Quotient aus der vom Leitstrahl Sonne - Planet überstrichenen
> Fläche und der dazu erforderlichen Zeit ist konstant.


### Kepler III

> Die Quadrate der Umlaufzeiten zweier Planeten verhalten sich
> wie die dritten Potenzen der großen Halbachsen ihrer Bahnen

---
## Quellen

* [https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html)
  * Entfernung Erde - Sonne
  * Geschwindigkeit Erde
* Oliver Natt. Physik mit Python. Springer Spektrum. 2020
  * Grundlagen Simulation und Animation mit Python
