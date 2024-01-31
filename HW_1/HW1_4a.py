import numpy as np
from matplotlib import pyplot as plt

v = np.arange(0, 101)
Fp = 0.5*0.24*1.0045*2.34*(v**2) + 0.008*2268*9.81 + 2268*9.81*np.sin(3.43*2*np.pi/360)

plt.title("Longintudinal Propulsion Force vs Velocity")
plt.grid()
plt.xlabel("Velocity [m/s]")
plt.ylabel("Long. Propulsion Force [N]")

plt.plot(v,Fp)
plt.show()

