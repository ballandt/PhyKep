"""Simulation Kepler II

Adrian Scheibe, Camillo Ballandt

Berechnet die Sektoren der durch das newtonsche Gravitationsgesetz gewonnenen
Daten und vergleicht die Flächen.
"""
from math import hypot
import numpy as np
from scipy.integrate import trapezoid
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.path as pth
import matplotlib.animation


# Anfangswerte

m_sonne = 1.989e30            # [kg] Sonnenmasse
m_erde = 5.97e24              # [kg] Erdmasse

d = np.array([149.598e9, 0])  # [m] Distanz Sonne - Erde
v = np.array([-6e3, -23e3])   # [m/s] Ausgangsgeschwindigkeit Erde

tag = 60 * 60 * 24            # [s] Tag in Sekunden
dt = 1 * tag                  # [s] Zeitschritt

G = 6.673e-11                 # [m^3/(kg*s^2)] Gravitationskonstante

x = []                        # Liste für x-Positionswerte
y = []                        # Liste für y-Positionswerte

abstand = 60                  # [d]
laenge = 30                   # [d]
f_position = abstand
dist = []


# Erdkreis
kreis_x = 0.5e10 * np.sin(np.linspace(0, 2*np.pi))
kreis_y = 0.5e10 * np.cos(np.linspace(0, 2*np.pi))

# Animation Grundlage

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Plotte Sonne
ax.plot(1e10 * np.sin(np.linspace(0, 2*np.pi)),
        1e10*np.cos(np.linspace(0, 2*np.pi)))

# Plotte Erdkreis
kreis, = ax.plot([], [])

# Plotte Planetenorbit
plot, = ax.plot(x, y)

# Plotte Geschwindigkeit
v_text = ax.text(-2e11, 2e11, "")
t_text = ax.text(-2e11, 1.7e11, "")

# Achseneinstellungen
ax.set_xlim(-2.5e11, 2.5e11)
ax.set_ylim(-2.5e11, 2.5e11)
plt.gca().set_aspect('equal', adjustable='box')

# Fläche
flaeche_x = [0]
flaeche_y = [0]
flaeche, = ax.plot(flaeche_x, flaeche_y)


def update(n):
    """Animationsupdate
    Berechnet die neue Position und gibt die aktualisierten Plots zurück.
    """
    # Greife auf globale Variablen zu
    global v, d, x, y, abstand, laenge, f_position, dist, flaeche_x, flaeche_y
    F = -G * m_sonne * m_erde / np.linalg.norm(d)**3 * d
    a = F / m_erde
    v = a*dt + v
    d = v*dt + d
    x.append(d[0])  # Zum Anfügen von Werten sind Listen besser als arrays
    y.append(d[1])
    # Fläche
    if n == f_position:
        inter = d
    elif f_position <= n < f_position + laenge:
        dist.append(hypot(d[0], d[1])**2)
        flaeche_x.append(d[0])
        flaeche_y.append(d[1])
        flaeche.set_data(flaeche_x, flaeche_y)
    elif n == f_position + laenge:
        t = np.linspace(f_position, f_position+laenge, 1)
        print(trapezoid(dist), t)
        f_position = n + abstand
        flaeche_x.append(0)
        flaeche_y.append(0)
        flaeche.set_data(flaeche_x, flaeche_y)
    # Plot-Aktualisierungen
    plot.set_data(x, y)
    kreis.set_data(kreis_x + d[0], kreis_y + d[1])
    v_text.set_text(f"v = {np.linalg.norm(v):5.0f} m/s")
    t_text.set_text(f"t = {n} d")
    return plot, kreis, v_text, t_text, flaeche


# Ausführung Animation (Aktualisierung alle 30 Millisekunden)
ani = mpl.animation.FuncAnimation(fig, update, interval=30, blit=True)

# Anzeige Plot
plt.show()
