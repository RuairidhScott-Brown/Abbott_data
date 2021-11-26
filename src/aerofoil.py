import matplotlib.pyplot as plt


with open("C:/Users/18rsc/Documents/imperial/year_3/abbott_data/data/aerofoil.txt", 'r') as file:
    lines = file.readlines()

print(lines)
x = []
y = []
for index,e in enumerate(lines):
    temp = e.split('\t')
    x.append(float(temp[0]))
    y.append(float(temp[1]))

fig, axs = plt.subplots(1,1)
axs.plot(x,y)
axs.set_xlabel(r'$x/c$', fontsize=20)
axs.set_ylabel(r'$y/c$', fontsize=20)
axs.set_ylim(-15,15)
plt.show()