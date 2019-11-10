import numpy as np
import matplotlib.pyplot as plt

#Plot the potential function in 2D projection
def V(x,y):
    Vx = 1.0*(1.0-x**2)**2
    Vy = 0.0
    Vy += -0.5*(x**2)*y**2 + y**4
    return Vx + Vy
N = 100
x = np.linspace(-2.5,2.5,N)
y = np.linspace(-2,2,N)
v = np.zeros((N,N))
for i in range(N):
    for j in range(N):
        v[j,i] = V(x[i],y[j])
cp=plt.pcolormesh(x,y,v,cmap='rainbow')
cbar=plt.colorbar(cp)
cbar.set_label('V(x,y)/$k_B$T',fontsize=18)
plt.clim(0,5)
plt.xlabel('x',fontsize=18)
plt.ylabel('y',fontsize=18)
plt.axvline(-2, linestyle='-', color='k')
plt.axvline(-1, linestyle='-', color='k')
plt.axvline(-0.5, linestyle='-', color='k')
plt.axvline(0, linestyle='-', color='k')
plt.axvline(0.5, linestyle='-', color='k')
plt.axvline(1, linestyle='-', color='k')
plt.axvline(2, linestyle='-', color='k')
#plt.grid('True',axis='y', ydata=[-100,-60,-20,20,60,100,150], color='r', linestyle='-', linewidth=2)
we_bin = np.arange(-2.0,2.0,0.1)
for i in we_bin:
    plt.axvline(i, linestyle=':', color='k')
x_tics = np.arange(-2.5,3.0,0.5)
plt.xticks(x_tics,fontsize=10)
plt.tick_params(labelsize=14)
plt.tight_layout()
#plt.show()
plt.savefig('11d-potential.pdf', format='pdf', bbox_inches='tight')
