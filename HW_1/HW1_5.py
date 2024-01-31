import numpy as np 
from matplotlib import pyplot as plt 
#Values to be changed
D = 1000 #Peak y-val [N]
y_a = 950 #y-asymptote [N]
rise = 900 #Force [N]
run = 0.2 #Slip Ratio
x_m = 1.3 #X-val at ymax
y_0 = rise/run #Slope at 0
v_r = 15 #rolling velocity [mph]
u = 10 #longitudinal velocity [mph]
v = 0 #lateral velocity[mph]


#Calcualted Values
Sigma_x = (u-v_r)/v_r #longitudinal slip ratio
Sigma_y = (v/v_r) #lateral slip ratio
alpha = np.arctan(v/v_r) #wheel slip angle

if Sigma_x > 0:
    braking = True
else:
    braking = False
if Sigma_y > 0:
    right = True
else:
    right = False

C = 2 - (2/np.pi)*np.arcsin(y_a/D) #Shape factor
B = y_0/(C*D) #Stiffness Factor
Bx = B*x_m
E1 = Bx-np.tan(np.pi/(2*C))
E2 = (Bx)-np.arctan(Bx)
E=E1/E2
x=np.arange(-1,1,0.01)
F = D*np.sin(C*np.arctan(B*x-E*(B*x-np.arctan(B*x))))

def G(arg1):
    print("Wheel Longitudinal Force:", D*np.sin(C*np.arctan(B*arg1-E*(B*arg1-np.arctan(B*arg1)))))

plt.title("Traction Force vs Slip Ratio")
plt.grid()
plt.xlabel("Slip Ratio")
plt.ylabel("Traction Force [N]")

plt.plot(x,F)
plt.show()

print("Wheel slip angle:",Sigma_x)
G(Sigma_x)

if braking == 1:
    print("Braking")
if braking == 0:
    print("Accelerating")
if right == 1:
    print("Turning Right")
if right == 0:
    print("Turning Left")
