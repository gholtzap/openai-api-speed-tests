import numpy as np
import matplotlib.pyplot as plt

from data.ada_data import averaged_ada_data 
from data.curie_data import averaged_curie_data
from data.babbage_data import averaged_babbage_data
from data.davinci_data import averaged_davinci_data

ada_data = averaged_ada_data
curie_data = averaged_curie_data
babbage_data = averaged_babbage_data
davinci_data = averaged_davinci_data

print("################")
print(ada_data)

temperatures = [0, 0.5, 1, 1.5, 2]
max_tokens = [32, 128, 512, 2048]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 5))

# Create heatmaps
c1 = ax1.imshow(ada_data, cmap='cividis', interpolation='nearest')
ax1.set_title("Ada")

c2 = ax2.imshow(curie_data, cmap='cividis', interpolation='nearest')
ax2.set_title("Curie")

c3 = ax3.imshow(babbage_data, cmap='cividis', interpolation='nearest')
ax3.set_title("Babbage")

c4 = ax4.imshow(davinci_data, cmap='cividis', interpolation='nearest')
ax4.set_title("Davinci")


# Set x and y labels
for ax in [ax1, ax2,ax3,ax4]:
    ax.set_xticks(np.arange(len(temperatures)))
    ax.set_yticks(np.arange(len(max_tokens)))
    ax.set_xticklabels(temperatures)
    ax.set_yticklabels(max_tokens)

    # Rotate x labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")

# Add colorbars
plt.colorbar(c1, ax=ax1)
plt.colorbar(c2, ax=ax2)
plt.colorbar(c3, ax=ax3)
plt.colorbar(c4, ax=ax4)

# Add x and y axis labels
ax1.set_ylabel("Max tokens")
ax1.set_xlabel("Temperature")
ax2.set_xlabel("Temperature")

plt.show()
