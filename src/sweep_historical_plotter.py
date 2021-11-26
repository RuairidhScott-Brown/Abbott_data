import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate

with open("C:/Users/18rsc/Documents/imperial/year_3/abbott_data/data/sweep_historical.txt", 'r') as file:
    lines = file.readlines()


x = []
y = []
y_lower = []
y_upper = []

for line in lines:
    elements = line.split(',')

    x.append(float(elements[0]))
    y.append(float(elements[1]))
    y_upper.append(float(elements[1])+5)
    y_lower.append(float(elements[1])-5)



Sweep_angel = scipy.interpolate.interp1d(x, y)



fig, axes = plt.subplots(1,1)
axes.plot(x, y, label = "Historical Trend")
axes.scatter(0.75, 33, color='red', label = "Chosen angle = 33")
axes.axvline(x=0.75, color='black', linestyle='--', label = "Chosen M = 0.75")
axes.fill_between(x, y_upper, y_lower,facecolor='#2ca02c', alpha=0.5, label = "Error")
axes.set_xlabel(r'$M$', fontsize=20)
axes.set_ylabel(r'$\Lambda$', fontsize=20)
plt.legend(loc=4)
plt.show()