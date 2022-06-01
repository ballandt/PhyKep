# Simulationen Keplersche Gesetze

![IMAGE](./README.image.png)

---

**Simulationen zu den Keplerschen Gesetzen**

Das Programm simuliert ein Zweikörpersystem **Erde-Sonne** bei
dem lediglich die Erdbewegung betrachtet wird. Die Berechnung der
Erdposition erfolgt durch **Linearisierung** der Bewegung mit der folgende
Gleichungen entstehen

> <i><vec>F&#8407; = G &centerdot; <sup> m<sub>1</sub> m<sub>2</sub> </sup> / <sub> d<sup>3</sup> </sub> &centerdot; d&#8407;
> 
> a&#8407; = <sup>F&#8407;</sup>/<sub>m</sub>
> 
> v&#8407; = a&#8407; &centerdot; &Delta;t
> 
> d&#8407; = v&#8407; &centerdot; &Delta;t </i>

Die Genauigkeit der Simulation verschlechtert sich bei sehr ausgeprägter
Ellipsenform und hohen Geschwindigkeiten bei großer Richtungsänderung.

**Simulationsprogramme**

1. `gravitation_newton.py`
   1. Nachweis [Kepler I](#kepler-i)
   2. Bewegungsberechnung als Grundlage für 2.
2. `kepler_2.py`
   1. Nachweis [Kepler 2](#kepler-ii)
   2. Flächen konstant
   1. Schneller in Sonnennähe
   2. Gravitationsmodell von 1. übernehmen

---
## Zeitplan

- [x] (27. Mai) Entwicklung Grundlage
- [x] (30. Mai) Tests
- [x] (30. Mai) Erster Release-Kandidat
- [x] (1. Juni) Zweiter Release-Kandidat
- [ ] (4. Juni) Dritter Release-Kandidat
- [ ] (10. Juni) **v1.0.0**

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
