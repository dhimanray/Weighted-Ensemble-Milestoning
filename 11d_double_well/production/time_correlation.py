#THIS CODE CALCULATES TIME CORRELATION FUNCTION

import numpy as np

def autocorr(x, t):
    return np.corrcoef(np.array([x[0:len(x)-t:1], x[t:len(x):1]]))

l = np.loadtxt('trajectory.dat')

dt = l[1][0] - l[0][0]

dt = 1 #unit in ns

x = l[100:,1]

f1 = open('time-correlation.dat','w')

for t in range(0,100000,200):
    cor = autocorr(x,t)
    print >>f1, t*dt, cor[0][1]
l = []
x = []

f1.close() 


