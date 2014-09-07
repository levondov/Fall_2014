import numpy as np
import matplotlib.pyplot as plt

k = 4*9e9*(1.6e-19)**2


a = np.linspace(0.2e-9,0.7e-9,1000)
f = k/(a**2)

plt.plot(a,f)
plt.title('Coulombic force for Magnesium oxide')
plt.xlabel('a (m)')
plt.ylabel('F_c (N)')
plt.axis([0,7e-10,0,2.5e-8])
plt.grid(True)

plt.savefig('graph_p2_13.pdf')
plt.show()



