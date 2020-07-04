import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt('distance-data.dat')

l = []
for i in range(10000,len(a)):
    l.append(a[i])
l = np.array((l))

histogm, r_edges = np.histogram(l[:,1], range=(2.35,9.0), bins=50, density=True)

#print histogm
zeros = np.where(histogm==0.0)
histogm[zeros] = 1e-14
freeE = -np.log(histogm)
r = np.zeros(len(r_edges)-1)
for j in range(len(r)):
    r[j] = (r_edges[j]+r_edges[j+1])*0.5
freeE += 2.0*np.log(r)
mini = np.min(freeE)
for i in range(len(freeE)):
    freeE[i] -= mini

f1 = open('1dPMF-jacobian','w')
for j in range(len(r)):
    print >>f1, r[j], freeE[j]
f1.close()



