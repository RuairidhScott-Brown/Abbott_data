import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate



ka = 0.87
t_c = 0.12
CL = 0.3

sweep = np.linspace(0,50, 100)
MDD = ka / np.cos(np.deg2rad(sweep)) - t_c / (np.cos(np.deg2rad(sweep)))**2 - CL / (10*np.cos(np.deg2rad(sweep))**3)

f_sweep = scipy.interpolate.interp1d(MDD, sweep)
sweep_angle =  f_sweep(0.78)
sweep_angle = round(float(sweep_angle),2)


sweep_angle_dir = np.rad2deg(np.arccos((0.7/0.78)))
sweep_angle_dir = round(sweep_angle_dir,2)

fig, ax = plt.subplots(1,1)
ax.plot(sweep, MDD, label = "Korn Equation")
ax.axvline(x=sweep_angle, color='black', linestyle='--', label = f"Sweep angle Korn {sweep_angle}")
ax.axvline(x=sweep_angle_dir, color='red', linestyle='-.', label = f"Sweep angle Geometry {sweep_angle_dir}")
ax.set_xlabel(r'$\Lambda ~ (\circ)$', fontsize=20)
ax.set_ylabel(r'$MDD$', fontsize=20)
ax.grid()
ax.legend(loc=2)
plt.show()