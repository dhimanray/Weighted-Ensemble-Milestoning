import numpy as np
import matplotlib.pyplot as plt

l71 = np.loadtxt('7_milestones/ct.dat')
l72 = np.loadtxt('7_milestones-trial2/ct.dat')
l73 = np.loadtxt('7_milestones-trial3/ct.dat')

l91 = np.loadtxt('9_milestones/ct.dat')
l92 = np.loadtxt('9_milestones-trial2/ct.dat')
l93 = np.loadtxt('9_milestones-trial3/ct.dat')

l = np.loadtxt('production/time-correlation.dat')

lmean1 = np.array([ np.mean(np.array([l71[i,1],l72[i,1],l73[i,1]])) for i in range(len(l71)) ])
lstd1 = np.array([ np.std(np.array([l71[i,1],l72[i,1],l73[i,1]])) for i in range(len(l71)) ])

lmean2 = np.array([ np.mean(np.array([l91[i,1],l92[i,1],l93[i,1]])) for i in range(len(l91)) ])
lstd2 = np.array([ np.std(np.array([l91[i,1],l92[i,1],l93[i,1]])) for i in range(len(l91)) ])

plt.errorbar(l91[:,0], lmean2, yerr=lstd2, elinewidth=0.1, c='b', ls='-', capsize=2, errorevery=3, uplims=False, lolims=False, barsabove=False, lw=3, label='WEM 9 Milestones')

plt.errorbar(l71[:,0], lmean1, yerr=lstd1, elinewidth=0.3, c='g', ls='-', capsize=2, errorevery=3, uplims=False, lolims=False, barsabove=False, lw=3, label='WEM 7 Milestones')

plt.plot(l[:,0], l[:,1], 'r-', lw=3, label='Regular LD')
plt.xlim(0,100000)
plt.ylim(0.0,1.0)
plt.xlabel('timesteps (t)',fontsize=18)
plt.ylabel('<x(0)x(t)>',fontsize=18)
handles, labels = plt.gca().get_legend_handles_labels()
order = [0,2,1]
plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order],fontsize=17)
#plt.legend(fontsize=17)
#plt.title('Barrier = 2.0 $k_BT$',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.tight_layout()
#plt.show()
plt.savefig('11d-time-corr.pdf')
