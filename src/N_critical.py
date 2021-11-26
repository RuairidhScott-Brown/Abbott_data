import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate

with open("C:/Users/18rsc/Documents/imperial/year_3/abbott_data/data/N_critical_fixed_NACA_663_218.txt", 'r') as file:
    lines = file.readlines()


x = []
y = []

for line in lines:
    elements = line.split(',')
    x.append(float(elements[0]))
    y.append(float(elements[1]))

Ncrit = scipy.interpolate.interp1d(x, y)



fig, axes = plt.subplots(1,1)
axes.plot(x, y)
wing_Ncrit = Ncrit(0.28)
angel_sweep = np.rad2deg(np.arccos(wing_Ncrit/0.78))
print(Ncrit(0.28))
print(angel_sweep)
plt.show()
