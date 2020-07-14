# Scripts for trajectory data analysis and visualization

```combine.sh```: Combine all the dcd files from ```traj_seg``` directory after removing solvent and ions. Check ```combine_traj.sh``` for usage example.

```combine_traj.sh```: Perform ```combine.sh``` for all milestones one by one.

The above scripts produced .nc files which are converted to .dcd using mdconvert

```pruning.py```: read the dcd output of ```combine.sh``` and mdconvert, remove excess trajectory segment outside the two adjacent milestone and write a pruned dcd

```state_12A.vmd```: Visualization of the ligand distribution around the protein for milestone at 12 Angstrom. It can be changed to other milestones by changing the name of the trajectory file read by the sript.
