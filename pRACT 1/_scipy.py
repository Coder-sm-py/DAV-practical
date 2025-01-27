from scipy.signal import chirp as cp
import numpy as np
import matplotlib.pyplot as plt  # Importing matplotlib for plotting

# Time vector
t_T = np.linspace(3, 10, 300)

# Generate a linear chirp signal
w_W = cp(t_T, f0=4, f1=2, t1=5, method='linear')

# Plotting the chirp signal
plt.plot(t_T, w_W)
plt.title("Linear Chirp")
plt.xlabel('Time in Seconds')
plt.show()
