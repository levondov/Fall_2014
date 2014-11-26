import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

font = {'family' : 'normal',
        'size'   : 16}

plt.rc('font', **font)

data1 = np.genfromtxt('metal_data.csv', delimiter=',')

temp_metal = data1[:,0]

temp_semi = np.array([-73,0 , 23 , 35 , 44 , 53 , 64, 73 , 83 ,95 , 100])
resist_semi = np.array([ 228,9.70 , 3.55 , 2.45 , 1.61 , 1.13 , 0.70 , 0.50 , 0.35 , 0.24 , 0.20])

temp_salt = np.array([400 , 450 , 500 , 550 , 600 , 650 , 700 , 750])
resist_salt = np.array([4.6e2 , 2.1e2 , 9.2e1 , 4.35e1 , 1.64e1 , 6.3 , 2.3 , 0.85 ])

plt.plot(temp_semi,resist_semi)
plt.scatter(temp_semi,resist_semi)
plt.xlabel("Temperature ($\degree$C)")
plt.ylabel("Resistance (k$\Omega$)")
plt.title("Semiconductor Resistance")

plt.grid(True)
plt.savefig("semi_full.pdf")

plt.figure()
plt.plot(temp_salt,resist_salt)
plt.scatter(temp_salt,resist_salt)
plt.xlabel("Temperature ($\degree$C)")
plt.ylabel("Resistance (k$\Omega$)")
plt.title("Salt Resistance")

plt.grid(True)
plt.savefig("salt_full.pdf")

plt.figure()
plt.xlabel("Temperature (K))")
plt.ylabel("Resistance (k$\Omega$)")
plt.title("Metal Resistance")
plt.grid(True)

plt.plot(temp_metal,1000*data1[:,1])
plt.scatter(temp_metal,1000*data1[:,1])
plt.plot(temp_metal,1000*data1[:,2])
plt.scatter(temp_metal,1000*data1[:,2])
plt.plot(temp_metal,1000*data1[:,3])
plt.scatter(temp_metal,1000*data1[:,3])
plt.plot(temp_metal,1000*data1[:,4])
plt.scatter(temp_metal,1000*data1[:,4])
plt.plot(temp_metal,1000*data1[:,5])
plt.scatter(temp_metal,1000*data1[:,5])

plt.legend(['sample 11', 'sample 12', 'sample 13', 'sample 14', 'sample 15'],loc = 'upper left',prop={'size':16})
plt.savefig("metal_full.pdf")

##################################################
X = 0.195/1.55
pth = 1.55

for i in range(1,6):
	alpha1 = data1[0,i]/data1[2,i]
	pr1 = ((X - alpha1)/(alpha1 - 1))*pth
	print (i,pr1)
	
####################################################

plt.figure()
plt.xlabel("1/T ($K^{-1}$)")
plt.ylabel("ln($G/G_0$) ($k\Omega^{-1}m^{-1}/k\Omega^{-1}m^{-1}$)")
plt.title("ln($G/G_0$) vs 1/T for Germanium sample")

plt.grid(True)
plt.plot(1./(temp_semi + 273),np.log(1/resist_semi))
plt.scatter(1./(temp_semi + 273),np.log(1/resist_semi))

plt.savefig("semi_full_eg.pdf")
x=1./(temp_semi[5:] + 273)
y=np.log(1/resist_semi[5:]	)

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print(slope, intercept, r_value, p_value, std_err)

#(-44246.928047413392, 13.469903542524477, -0.99971629807973661, 1.2071875221474409e-07, 527.09838661380536)

Egap = (-1*2*slope*1.38e-23)/(1.602e-19)
print("TESTT")
print(Egap)

##################################################

plt.figure()
plt.xlabel("1/T ($K^{-1}$)")
plt.ylabel("ln($G/G_0$) ($k\Omega^{-1}m^{-1}/k\Omega^{-1}m^{-1}$)")
plt.title("ln($G/G_0$) vs 1/T for Salt  sample")

plt.grid(True)
plt.plot(1./(temp_salt + 273),np.log(1/resist_salt))
plt.scatter(1./(temp_salt + 273),np.log(1/resist_salt))

plt.savefig("salt_full_eg.pdf")
x1=1./(temp_salt + 273)
y1=np.log(1/resist_salt)

slope, intercept, r_value, p_value, std_err = stats.linregress(x1,y1)
print(slope, intercept, r_value, p_value, std_err)

x1half=x1[0:4:1]
x2half=x1[4:8:1]
y1half=y1[0:4:1]
y2half=y1[4:8:1]

slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(x1half,y1half)
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(x2half,y2half)
print(slope1,slope2)
print(slope2/1.38e-23)
E = slope1/1.38e-23
print(-2*(slope1*1.38e-23+E))









#plt.show()
