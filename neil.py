import matplotlib.pyplot as p
import numpy as np
amt=15
l=np.random.randint(0,100,amt)
x=np.arange(0,amt,1)
n=len(l)
for i in range(n):
    for j in range(0,n-i-1):
        p.bar(x,l)
        p.pause(0.01)
        p.clf()
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
p.show()