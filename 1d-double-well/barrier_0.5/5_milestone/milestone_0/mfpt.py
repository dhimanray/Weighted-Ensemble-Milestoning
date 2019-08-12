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

# In[9]:


#get_ipython().magic(u'matplotlib inline')
#from matplotlib import pyplot as plt
import numpy as np
import /home/dhiman/Miniconda2/envs/westpa-2017.10/westpa-2017.10/bin/w_ipa
w = w_ipa.WIPI()
# At startup, it will load or run the analysis schemes specified in the configuration file (typically west.cfg)
w.main()
w.interface = 'matplotlib'


# In[13]:


total_iteration = 200

it = [0.0 for i in range(total_iteration)]

flux = 0.0
flux_array = []
sink = -0.6

lifetime = 0.0
for i in range(total_iteration):
    w.iteration = i+1
    #final_trajectories = w.current.seg_id
    #for k in range(final_trajectories.size):
        #traj_trace = w.trace(final_trajectories[i])
        #trajectory = traj_trace['pcoord']
        #weights_array = traj_trace['weights']
    l = w.current.pcoord
    wts = w.current.weights
    tau = 21
    
    for j in range(len(l)):
        #print j
            
        if l[j][0] < sink and l[j][tau-1] >= sink:
        
            #print l[j][0], l[j][tau-1]
            #print i, wts[j]
            it[i] += wts[j]
            flux += wts[j]/int(i)
            lifetime += wts[j]*i
    flux_array.append(flux)
    #print "done_%d"%(i+1)
        #for j in range(tau*i,tau*(i+1)):
        #if trajectory[i*tau][0] > 1.0:
         #   print trajectory[i*tau][0], i, weights_array[i]
print "MFPT = ", 1./flux     
print "lifetime = ", lifetime/sum(it)
print sum(it)
print sum(it)/flux


# In[5]:


print "MFPT = ", float(tau)/flux


# In[3]:


# There's a built in plotting interface that can be used to plot interesting things!
# Try running this command directly from the terminal in w_ipa.
#print(w.state_labels)
#w.current.direct.rate_evolution.plot(interface='matplotlib')
#print("Rate evolution from state 0 to 1")
#w.current.direct.rate_evolution.plot(1,0,interface='matplotlib')
#print w.current.direct.rate_evolution['expected']
#print w.current.direct.state_pop_evolution.plot(1,0,interface='matplotlib')
#print w.current.direct.successful_trajectories
#print("Rate evolution from state 1 to 0")
#w.current.direct.total_fluxes.plot(1,0,interface='matplotlib')


# In[4]:


#w.iteration = 1000
#final_trajectories = w.current.seg_id
#traj_trace = w.trace(final_trajectories[599])
#print('What data can we access from our trace for segment {}?'.format(final_trajectories[45]))
#print(traj_trace.keys())
# Then plot something interesting about it, like the pcoord or the weight changes over time.
# The resulting plot is per time point, not iteration.
#plt.plot(traj_trace['pcoord'])
#plt.show()
#plt.plot(np.log10(traj_trace['weights']))
#plt.show()
#trajectory = traj_trace['pcoord']
#print trajectory


# In[11]:


#w.iteration = 1
#w.current.bins
#l1 = w.current.pcoord
#print len(l1)
#w.current


# In[6]:


#print it
#f1 = open('FPTD.dat','w')

#for i in range(len(it)):
#    print >>f1, i*tau, it[i]
    
#f1.close()


# In[7]:


#plt.plot(it)


# In[16]:


#w.iteration = 1000
#sum(w.current.weights)


# In[8]:


#plt.plot(flux_array)


# In[ ]:




