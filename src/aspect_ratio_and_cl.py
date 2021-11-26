import matplotlib.pyplot as plt
import numpy as np


CL_0 = 0.1
AR = 8
AoA = np.linspace(-5,15, 100)
CL = CL_0 / (1 + CL_0/(np.pi * AR))

fig, axes = plt.subplots(1,1)
axes.plot(AoA, CL)
plt.show()