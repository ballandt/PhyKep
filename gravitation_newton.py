"""Simulation Gravitationsgesetz

Adrian Scheibe, Camillo Ballandt

Reines Gravitationsgesetz ausgelegt auf Erde und Sonne. Markierungen und
Skalierung absolut.

Grundlage:
F = G * m1 * m2 / norm(d)**3 * d
a = F / m
v = a * dt + v0
d = v * dt + d0

Sonne und Erde werden als Kreise dargestellt, der Orbit der Erde als Graph.
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation


# Anfangswerte
# === Veränderbar ===
v = np.array([-6e3, -23e3])   # [m/s] Ausgangsgeschwindigkeit Erde

# === Veränderung nicht empfohlen ===
m_sonne = 1.989e30            # [kg] Sonnenmasse
m_erde = 5.97e24              # [kg] Erdmasse

d = np.array([149.598e9, 0])  # [m] Distanz Sonne - Erde

tag = 60 * 60 * 24            # [s] Tag in Sekunden
dt = 1 * tag                  # [s] Zeitschritt

G = 6.673e-11                 # [m^3/(kg*s^2)] Gravitationskonstante

x = []                        # Liste für x-Positionswerte
y = []                        # Liste für y-Positionswerte
# === ===

# Animation Grundlage

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Erdkreis
kreis_x = 0.5e10 * np.sin(np.linspace(0, 2*np.pi))
kreis_y = 0.5e10 * np.cos(np.linspace(0, 2*np.pi))
# Plotte Erdkreis
kreis, = ax.plot([], [])

# Plotte Sonne
ax.plot(1e10 * np.sin(np.linspace(0, 2*np.pi)),
        1e10*np.cos(np.linspace(0, 2*np.pi)))


# Plotte Planetenorbit
plot, = ax.plot(x, y)

# Plotte Zeit, Geschwindigkeit
t_text = ax.text(-2e11, 1.7e11, "")
v_text = ax.text(-2e11, 2e11, "")

# Achseneinstellungen
ax.set_xlim(-2.5e11, 2.5e11)
ax.set_ylim(-2.5e11, 2.5e11)
plt.gca().set_aspect('equal', adjustable='box')


def update(n):
    """Animationsupdate
    Berechnet die neue Position und gibt die aktualisierten Plots zurück.
    """
    global v, d, x, y  # Greife auf globale Variablen zu
    # Gravitationsmodell
    F = -G * m_sonne * m_erde / np.linalg.norm(d)**3 * d
    a = F / m_erde
    v = a*dt + v
    d = v*dt + d
    x.append(d[0])  # Zum Anfügen von Werten sind Listen besser als arrays
    y.append(d[1])
    # Plot-Aktualisierungen
    plot.set_data(x, y)
    kreis.set_data(kreis_x + d[0], kreis_y + d[1])
    v_text.set_text(
        f"v = {int(round(np.linalg.norm(v), -3))} $\\frac{{m}}{{s}}$"
    )
    t_text.set_text(f"t = {n} d")
    return plot, kreis, t_text, v_text


# Ausführung Animation (Aktualisierung alle 30 Millisekunden)
ani = mpl.animation.FuncAnimation(fig, update, interval=30, blit=True)

# Anzeige Plot
plt.show()
