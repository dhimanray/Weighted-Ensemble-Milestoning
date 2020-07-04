import numpy as np
import matplotlib.pyplot as plt

#mps = [2.45, 2.7, 3.6, 4.6, 7.0, 9.0, 11.0]

l11 = np.loadtxt('../trial_1/dataset/free-energy-error-analysis.dat')
l12 = np.loadtxt('../trial_2/dataset/free-energy-error-analysis.dat')
l13 = np.loadtxt('../trial_3/dataset/free-energy-error-analysis.dat')

l2 = np.loadtxt('free-energy-error-analysis.dat')

l3 = np.loadtxt('../../../long_production/1dPMF-jacobian')

l11[:,1] += 2.*np.log(l11[:,0])
l11[:,1] -= np.min(l11[:,1])
l12[:,1] += 2.*np.log(l12[:,0])
l12[:,1] -= np.min(l12[:,1])
l13[:,1] += 2.*np.log(l13[:,0])
l13[:,1] -= np.min(l13[:,1])
l2[:,1] += 2.*np.log(l2[:,0])
l2[:,1] -= np.min(l2[:,1])


plt.plot(l11[:7,0], l11[:7,1], c='g', ls='-',lw=3, label='Trial_1')
plt.plot(l12[:7,0], l12[:7,1], c='b', ls='-',lw=3, label='Trial_2')
plt.plot(l13[:7,0], l13[:7,1], c='r', ls='-',lw=3, label='Trial_3')
plt.plot(l2[:7,0], l2[:7,1], c='k', ls='-',lw=3, label='Average')
plt.plot(l3[:,0], l3[:,1], c='m', ls='-',lw=3, label='300 ns MD')

plt.fill_between(l11[:7,0], l11[:7,1]-l11[:7,2], l11[:7,1]+l11[:7,2], facecolor='xkcd:lightgreen')
plt.fill_between(l12[:7,0], l12[:7,1]-l12[:7,2], l12[:7,1]+l12[:7,2], facecolor='xkcd:lightblue')
plt.fill_between(l13[:7,0], l13[:7,1]-l13[:7,2], l13[:7,1]+l13[:7,2], facecolor='xkcd:pink')
plt.fill_between(l2[:7,0], l2[:7,1]-l2[:7,2], l2[:7,1]+l2[:7,2], facecolor='xkcd:gray')

#plt.axhline(y=expt,c='m',lw=3)

plt.xlabel('Distance between Na+ and Cl- ($\AA$)',fontsize=18)
plt.ylabel('PMF ($k_BT$)',fontsize=18)
plt.legend(fontsize=16,ncol=2)
#plt.xlim(2,9)
#plt.ylim(0,7)
plt.xticks([2.5,3.5,5,7,9],fontsize=16)
plt.yticks(fontsize=16)
plt.tight_layout()
#plt.show()
plt.savefig('NaCl-free-energy-jacobian-plot.pdf')
