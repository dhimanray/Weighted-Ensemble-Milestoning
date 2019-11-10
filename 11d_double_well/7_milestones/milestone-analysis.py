#THIS CODE CALCULATES THE MEAN FIRST PASSAGE TIME 
#FROM MILESTONE LIFETIME AND TRANSITION PROBABILITY 
#MATRIX
#--------------------------------------------------

import numpy as np
#number of milestones (including end points)
N = 7

#starting milestone
Ns = 2

K = np.zeros((N,N)) 

t = np.zeros(N)

for i in range(N-1):
    l = np.loadtxt('milestone_%d/milestone-data.dat'%i)
    K[i,i+1] = l[3]
    if i!=0:
        K[i,i-1] = l[4]
    t[i] = l[2]
print '----------- Rate Matrix K before Normalization ---------------------'
print K
#normalize K
for i in range(len(K)):
    totp = sum(K[i,:])
    print totp
    if totp!=0:
        for j in range(N):
            K[i,j] = K[i,j]/totp

print '----------- Rate Matrix K after Normalization ---------------------'
print K
print '----------- Lifetime of the milestones (t) ------------------------------'
print t
#calculate first passage time from ti and K
I = np.identity(N)
inverse = np.linalg.inv(np.subtract(I,K))
print '----------- (I-K)^-1*t ------------------------'
print np.dot(inverse,t)
p = np.zeros(N)
p[Ns-1] = 1.0
mfpt = np.dot(p,np.dot(inverse,t))
print '----------- (I-K)^-1 ------------------------'
print inverse
print '---------- Mean First Passage Time ----------'
print mfpt
print 'MFPT = ', mfpt, 'time steps'
