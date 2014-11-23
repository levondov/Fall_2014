import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.0,0.02,10)

m1 = 6.9e3
m2 = 72.4e3
m3 = 46.2e3
m4 = 39.7e3


plt.plot(x,x*m1)
plt.plot(x,x*m2)
plt.plot(x,x*m3)
plt.plot(x,x*m4)
plt.grid(True)

plt.title("Stress vs Strain for composites,fibers, and matrices")
plt.xlabel("$\epsilon$ (mm/mm)")
plt.ylabel("$\sigma$ (MPa)")
plt.axis([0,0.02,0,1500])
plt.legend(["Epoxy (matrix)","E-glass (fiber)", "Composite (60% vol)","Composite (50% vol)"],"upper left")


plt.savefig("1247plot.pdf")
plt.show()
