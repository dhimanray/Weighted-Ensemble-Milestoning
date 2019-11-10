import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt('trajectory.dat')

l = []
for i in range(len(a)):
    l.append(a[i])
l = np.array((l))

histogm, psi_edges = np.histogram(l[:,1], bins=180, density=True)

#print histogm
zeros = np.where(histogm==0.0)
histogm[zeros] = 1e-14
freeE = -0.6*np.log(histogm)
#freeE = np.matrix.transpose(freeE)
#print freeE

mini = np.min(freeE)
for i in range(len(freeE)):
    freeE[i] -= mini

f1 = open('1dPMF','w')
for j in range(len(psi_edges)-1):
    print >>f1, (psi_edges[j]+psi_edges[j+1])*0.5, freeE[j]
f1.close()
