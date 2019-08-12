import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt('A_production.colvars.traj')

l = []
for i in range(1000,len(a)):
    l.append(a[i])
l = np.array((l))

histogm, phi_edges, psi_edges = np.histogram2d(l[:,1], l[:,2], bins=180, density=True)

#print histogm
zeros = np.where(histogm==0.0)
histogm[zeros] = 1e-14
freeE = -0.6*np.log(histogm)
freeE = np.matrix.transpose(freeE)
#print freeE

f1 = open('2dPMF','w')
for i in range(len(phi_edges)-1):
    for j in range(len(phi_edges)-1):
        print >>f1, (phi_edges[i]+phi_edges[i+1])*0.5, (psi_edges[i]+psi_edges[i+1])*0.5 - 180.0 , freeE[i,j]
f1.close()

cp=plt.pcolormesh(phi_edges,psi_edges,freeE,cmap='nipy_spectral')
plt.legend()
plt.colorbar(cp)
plt.clim(5.5,8.5)
plt.show()

#dhist, psi_edges = np.histogram( l[:,2], bins=180, density=True)
#zeros = np.where(dhist==0.0)
#dhist[zeros] = 1e-14
#dfreeE = -0.6*np.log(dhist)
#for i in range(len(dfreeE)):
    #print 0.5*(psi_edges[i]+psi_edges[i+1]),  dfreeE[i]


