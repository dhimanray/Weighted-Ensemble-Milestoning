import numpy as np
import numpy as np

mps = [2.45, 2.7, 3.6, 4.6, 5.6, 7.0, 9.0, 11.0, 13.0]
N = len(mps)

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
K[N-1,N-2] = 1.0    #reflecting boundary condition (Graziloli and Andricioaei, JCP, 149, 084103 (2018) Page 4)

#define function to calculate Log likelihood of any matrix K given Nhit and t
def Like(K,Nhit,t,N):
    L = 1.0
    for i in range(N-1):
        try:
            N_alpha = Nhit[i,i-1] + Nhit[i,i+1]
        except:
            N_alpha = Nhit[i,i+1]

        L *= (K[i,i+1]**Nhit[i,i+1])*np.exp(-K[i,i+1]*N_alpha*t[i])

        if i!=0:
            L *= (K[i,i-1]**Nhit[i,i-1])*np.exp(-K[i,i-1]*N_alpha*t[i])
    return L

#define function to calculate free energy profile from a given matrix
def G(Q,t,N):
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
    p_x = np.multiply(q_stat,t)    #choose the eigenvector corresponding to eigenvalue 1 (the first eigenvector in the sorted matrix)
    p_x = p_x/sum(p_x)

    G = np.zeros(len(p_x))
    G += 2.0*np.log(np.asarray(mps))
    for i in range(len(G)):
        G[i] -= np.log(p_x[i])
    G -= np.min(G)


    return G



#list to store free energy values
G_list = []


#files to write data
f1 = open('free-energy-error-analysis.dat','w')
print >>f1, '#r #free-energy #uncertainty'

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
        F = G(Q,t,N)

    if (k+1)%500 == 0:
        G_list.append(F)
        counter += 1

a = np.asarray(G_list)
#print G_list        
for i in range(len(F)-1):
     print >>f1, mps[i], np.mean(a[:,i]), 1.96*np.sqrt(np.std(a[:,i])**2/counter)
f1.close()



