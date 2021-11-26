import matplotlib.pyplot as plt
import numpy as np 
import sympy as sym
import scipy.interpolate


t_c = np.linspace(6, 40, 100)
weight = 1 / np.sqrt(t_c)




#Mddeff, t_c = sym.symbols("Mddeff t_c")
#sweep = 29
#M_star = 1
#CL = 0.3
#eq = sym.Eq(0.3 * np.cos(np.deg2rad(sweep)) * ((1 - ((5 + Mddeff**2)/(5 + (M_star - 0.25*CL)**2))**3.5) * (1 - Mddeff**2)**0.5/(Mddeff**2) )**(2/3), t_c)
#print(sym.nsolve(eq, Mddeff, 0.5))



sweep = 29
M_star = 1
Mddeff = 0.8*np.cos(np.deg2rad(sweep))**(0.5)
CL = 0.3
print(Mddeff)

Mddeff = np.linspace(0.4,0.9,100)
#print(Mddeff)
toren_5 = []
toren_10 = []
toren_15 = [] 
toren_20 = []
toren_25 = []
toren_30 = []


def Toren(sweep, i):
    M_star = 1
    CL = 0.3
    t = 0.3 * np.cos(np.deg2rad(sweep)) * ((1 - ((5 + i**2)/(5 + (M_star - 0.25*CL)**2))**3.5) * (1 - i**2)**0.5/(i**2) )**(2/3)
    return t


for index, i in enumerate(Mddeff):
    toren_5.append(Toren(30, i)*100)
    toren_10.append(Toren(30, i)*100)
    toren_15.append(Toren(30, i)*100)
    toren_20.append(Toren(30, i)*100)
    toren_25.append(Toren(30, i)*100)
    toren_30.append(Toren(30, i)*100)



fig, ax = plt.subplots(1,1)
ax.plot(t_c, weight)
ax.axvline(x = 12, color='black', linestyle='--', label = "Chosen t/c (%)")
ax.set_xlabel(r'$t/c$', fontsize=20)
ax.set_ylabel(r'$W~(N)}$', fontsize=20)
plt.grid()


fig, ax = plt.subplots(1,1)
ax.plot(toren, Mddeff)
ax.axvline(x = 12, color='black', linestyle='--', label = "Chosen t/c (%)")
ax.set_xlabel(r'$t/c$', fontsize=20)
ax.set_ylabel(r'$M_{dd,ff}$', fontsize=20)
plt.grid()

plt.show()