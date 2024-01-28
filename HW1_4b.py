import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0,46)

print(x)

Y = 10*np.cos(x*2*np.pi/360) + 20*np.cos(5*2*np.pi/360)
plt.title("Lateral force vs Wheel angle")
plt.grid()
plt.xlabel("Wheel Angle [deg]")
plt.ylabel("Lateral Force [N]")
plt.xticks([0,5,10,15,20,25,30,35,40,45])
plt.plot(x,Y)
plt.show()