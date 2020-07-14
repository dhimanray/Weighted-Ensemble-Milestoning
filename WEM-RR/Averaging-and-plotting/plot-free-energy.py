import numpy as np
import matplotlib.pyplot as plt

mps1 = [ 6.0 + 2.0*i for i in range(12)]
mps0 = [ 5.0 ]
mps = mps0 + mps1

l11 = np.loadtxt('../trial_1/dataset/free-energy-error-analysis.dat')
l12 = np.loadtxt('../trial_2/dataset/free-energy-error-analysis.dat')
l13 = np.loadtxt('../trial_3/dataset/free-energy-error-analysis.dat')

l2 = np.loadtxt('free-energy-error-analysis.dat')

#experimental free energy
expt = -np.log(0.5*1E-3)


plt.plot(l11[:,0], l11[:,1], c='g', ls='-',lw=3, label='Trial_1')
plt.plot(l12[:,0], l12[:,1], c='b', ls='-',lw=3, label='Trial_2')
plt.plot(l13[:,0], l13[:,1], c='r', ls='-',lw=3, label='Trial_3')
plt.plot(l2[:,0], l2[:,1], c='k', ls='-',lw=3, label='Average')

plt.fill_between(l11[:,0], l11[:,1]-l11[:,2], l11[:,1]+l11[:,2], facecolor='xkcd:lightgreen')
plt.fill_between(l12[:,0], l12[:,1]-l12[:,2], l12[:,1]+l12[:,2], facecolor='xkcd:lightblue')
plt.fill_between(l13[:,0], l13[:,1]-l13[:,2], l13[:,1]+l13[:,2], facecolor='xkcd:pink')
plt.fill_between(l2[:,0], l2[:,1]-l2[:,2], l2[:,1]+l2[:,2], facecolor='xkcd:gray')

plt.axhline(y=expt,c='m',lw=3)
plt.text(5,expt+0.5,'Experiment',fontsize=16)

plt.xlabel('Protein-Ligand Distance ($\AA$)',fontsize=18)
plt.ylabel('Free energy ($k_BT$)',fontsize=18)
plt.legend(fontsize=16,ncol=1,loc="lower right")
plt.xticks(mps,fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
#plt.show()
plt.savefig('free-energy-plot-cons-release.pdf')
