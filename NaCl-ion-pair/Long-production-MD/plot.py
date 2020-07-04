import numpy as np
import matplotlib.pyplot as plt

l = np.loadtxt('distance-data.dat')
l = l.T
plt.plot(l[0]*1E-6,l[1],lw=0.6)
plt.ylim(0,10)
plt.xlabel('Time (ns)',fontsize=14)
plt.ylabel('Na$^+$ Cl$^-$ distance ($\AA$)',fontsize=14)
plt.tight_layout()
plt.show()
#plt.savefig('all-trajectories.pdf')
