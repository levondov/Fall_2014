import numpy as np
import matplotlib.pyplot as plt


profile1 = np.genfromtxt('profile1.txt', delimiter='   ')

profile1x_reduced = np.array([])
profile1y_reduced = np.array([])

# Get specific points so graph looks decent
for i in range(0,np.size(profile1[:,0])):
	if(profile1[i,0] <= 11):
		profile1x_reduced = np.append(profile1x_reduced,[profile1[i,0]])
		profile1y_reduced = np.append(profile1y_reduced,[profile1[i,1]])
		
plt.vlines(0.2104,2,20,color='red',linestyles='dashed')
plt.hlines(16.74,-2,0.2104,color='green',linestyles='dashed')
plt.plot(profile1x_reduced,profile1y_reduced)
plt.scatter(profile1x_reduced,profile1y_reduced)
plt.axis([-2,12,2,20])
plt.xlabel("Distance ($\mu$m)")
plt.ylabel("log10(active(Boron))")
plt.title("Dopant profile through field oxide and silicon")
plt.grid(True)

plt.savefig("profile1.pdf")

plt.show()

1.67433e+01
