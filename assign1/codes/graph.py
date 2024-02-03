import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
data = np.loadtxt("data12.dat")

# Separate n and x(n) values
n_values, x_values = data[:, 0], data[:, 1]

# Plot the graph
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r-', label=r'$x(n) = (3 + 5n)u(n)$')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.legend()
plt.savefig('x(n)_vs_n.png')
