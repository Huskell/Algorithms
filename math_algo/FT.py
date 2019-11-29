from random import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import use

class window:
    def __init__(self):
        self.queue = [0 for _ in range(80)]

    def push(self, element):
        self.queue.pop(0)
        self.queue.insert(-1, element)

    def get(self):
        return self.queue

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
        out_arr.append(abs(summ))
        # out_arr2.append(summ2)
        summ = 0
        # summ2 = 0

    return out_arr

def inverse_FT(arr):
    size_array = len(arr)
    out_arr = []
    summ = 0
    for i in range(79,size_array):
        for k in range(size_array):
            for n in range(size_array):
                # summ = summ + (arr[n] * np.exp(-1j * (2 * np.pi / size_array) * n * k))
                summ = summ + (arr[n]*(np.cos((2*np.pi/size_array)*n*k) + 1j*np.sin((2*np.pi/size_array)*n*k)))
            summ = summ/size_array
            out_arr.append(summ)
            summ = 0
    return arr




m = [i/1 for i in range(100)]
Nsin = [np.sin(2*np.pi*50 + i) for i in m]
Ncos = [np.cos(2*np.pi*50 + i) for i in m]
# N = [np.cos(i)*random() for i in m]

# print(N)
#print(FT([5, 2, 4, -1]))

# plt.plot(m, N)
plt.plot(m, Nsin)
# plt.plot(m, Ncos)
plt.plot(m, FT(Nsin), '--')
plt.plot(m,np.fft.fft(Nsin), '--')
# plt.plot(m,'-o')
use('tkagg')
plt.show()