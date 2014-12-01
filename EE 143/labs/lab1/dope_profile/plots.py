import numpy as np
import matplotlib.pyplot as plt



profile0 = np.genfromtxt('profile0.txt',delimiter='    ')

profile0x_reduced = np.array([])
profile0y_reduced = np.array([])

# Get specific points so graph looks decent
for i in range(0,np.size(profile0[:,0])):
	if(profile0[i,0] <= 11):
		profile0x_reduced = np.append(profile0x_reduced,[profile0[i,0]])
		profile0y_reduced = np.append(profile0y_reduced,[profile0[i,1]])
		
plt.vlines(0,2,20,color='red',linestyles='dashed')
plt.hlines(17.34,-2,0.1488,color='green',linestyles='dashed')
plt.plot(profile0x_reduced,profile0y_reduced)
plt.scatter(profile0x_reduced,profile0y_reduced)
plt.axvspan(0, 2, alpha=0.5, color='red')

plt.axis([-1,1,2,20])
plt.xlabel("Distance ($\mu$m)")
plt.ylabel("log10(active(Boron))")
plt.title("Dopant profile through silicon")
plt.grid(True)
plt.savefig('profile0.pdf')
#######################################################################
profile1 = np.genfromtxt('profile1.txt', delimiter='   ')

profile1x_reduced = np.array([])
profile1y_reduced = np.array([])

plt.figure()
# Get specific points so graph looks decent
for i in range(0,np.size(profile1[:,0])):
	if(profile1[i,0] <= 11):
		profile1x_reduced = np.append(profile1x_reduced,[profile1[i,0]])
		profile1y_reduced = np.append(profile1y_reduced,[profile1[i,1]])
		
plt.vlines(-0.2698,2,20,color='red',linestyles='dashed')
plt.vlines(0.2104,2,20,color='red',linestyles='dashed')
plt.hlines(16.74,-2,0.03016,color='green',linestyles='dashed')
plt.plot(profile1x_reduced,profile1y_reduced)
plt.scatter(profile1x_reduced,profile1y_reduced)
plt.axvspan(-0.2698, 0.2104, alpha=0.5, color='green')
plt.axvspan(0.2104, 2, alpha=0.5, color='red')

plt.axis([-1,1,2,20])
plt.xlabel("Distance ($\mu$m)")
plt.ylabel("log10(active(Boron))")
plt.title("Dopant profile through field oxide")
plt.grid(True)

# Peak concentration of 10^16.74, interface of si-sio2 at 0.2104 microns

plt.savefig("profile1.pdf")


#######################################################################################
plt.figure()

profile2 = np.genfromtxt('profile2.txt', delimiter='    ')

profile2x_reduced = np.array([])
profile2y_reduced = np.array([])

# Get specific points so graph looks decent
for i in range(0,np.size(profile2[:,0])):
	if(profile2[i,0] <= 11):
		profile2x_reduced = np.append(profile2x_reduced,[profile2[i,0]])
		profile2y_reduced = np.append(profile2y_reduced,[profile2[i,1]])

plt.vlines(0.1594,2,20,color='red',linestyles='dashed')
plt.vlines(0.2490,2,20,color='red',linestyles='dashed')
plt.hlines(15.16,-2,0.2104,color='green',linestyles='dashed')
plt.plot(profile2x_reduced,profile2y_reduced)
plt.scatter(profile2x_reduced,profile2y_reduced)
plt.axvspan(0.1594, 0.2490, alpha=0.5, color='green')
plt.axvspan(0.2490, 2, alpha=0.5, color='red')

plt.axis([-1,1,2,20])
plt.xlabel("Distance ($\mu$m)")
plt.ylabel("log10(active(Boron))")
plt.title("Dopant profile through gate oxide")
plt.grid(True)

plt.savefig('profile2.pdf')
########################################################################################
plt.figure()

profile3 = np.genfromtxt('profile3.txt', delimiter='    ')

profile3x_reduced = np.array([])
profile3y_reduced = np.array([])

# Get specific points so graph looks decent
for i in range(0,np.size(profile3[:,0])):
	if(profile3[i,0] <= 11):
		profile3x_reduced = np.append(profile3x_reduced,[profile3[i,0]])
		profile3y_reduced = np.append(profile3y_reduced,[profile3[i,1]])

plt.vlines(-0.2406,2,20,color='red',linestyles='dashed')
plt.vlines(0.1594,2,20,color='red',linestyles='dashed')
plt.vlines(0.2490,2,20,color='red',linestyles='dashed')
plt.hlines(15.16,-2,0.9945,color='green',linestyles='dashed')
plt.plot(profile3x_reduced,profile3y_reduced)
plt.scatter(profile3x_reduced,profile3y_reduced)
plt.axvspan(0.1594, 0.2490, alpha=0.5, color='green')
plt.axvspan(0.2490, 2, alpha=0.5, color='red')
plt.axvspan(-0.2406,0.1594, alpha=0.5, color='purple')

plt.axis([-1,1,2,20])
plt.xlabel("Distance ($\mu$m)")
plt.ylabel("log10(active(Boron))")
plt.title("Dopant profile through Poly deposition")
plt.grid(True)

plt.savefig('profile3.pdf')

################################################################
plt.figure()

profile4 = np.genfromtxt('profile4.txt', delimiter='    ')

profile4x_reduced = np.array([])
profile4y_reduced = np.array([])

# Get specific points so graph looks decent
for i in range(0,np.size(profile4[:,0])):
	if(profile4[i,0] <= 11):
		profile4x_reduced = np.append(profile4x_reduced,[profile4[i,0]])
		profile4y_reduced = np.append(profile4y_reduced,[profile4[i,1]])

plt.vlines(0.2490,2,20,color='red',linestyles='dashed')
plt.hlines(15.03,-2,1.159,color='green',linestyles='dashed')
plt.plot(profile4x_reduced,profile4y_reduced)
plt.scatter(profile4x_reduced,profile4y_reduced)
plt.axvspan(0.2490, 2, alpha=0.5, color='red')

plt.axis([-1,2,2,20])
plt.xlabel("Distance ($\mu$m)")
plt.ylabel("log10(active(Boron))")
plt.title("Dopant profile after pre-diffusion")
plt.grid(True)

plt.savefig('profile4.pdf')

#################################################################
plt.figure()

profile5 = np.genfromtxt('profile5.txt', delimiter='    ')

profile5x_reduced = np.array([])
profile5y_reduced = np.array([])

# Get specific points so graph looks decent
for i in range(0,np.size(profile5[:,0])):
	if(profile5[i,0] <= 11):
		profile5x_reduced = np.append(profile5x_reduced,[profile5[i,0]])
		profile5y_reduced = np.append(profile5y_reduced,[profile5[i,1]])

plt.vlines(-0.1112,2,20,color='red',linestyles='dashed')
plt.vlines(0.2939,2,20,color='red',linestyles='dashed')
plt.hlines(21.4,-2,0.09628,color='green',linestyles='dashed')
plt.plot(profile5x_reduced,profile5y_reduced)
plt.scatter(profile5x_reduced,profile5y_reduced)
plt.axvspan(-0.1112, 0.2939, alpha=0.5, color='green')
plt.axvspan(0.2939, 2, alpha=0.5, color='red')

plt.axis([-1,2,2,22])
plt.xlabel("Distance ($\mu$m)")
plt.ylabel("log10(active(Boron))")
plt.title("Dopant profile after drive-in")
plt.grid(True)

plt.savefig('profile5.pdf')













plt.show()

