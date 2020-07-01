#protein-ligand distance for each frame

import numpy as np
import MDAnalysis as md

u = md.Universe('ionized.psf','1d7j_production_NPT.dcd')

protein = u.select_atoms("protein")

ligand = u.select_atoms("bynum 1664:1677")

#ever = u.select_atoms("all")

#rlist = [0,5,208,891,914,950,994,999]

f1 = open('distances.dat','w')
print('# frame index   #distance',file=f1)
for ts in u.trajectory:
    a = protein.center_of_mass()
    b = ligand.center_of_mass()
    r = np.linalg.norm(a-b)
    print(ts.frame,r,file=f1)
f1.close()

#    if ts.frame in rlist:
#        with md.Writer('milestone-pdb/fkbp-buq-r=%dA.pdb'%int(round(r)),ever.n_atoms) as W:
#            W.write(ever)
#            print('pdb-written')



