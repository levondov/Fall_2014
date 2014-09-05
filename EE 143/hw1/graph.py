import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.plot([1,2,3,4],[10,100,1000,10000])
ax.set_yscale('log')
plt.grid(True)
plt.show()




