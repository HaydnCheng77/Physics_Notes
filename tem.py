import numpy as np
import matplotlib.pyplot as plt

# Define the extended grid over [-100, 100] × [-100, 100]
x = np.linspace(-20, 20, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

# Define the function f(x,y) = x * y * exp(x - y)
Z = X * Y * np.exp(X - Y)

# Mask out everything except the second quadrant (x < 0, y > 0)
mask = ~((X < 0) & (Y > 0))       # True outside Q2, False inside
Z_masked = np.ma.masked_where(mask, Z)

# Create the contour plot with 200 levels
plt.figure(figsize=(8, 8))
contours = plt.contour(
    X, Y, Z_masked,
    levels=200,
    cmap='viridis'
)
plt.clabel(contours, inline=True, fontsize=4)
plt.title(r'Contour plot of $f(x,y) = x\,y\,e^{\,x - y}$ (Q2 only, extended grid)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
