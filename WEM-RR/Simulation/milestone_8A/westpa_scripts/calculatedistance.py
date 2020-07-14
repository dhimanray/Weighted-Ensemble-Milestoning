import numpy as np

endpoint1 = 6.0
endpoint2 = 10.0

l = np.loadtxt('parent_r.dat')

r = l[len(l)-1]

#print("{:.2f}".format(psi))

l = []

l = np.loadtxt('seg.colvars.traj')

for i in range(len(l)):
    if r > endpoint1 and r < endpoint2:
        r = l[i,1]
    print("{:.2f}".format(r))
