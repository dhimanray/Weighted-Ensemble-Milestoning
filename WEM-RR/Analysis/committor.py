import numpy as np
import numpy as np

#mps = [6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0]
mps1 = [ 6.0 + 2.0*i for i in range(12)]
mps0 = [ 5.0 ]
mps = mps0 + mps1

N = len(mps)
#N = 7

#---------- construct K^(c) matrix (Elber et. al. Entropy (2016))----------------------------------------
K = np.zeros((N,N))

t = np.zeros(N)

Nhit = np.zeros((N,N))

for i in range(N-1):
    l = np.loadtxt('milestone_%dA/milestone-data.dat'%(mps[i]))
    K[i,i+1] = l[3]
    Nhit[i,i+1] = l[5]
    if i!=0:
        K[i,i-1] = l[4]
        Nhit[i,i-1] = l[6]
    t[i] = l[2]
#make all elements of the first two rows to zero
#we discard the first milestone as second milestone is bound state
for i in range(N):
    K[0,i] = 0.0
    K[1,i] = 0.0
#boundary condition: trajectories get stuck at last milesone
K[N-1,N-1] = 1.0

#--------------- Multiply K repeatedly to get the committor -----#
#tolerence
tol = 1E-3

f1 = open('committor.dat','w')

K_new = K
C = K[:,N-1]
for i in range(1000):
    K_new = np.dot(K_new,K)
    C_new = K_new[:,N-1] #commitor is the last column of K_new
    if np.linalg.norm(C_new - C) < tol:
        C = C_new
        print 'converged at iteration: ',i
        break
    else :
        C = C_new
    #print C

for i in range(len(C)):
    print >>f1, mps[i], C[i]
f1.close()
