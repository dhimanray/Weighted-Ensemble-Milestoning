import numpy as np
import matplotlib.pyplot as plt

l1 = np.loadtxt('stationary-distribution.dat')
l2 = np.loadtxt('../production/1dPMF')


for i in range(len(l1)):
    l1[i,1] = -0.6*np.log(l1[i,1])
    print l1[i,1]
mini = np.min(l1[:,1])
for i in range(len(l1)):
    l1[i,1] -= mini
plt.plot(l1[:,0], l1[:,1], 'b-', lw=3, label='WEM 8 Milestones')
plt.plot(l2[:,0], l2[:,1], 'r-', lw=3, label='1 $\mu$s Langevin Dynamics')
plt.xlim(-100.0,180.0)
plt.ylim(0.0,4.0)
plt.xlabel('$\psi (^{\circ})$',fontsize=14)
plt.ylabel('PMF (kcal/mol)',fontsize=14)
plt.legend()
#plt.title('Barrier = 2.0 $k_BT$',fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.show()
plt.savefig('pmf.pdf')
