import numpy as np
import numpy as np

mps = [2.45, 2.7, 3.6, 4.6, 5.6, 7.0, 9.0, 11.0, 13.0]
N = len(mps)

#starting milestone (reactant or bound state) (index starts from 1)
Ns = 2


#---------- construct K matrix ----------------------------------------
K = np.zeros((N,N))

t = np.zeros(N)

Nhit = np.zeros((N,N))

for i in range(N-1):
    l = np.loadtxt('milestone_%d/milestone-data.dat'%i)
    K[i,i+1] = l[3]
    Nhit[i,i+1] = l[5]
    if i!=0:
        K[i,i-1] = l[4]
        Nhit[i,i-1] = l[6]
    t[i] = l[2]
K[N-1,0] = 1.0    #cyclic or periodic boundary condition to get steady state


#define function to calculate free energy profile and Mean first passage time from a given matrix
def MFPT(Q,t,N):
    K = Q.copy()
    #multiply the t[i]'s to get back the actual K
    for i in range(N):
        for j in range(N):
            if t[i] != 0:
                K[i,j] *= t[i]

    for i in range(N):
        K[i,i] = 0.0 #make sure diagonal elements are zero
        totp = sum(K[i,:])
        for j in range(N):
            K[i,j] = K[i,j]/totp
    #calculate eigen values
    w,v = np.linalg.eig(K)
    #_____________________________________________________________________________#
    # [--q---]^t*[  K matrix ] = [---q --]^t
    # is solved by finding eigenvectors of K matrix
    # satisfying [ K ][--q--] = [--q--]
    # then inverting the eigenvector matrix and finding the 
    # row corresponding to eigenvealue 1
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

    #sort the eigenvalues and eigenvectors
    idx = w.argsort()[::-1]
    w = w[idx]
    v = v[:,idx]

    q_matrix =  np.linalg.inv(v)
    q_stat = q_matrix[0]

    #iend = 7 #product milestone (index starts from 1)

    tau = np.dot(q_stat[Ns-1:Nend],t[Ns-1:Nend])/q_stat[Nend-1]  

    #-------------------------------------------------------------------------#
    

    #tau_back = np.dot(q_stat[1:iend],t[1:iend])/q_stat[1]  #mfpt of referse process

   # print tau*0.2, tau_back*0.2
    return tau #, tau_back




#list to store mfpt values
tau_list = []
#tau_back_list = []

f2 = open('mfpt-all.dat','w')
print >>f2, '#distance #MFPT #standard_deviation #95%_uncertainty'

#loop over milestones
for Nend in range(Ns+1,N):

    #Perform nonreversible element shift Monte Carlo to sample rate matrices
    N_total = 10000 #Number of trials
    counter = 0
    for k in range(N_total):
        Q = K.copy()
        #construct Q matrix
        for i in range(N):
            for j in range(N):
                if t[i] != 0:
                    Q[i,j] = Q[i,j]/t[i]
        for i in range(len(Q)):
            Q[i,i] = -np.sum(Q[i])
        #choose one of the non-zero elements to change
        r1 = np.random.randint(0,N-1)
        if r1 == 0:
            Q_ab = Q[r1,r1+1]
        else :
            r2 = np.random.randint(0,1)
            if r2 == 0:
                Q_ab = Q[r1,r1-1]
            else :
                Q_ab = Q[r1,r1+1]
        

        delta = np.random.exponential(scale=Q_ab) - Q_ab


        log_pacc = Nhit[r1,r1+1]*np.log((Q_ab + delta)/Q_ab) - delta * t[r1]*np.sum(Nhit[r1])

        r = np.random.uniform(low=0.0,high=1.0)

        if np.log(r) < log_pacc :  #accept
            Q[r1,r1] -= delta
            if r1 == 0:
                Q[r1,r1+1] += delta
            else :
                if r2 == 0 :
                    Q[r1,r1-1] += delta
                else :
                    Q[r1,r1+1] += delta

            #now use this matrix to calculate free energy
            tau = MFPT(Q,t,N)
            tau = tau.real * 0.2 #convert to ps unit
            
        #only include after 500 steps 
        if (k+1)%500 == 0:
            tau_list.append(tau)
            counter += 1

        
    b = np.asarray(tau_list)
    print >>f2, mps[Nend-1], np.mean(b), np.std(b), 1.96*np.sqrt(np.std(b)**2/counter)
        
f2.close()



