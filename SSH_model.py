import matplotlib.pyplot as plt
import numpy as np

v = [0, 0.4, 0.5, 0.6, 1]
w = [1.0, 0.6, 0.5, 0.4, 0]

k = np.linspace(-np.pi, np.pi, 1000)

fig, ax = plt.subplots(1, 5, figsize=(15, 4), sharey=True)

for i in range(5):
    E = np.sqrt(v[i]**2 + w[i]**2 + 2*v[i]*w[i]*np.cos(k))

    ax[i].plot(k, E)
    ax[i].plot(k, -E)

    ax[i].set_title(f"v={v[i]}, w={w[i]}")
    ax[i].grid(True)

    ax[i].set_xticks([-np.pi, 0, np.pi])
    ax[i].set_xticklabels([r"$-\pi$", "0", r"$\pi$"])

    ax[i].set_xlabel(r"$k$")

ax[0].set_ylabel(r"$E(k)$")

plt.suptitle("SSH Dispersion Relation", fontsize=14)
plt.tight_layout()
plt.show()