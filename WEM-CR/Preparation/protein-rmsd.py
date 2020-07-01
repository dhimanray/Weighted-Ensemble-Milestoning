
import numpy as np
import matplotlib.pyplot as plt 
import MDAnalysis as md 
from MDAnalysis import analysis
from MDAnalysis.analysis import rms

f1 = open('protein-rmsd.dat','w')
ref = md.Universe('ionized.psf', 'ionized.pdb')
u = md.Universe('ionized.psf','1d7j_production_NPT.dcd')

protein = u.select_atoms("protein")

ligand = u.select_atoms("bynum 1664:1677")

R = md.analysis.rms.RMSD(u, ref,
           select="backbone",             # superimpose on whole backbone of the whole protein
           groupselections=["protein"])

R.run()

RMSD = R.rmsd.T
for j in range(len(RMSD[0])):
    print(RMSD[0,j],RMSD[3,j],file=f1)
    

f1.close()


