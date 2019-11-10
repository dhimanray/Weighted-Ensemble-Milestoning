#THIS CODE CALCULATES TIME CORRELATION FUNCTION FROM LONG TRAJECTORY
#USING EQUATION (14) OF J. Chem. Phys 149, 084104 (2018)
#------------------------------------------------------------------- 

import numpy as np
import scipy.interpolate as intp

#l = np.loadtxt('long-trajectory.dat')
l = np.loadtxt('single-trajectory.dat')
#find out where the second t=0 is, that is the size of each trajectory
#for i in range(1,len(l)/100):
#    if l[i,0] == 0:
#        Nstep = i
#        break
Nstep = len(l)
M = len(l)/Nstep    #Number of trajectories

#grid for interpolation
t = np.linspace(0,l[Nstep-1,0],num=(l[Nstep-1,0]))

x = intp.griddata(l[:,0], l[:,1], t, method='linear')

#for i in range(len(t)):
#print t[i], x[i]

def autocorr(x, t):
    return np.corrcoef(np.array([x[0:len(x)-t:1], x[t:len(x):1]]))

#dt = x[1] - x[0]
#dt = 20.0/1000000 #timestep = 20 fs to ns
dt = 1.0

for t in range(0,100000,200):
    cor = autocorr(x,t)
    print t*dt, cor[0][1]

x = []

