#Obtaining starting structures for milestoning simulation

import numpy as np
import MDAnalysis as md

u = md.Universe('ionized.psf','1d7j_production_NPT.dcd')

protein = u.select_atoms("protein")

ligand = u.select_atoms("bynum 1664:1677")

ever = u.select_atoms("all")

l = np.loadtxt('milestones.dat')
l = l.T

rlist = l[1]

#print(rlist)

for ts in u.trajectory:
    a = protein.center_of_mass()
    b = ligand.center_of_mass()
    r = np.linalg.norm(a-b)
    print(ts.frame,r)

    if ts.frame in rlist:
        with md.Writer('milestones/FKBP_BUT_r=%dA.pdb'%l[0,np.where(rlist==ts.frame)],ever.n_atoms) as W:
            W.write(ever)
            print('pdb-written')
