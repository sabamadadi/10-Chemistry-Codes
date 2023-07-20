import matplotlib.pyplot as plt

models = ['Thomson', 'Rutherford', 'Bohr']
years = [1897, 1911, 1913]
radii = [0.01, 0.1, 0.5]

fig, ax = plt.subplots()

ax.plot(years, radii, marker='o', linestyle='-', color='blue')

ax.set_xlabel('Year')
ax.set_ylabel('Atomic Radius')
ax.set_title('Evolution of Atomic Models')

for model, year, radius in zip(models, years, radii):
    ax.annotate(model, xy=(year, radius), xytext=(5, 5), textcoords='offset points')

plt.show()
