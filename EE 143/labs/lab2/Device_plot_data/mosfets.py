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
## delta W
plt.figure()
x = np.array([10,15,20])
y = np.array([0.004,0.0058,0.0063])*1000

slope4, intercept4, r_value, p_value, std_err = stats.linregress(x,y/2)
x5 = np.linspace(-intercept4/slope4,20,100)

plt.scatter(x,y/2)
plt.plot(x5,slope4*x5 + intercept4)
#print(-intercept4/slope4)

plt.grid(True)
plt.axis([-10,25,0,3.5])
plt.xlabel('$W_{drawn}$ ($\mu m$)')
plt.ylabel('$1/R_{meas}$ (1/$\Omega$)')
plt.title('R measured vs Channel Width')
plt.savefig('D9Rplot.pdf')
## Vt vs Weff
plt.figure()
x5 = np.array([18.33,23.33,28.33])
y5 = np.array([-4.98,-5.46,-4.91])

plt.plot(x5,y5)
plt.scatter(x5,y5)
plt.grid(True)
#plt.axis([-10,25,0,3.5])
plt.xlabel('$W_{eff}$ ($\mu m$)')
plt.ylabel('$V_t$ (V)')
plt.title('Threshold voltage vs Effective channel Width')
plt.savefig('D9Wplot.pdf')
## Ueff vs VG
plt.figure()
device102 = np.genfromtxt('D10IMG2.TXT.csv', delimiter=',',skip_header=113) #113
slope102, intercept102, r_value, p_value, std_err = stats.linregress(device102[0:13,0],device102[0:13,1])
x102 = np.linspace(-intercept102/slope102,12,100)
y102 = slope102*x102 + intercept102
ueff = y102[1:]/(1.07e-5*(x102[1:] + 4.92))


plt.plot(x102[1:],ueff)
plt.scatter(x102[1:],ueff)
plt.grid(True)
plt.xlabel('V_G (V)')
plt.ylabel('$\mu_{eff}$ (${cm}^{2}$/ V-s)')
plt.title('Effective electron mobility vs Gate voltage')
plt.savefig('D10Uplot.pdf')
### vt vs vsb 0.7 
device102 = np.genfromtxt('D10IMG2.TXT.csv', delimiter=',',skip_header=113) #113
slope102, intercept102, r_value, p_value, std_err = stats.linregress(device102[0:13,0],device102[0:13,1])
slope102a, intercept102a, r_value, p_value, std_err = stats.linregress(device102[13:26,0],device102[13:26,1])
slope102b, intercept102b, r_value, p_value, std_err = stats.linregress(device102[26:39,0],device102[26:39,1])
#print(-intercept102/slope102)
#print(-intercept102a/slope102a)
#print(-intercept102b/slope102b)
## body effect parameter
plt.figure()
x6 = np.array([np.sqrt(0.7),np.sqrt(0.7+1),np.sqrt(0.7+2)])
y6 = np.array([-4.92,-4.55,-4.18])
slope6, intercept6, r_value, p_value, std_err = stats.linregress(x6,y6)

x6a = np.linspace(0,10,100)
y6a = slope6*x6a + intercept6

#print(slope6)
plt.grid(True)
plt.scatter(x6,y6)
plt.plot(x6a,y6a)
plt.xlabel('$\sqrt{V_{SB} + 0.7}$ (V)')
plt.ylabel('V_t (V)')
plt.title('Estimation of body effect paramter')
plt.savefig('D10Gplot.pdf')
### Inverter shit
device14 = np.genfromtxt('D14IMG1.TXT.csv', delimiter=',',skip_header=113) #113
mins = np.abs(device14[0,0] - device14[0,1])
minx = 0;
for i in range(0,np.size(device14,0)):
	if (np.abs(device14[i,0] - device14[i,1]) < mins):
		mins = np.abs(device14[i,0] - device14[i,1]) 
		minx = i;
#print(device14[minx,0],device14[minx,1],mins)
#### More Inverter shit
plt.figure()
x = np.linspace(0.25,1,100)
yi1 = (1/170.)*(-8*np.sqrt(400*(x**2) - 135*x + 9) + 160*x - 27) #vdd = 0
yi2 = (1/170.)*(-4*np.sqrt(2)*np.sqrt(800*(x**2) - 170*x - 17) + 160*x - 17) #vdd = 1
yi3 = (1/170.)*(-8*np.sqrt(400*(x**2) - 35*x - 76) + 160*x - 7) #vdd = 2

plt.plot(x,yi1)
plt.plot(x,yi2)
plt.plot(x,yi3)

plt.grid(True)
plt.xlabel('$V_{in}$ (V)')
plt.ylabel('V_out (V)')
plt.title('$V_{out}$ vs $V_{in}$ for theoretical Inverter')
plt.legend(['$V_{dd}$ = 0','$V_{dd}$ = 1','$V_{dd}$ = 2'],loc =1)
plt.savefig('D14theoplot.pdf')





plt.show()
