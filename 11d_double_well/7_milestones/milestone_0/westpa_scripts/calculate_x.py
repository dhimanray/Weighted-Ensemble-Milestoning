import numpy as np

endpoint = -1.0
#endpoint2 = -0.5

l = np.loadtxt('parent.dat')

x_start = l[len(l)-1,0]
Nd = len(l[0]) - 1  #Number of y dimentions
y_start = np.zeros(Nd)
for k in range(Nd):
    y_start[k] = l[len(l)-1,(k+1)]

N = 20

print("{:.2f}".format(x_start))

l = []

#THIS CODE GENERATES OVERDAMPED LANGEVIN TRAJECTORIES FOR WEIGHTED ENSEMBLE PATH SAMPLING
import numpy as np

#define the double well potential function
#y is an array which has many harmonic oscillators coupled with reaction coordinate
def V(x,y):
    Vx = 1.0*(1.0-x**2)**2
    Vy = 0.0
    for i in range(len(y)):
        Vy += -0.5*(x**2)*y[i]**2 + y[i]**4
    return Vx + Vy

#define the first derivative of potential
def dVdx(x,y):
    dVx = -4.0*x*(1.0-x**2)
    dVy = 0.0
    for i in range(len(y)):
        dVy += -x*y[i]**2 
    return dVx + dVy
def dVdy(x,y,i):
    return -(x**2)*y[i] + 4.0*y[i]**3

#define parameters for trajectory
#Nd = 10 #Number of y dimentions
t_start = 0.0
#x_start = -1.0
#y_start = 0.5
x_end = 1.0
dt = 1.0
m = 1.0
gamma = 2000.0
beta = 1.0  #beta = 1/kT
#M = 10000    #number of trajectories
#N = 10000    #number of steps

#=============== VARIANCE =================#
#variance of the gaussian noise is given by 
# (2*k*T*dt)/(m*gamma)


variance = 2*dt/(m*gamma*beta)

#standard deviation
sigma = variance**0.5


#=============== PROPAGATION ==============#
# x(j+1) = x(j) - (kT*dt/(m*gamma))*(dV/dx) + xrand

f1 = open('trajectory.dat','w')
print >>f1, '#time    #x    #y'

#initiate the y array
y = np.zeros(Nd)

x = x_start
for i in range(len(y)):
    y[i] = y_start[i]
for i in range(N):
    if x < endpoint:
        xrand = np.random.normal(0,sigma,None)
        xnew = x - (dt/(m*gamma))*dVdx(x,y) + xrand
        #print >>f1, ("{:.2f}".format(xnew)),
        for k in range(len(y)):
    	    yrand = np.random.normal(0,sigma,None)
    	    ynew = y[k] - (dt/(m*gamma))*dVdy(x,y,k) + yrand
    	    y[k] = ynew.copy()
            #print >>f1, ("{:.2f}".format(y[k])),
        #print >>f1, '' 
        x = xnew.copy()
    #print >>f1, i+1, x, y[0]
    print >>f1, ("{:.2f}".format(x)),
    for k in range(len(y)):
        print >>f1, ("{:.2f}".format(y[k])),
    print >>f1, ''
    print("{:.2f}".format(x))    

f1.close()

