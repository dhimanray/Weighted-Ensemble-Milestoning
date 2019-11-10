#!/usr/bin/env python
import MDAnalysis
import MDAnalysis.lib.distances

# Load the trajectories for the current segment and the parent segment.
# We need all timepoints from the current segment, and the final timepoint
# from the parent segment (which is where the current segment starts)
parent_universe = MDAnalysis.Universe('structure.psf', 'parent.dcd')
current_universe = MDAnalysis.Universe('structure.psf', 'seg.dcd')

# Go to the last timepoint of the parent trajectory and calculate the distance
# between the ions
#parent_nacl = parent_universe.select_atoms('resname SOD or resname CLA')
#parent_universe.trajectory[-1]
#dist = MDAnalysis.analysis.distances.self_distance_array(parent_nacl.atoms.positions, box=parent_universe.dimensions)[0]

#kill trajectories beyond this endpoint
endpoint = 160.0

#index which is chaged from 0 to 1 when reaches endpoint
ind = 0

# Go to the last timepoint of the parent trajectory and calculate the dihedral angle
x1 = parent_universe.select_atoms('bynum 7')
x2 = parent_universe.select_atoms('bynum 9')
x3 = parent_universe.select_atoms('bynum 15')
x4 = parent_universe.select_atoms('bynum 17')

#calculate position of the atoms
r1 = x1.positions
r2 = x2.positions
r3 = x3.positions
r4 = x4.positions

#calculate the dihedral angle
psi = MDAnalysis.lib.distances.calc_dihedrals(r1,r2,r3,r4)

psi = psi*(180.0/3.14159)
psi = psi[0]

if psi > endpoint:
    ind = 1

if ind==0:
    print("{:.2f}".format(psi))
#elif ind==1:
else :
    print("{:.2f}".format(endpoint))


# Now calculate the dihedral angle for each timepoint of the current
# trajectory.


for ts in current_universe.trajectory:
    x1 = current_universe.select_atoms('bynum 7')
    x2 = current_universe.select_atoms('bynum 9')
    x3 = current_universe.select_atoms('bynum 15')
    x4 = current_universe.select_atoms('bynum 17')
    #calculate position of the atoms
    r1 = x1.positions
    r2 = x2.positions
    r3 = x3.positions
    r4 = x4.positions
#    print r1

    #calculate the dihedral angle
    psi = MDAnalysis.lib.distances.calc_dihedrals(r1,r2,r3,r4)
    psi = psi*(180.0/3.14159)
    psi = psi[0]

    if psi > endpoint:
        ind = 1

#    print ind
    if ind==0:
        print("{:.2f}".format(psi))
#    elif ind==1:
    else :
        print("{:.2f}".format(endpoint))




