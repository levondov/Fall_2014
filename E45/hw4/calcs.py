import numpy as np


def d(h,k,l):
	d = 0.420/np.sqrt(h*h + k*k + l*l)
	return d

def t2(d):
	t2 = (180*2*np.arcsin(0.1542/(2*d)))/np.pi
	return t2	
	
d1 = d(1,1,1)
d2 = d(2,0,0)
d3 = d(2,2,0)
d4 = d(3,1,1)
d5 = d(2,2,2)
d6 = d(4,0,0)

tt1 = t2(d1)
tt2 = t2(d2)
tt3 = t2(d3)
tt4 = t2(d4)
tt5 = t2(d5)
tt6 = t2(d6)

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)

print(tt1)
print(tt2)
print(tt3)
print(tt4)
print(tt5)
print(tt6)
