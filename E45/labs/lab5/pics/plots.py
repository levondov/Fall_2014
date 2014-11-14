import numpy as np
import matplotlib.pyplot as plt

font = {'family' : 'normal',
        'size'   : 16}

plt.rc('font', **font)

x,y,junk=np.genfromtxt("labsec103_Nov4_p1.rtf", unpack=True)


plt.plot(x,y)
plt.xlabel("Time (seconds)")
plt.ylabel("Temperature ($\degree$C)")
plt.title("Temperature plot for heating of Nichrome sample")
plt.grid(True)

plt.savefig("fig1.pdf")

x1 = np.array([])
y1 = np.array([])

plt.figure()
for i in range(0,np.size(x)):
	if ((x[i] >= 350) & (x[i] <= 1700)):
		x1 = np.append(x1,x[i])
		y1 = np.append(y1,y[i])


plt.plot(x1,y1)
plt.grid(True)
plt.axis((350,1700,800,1100))	
plt.xlabel("Time (seconds)")
plt.ylabel("Temperature ($\degree$C)")
plt.title("Temperature plot for heating of Nichrome sample")
plt.savefig("fig2.pdf")

plt.figure()
x2 = [1./8,2./8,3./8,4./8,5./8,6./8,7./8,1,9./8,10./8,11./8,12./8,13./8,14./8,15./8,2]
y2 = [79.5,66.2,61.4,58.0,59.8,62.1,62.9,64.8,65.0,65.7,61.4,72.9,66.0,73.2,80.9,82.0]
plt.plot(x2,y2)
plt.scatter(x2,y2)
plt.axis((0,2,55,85))
plt.grid(True)
plt.xlabel("length of sample (inches)")
plt.ylabel("Hardness (HRA)")
plt.title("Nichrome hardness across sample")
plt.savefig("fig3.pdf")

plt.show()
