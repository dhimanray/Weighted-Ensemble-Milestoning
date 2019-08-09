import numpy as np

l = np.loadtxt('first_passage_times_unbiased.dat')

max_time = 50000
num_bins = 5000
bin_width = float(max_time)/float(num_bins)

dist = [0.0 for i in range(num_bins)]
for i in range(len(l)):
    index = int(l[i]/bin_width)
    if index < num_bins:
        dist[index] += 1.0
f2 = open('distribution1.dat','w')
for i in range(len(dist)):
    print >>f2, (i)*bin_width, float(dist[i])/sum(dist)
f2.close()

flux = 0.0
for i in range(len(l)):
    flux += 1./l[i]

print len(l)/flux
dist = []


