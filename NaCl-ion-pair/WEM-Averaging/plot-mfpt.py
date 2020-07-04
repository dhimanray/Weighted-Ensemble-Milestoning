import numpy as np
import matplotlib.pyplot as plt

mps1 = [ 6.0 + 2.0*i for i in range(12)]
mps0 = [ 5.0 ]
mps = mps0 + mps1

l11 = np.loadtxt('../trial_1/dataset/mfpt-all.dat')
l12 = np.loadtxt('../trial_2/dataset/mfpt-all.dat')
l13 = np.loadtxt('../trial_3/dataset/mfpt-all.dat')

l2 = np.loadtxt('mfpt-all.dat')

#data from regular MD
#exact = np.loadtxt('../../regular_mfpt/data/regular-mfpt-data.dat')

plt.plot(l11[:,0], l11[:,1], c='g', ls='-',lw=3, label='Trial_1')
plt.plot(l12[:,0], l12[:,1], c='b', ls='-',lw=3, label='Trial_2')
plt.plot(l13[:,0], l13[:,1], c='r', ls='-',lw=3, label='Trial_3')
plt.plot(l2[:,0], l2[:,1], c='k', ls='-',lw=3, label='Average')

plt.fill_between(l11[:,0], l11[:,1]-l11[:,3], l11[:,1]+l11[:,3], facecolor='xkcd:lightgreen',alpha=0.5)
plt.fill_between(l12[:,0], l12[:,1]-l12[:,3], l12[:,1]+l12[:,3], facecolor='xkcd:lightblue',alpha=0.5)
plt.fill_between(l13[:,0], l13[:,1]-l13[:,3], l13[:,1]+l13[:,3], facecolor='xkcd:pink',alpha=0.5)
plt.fill_between(l2[:,0], l2[:,1]-l2[:,3], l2[:,1]+l2[:,3], facecolor='xkcd:gray',alpha=0.5)

plt.axhline(y=1253,lw=3,c='m')
#plt.plot(exact[:,0], exact[:,1], c='m', ls='-',lw=3, label='Regular MD')
#plt.fill_between(exact[:,0], exact[:,1]-exact[:,3], exact[:,1]+exact[:,3], facecolor='xkcd:red',alpha=0.3)
plt.yscale('log')
plt.ylim(500,4000)
plt.xlabel('Distance between Na+ and Cl- ($\AA$)',fontsize=18)
plt.ylabel('Mean First passage time (ps)',fontsize=18)
plt.legend(fontsize=16,ncol=2)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
#plt.show()
plt.savefig('NaCl-mfpt-plot.pdf')
