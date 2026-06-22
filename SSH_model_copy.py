import matplotlib.pyplot as plt
import numpy as np


v = 0.5
w = 1
N = 20

H = np.zeros((2*N,2*N))

for m in range(N):

    H[2*m,2*m+1] = v
    H[2*m+1,2*m] = v

    if m < N-1:
        H[2*m+1,2*m+2] = w
        H[2*m+2,2*m+1] = w

eigvals, eigvecs = np.linalg.eigh(H)

idx = np.argmin(np.abs(eigvals))
psi = eigvecs[:,idx]

psi = np.array(psi)
prob = np.abs(psi)**2
prob_A = prob[0::2]
prob_B = prob[1::2]

cells = np.arange(N)
width = 0.4

plt.bar(cells - width/2, prob_A, width, label='A')
plt.bar(cells + width/2, prob_B, width, label='B')


plt.xlabel("Unit Cell")
plt.ylabel(r"$|\psi|^2$")
plt.legend()

plt.show()