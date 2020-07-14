import numpy as np
import matplotlib.pyplot as plt

mps1 = [ 6.0 + 2.0*i for i in range(6)]
mps0 = [ 5.0 ]
mps = mps0 + mps1

l11 = np.loadtxt('../trial_1/dataset/committor-16A.dat')
l12 = np.loadtxt('../trial_2/dataset/committor-16A.dat')
l13 = np.loadtxt('../trial_3/dataset/committor-16A.dat')

l2 = np.zeros((len(l11),2))
for i in range(len(l2)):
    a = [l11[i,1],l12[i,1],l13[i,1]]
    a = np.asarray(a)
    l2[i,0] = np.mean(a)
    #l2[i,1] = 2.48*np.std(a) #95% confidence interval
    l2[i,1] = np.std(a)


plt.plot(l11[:,0], l2[:,0], c='g', ls='-',lw=3, label='WEM-CR')

plt.fill_between(l11[:,0], l2[:,0]-l2[:,1], l2[:,0]+l2[:,1], facecolor='xkcd:lightgreen')


plt.xlabel('Protein-Ligand Distance ($\AA$)',fontsize=18)
plt.ylabel(r'Committor probability (C)',fontsize=18)
plt.legend(fontsize=18,ncol=2)
plt.xticks(mps,fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
#plt.show()
plt.savefig('committor-plot-16A-cons-release.pdf')
