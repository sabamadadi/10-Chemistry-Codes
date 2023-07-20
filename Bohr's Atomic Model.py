import matplotlib.pyplot as plt
import numpy as np

nucleus_radius = 0.2
electron_radius = 0.05
orbit_radii = [0.5, 0.8, 1.1]  # Orbit radii for electrons
orbit_colors = ['r', 'g', 'b']  # Colors for each orbit

fig, ax = plt.subplots()

nucleus = plt.Circle((0, 0), nucleus_radius, color='k')
ax.add_artist(nucleus)

for i, radius in enumerate(orbit_radii):
    orbit = plt.Circle((0, 0), radius, color=orbit_colors[i], fill=False)
    ax.add_artist(orbit)

num_electrons = len(orbit_radii)
theta = np.linspace(0, 2*np.pi, num_electrons, endpoint=False)
x = [orbit_radii[i] * np.cos(theta[i]) for i in range(num_electrons)]
y = [orbit_radii[i] * np.sin(theta[i]) for i in range(num_electrons)]
electrons = [plt.Circle((x[i], y[i]), electron_radius, color='k') for i in range(num_electrons)]
for electron in electrons:
    ax.add_artist(electron)

ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

ax.axis('off')

plt.show()
