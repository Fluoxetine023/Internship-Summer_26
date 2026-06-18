import matplotlib.pyplot as plt
import numpy as np

v = 0.5
w = 0.6

k = np.linspace(-np.pi, np.pi, 1000)

E = np.sqrt(v**2 + w**2 + 2*v*w*np.cos(k))

plt.plot(k,E)
plt.plot(k,-E)

plt.grid()
plt.show()