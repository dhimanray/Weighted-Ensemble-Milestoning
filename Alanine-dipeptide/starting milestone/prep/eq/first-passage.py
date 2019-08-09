import numpy as np

l = np.loadtxt('A_production.colvars.traj')

#for i in range(len(l)):
#    if l[i,2] <= -150.0:
#        l[i,2] += 360.0

a = 1   #state 1 and state 2
tt = [] #transition times

for i in range(len(l)):
    if l[i,2] >= 140.0 or l[i,2] <= -160.0:
        anew = 2
        #print l[i,2], anew
        if anew!=a:
            a = anew
            #print 'change'
            #print l[i,2], a
            tt.append( np.array([l[i,0]*0.002, a, l[i,2]]) )
    if l[i,2] <= -60.0 and l[i,2] >= -140.0: 
        anew = 1
        #print l[i,2], anew
        if anew!=a:
            a = anew
            #print 'change'
            #print l[i,2], a
            tt.append( np.array([l[i,0]*0.002, a, l[i,2]]) )

#ifor i in range(len(tt)):
#    print tt[i]
fpt1to2 = []
fpt2to1 = []

for i in range(len(tt)-1):
    if tt[i][1] == 1 and tt[i+1][1] == 2:
        fpt1to2.append(tt[i+1][0] - tt[i][0])
    if tt[i][1] == 2 and tt[i+1][1] == 1:
        fpt2to1.append(tt[i+1][0] - tt[i][0])

np.array(( fpt1to2 ))
np.array(( fpt2to1 ))
for i in range(len(fpt1to2)):
    print fpt1to2[i]

mean1 = np.mean( fpt1to2 )
mean2 = np.mean( fpt2to1 )

std1 = np.std( fpt1to2 )
std2 = np.std( fpt2to1 )

print "Transition 1 to 2: MFPT =", mean1, "+/-", std1

print "Transition 2 to 1: MFPT =", mean2, "+/-", std2
