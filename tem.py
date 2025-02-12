import numpy as np
import matplotlib.pyplot as plt

# Parameters
N_modes = 8  # Number of masses for mode cases
L_modes = 6  # Length of system for mode cases
A_modes = 1.5  # Amplitude of wave for mode cases

N_large = 8  # Number of masses for large mode case
L_large = 6  # Length of system for large mode case
A_large = 1.5   # Amplitude of wave for large mode case

modes = [3, 17]  # Isolated modes

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes = axes.flatten()

# Mode Cases
colors = ['green', 'purple']
for idx, m in enumerate(modes):
    if m == 3:
        N = N_modes
        L = L_modes
        A = A_modes
    else:
        N = N_large
        L = L_large
        A = A_large
    
    x = np.linspace(0, L, N)
    y = A * np.sin(m * np.pi * x / L)
    
    axes[idx].scatter(x, y, color='brown', s=100, zorder=3)
    for i in range(N - 1):
        axes[idx].plot([x[i], x[i+1]], [y[i], y[i+1]], color='black', linewidth=1)
    
    x_dense = np.linspace(0, L, 100)
    y_envelope = A * np.sin(m * np.pi * x_dense / L)
    axes[idx].plot(x_dense, y_envelope, '--', color=colors[idx], linewidth=1)
    
    axes[idx].axhline(0, color='black', linestyle='dotted')
    axes[idx].set_title(f"m={m}", fontsize=14, color='red')
    axes[idx].set_xticks([])
    axes[idx].set_yticks([])
    axes[idx].set_xlim(-0.2, L + 0.2)
    axes[idx].set_ylim(-A-0.5, A+0.5)
    axes[idx].grid(True, linestyle=':', linewidth=0.5)

plt.tight_layout()
plt.show()
