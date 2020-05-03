import numpy as np
#number of milestones (including end points)
N = 7

#starting milestone
Ns = 2

K = np.zeros((N,N))

Nhit = np.zeros((N,N))

t = np.zeros(N)


for i in range(N-1):
    l = np.loadtxt('../milestone_%d/milestone-data.dat'%i)
    K[i,i+1] = l[3]
    Nhit[i,i+1] = l[5]
    if i!=0:
        K[i,i-1] = l[4]
        Nhit[i,i-1] = l[6]
    t[i] = l[2]

#print K

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

#define function to calculate mean first passage time from a given Q matrix
def MFPT(Q,t,N):
    #make sue diagonal elements are zero
    K = Q.copy()
    #multiply the t[i]'s to get back the actual K
    for i in range(N):
        for j in range(N):
            K[i,j] *= t[i]
    #normalize K
    for i in range(len(K)):
        K[i,i] = 0.0
        totp = np.sum(K[i,:])
        #print totp
        if totp!=0:
            for j in range(N):
                K[i,j] = K[i,j]/totp

    #calculate first passage time from ti and K
    I = np.identity(N)
    inverse = np.linalg.inv(np.subtract(I,K))
    p = np.zeros(N)
    p[Ns-1] = 1.0
    mfpt = np.dot(p,np.dot(inverse,t))
    return mfpt

#calculate Likelihood of the original transition matrix
#L_K = Like(K,Nhit,t,N)
#print np.log(L_K)

#list to store MFPT values
mfpt_list = []

#Perform nonreversible element shift Monte Carlo to sample rate matrices
N_total = 500 #Number of trials
N_acc = 0
print '#k #mean #standard deviation'

for k in range(N_total):
    Q = K.copy()
    #construct Q matrix
    #Q = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            if t[i] != 0:
                Q[i,j] = Q[i,j]/t[i]
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
        
    #Q_ab = Q[r1,r1+r2]
    #for i in range(N-1):
    #generate random number from exponential distribution within [-q_ij,inf) with mean zero
        #if i!=0:
        #    Q_ab = min([K[i,i-1],K[i,i+1]])
        #else :
        #    Q_ab = K[i,i+1]

    delta = np.random.exponential(scale=Q_ab) - Q_ab

    #pacc = ((Q_ab + delta)/Q_ab)**Nhit[r1,r1+1] * np.exp(-Q_ab*t[r1]*np.sum(Nhit[r1]))

    log_pacc = Nhit[r1,r1+1]*np.log((Q_ab + delta)/Q_ab) - delta * t[r1]*np.sum(Nhit[r1])
    #print log_pacc

    r = np.random.uniform(low=0.0,high=1.0)

    if np.log(r) < log_pacc :  #accept
        Q[r1,r1] -= delta
            #Q[r1,r1+r2] += delta
        if r1 == 0:
            Q[r1,r1+1] += delta
        else :
            if r2 == 0 :
                Q[r1,r1-1] += delta
            else :
                Q[r1,r1+1] += delta

    #accept or reject this matrix according to acceptance criteria
    #L_Q = Like(Q,Nhit,t,N)
    #r = np.random.uniform(low=0.0,high=1.0)
    #if L_Q/L_K <= r : 
        #now use this matrix to calculate mean first passage time
        mfpt = MFPT(Q,t,N)
    
        #print 'delta = ', delta, 'r1 = ', r1, 'MFPT = ', mfpt/50.0, 'ps'

        mfpt_list.append(mfpt/50.0)

        N_acc += 1
        
        
    if (k+1)%5 == 0 and k/5 != 0:
        a = np.asarray(mfpt_list)
        print k, np.mean(a), np.std(a)
        
print "#N_acc = ", N_acc 



