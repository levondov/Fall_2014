import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.integrate import simps


x1,y1=np.genfromtxt("Section-102-James_Tensile-Test-1018mildsteel.txt", unpack=True, skiprows = 1)
x2,y2=np.genfromtxt("Section-102-James_Tensile-Test-4340.txt", unpack=True, skiprows = 1)
x3,y3=np.genfromtxt("Section-102-James_Tensile-Test-Al-Cu.txt", unpack=True, skiprows = 1)

y1e = y1/(np.pi*(0.233)/4)
y2e = y2/(np.pi*(0.235)/4)
y3e = y3/(np.pi*(0.254)/4)
x1e = x1/1.884
x2e = x2/1.973
x3e = x3/1.908

#plt.plot(x1,y1)
#plt.grid(True)
#plt.title('Stress vs Strain for Steel-1018')
#plt.xlabel('strain (in)')
#plt.ylabel('Stress (lb)')
#plt.savefig('1018.pdf')

#plt.figure()
#plt.plot(x2,y2)
#plt.grid(True)
#plt.title('Stress vs Strain for Steel-4340')
#plt.xlabel('strain (in)')
#plt.ylabel('Stress (lb)')
#plt.savefig('4340.pdf')

#plt.figure()
#plt.plot(x3,y3)
#plt.grid(True)
#plt.title('Stress vs Strain for Al-Cu')
#plt.xlabel('strain (in)')
#plt.ylabel('Stress (lb)')
#plt.savefig('alcu.pdf')

slopex1 = np.array([])
slopey1 = np.array([])
slopex2 = np.array([])
slopey2 = np.array([])
slopex3 = np.array([])
slopey3 = np.array([])

#plt.figure()
#plt.plot(x1e,y1e)
#plt.grid(True)
#plt.title('Engineer Stress vs Strain for Steel-1018')
#plt.xlabel('strain (in/in)')
#plt.ylabel('Stress (psi)')
#plt.savefig('1018e.pdf')

############ 1018 #########

#modulus of elasticity
size = 0
for i in range(0,x1.shape[0]):
	
	if ((x1e[i] >= 0.0075) & (x1e[i] <= 0.01)):
		slopex1 = np.insert(slopex1,size,x1e[i])
		slopey1 = np.insert(slopey1,size,y1e[i])
		size+=1
size = 0
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(slopex1,slopey1)
localmin = 8000

#yield strength
for i in range(0,x1e.shape[0]):
	if ((x1e[i] >= 0.03) & (x1e[i] <= 0.032) & (y1e[i] < localmin)):
		localmin = y1e[i]
		
#tensile strength
localmax1 = 0
for i in range(0,x1e.shape[0]):
	if ((x1e[i] >= 0.15) & (x1e[i] <= 0.35) & (y1e[i] > localmax1)):
		localmax1 = y1e[i]
		
print(localmax1)
##########################################

#plt.figure()
#plt.plot(x2e,y2e)
#plt.grid(True)
#plt.title('Engineering Stress vs Strain for Steel-4340')
#plt.xlabel('strain (in/in)')
#plt.ylabel('Stress (psi)')
#plt.savefig('4340e.pdf')

############## 4340 ##############

#modulus of elasticity
for i in range(0,x2.shape[0]):
	
	if ((x2e[i] >= 0.02) & (x2e[i] <= 0.025)):
		slopex2 = np.insert(slopex2,size,x2e[i])
		slopey2 = np.insert(slopey2,size,y2e[i])
		size+=1
size = 0
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(slopex2,slopey2)

#yield strength
b2 = 4000 - slope2*0.0148
xoffset2 = np.linspace(0.01,0.04,1000)
yoffset2 = slope2*xoffset2 + b2
#plt.plot(xoffset2,yoffset2)

#tensile strength
localmax2 = 0
for i in range(0,x2e.shape[0]):
	if ((x2e[i] >= 0.03) & (x2e[i] <= 0.04) & (y2e[i] > localmax2)):
		localmax2 = y2e[i]
		
print(localmax2)
#################################################

plt.figure()
plt.plot(x3e,y3e)
plt.grid(True)
#plt.title('Engineering Stress vs Strain for Al-Cu')
#plt.xlabel('strain (in/in)')
#plt.ylabel('Stress (psi)')
#plt.savefig('alcue.pdf')



####################################### AlCu #######################

#modulus of elasticity
for i in range(0,x3.shape[0]):
	
	if ((x3e[i] >= 0.013) & (x3e[i] <= 0.016)):
		slopex3 = np.insert(slopex3,size,x3e[i])
		slopey3 = np.insert(slopey3,size,y3e[i])
		size+=1
size = 0
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(slopex3,slopey3)

#yield strength
b3 = slope3*0.012*-1
xoffset = np.linspace(0.012,0.0225,1000)
yoffset = slope3*xoffset + b3
plt.plot(xoffset,yoffset)

#tensile strength
localmax3 = 0
for i in range(0,x3e.shape[0]):
	if ((x3e[i] >= 0.15) & (x3e[i] <= 0.25) & (y3e[i] > localmax3)):
		localmax3 = y3e[i]
		
print(localmax3)

#########################################################################

### fracture stress
f1 = 1805.2/(np.pi*(0.206)/4)
f2 = 10726.9/(np.pi*(0.234)/4)
f3 = 3050.8/(np.pi*(0.232)/4)
print('frac stress')
print(f1)
print(f2)
print(f3)

#### area reduction
a1 = (np.pi*(0.206)/4)/(np.pi*(0.233)/4)
a2 = (np.pi*(0.234)/4)/(np.pi*(0.235)/4)
a3 = (np.pi*(0.232)/4)/(np.pi*(0.254)/4)

print('area reduction')
print(a1,a2,a3)

#### integrate

ai1 = simps(y1e,x1e)
ai2 = simps(y2e,x2e)
ai3 = simps(y3e,x3e)

print('integrals')
print(ai1,ai2,ai3)

############################################

# stress strain true

x1et = np.log(1 + x1e)
x2et = np.log(1 + x2e)
x3et = np.log(1 + x3e)
y1et = y1e*(1 + x1e)
y2et = y2e*(1 + x2e)
y3et = y3e*(1 + x3e)

plt.figure()
plt.plot(x1e,y1e,label='Engineering')
plt.plot(x1et,y1et,label='True')
plt.grid(True)
plt.title('True and Engineering Stress vs Strain for Steel-1018')
plt.xlabel('strain (in/in)')
plt.ylabel('Stress (psi)')
plt.legend(loc=2)
plt.savefig('1018et.pdf')

plt.figure()
plt.plot(x2e,y2e,label='Engineering')
plt.plot(x2et,y2et,label='True')
plt.grid(True)
plt.title('True and Engineering Stress vs Strain for Steel-4340')
plt.xlabel('strain (in/in)')
plt.ylabel('Stress (psi)')
plt.legend(loc=2)
plt.savefig('4340et.pdf')

plt.figure()
plt.plot(x3e,y3e,label='Engineering')
plt.plot(x3et,y3et,label='True')
plt.grid(True)
plt.title('True and Engineering Stress vs Strain for Al-Cu')
plt.xlabel('strain (in/in)')
plt.ylabel('Stress (psi)')
plt.legend(loc=2)
plt.savefig('alcuet.pdf')

plt.show()












































