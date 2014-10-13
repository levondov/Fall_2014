import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf
degree_sign= u'\N{DEGREE SIGN}'

x = np.linspace(-20e-6,20e-6,100)

temp = x/(2*np.sqrt(1e-14*3600))
temp2 = x/(2*np.sqrt(1e-13*3600))

cx = 50*(1-erf(temp))
cx2 = 50*(1-erf(temp2))

plt.plot(x,cx)
plt.plot(x,cx2)
plt.grid(True)
plt.axis([-0.00002,0.00002,0,100])
plt.xlabel('distance diffused into Metal B (meters)')
plt.ylabel('concentration profile (at %)')
plt.title('concentration profile of metal A after 1 hour')
plt.legend(['1000 $^\circ$C','1200 $^\circ$C'])
plt.savefig('p3_graph.pdf')
print(degree_sign)
plt.show()
