import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'normal',
        'size'   : 16}

plt.rc('font', **font)

x,y=np.genfromtxt("lab3sec102datalevon.rtf", unpack=True, skiprows = 1)
x1 = np.array([])
y1 = np.array([])
print(np.size(x,0))
for i in range(0,np.size(x,0)):
	if (x[i] < 1300):
		x1 = np.append(x1,x[i])
		y1 = np.append(y1,y[i])

#plt.plot(x,y)
plt.plot(x1,y1)
plt.title("Cooling curve for 15 % Sb in Pb")
plt.ylabel("Temperature $\degree$C")
plt.xlabel("Time (sec)")
plt.grid(True)

plt.savefig("graph1.pdf")
#plt.show()
