#!/usr/bin/env python
# coding: utf-8

# **Jupyter: w_ipa**
# 
# This is an example jupyter/ipython notebook for WESTPA simulations, designed for interactive analysis using w_ipa.  Use this as a template for further browser-based interactive analysis of simulations.
# 
# You'll want to start each notebook session with the following:
# 
# ```
#     import w_ipython
#     w = w_ipython.WIPI()
#     w.main()
# ```
# 
# The w object can then be used for analysis.  Schemes can be listed and changed with
# 
# ```
#     w.list_schemes
#     w.scheme = SCHEME_NUMBER/NAME
# ```
# 
# Run help(w), or w.introduction for more details.
# 
# Happy analyzing!

# In[1]:


#get_ipython().magic(u'matplotlib inline')
from matplotlib import pyplot as plt
import numpy as np
import w_ipa
w = w_ipa.WIPI()
# At startup, it will load or run the analysis schemes specified in the configuration file (typically west.cfg)
w.main()
w.interface = 'matplotlib'


# In[2]:


#========================================================
#CALCULATING MILESTONE LIFETIME
#========================================================
total_iteration = 500

it = [0.0 for i in range(total_iteration)]

flux = 0.0
flux_array = []
sink1 = 4.6

it_back = [0.0 for i in range(total_iteration)]
flux_back = 0.0
flux_back_array = []
sink2 = 2.6

lifetime = 0.0
force_eval = 0.0

count_forward = 0
count_backward = 0
for i in range(total_iteration):
    w.iteration = i+1
    l = w.current.pcoord
    wts = w.current.weights
    tau = 11
    #print sum(wts)
    force_eval += (tau-1)*w.current.walkers*0.01
    print 'total simulation time = ', force_eval, 'ps'
    for j in range(len(l)):
        #print j
            
        if l[j][0] < sink1 and l[j][tau-1] >= sink1:
            it[i] += wts[j]
            #print wts[j], 'forwd'
            count_forward += 1
            for k in range(tau):
                if l[j][k] < sink1 and l[j][k+1] >= sink1:
                    flux += wts[j]
                    lifetime += wts[j]*(i*(tau-1)+k)
                    break
            #break
                    
        if l[j][0] > sink2 and l[j][tau-1] <= sink2:
            #print l[j,0], l[j,tau-1]
            it_back[i] += wts[j]
            #print wts[j], 'backwd'
            count_backward += 1
            for k in range(tau):
                #print 'elmnts',l[j,k]
                if l[j][k][0] > sink2 and l[j][k+1][0] <= sink2:
                    flux_back += wts[j]
                    #print flux_back, 'fback'
                    lifetime += wts[j]*(i*(tau-1)+k)
                    break
            #break
    flux_array.append(flux)
    flux_back_array.append(flux_back)
flux = flux/(total_iteration*(tau-1))

print "MFPT = ", 1./flux     
print "MFPT_back = ", 1./flux_back
print "lifetime = ", lifetime
print "forward probability = ", sum(it)
print "backward probability = ", sum(it_back)

f1 = open('milestone-data.dat','w')
print >>f1, "#MFPT  #MFPT_back  #lifetime  #forward probability  #backward probability #forward count #backward count"
print >>f1, 1./flux, 1./flux_back, lifetime, sum(it), sum(it_back), count_forward, count_backward
f1.close()


# In[3]:


#Forward and backward first passage time distributions
plt.plot(it)
plt.plot(it_back)


# In[4]:


#check for convergence
plt.plot(flux_array)
plt.plot(flux_back_array)
f1 = open('flux.dat','w')
print >>f1, '#time #flux_forward #flux_backward'

for i in range(len(it)):
    print >>f1, i*(tau-1), flux_array[i], flux_back_array[i]
    
f1.close()


# In[5]:


print it
f1 = open('FPTD_forward.dat','w')

for i in range(len(it)):
    print >>f1, i*(tau-1), it[i]
    
f1.close()


f2 = open('FPTD_back.dat','w')

for i in range(len(it)):
    print >>f2, i*(tau-1), it_back[i]
    
f2.close()


# In[ ]:




