import numpy as np
import numpy as np

#mps = [6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0, 24.0]
mps1 = [ 6.0 + 2.0*i for i in range(12)]
mps0 = [ 5.0 ]
mps = mps0 + mps1

#reverse the array
mps = mps[::-1]

N = len(mps)

#starting milestone (unbound state) (index starts from 1)
Ns = 7

#target milestone (bound state) (index starts from 1)
Nend = 12 #r = 6.0 A

#---------- construct K matrix ----------------------------------------
K = np.zeros((N,N))

t = np.zeros(N)

Nhit = np.zeros((N,N))

for i in range(N-1):
    l = np.loadtxt('milestone_%dA/milestone-data.dat'%(mps[i]))
    #print mps[i], l
    #use different index of l for the reverse process, (all forward are backward here)
    K[i,i+1] = l[4]
    Nhit[i,i+1] = l[6]
    if i!=0:
        K[i,i-1] = l[3]
        Nhit[i,i-1] = l[5]
    t[i] = l[2]
K[N-1,0] = 1.0    #cyclic or periodic boundary condition to get steady state

#print K


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
#tau_list = []
tau_back_list = []

#f2 = open('mfpt-error-analysis.dat','w')
#print >>f2, '#iteration #MFPT #uncertainty'
f3 = open('back-mfpt-error-analysis.dat','w')
print >>f3, '#iteration #MFPT_back #uncertainty'

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
    #print Q
    for i in range(len(Q)):
        Q[i,i] = -np.sum(Q[i])
    #choose one of the non-zero elements to change
    r1 = np.random.randint(0,N-1)
    if r1 == 0:
        #r2 = np.random.randint(0,1)
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
        tau_back = MFPT(Q,t,N)
        #print F
        #tau = tau.real * 0.2 #convert to ps unit
        tau_back = tau_back.real * 0.2 #convert to ps unit
    
    if (k+1)%500 == 0:
        tau_back_list.append(tau_back)

        counter += 1

        
        #b = np.asarray(tau_list)
	#print >>f2, k+1, np.mean(b), 1.96*np.sqrt(np.std(b)**2/counter)
        c = np.asarray(tau_back_list)
        print >>f3, k+1, np.mean(c), 1.96*np.sqrt(np.std(c)**2/counter)
        
#f2.close()
f3.close()        



