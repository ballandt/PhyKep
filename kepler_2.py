"""Simulation Kepler II

Adrian Scheibe, Camillo Ballandt

Berechnet die Sektoren der durch das newtonsche Gravitationsgesetz gewonnenen
Daten und vergleicht die Flächen.

Sonne und Erde werden als Kreise dargestellt. Orbit als Graph. Fläche als
Polygon. Die Berechnung der Fläche erfolgt ebenfalls mit Polygonen.

Genauigkeit des Orbits siehe gravitation_newton.py. Fläche bleibt auch sonst
für Anzeige.
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from shapely.geometry import Polygon as sPoly
import matplotlib.animation


# Anfangswerte

# Veränderbar
d = np.array([149.598e9, 0])    # [m] Distanz Sonne - Erde
v = np.array([0, -29.29e3])  # [m/s] Ausgangsgeschwindigkeit Erde (0, 29e3)

# Einstellungen für die Flächenmessungen
abstand = 60                    # [d] Abstand zwischen Flächenmessungen
laenge = 30                     # [d] Länge der Flächenmessungen
f_position = abstand            # [d] Position des Flächenbeginns

# === Veränderung nicht empfohlen ===
m_sonne = 1.989e30              # [kg] Sonnenmasse
m_erde = 5.97e24                # [kg] Erdmasse

tag = 60 * 60 * 24              # [s] Tag in Sekunden
dt = 1 * tag                    # [s] Zeitschritt

G = 6.673e-11                   # [m^3/(kg*s^2)] Gravitationskonstante

x = []                          # Liste für x-Positionswerte
y = []                          # Liste für y-Positionswerte
# === ===


# Animation Grundlage
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Erdkreis
# Extra-Plot um Position der Erde zu verdeutlichen
# Wird an aktuelle Plotposition addiert
kreis_x = 0.5e10 * np.sin(np.linspace(0, 2*np.pi))
kreis_y = 0.5e10 * np.cos(np.linspace(0, 2*np.pi))
# Plotte Erdkreis
kreis, = ax.plot([], [])

# Plotte Sonne
ax.plot(1e10 * np.sin(np.linspace(0, 2*np.pi)),
        1e10*np.cos(np.linspace(0, 2*np.pi)))

# Plotte Erdorbit
# Aktuelle Position wird in `update` angefügt
plot, = ax.plot(x, y)

# Plotte Zeit, Fläche
# Wird von `update` aktualisiert
t_text = ax.text(-2e11, 1.7e11, "")
a_text = ax.text(-2e11, 2e11, "A = ")

# Achseneinstellungen
ax.set_xlim(-2.5e11, 2.5e11)
ax.set_ylim(-2.5e11, 2.5e11)
plt.gca().set_aspect('equal', adjustable='box')

# Fläche
flaechen_punkte = [(0, 0)]
flaeche_poly = Polygon(flaechen_punkte, facecolor="red")
flaeche = 0
ax.add_patch(flaeche_poly)


def update(n):
    """Animationsupdate
    Berechnet die neue Position und gibt die aktualisierten Plots zurück.
    """
    # Greife auf globale Variablen zu
    global v, d, x, y, abstand, laenge, f_position, flaechen_punkte, flaeche
    # Newtonsches Gravitationsmodell
    F = -G * m_sonne * m_erde / np.linalg.norm(d)**3 * d
    a = F / m_erde
    v = a*dt + v
    d = v*dt + d
    x.append(d[0])  # Zum Anfügen von Werten sind Listen besser als arrays
    y.append(d[1])
    # Plot-Aktualisierungen
    # Erdorbit
    plot.set_data(x, y)
    # Erdform
    kreis.set_data(kreis_x + d[0], kreis_y + d[1])
    # Zeit
    t_text.set_text(f"t = {n} d")
    # Fläche
    if f_position <= n < f_position + laenge:
        # Erde befindet sich im eingestellten Flächenbereich
        flaechen_punkte.append(d)
        flaeche_poly.set_xy(flaechen_punkte)
        if n > f_position + 2:
            # Polygon kann erst mit drei Punkten gebildet werden
            teilflaeche = sPoly(flaechen_punkte).area
            a_text.set_text(
                f"A = {np.format_float_scientific(teilflaeche, precision=5)} "
                f"$m^2$"
            )
    elif n == f_position + laenge:
        # Ende des Polygons
        poly = sPoly(flaechen_punkte)
        flaeche = poly.area
        a_text.set_text(
            f"A = {np.format_float_scientific(flaeche, precision=5)} $m^2$"
        )
        # Reset Flächenberechnung
        flaechen_punkte = [(0, 0)]
        # Nächster Ankerpunkt für Flächenberechnung
        f_position += abstand
    return plot, kreis, t_text, flaeche_poly, a_text


# Ausführung Animation (Aktualisierung alle 30 Millisekunden)
ani = mpl.animation.FuncAnimation(fig, update, interval=30, blit=True)

# Anzeige Plot
plt.show()
