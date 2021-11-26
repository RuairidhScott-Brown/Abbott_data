import matplotlib.pyplot as plt
import numpy as np

#general parameters
M_crit = 0.7
M_cruise = 0.78
M_dd = M_crit + 0.08
CL = 0.27


#don't actually need sweep really
#we want the MDD = M_cruise but MDD is already higher than M_cruise
sweep_25 = 0
M_eff = M_cruise * np.cos(np.deg2rad(sweep_25))
M_ddeff = M_dd * (np.cos(np.deg2rad(sweep_25)))
M_r = M_ddeff / M_eff

t_c = 0.3 * np.cos(np.deg2rad(sweep_25)) * ((1 - ((5 + M_ddeff**2)/(5 + (1.05 - 0.25*CL)**2))**3.5) * (1 - M_ddeff**2)**0.5/(M_ddeff**2) )**(2/3)

