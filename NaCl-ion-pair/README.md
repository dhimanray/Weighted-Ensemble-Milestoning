## Steps for simulating a generic system

1) Perform short equilibration in the ```prep/eq``` directory. Output name should be ```milestone_equilibration```.

2) Store all input files for simulation in ```namd_config``` directory. Make sure the name of the input restart file (.coor, .vel and .xsc) is ```parent```and the output name is ```seg```.

3) Specify the bin distribution, number of trajectories per bin, number of iterations, iteration length etc. in the ```west.cfg``` and ```west.new.cfg``` appropriately.

4) Modify ```westpa_scripts/calculatedistance.py``` to put in values of the two neighbouring milestones.

5) The job is run by submitting the ```job.sh``` file using ```qsub``` command.


## Analysis scripts

These scripts are available in Analysis directory.

```mfpt-all.py```: calculte mean first passage time (MFPT) to all other milestones starting from a given starting milestone

```mfpt-reverse-milestoning.py```: Same as above but the MFPT is calculated for the reverse process.

```free-energy-milestoning.py```: Calculate free energy profile as a function of reaction coordinate at each milestone

```runall.sh```: Convert all .ipynb analysis files into .py files and perform analysis in terminal (parallelized for 8 cores)

## Scripts for averaging and plotting

Scripts are available in the averaging and plotting directory.

```dir.sh```: Generates the directory structure. Run before ```combine.py```

```combine.py```: Combine the statistics of three trials and generates an average transition kernel and lifetime vector. This program generates ```milestone-data.dat``` files in the directory of each milestone.

File names for plotting codes are self-explanatory.



