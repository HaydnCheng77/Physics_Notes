import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the domain for x and y
x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)

# Define the surfaces
Z1 = np.sqrt(np.maximum(0, 4 - X**2 - Y**2))  # z = sqrt(4 - x^2 - y^2), ensure no negative values
Z2 = 1 - 2 * (X**2 + Y**2)                   # z = 1 - 2(x^2 + y^2)
Z3 = X * Y                                   # z = xy
Z4 = X**2 - Y**2                             # z = x^2 - y^2

# Create 3D surface plots
fig = plt.figure(figsize=(16, 12))

# Plot (i) z = sqrt(4 - x^2 - y^2)
ax1 = fig.add_subplot(241, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_title('(i) z = sqrt(4 - x^2 - y^2)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

# Plot (ii) z = 1 - 2(x^2 + y^2)
ax2 = fig.add_subplot(242, projection='3d')
ax2.plot_surface(X, Y, Z2, cmap='coolwarm')
ax2.set_title('(ii) z = 1 - 2(x^2 + y^2)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

# Plot (iii) z = xy
ax3 = fig.add_subplot(243, projection='3d')
ax3.plot_surface(X, Y, Z3, cmap='plasma')
ax3.set_title('(iii) z = xy')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')

# Plot (iv) z = x^2 - y^2
ax4 = fig.add_subplot(244, projection='3d')
ax4.plot_surface(X, Y, Z4, cmap='cividis')
ax4.set_title('(iv) z = x^2 - y^2')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('z')

# Create contour plots
fig2 = plt.figure(figsize=(16, 12))

# Contour (i) z = sqrt(4 - x^2 - y^2)
ax5 = fig2.add_subplot(241)
contour1 = ax5.contour(X, Y, Z1, cmap='viridis')
ax5.set_title('(i) Contour of z = sqrt(4 - x^2 - y^2)')
ax5.set_xlabel('x')
ax5.set_ylabel('y')

# Contour (ii) z = 1 - 2(x^2 + y^2)
ax6 = fig2.add_subplot(242)
contour2 = ax6.contour(X, Y, Z2, cmap='coolwarm')
ax6.set_title('(ii) Contour of z = 1 - 2(x^2 + y^2)')
ax6.set_xlabel('x')
ax6.set_ylabel('y')

# Contour (iii) z = xy
ax7 = fig2.add_subplot(243)
contour3 = ax7.contour(X, Y, Z3, cmap='plasma')
ax7.set_title('(iii) Contour of z = xy')
ax7.set_xlabel('x')
ax7.set_ylabel('y')

# Contour (iv) z = x^2 - y^2
ax8 = fig2.add_subplot(244)
contour4 = ax8.contour(X, Y, Z4, cmap='cividis')
ax8.set_title('(iv) Contour of z = x^2 - y^2')
ax8.set_xlabel('x')
ax8.set_ylabel('y')

# Show plots
plt.show() 

#sdfqwe