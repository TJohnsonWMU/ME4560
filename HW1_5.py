import numpy as np 
from matplotlib import pyplot as plt 

D = 1100 #Peak y-val (N)
y_a = 1100 #y-asymptote (N)
C = 2 - (2/np.pi)*np.arcsin(y_a/D) #Shape factor
rise = 900 #Force N
run = 0.2 #Slip Ratio
y_0 = 900/0.2 #Slope at 0
B = y_0/(C*D) #Stiffness Factor
x_m = 1.3 #X-val at ymax
E = ((B*x_m)-np.tan(np.pi/(2*C)))/((B*x_m)-np.arctan(B*x_m))
x=np.arange(0.1,7,0.1)
F = D*np.sin(C*np.arctan(B*x-E*(B*x-np.arctan(B*x))))
print(C,B,E)
