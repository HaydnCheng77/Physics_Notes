import numpy as np
import matplotlib.pyplot as plt

# Define the function z = xy exp(x + y)
def z_function(x, y):
    return x * y * np.exp(x + y)

# Create a grid of x and y values
x = np.linspace(-1, 1, 100)  # Range of x values
y = np.linspace(-1, 1, 100)  # Range of y values
X, Y = np.meshgrid(x, y)     # Create a meshgrid for x and y

# Compute z values for the grid
Z = z_function(X, Y)

# Plot the contour map
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, 20, cmap='viridis')  # Contour plot with 20 levels
plt.clabel(contour, inline=True, fontsize=8)        # Add labels to the contours
plt.title(r"Contour Plot of $z = xy \exp(x + y)$")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(contour, label="z")                    # Add a colorbar for the contour levels
plt.grid(alpha=0.3)

# Show the plot
plt.show()