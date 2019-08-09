import numpy as np

l = np.loadtxt('seg.colvars.traj')

for i in range(len(l)):
    psi = l[i,2]
    print("{:.2f}".format(psi))
