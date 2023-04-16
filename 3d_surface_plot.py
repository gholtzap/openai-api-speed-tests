import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from data.ada_data import averaged_ada_data
from data.curie_data import averaged_curie_data
from data.babbage_data import averaged_babbage_data
from data.davinci_data import averaged_davinci_data

temperatures = np.array([0, 0.5, 1, 1.5, 2])
max_tokens = np.array([32, 128, 512, 2048])

# Generate a grid
T, M = np.meshgrid(temperatures, max_tokens)

ada_data = np.array(averaged_ada_data)
curie_data = np.array(averaged_curie_data)
babbage_data = np.array(averaged_babbage_data)
davinci_data = np.array(averaged_davinci_data)

fig = plt.figure(figsize=(24, 12))

# Ada plot
ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(T, M, ada_data, cmap='cividis', alpha=0.8)
ax1.set_title("Ada")
ax1.set_xlabel("Temperature")
ax1.set_ylabel("Max tokens")
ax1.set_zlabel("Response time")

# Curie plot
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(T, M, curie_data, cmap='cividis', alpha=0.8)
ax2.set_title("Curie")
ax2.set_xlabel("Temperature")
ax2.set_ylabel("Max tokens")
ax2.set_zlabel("Response time")

# Babbage plot
ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(T, M, babbage_data, cmap='cividis', alpha=0.8)
ax3.set_title("Babbage")
ax3.set_xlabel("Temperature")
ax3.set_ylabel("Max tokens")
ax3.set_zlabel("Response time")

# Davinci plot
ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(T, M, davinci_data, cmap='cividis', alpha=0.8)
ax4.set_title("Davinci")
ax4.set_xlabel("Temperature")
ax4.set_ylabel("Max tokens")
ax4.set_zlabel("Response time")

plt.show()
