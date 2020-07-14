# Weighted Ensemble Milestoning with Restraint Release (WEM-RR)

The first implementation of WEM schem sufferes from the problem of having a single starting structure per milestone. In presence of slow orthogonal degrees of freedom it results in high variance in the results in a same system is simulated multiple times. In the WEM-RR scheme the first few (10 here) iterations are performed with a harmonic restraint on the reaction coordinate confining the system on the milestone interface. Using the weighted ensemble method 2N starting structures are generated where N is the number of trajectories per bin. Then the restraint is removed and the original simulation is initiated from this starting structures. 

## Important scripts

'''west.cfg''': This script is the configuration file for the initial restrained iterations. Number of iteration is small (10).
