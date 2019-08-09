import numpy as np
import scipy.interpolate as intp
import matplotlib.pyplot as plt

a = np.loadtxt('single-trajectory.dat')

l = a[:500000]
Nstep = len(l)

#grid for interpolation
t = np.linspace(0,l[Nstep-1,0],num=(l[Nstep-1,0]/100))

x = intp.griddata(l[:,0], l[:,1], t, method='linear')

for i in range(len(l)):
    l[i,0] = l[i,0]*0.02

for i in range(len(x)):
    t[i] = t[i]*0.02

plt.scatter(l[:,0], l[:,1],lw=0.6, label='Trajectory in milestone space')
plt.plot( t, x, 'g--', lw=0.3, label='Interpolated trajectory')
plt.xlim(0,10000)
plt.xlabel('time (ps)',fontsize=14)
plt.ylabel('$\psi (^{\circ})$',fontsize=14)
plt.yticks([-100,-60,-20,20,60,100,150,180])
plt.ylim(-120,250)
plt.legend()
#plt.show()
plt.savefig('Interpolated-trajectory.pdf')

