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
np.set_printoptions(threshold=np.inf)
import w_ipa
w = w_ipa.WIPI()
# At startup, it will load or run the analysis schemes specified in the configuration file (typically west.cfg)
w.main()
w.interface = 'matplotlib'


# In[2]:


total_iteration = 600

it = [0.0 for i in range(total_iteration)]

flux = 0.0
flux_array = []
sink = 11.0

lifetime = 0.0
force_eval = 0.0

count_forward = 0
count_backward = 0
for i in range(total_iteration):
    w.iteration = i+1
    l = w.current.pcoord
    wts = w.current.weights
    tau = 11
    force_eval += (tau-1)*w.current.walkers*0.01
    print 'total simulation time = ', force_eval, 'ps'
    for j in range(len(l)):
        #print j
            
        if l[j][0] > sink and l[j][tau-1] <= sink:
            it[i] += wts[j]
            #print wts[j]
            count_backward += 1
            for k in range(tau):
                #print k
                if l[j][k] > sink and l[j][k+1] <= sink:
                    flux += wts[j]
                    lifetime += wts[j]*(i*(tau-1)+k)
                    break
            #break
    print flux
    flux_array.append(flux)
flux = flux/(total_iteration*(tau-1))
print "MFPT = ", 1./flux     
print "lifetime = ", lifetime/sum(it)
print sum(it)
print sum(it)/flux

f1 = open('milestone-data.dat','w')
print >>f1, "#MFPT  #MFPT_back  #lifetime  #forward probability  #backward probability #forward count #backward count"
print >>f1, 1./flux, 0.0, lifetime, sum(it), 0.0, count_forward, count_backward
f1.close()


# In[3]:


print it
f1 = open('FPTD.dat','w')

for i in range(len(it)):
    print >>f1, i*(tau-1), it[i]
    
f1.close()


# In[4]:


plt.plot(it)


# In[6]:


plt.plot(flux_array)
f1 = open('flux.dat','w')
print >>f1, '#time #flux'

for i in range(len(it)):
    print >>f1, i*(tau-1), flux_array[i]
    
f1.close()


# In[ ]:




