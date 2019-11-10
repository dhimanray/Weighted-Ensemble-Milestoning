#THIS CODE CALCULATES THE EQULIBRIUM PROBABILITY 
#DISTRIBUTION FROM MILESTONE FLUX
#--------------------------------------------------

import numpy as np
#number of milestones (including end points) #for all the space, don't stop at transition endpoint
N = 8

#position of milestones
mile = [ -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0 ]

#---------- construct K matrix ----------------------------------------
K = np.zeros((N,N)) 

t = np.zeros(N)

for i in range(N-1):
    l = np.loadtxt('milestone_%d/milestone-data.dat'%i)
    K[i,i+1] = l[3]
    if i!=0:
        K[i,i-1] = l[4]
    t[i] = l[2]
K[N-1,N-2] = 1.0    #reflecting boundary condition (Graziloli and Andricioaei, JCP, 149, 084103 (2018) Page 4)
#print K

#---------normalize K----------------------------------------------
for i in range(N):
    totp = sum(K[i,:])
    print totp
    for j in range(N):
        K[i,j] = K[i,j]/totp

print 'Normalized Rate Matrix'
print K

#---------------- get eigenvalues of K -----------------------------------

w,v = np.linalg.eig(K)

print 'Eigenvalues of Rate Matrix K: ', w

#_____________________________________________________________________________#
# [--q---]^t*[  K matrix ] = [---q --]^t
# is solved by finding eigenvectors of K matrix
# satisfying [ K ][--q--] = [--q--]
# then inverting the eigenvector matrix and finding the 
# row corresponding to eigenvealue 1
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


q_matrix =  np.linalg.inv(v)
p_x = np.multiply(q_matrix[5],t)    #choose the eigenvector corresponding to eigenvalue 1 (the index of milestone where things start x = -1)
p_x = p_x/sum(p_x)
print 'Probability values: ', p_x

#------------------------------------------------------------------------------#
f1 = open('stationary-distribution.dat','w')
print >>f1, '### Equilibrium probability distribution along reaction coordinate ###'
for i in range(N-1):
    print >>f1, mile[i], p_x[i]
f1.close()

