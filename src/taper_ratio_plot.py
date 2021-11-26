import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate

with open("C:/Users/18rsc/Documents/imperial/year_3/abbott_data/data/taper_ratio_untwisted.txt", 'r') as file:
    lines_untwisted = file.readlines()

with open("C:/Users/18rsc/Documents/imperial/year_3/abbott_data/data/taper_ratio_twisted.txt", 'r') as file:
    lines_twisted = file.readlines()



S = 22.2
b = 12.9

x_untwisted = []
y_untwisted = []

for line in lines_untwisted:
    elements = line.split(',')

    x_untwisted.append(float(elements[0]))
    y_untwisted.append(float(elements[1]))

taper_ratio_untwisted = scipy.interpolate.interp1d(x_untwisted, y_untwisted)

x_twisted = []
y_twisted = []

x_twisted_upper = []
x_twisted_lower = []
y_twisted_upper = []
y_twisted_lower = []

for line in lines_twisted:
    elements = line.split(',')

    x_twisted.append(float(elements[0]))
    x_twisted_upper.append(float(elements[0]) + 5)
    x_twisted_lower.append(float(elements[0]) - 5)

    y_twisted.append(float(elements[1]))

taper_ratio_twisted = scipy.interpolate.interp1d(x_twisted, y_twisted)


fig, axes = plt.subplots(1,1)
axes.plot(x_untwisted, y_untwisted)
axes.plot(x_twisted, y_twisted)

taper_ratio = taper_ratio_twisted(29)
print(taper_ratio_twisted(29))

C_root = 2 * ( (S) / (b*(1 + taper_ratio)) )
C_tip = taper_ratio * C_root
print(C_root)
print(C_tip)
plt.show()