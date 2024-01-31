import numpy as np
from matplotlib import pyplot as plt

hwfet = np.loadtxt('hwycol.txt', dtype = float)

time_s = hwfet[:,0]
velocity_mps = hwfet[:,1]*0.44704

acceleration_mpsps = np.diff(velocity_mps, prepend = 0)

C_D = 0.24   #Drag coeff.
rho = 1.0045 #Air density [kg/m^3]
A = 2.34     #Frontal Area [m^2]
theta = 0    #Angle of road [deg]
C_rr = 0.008 #Coeff. of rolling res.
m = 2268     #Mass [kg]
g = 9.81     #Acceleration of gravity [m/s^2]

W = m*g*np.sin(theta*(np.pi/180))
F_rr = C_rr*m*g
F_D = 0.5*C_D*rho*A*velocity_mps**2

F_prop = m*acceleration_mpsps - F_D - F_rr

plt.plot(time_s, F_prop)
plt.xlabel("Time [s]")
plt.ylabel("Propulsion Force [N]")
plt.title('2012 Tesla Model S - EPA Highway Drive Cycle')
plt.grid()
plt.show()
