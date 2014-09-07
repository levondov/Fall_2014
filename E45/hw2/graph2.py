import numpy as np
import matplotlib.pyplot as plt

element = [19,20,21,22,23,24,25,26,27,28,29,30,31];
a = [2*0.231,2*0.197,2*0.160,2*0.147,2*0.132,2*0.125,2*0.112,2*0.124,2*0.125,2*0.125,2*0.128,2*0.133,2*0.135];

plt.plot(element,a,'bo')
plt.title('Bond length for metals K - Ga')
plt.xlabel('element atomic #')
plt.ylabel('a (nm)')
plt.axis()
plt.grid(True)

plt.savefig('graph_p2_46.pdf')
plt.show()


