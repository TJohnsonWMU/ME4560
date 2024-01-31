import numpy as np
from matplotlib import pyplot as plt

ftp = np.loadtxt('ftpcol.txt', dtype = int)
time_s = ftp[:,0]
speed_mph = ftp[:,1]

plt.plot(time_s, speed_mph)
plt.xlabel("Time [s]")
plt.ylabel("Speed [mph]")
plt.show

speed_mps = speed_mph*0.44704
accel_mpsps = np.diff(speed_mps, prepend = 0)

plt.plot(time_s,accel_mpsps)
plt.xlabel("Time [s]")
plt.ylabel("Acceleration [m/s^2]")
plt.show()

distance_m = np.cumsum(speed_mps)
plt.plot(distance_m, speed_mps)
plt.xlabel("Distance [m]")
plt.ylabel("Velocity [m/s]")
plt.show
