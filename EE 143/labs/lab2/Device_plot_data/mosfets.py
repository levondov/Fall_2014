import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


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



slope, intercept, r_value, p_value, std_err = stats.linregress(x1,y1)
## delta L
plt.figure()
x = np.array([4,6,8,10])
y1= np.array([0.458,0.1775,0.109,0.0775])
y2 = np.array([0.478,0.188,0.116,0.0825])
y3 = np.array([0.495,0.198,0.123,0.0855])

slope1, intercept1, r_value, p_value, std_err = stats.linregress(x,2/y1)
slope2, intercept2, r_value, p_value, std_err = stats.linregress(x,4/y2)
slope3, intercept3, r_value, p_value, std_err = stats.linregress(x,6/y3)
x1 = np.linspace(2,12,100)

plt.plot(x1,slope1*x1 + intercept1)
plt.plot(x1,slope2*x1 + intercept2)
plt.plot(x1,slope3*x1 + intercept3)

plt.scatter(x,2/y1)
plt.scatter(x,4/y2)
plt.scatter(x,6/y3)

plt.grid(True)
plt.xlabel('$L_{drawn}$ ($\mu m$)')
plt.ylabel('$R_{meas}$ (k$\Omega$)')
plt.title('R measured vs Gate Length')
plt.legend(['$V_{gt} = 2 V$','$V_{gt} = 4 V$','$V_{gt} = 6 V$'],loc=2)
plt.savefig('D8Rplot.pdf')


plt.show()
