import matplotlib.pyplot as plt

# Atomic radius data (example values)
atomic_numbers = [1, 6, 11, 16, 19, 26]
atomic_radii = [0.53, 0.77, 1.86, 0.88, 1.80, 1.25]

# Plot the atomic radius changes
plt.plot(atomic_numbers, atomic_radii, marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Atomic Radius Changes along the Periodic Table')
plt.xlabel('Atomic Number')
plt.ylabel('Atomic Radius (Angstrom)')
plt.grid(True)

# Display the plot
plt.show()
