import matplotlib.pyplot as plt

# Data for atomic model changes
models = ['Thomson', 'Rutherford', 'Bohr']
years = [1897, 1911, 1913]
radii = [0.01, 0.1, 0.5]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(years, radii, marker='o', linestyle='-', color='blue')

# Add labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Atomic Radius')
ax.set_title('Evolution of Atomic Models')

# Add text annotations for each model
for model, year, radius in zip(models, years, radii):
    ax.annotate(model, xy=(year, radius), xytext=(5, 5), textcoords='offset points')

# Show the plot
plt.show()
