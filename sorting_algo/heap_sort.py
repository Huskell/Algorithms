from random import randint
from data_str.heap import bin_heap

N = [randint(0,100) for _ in range(10000)]

def heap_sort(N):
    m = len(N)
    arr2 = []
    while m > 0:
        arr = bin_heap().buildHeap(N)
        arr2.append(arr.pop(0))
        m -= 1
    return arr2



print(N)
print(heap_sort(N))
