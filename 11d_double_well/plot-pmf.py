import numpy as np
import matplotlib.pyplot as plt

l11 = np.loadtxt('7_milestones/stationary-distribution.dat')
l12 = np.loadtxt('7_milestones-trial2/stationary-distribution.dat')
l13 = np.loadtxt('7_milestones-trial3/stationary-distribution.dat')

l21 = np.loadtxt('9_milestones/stationary-distribution.dat')
l22 = np.loadtxt('9_milestones-trial2/stationary-distribution.dat')
l23 = np.loadtxt('9_milestones-trial3/stationary-distribution.dat')

l2 = np.loadtxt('production/1dPMF')


for i in range(len(l11)):
    l11[i,1] = -0.6*np.log(l11[i,1])
   #print l1[i,1]
mini1 = np.min(l11[:,1])
for i in range(len(l11)):
    l11[i,1] -= mini1

for i in range(len(l12)):
    l12[i,1] = -0.6*np.log(l12[i,1])
   # print l1[i,1]
mini2 = np.min(l12[:,1])
for i in range(len(l12)):
    l12[i,1] -= mini2

for i in range(len(l13)):
    l13[i,1] = -0.6*np.log(l13[i,1])
   # print l1[i,1]
mini3 = np.min(l13[:,1])
for i in range(len(l13)):
    l13[i,1] -= mini3

for i in range(len(l21)):
    l21[i,1] = -0.6*np.log(l21[i,1])
   #print l1[i,1]
mini1 = np.min(l21[:,1])
for i in range(len(l21)):
    l21[i,1] -= mini1

for i in range(len(l22)):
    l22[i,1] = -0.6*np.log(l22[i,1])
   # print l1[i,1]
mini2 = np.min(l22[:,1])
for i in range(len(l22)):
    l22[i,1] -= mini2

for i in range(len(l23)):
    l23[i,1] = -0.6*np.log(l23[i,1])
   # print l1[i,1]
mini3 = np.min(l23[:,1])
for i in range(len(l23)):
    l23[i,1] -= mini3

lmean1 = np.array([ np.mean(np.array([l11[i,1],l12[i,1],l13[i,1]])) for i in range(len(l11)) ]) 
lstd1 = np.array([ np.std(np.array([l11[i,1],l12[i,1],l13[i,1]])) for i in range(len(l11)) ])

lmean2 = np.array([ np.mean(np.array([l21[i,1],l22[i,1],l23[i,1]])) for i in range(len(l21)) ]) 
lstd2 = np.array([ np.std(np.array([l21[i,1],l22[i,1],l23[i,1]])) for i in range(len(l21)) ])

plt.errorbar(l11[:,0], lmean1, yerr=lstd1, c='g', ls='-', elinewidth=1, capsize = 5, barsabove=True, lw=3, label='WEM 7 Milestones')
plt.errorbar(l21[:,0], lmean2, yerr=lstd2, c='b', ls='-', elinewidth=1, capsize = 5, barsabove=True, lw=3, label='WEM 9 Milestones')
plt.plot(l2[:,0], l2[:,1], 'r-', lw=3, label='Regular LD')
plt.xlim(-2.2,2.2)
plt.ylim(0.0,4.5)
plt.xlabel('x',fontsize=18)
plt.ylabel('Free Energy (kcal/mol)',fontsize=18)
plt.legend(fontsize=17)
#plt.title('Barrier = 2.0 $k_BT$',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.tight_layout()
#plt.show()
plt.savefig('11d-free-energy.pdf')
