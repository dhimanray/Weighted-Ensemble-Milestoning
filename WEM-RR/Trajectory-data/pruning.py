import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as md
from MDAnalysis import analysis

u = md.Universe('nowat.parm7','milestone_12A.dcd')

protein = u.select_atoms("protein")
#trp59 = u.select_atoms("resid 59")

ligand = u.select_atoms("resid 108")
ever = u.select_atoms("all")

'''for ts in u.trajectory:
    #a = trp59.center_of_mass()
    b = ligand.center_of_mass()
    a = protein.center_of_mass()
    r = np.linalg.norm(a-b)'''

with md.Writer("mile_12A_pruned.dcd", ever.n_atoms) as W:
    for ts in u.trajectory:
        b = ligand.center_of_mass()
        a = protein.center_of_mass()
        r = np.linalg.norm(a-b)

        if r > 10.0 and r < 14.0:
            W.write(ever)




