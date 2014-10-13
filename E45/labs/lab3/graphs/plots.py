import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.integrate import simps

font = {'family' : 'normal',
        'size'   : 16}

plt.rc('font', **font)

x,y=np.genfromtxt("lab3.sec102.levon.kira.avyay", unpack=True, skiprows = 1)


plt.plot(x,y)
plt.title('Brass Sample Heating')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature ($^\circ$C)')
plt.grid(True)


x1 = np.array([])
y1 = np.array([])

for i in range (0,x.size):
	if ((i >= 830) & (i <= 1740)):
		x1 = np.append(x1,x[i])
		y1 = np.append(y1,y[i])
plt.savefig('graph1.pdf')

plt.figure()
plt.plot(x1,y1)
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature ($^\circ$C)')
plt.grid(True)
plt.savefig('graph2.pdf')

plt.figure()
x2 = [5,15,25,35,45]
y2 = [9.3,13.0,44.0,50.9,51.2]
plt.plot(x2,y2)
plt.scatter(x2,y2)
plt.grid(True)
plt.xlabel('Percent Reduction in Thickness (%)')
plt.ylabel('Rockwell Hardness (HRA)')
plt.title('Hardness vs Percent Reduction in Thickness')
plt.savefig('graph3.pdf')

plt.show()

















