import numpy as np
import matplotlib.pyplot as plt


## Device8a, plot 1
plt.figure()
x1 = np.array([4,6,8,10])
y1 = np.array([-0.0725,-0.122,-0.213,-0.368])
plt.plot(x1,y1)
plt.scatter(x1,y1)

plt.grid(True)
plt.xlabel("$L_{drawn}$ ($\mu m$)")
plt.ylabel("$\lambda$ ($V^{-1}$)")
plt.title("$\lambda$ vs MOSFET gate Length")
plt.savefig("D8plot.pdf")

plt.show()
