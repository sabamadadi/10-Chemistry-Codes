import matplotlib.pyplot as plt

atomic_numbers = [1, 6, 11, 16, 19, 26]
atomic_radii = [0.53, 0.77, 1.86, 0.88, 1.80, 1.25]

plt.plot(atomic_numbers, atomic_radii, marker='o', linestyle='-', color='b')

plt.title('Atomic Radius Changes along the Periodic Table')
plt.xlabel('Atomic Number')
plt.ylabel('Atomic Radius (Angstrom)')
plt.grid(True)

plt.show()
