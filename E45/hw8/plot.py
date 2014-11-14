import numpy as np
import matplotlib.pyplot as plt


x = [100, 60, 20, 0, -20, -40, -60, -80, -100, -140, -180];
y = [84.9,82.8,81.2,77.9,74.5,67.8,50.8,36.0,28.1,25.6,25.1];


plt.plot(x,y)
plt.scatter(x,y)
plt.grid(True)
plt.xlabel("Temperature ($\degree$C)")
plt.ylabel("Impact energy, J")
plt.title("Charpy impact test for a particular structural steel")


plt.savefig("p2.pdf")

plt.figure()

kic =  170
x = np.linspace(0.1e-3,100e-3,1000)
sigma = kic/(np.sqrt(np.pi*x))
plt.gca().set_xscale('log')
plt.axis([0.1e-3,100e-3, 0, 2000])
plt.plot(x,sigma)
plt.hlines(1000,0.1e-3,.0092,color='red')
plt.vlines(0.0092,0,1000,color='red')
plt.grid(True)
plt.ylabel("Stress, $\sigma$ (MPa)")
plt.xlabel("flaw size (meters)")
plt.title("Design plot for a pressure vessel steel")

plt.savefig("p3.pdf")

plt.figure()

x = [100,65,21]
y = [95,125,135]
plt.plot(x,y)
plt.grid(True)
plt.axis([0,120,0,140])
plt.scatter(x,y)
plt.hlines(100,0,94.17,color='red')
plt.vlines(94.17,0,100,color='red')
plt.xlabel("Temperature ($\degree$C)")
plt.ylabel("Fatigue strength (MPa)")
plt.title("Fatigue vs temperature for C11000 copper")

plt.savefig("p4.pdf")









plt.show()
