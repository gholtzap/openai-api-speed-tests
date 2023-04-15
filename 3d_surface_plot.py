import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

temperatures = np.array([0, 0.5, 1, 1.5, 2])
max_tokens = np.array([32, 128, 512, 2048])

# Generate a grid
T, M = np.meshgrid(temperatures, max_tokens)

# Data
ada_data = np.array([
    [0.26,	0.26,	0.27,	0.26,	0.26],
    [0.68,	0.61,	0.64,	0.76,	0.75],
    [0.75,	0.76,	0.97,	2.51,	2.93],
    [0.71,	0.78,	1.95,	3.91,	9.33]
])

curie_data = np.array([
    [0.34, 0.34, 0.31, 0.35, 0.35],
    [0.64, 0.76, 0.71, 0.89, 1.08],
    [0.66, 0.63, 0.88, 1.59, 2.65],
    [0.70, 0.61, 0.78, 2.33, 6.16]
])

fig = plt.figure(figsize=(12, 6))

# Ada plot
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(T, M, ada_data, cmap='viridis', alpha=0.8)
ax1.set_title("Ada")
ax1.set_xlabel("Temperature")
ax1.set_ylabel("Max tokens")
ax1.set_zlabel("Response time")

# Babbage plot
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(T, M, curie_data, cmap='viridis', alpha=0.8)
ax2.set_title("Babbage")
ax2.set_xlabel("Temperature")
ax2.set_ylabel("Max tokens")
ax2.set_zlabel("Response time")

plt.show()
