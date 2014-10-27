import numpy as np
import matplotlib.pyplot as plt


plt.plot([1000,700],[100,100],'b',linewidth=2)
plt.hold(True)
plt.plot([1000,700],[0,0],'r',linewidth=2)
plt.plot([1000,700],[0,0],'g')

plt.plot([700,0],[0,0],'b',linewidth=2)
plt.plot([700,0],[88.8,88.8],'r',linewidth=2)
plt.plot([700,0],[11.2,11.2],'g',linewidth=2)

#plt.axes([1000,0,0,105])
plt.ylim([-5,105])
plt.xlim([1000,0])
plt.grid(True)
l1 = 'ferrite ($\\alpha$)';
l2 = 'cementite (${Fe}_{3} C$)'
plt.legend(["austenite ($\gamma$)",l1,l2],loc=7)
plt.xlabel("Temperature ($\degree$C)")
plt.ylabel("wt % C")
plt.title("wt % of phase present vs temperature for 0.77 wt % C eutectoid steel")

plt.savefig("p9_45.pdf")
#plt.show()

