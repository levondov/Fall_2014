import numpy as np
import matplotlib.pyplot as plt

a = np.array([4.4,4.5,4.45,4.4,4.6,4.5,2.6,2.7,2.65,2.5,2.6,2.55,2.7,2.9,2.8])

pArea = np.pi *np.power((a/2),2)
loadAndArea = 3000/pArea[0:6]
loadAndArea2 = 500/pArea[6:]

loadAndArea = (10 - np.sqrt(100 - np.power(a,2)))*((np.pi * 10)/2)
loadAndArea3000 = 3000/loadAndArea[0:6]
loadAndArea500 = 500/loadAndArea[6:]

#print(loadAndArea)
#print(loadAndArea2)
#print(loadAndArea3000)
#print(loadAndArea500)

nStress = [0.408,0.818,1.23,2.04]
x1 = [-6.37e-3,-9.55e-3,-15.9e-3,-15.9e-3]
y1 = [9.40e-3,9.40e-3,18.8e-3,34.5e-3]
x2 = [0,-31.3e-3,-31.3e-3,-31.3e-3]
y2 = [31.3e-3,62.5e-3,93.8e-3,156e-3]

f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True, sharey=True)
ax1.plot(x1,nStress)
ax1.scatter(x1,nStress)
ax2.plot(y1,nStress)
ax2.scatter(y1,nStress)
ax3.plot(x2,nStress)
ax3.scatter(x2,nStress)
ax4.plot(y2,nStress)
ax4.scatter(y2,nStress)
ax1.set_title("longitudinal and transverse strain vs nominal applied stress")
ax1.set_xlabel("x1 strain (in/in)")
ax1.set_ylabel("stress (psi)")
ax1.grid(True)
ax2.set_xlabel("y1 strain (in/in)")
ax2.set_ylabel("stress (psi)")
ax2.grid(True)
ax3.set_xlabel("x2 strain (in/in)")
ax3.set_ylabel("stress (psi)")
ax3.grid(True)
ax4.set_xlabel("y2 strain (in/in)")
ax4.set_ylabel("stress (psi)")
ax4.grid(True)

f.subplots_adjust(hspace=0.3)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig("graph_p4.pdf")
plt.show()

