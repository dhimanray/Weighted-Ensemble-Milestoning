import numpy as np

l = np.loadtxt('distance-data.dat')

#for i in range(len(l)):
#    if l[i,2] <= -150.0:
#        l[i,2] += 360.0

a = 1   #state 1 and state 2
tt = [] #transition times

for i in range(10,len(l)):
    if l[i,1] >= 7.0: 
        anew = 2
        #print l[i,2], anew
        if anew!=a:
            a = anew
            #print 'change'
            #print l[i,2], a
            tt.append( np.array([l[i,0]*0.01, a, l[i,1]]) )
    if l[i,1] <= 3.6 : 
        anew = 1
        #print l[i,2], anew
        if anew!=a:
            a = anew
            #print 'change'
            #print l[i,2], a
            tt.append( np.array([l[i,0]*0.01, a, l[i,1]]) )

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
    print fpt1to2[i], fpt2to1[i]


mean1 = np.mean( fpt1to2 )
mean2 = np.mean( fpt2to1 )

std1 = np.std( fpt1to2 )
std2 = np.std( fpt2to1 )

print "#Transition 1 to 2: MFPT =", mean1, "+/-", 1.96*std1/np.sqrt(len(fpt1to2)), "N = ", len(fpt1to2)

print "#Transition 2 to 1: MFPT =", mean2, "+/-", 1.96*std2/np.sqrt(len(fpt2to1)), "N = ", len(fpt2to1)

