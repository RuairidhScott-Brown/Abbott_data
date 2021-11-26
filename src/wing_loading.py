import matplotlib.pyplot as plt
import numpy as np




u = 0
v = 0
a = 1
b = 1.3

t = np.linspace(0,np.pi/2, 100)


S = 22.2
b = 12.9
taper_ratio = 0.22862345023025152

C_root = 2 * ( (S) / (b*(1 + taper_ratio)) )
C_tip = taper_ratio * C_root

quater_chord_root = 0.25*C_root
quater_chord_tip = 0.25*C_tip

length_1 = np.tan(np.deg2rad(29))*b
point_1 = length_1 - quater_chord_tip + quater_chord_root
angle_1 = np.rad2deg(np.arctan(point_1/b))
print(angle_1)

point_2 = length_1 + 0.75*C_tip + quater_chord_root

angle_2 = np.rad2deg(np.arctan((point_2 - C_root)/b))
print(angle_2)


x_c = np.linspace(0, -b, 100)


grad_1 = np.tan(np.deg2rad(angle_1))
y_1 = grad_1 * x_c

grad_2 = np.tan(np.deg2rad(angle_2))
y_2 = grad_2 * x_c - C_rootdryh


y = - (y_2 - y_1)
print(y)


L = (0.5*0.302748958*230.022**2 * 0.3) * y
avg = np.average(L)
L_fixed = L / avg

x_fixed = -(x_c)/b
fig, axes = plt.subplots(1,1)
axes.plot(u + a*np.cos(t), v + 1.3*np.sin(t)) 
axes.plot(x_fixed, L_fixed)
plt.show()