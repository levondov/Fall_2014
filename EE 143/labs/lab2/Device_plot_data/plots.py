import numpy as np
import matplotlib.pyplot as plt


## Device 2a
device2a = np.genfromtxt('D2AIMG.TXT.csv', delimiter=',',skip_header=108)

plt.plot(device2a[:,0],device2a[:,1])
plt.axis([-2,2,-.15,.15])
plt.grid(True)
plt.xlabel("VDiff (V)")
plt.ylabel("IA (A)")
plt.title("Resistor 2a measurement plot")

plt.savefig("D2aplot.pdf")
## Device 2b
plt.figure()
device2b = np.genfromtxt('D2BIMG.TXT.csv', delimiter=',',skip_header=108)

plt.plot(device2b[:,0],device2b[:,1])
plt.axis([-2,2,-.15,.15])
plt.grid(True)
plt.xlabel("VDiff (V)")
plt.ylabel("IA (A)")
plt.title("Resistor 2b measurement plot")

plt.savefig("D2bplot.pdf")
## Device 2c
plt.figure()
device2c = np.genfromtxt('D2CIMG.TXT.csv', delimiter=',',skip_header=108)

plt.plot(device2c[:,0],device2c[:,1])
plt.axis([-2,2,-.05,.05])
plt.grid(True)
plt.xlabel("VA (V)")
plt.ylabel("IA (A)")
plt.title("Resistor 2c measurement plot")

plt.savefig("D2cplot.pdf")
## Device 2d
plt.figure()
device2d = np.genfromtxt('D2DIMG.TXT.csv', delimiter=',',skip_header=108)

plt.plot(device2d[:,0],device2d[:,1])
plt.axis([-2,2,-.015,.015])
plt.grid(True)
plt.xlabel("VA (V)")
plt.ylabel("IA (A)")
plt.title("Resistor 2d measurement plot")

plt.savefig("D2dplot.pdf")
## Device 7, plot 1 forward operation
plt.figure()
device7a = np.genfromtxt('D7IMG1.TXT.csv', delimiter=',',skip_header=108)

plt.plot(device7a[:,0],1000*device7a[:,1])
plt.grid(True)
plt.xlabel("VA (V)")
plt.ylabel("IA (mA)")
plt.title("Diode forward operation")

plt.savefig("D7aplot.pdf")
## Device 7, plot 2 reverse operation
plt.figure()
device7b = np.genfromtxt('D7IMG2.TXT.csv', delimiter=',',skip_header=108)

plt.plot(device7b[:,0],1000*device7b[:,1])
plt.grid(True)
plt.axis([0, 5, 0.015,0.055])
plt.xlabel("VA (V)")
plt.ylabel("IA (mA)")
plt.title("Diode reverse operation")

plt.savefig("D7bplot.pdf")
## Device8a, plot 1
plt.figure()
device8a = np.genfromtxt('D8AIMG1.TXT.csv', delimiter=',',skip_header=113) #113
start = 0;

for i in range(0,np.size(device8a,0)):
	if (device8a[i,0] < device8a[i-1,0]):
		plt.plot(device8a[start:i,0],device8a[start:i,1],'b')
		start = i
		
plt.grid(True)
plt.xlabel("VD (V)")
plt.ylabel("ID (A)")
plt.title("Mosfet 8a, Test 1 plot")
plt.savefig("D8a1plot.pdf")
## Device8b, plot 1
plt.figure()
device8b = np.genfromtxt('D8BIMG1.TXT.csv', delimiter=',',skip_header=113) #113
start = 0;

for i in range(0,np.size(device8b,0)):
	if (device8b[i,0] < device8b[i-1,0]):
		plt.plot(device8b[start:i,0],device8b[start:i,1],'b')
		start = i
		
plt.grid(True)
plt.xlabel("VD (V)")
plt.ylabel("ID (A)")
plt.title("Mosfet 8b, Test 1 plot")
plt.savefig("D8b1plot.pdf")
## Device8c, plot 1
plt.figure()
device8c = np.genfromtxt('D8CIMG1.TXT.csv', delimiter=',',skip_header=113) #113
start = 0;

for i in range(0,np.size(device8c,0)):
	if (device8c[i,0] < device8c[i-1,0]):
		plt.plot(device8c[start:i,0],device8c[start:i,1],'b')
		start = i
		
plt.grid(True)
plt.xlabel("VD (V)")
plt.ylabel("ID (A)")
plt.title("Mosfet 8c, Test 1 plot")
plt.savefig("D8c1plot.pdf")
## Device8d, plot 1
plt.figure()
device8d = np.genfromtxt('D8DIMG1.TXT.csv', delimiter=',',skip_header=113) #113
start = 0;

for i in range(0,np.size(device8d,0)):
	if (device8d[i,0] < device8d[i-1,0]):
		plt.plot(device8d[start:i,0],device8d[start:i,1],'b')
		start = i
		
plt.grid(True)
plt.xlabel("VD (V)")
plt.ylabel("ID (A)")
plt.title("Mosfet 8d, Test 1 plot")
plt.savefig("D8d1plot.pdf")
## Device8a, plot 2
plt.figure()
device8a2 = np.genfromtxt('D8AIMG2.TXT.csv', delimiter=',',skip_header=113) #113
start = 0;

for i in range(0,np.size(device8a2,0)):
	if (device8a2[i,0] < device8a2[i-1,0]):
		plt.plot(device8a2[start:i,0],1000*device8a2[start:i,1],'b')
		start = i
		
plt.grid(True)
plt.xlabel("VG (V)")
plt.ylabel("ID (mA)")
plt.title("Mosfet 8a, Test 2 plot")
plt.savefig("D8a2plot.pdf")
## Device8b, plot 2
plt.figure()
device8b2 = np.genfromtxt('D8BIMG2.TXT.csv', delimiter=',',skip_header=113) #113
start = 0;

for i in range(0,np.size(device8b2,0)):
	if (device8b2[i,0] < device8b2[i-1,0]):
		plt.plot(device8b2[start:i,0],1000*device8b2[start:i,1],'b')
		start = i
		
plt.grid(True)
plt.xlabel("VG (V)")
plt.ylabel("ID (mA)")
plt.title("Mosfet 8b, Test 2 plot")
plt.savefig("D8b2plot.pdf")
## Device8c, plot 2
plt.figure()
device8c2 = np.genfromtxt('D8CIMG21.TXT.csv', delimiter=',',skip_header=113) #113
start = 0;

for i in range(0,np.size(device8c2,0)):
	if (device8c2[i,0] < device8c2[i-1,0]):
		plt.plot(device8c2[start:i,0],1000*device8c2[start:i,1],'b')
		start = i
		
plt.grid(True)
plt.xlabel("VG (V)")
plt.ylabel("ID (mA)")
plt.title("Mosfet 8c, Test 2 plot")
plt.savefig("D8c2plot.pdf")
## Device8d, plot 2
plt.figure()
device8d2 = np.genfromtxt('D8DIMG2.TXT.csv', delimiter=',',skip_header=113) #113
start = 0;

for i in range(0,np.size(device8d2,0)):
	if (device8d2[i,0] < device8d2[i-1,0]):
		plt.plot(device8d2[start:i,0],1000*device8d2[start:i,1],'b')
		start = i
		
plt.grid(True)
plt.xlabel("VG (V)")
plt.ylabel("ID (mA)")
plt.title("Mosfet 8d, Test 2 plot")
plt.savefig("D8d2plot.pdf")









#plt.show()
