import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

oxygen = [0, 0, 0]
hydrogen1 = [-0.757, 0.586, 0]
hydrogen2 = [0.757, 0.586, 0]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(*oxygen, color='red', label='Oxygen')
ax.scatter(*hydrogen1, color='blue', label='Hydrogen')
ax.scatter(*hydrogen2, color='blue')

ax.plot([oxygen[0], hydrogen1[0]], [oxygen[1], hydrogen1[1]], [oxygen[2], hydrogen1[2]], color='black')
ax.plot([oxygen[0], hydrogen2[0]], [oxygen[1], hydrogen2[1]], [oxygen[2], hydrogen2[2]], color='black')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

ax.legend()

plt.show()
