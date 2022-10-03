

# 7:Repeat computer simulation of question no 6,for simultaneous
# rolling 3,5 and 10 dices and plot respective P(n) as a function of n.


import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint

P= lambda n: [sum(randint(6,size=n)) for i in range(trial)]
markers=['o','^','p','_']
n , trial = 3 , 10000

for i in range(4):
    x,y=np.unique(P(n),return_counts=True)
    x=x/n
    y=y/np.max(y)
    plt.plot(x,y,marker=markers[i])
    n=2*n+1

plt.xlabel('n')
plt.ylabel('P(n)')
plt.legend(['n=3','n=5','n=10'])
plt.show()
