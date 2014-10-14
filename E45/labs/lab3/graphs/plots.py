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

plt.figure()
x3 = [1./8,2./8,3./8,4./8,5./8,6./8,7./8,1,9./8,10./8,11./8,12./8,13./8,14./8,15./8]
y3 = [51.2,52.7,54.5,54.5,51.7,34.0,23.5,21.5,20.0,16.1,12.6,11.5,8.5,9.5,11.9]
plt.plot(x3,y3)
plt.scatter(x3,y3)
plt.grid(True)
plt.xlabel("length (inch)")
plt.ylabel("Rockwell Hardness (HRA)")
plt.title("Hardness along most deformed edge of sample")
plt.savefig('graph4.pdf')

plt.show()

















