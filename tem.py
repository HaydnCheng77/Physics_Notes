import numpy as np
import matplotlib.pyplot as plt

# x = m/M runs from 1/3 down to 1/10
x = np.linspace(0, 0.5, 400)
y = np.abs(1 - 10*x) / (1 + 8*x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, lw=2, color='orange')
# Mark the endpoints
plt.scatter([1/3, 1/10], 
            [np.abs(1 - 10*(1/3)) / (1 + 8*(1/3)), 
             np.abs(1 - 10*(1/10)) / (1 + 8*(1/10))], 
            color='red')
plt.text(1/3, (np.abs(1 - 10*(1/3)) / (1 + 8*(1/3))) + 0.03, 'm/M=1/3', ha='center')
plt.text(1/10, (np.abs(1 - 10*(1/10)) / (1 + 8*(1/10))) + 0.03, 'm/M=1/10', ha='center')

plt.title('Normalized body amplitude $(|1 - 10x|)/(1 + 8x)$ vs. $x = m/M$')
plt.xlabel('$x = m/M$')
plt.ylabel('$(|1 - 10x|)/(1 + 8x)$')
plt.grid(True)
plt.xlim(0.10, 0.3333)
plt.ylim(0, max(y)*1.1)
plt.show()
