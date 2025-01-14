import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function z = xy * exp(x + y)
def func(x, y):
    return x * y * np.exp(x + y)

# Generate grid points for x and y
x = np.linspace(-2, 2, 100)  # Range for x
y = np.linspace(-2, 2, 100)  # Range for y
x, y = np.meshgrid(x, y)

# Calculate z values
z = func(x, y)

# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# Add labels and a color bar
ax.set_title('3D Plot of z = xy * exp(x + y)', fontsize=14)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
fig.colorbar(surf, shrink=0.5, aspect=10)

# Show the plot
plt.tight_layout()
plt.show()