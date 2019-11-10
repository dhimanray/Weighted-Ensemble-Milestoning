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
#define the first derivative of potential
#def dVdx(x,y):
#    dx = 0.001
#    return (V(x+dx,y) - V(x-dx,y))/(2.0*dx)
#def dVdy(x,y,i):
#    dy = 0.001
 #   y_1 = y
#    y_2 = y
#    y_1[i] = y[i] + dy
#    y_2[i] = y[i] - dy
#    derivative = (V(x,y_1)-V(x,y_2))/(2.0*dy)
#    y_1 = []
#    y_2 = []
#    return derivative

#define parameters for trajectory
Nd = 10 #Number of y dimentions
t_start = 0.0
x_start = -1.0
y_start = 0.5
x_end = 1.0
dt = 1.0
m = 1.0
gamma = 2000.0
beta = 1.0  #beta = 1/kT
#M = 10000    #number of trajectories
N = 10000    #number of steps

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
    y[i] = y_start
for i in range(N):
    xrand = np.random.normal(0,sigma,None)
    xnew = x - (dt/(m*gamma*beta))*dVdx(x,y) + xrand
    for k in range(len(y)):
    	yrand = np.random.normal(0,sigma,None)
    	ynew = y[k] - (dt/(m*gamma*beta))*dVdy(x,y,k) + yrand
    	y[k] = ynew.copy()
    x = xnew.copy()
    print >>f1, i+1, x, y[0]
        

f1.close()

