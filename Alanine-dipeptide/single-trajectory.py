#THIS CODE GENERATES LONG TRAJECTORIES FOR CALCULATING C(t) TIME CORRELATION FUNCTION FROM MILESTONING DATA 
# --------- Dhiman Ray (Ioan Andricioaei group), UC Irvine ---------

import numpy as np


#------------------------------------------------------------------
#So if we give our data sample that has a specific distribution, 
#the inverse_transform_sampling function will return a dataset with 
#exactly the same distribution. Here the advantage is that we can 
#get our own sample size by specifying it in the n_samples variable
#------------------------------------------------------------------
#import scipy.interpolate as interpolate

#def inverse_transform_sampling(data, n_samples):
#    hist = np.array([data[i,1] for i in range(len(data)-1)])
#    bin_edges = data[:,0]
#    cum_values = np.zeros(bin_edges.shape)
#    cum_values[1:] = np.cumsum(hist*np.diff(bin_edges))
#    inv_cdf = interpolate.interp1d(cum_values, bin_edges)
#    r = np.random.rand(n_samples)
#    return inv_cdf(r)
#------------------------------------------------------------------
def random_from_dist(data, n_samples):
    indices = data[:,0]
#    print indices
    values = data[:,1]
#    print values
    weights=values/np.sum(values)
#    print weights
    new_random=np.random.choice(indices,n_samples,p=weights)
#    print new_random
    return new_random
#parameters ----------------------------------
N = 8 #Number of milestones

Nstep = 500000 #Number of steps each milestone is visited in a long trajectory

start = 2 #Start from second milestone

ms = [ -100.0, -60.0, -20.0, 20.0, 60.0, 100.0, 150.0, 180.0 ] #milestone positions

#--------- Transition probability between milestones -------------------

Tp = []     #Transition probability between milestones

for i in range(N):
    l = np.loadtxt('milestone_%d/milestone-data.dat'%i)
    Tp.append([l[3]/(l[3]+l[4]),l[4]/(l[3]+l[4])])   #normalized Forward probability and backward probability for each milestone

#print Tp

#--------- First passage times ------------------------------------------

FPT = []
for i in range(N):
    #print i
    if i==0:
        l = np.loadtxt('milestone_%d/FPTD.dat'%i)

        a = random_from_dist(l, Nstep)
        b = [0.0 for j in range(Nstep)]

    elif i==(N-1):
        l = np.loadtxt('milestone_%d/FPTD.dat'%i)
        
        a = [0.0 for j in range(Nstep)]
	b = random_from_dist(l, Nstep)
    else :
        l = np.loadtxt('milestone_%d/FPTD_forward.dat'%i)
        a = random_from_dist(l, Nstep)
        l1 = np.loadtxt('milestone_%d/FPTD_back.dat'%i)
        b = random_from_dist(l1, Nstep)


    FPT.append([a,b])

#---------- Generate Long Trajectory --------------------------------------

f1 = open('single-trajectory.dat','w')
t = 0.0     #Time start
m = start - 1 #milestone

print >>f1, "# Time   Position  "

print >>f1, t, ms[m]

for j in range(Nstep):
    #generate random number to check whether to transit forward or backward
    r = np.random.random()
    #print m
    if r < Tp[m][0]:    #step forward
        #choose transition time from FPT
        dt = FPT[m][0][j]
        #transit forward
        m += 1
    else :  #step backward
        #choose transition time from FPT
        dt = FPT[m][1][j]
        #transit forward
        m -= 1
    t += dt
    
    print >>f1, t, ms[m]

f1.close()
#print a
