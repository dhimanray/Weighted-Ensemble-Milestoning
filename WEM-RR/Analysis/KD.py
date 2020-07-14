import numpy as np
import matplotlib.pyplot as plt

l1 = np.loadtxt('mfpt-all.dat')
l2 = np.loadtxt('mfpt-reverse-all.dat')

l1 = l1.T
l2 = l2.T

toff = l1[1]
ton = l2[1][::-1]

print toff, ton

KD = ton/(toff*225.56)

plt.plot(l1[0],KD)
plt.ylim(0,1E-3)
plt.show()
