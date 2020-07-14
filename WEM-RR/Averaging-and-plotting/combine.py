#Averaging of WEM datasets

import numpy as np

N = 3 #number of datasets to be averaged

for i in range(4,30,2):
    t = 0.0
    prob_forward = 0.0
    prob_back = 0.0
    n_tot = 0
    n1 = 0
    n2 = 0
    for j in range(1,N+1):
        if i==4:
            l = np.loadtxt('../trial_%d/dataset/milestone_5A/milestone-data.dat'%j)
        else :
            l = np.loadtxt('../trial_%d/dataset/milestone_%dA/milestone-data.dat'%(j,i))
        lifetime = l[2]
        forward = l[3]
        backward = l[4]
        n_forward = l[5]
        n_backward = l[6]

        t += lifetime*(n_forward + n_backward)
        n_tot += n_forward + n_backward
        prob_forward += forward
        prob_back += backward
        n1 += n_forward
        n2 += n_backward

    t /= n_tot
    prob_forward /= N
    prob_back /= N

    if i==4:
        f1 = open('milestone_5A/milestone-data.dat','w')
    else :
        f1 = open('milestone_%dA/milestone-data.dat'%i,'w')
    print >>f1, "#MFPT  #MFPT_back  #lifetime  #forward probability  #backward probability #forward count #backward count"
    print >>f1, 0.0, 0.0, t, prob_forward, prob_back, n1, n2
    f1.close()

