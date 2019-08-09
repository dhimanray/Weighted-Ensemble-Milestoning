import MDAnalysis as md

u = md.Universe('A.psf','A_production.dcd')

for ts in u.trajectory:             #loop over frames of trajectory
#---------- CALCULATE CHI ------------------#
    #select the atom objects
    x1 = u.select_atoms('bynum 5')
    x2 = u.select_atoms('bynum 7')
    x3 = u.select_atoms('bynum 9')
    x4 = u.select_atoms('bynum 15')

    #calculate position of the atoms
    r1 = x1.positions
    r2 = x2.positions
    r3 = x3.positions
    r4 = x4.positions

    #calculate the dihedral angle
    chi = md.lib.distances.calc_dihedrals(r1,r2,r3,r4)

#---------- CALCULATE CHI ------------------#
    #select the atom objects
    x1 = u.select_atoms('bynum 7')
    x2 = u.select_atoms('bynum 9')
    x3 = u.select_atoms('bynum 15')
    x4 = u.select_atoms('bynum 17')

    #calculate position of the atoms
    r1 = x1.positions
    r2 = x2.positions
    r3 = x3.positions
    r4 = x4.positions

    #calculate the dihedral angle
    theta = md.lib.distances.calc_dihedrals(r1,r2,r3,r4)


    print chi[0]*180.0/3.14, theta[0]*180.0/3.14

