import numpy as np

endpoint = -60.0

l = np.loadtxt('parent_psi.dat')

psi = l[len(l)-1]

#print("{:.2f}".format(psi))

l = []

l = np.loadtxt('seg.colvars.traj')

for i in range(len(l)):
    if psi < endpoint:
        psi = l[i,2]
    print("{:.2f}".format(psi))
