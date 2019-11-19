from random import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import use



def FT(arr):
    size_array = len(arr)
    out_arr = []
    out_arr2 = []
    summ = 0
    # summ2 = 0
    for k in range(size_array):
        for n in range(size_array):
            summ = summ + (arr[n]*np.exp(-1j*(2*np.pi/size_array)*n*k))
            # summ2 = summ2 +(arr[n]*(np.cos((2*np.pi/size_array)*n*k)-1j*np.sin((2*np.pi/size_array)*n*k)))
        out_arr.append(summ)
        # out_arr2.append(summ2)
        summ = 0
        # summ2 = 0

    return out_arr

def inverse_FT(N):
    pass




m = [i/10 for i in range(1000)]
Nsin = [np.sin(i) for i in m]
Ncos = [np.cos(i) for i in m]
N = [np.cos(i)*random() for i in m]

# print(N)
#print(FT([5, 2, 4, -1]))

# plt.plot(m, N)
plt.plot(m, Nsin)
plt.plot(m, Ncos)
plt.plot(m, FT(Nsin), '--')
use('tkagg')
plt.show()