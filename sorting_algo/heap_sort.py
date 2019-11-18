from random import randint
from data_str.heap import bin_heap

N = [randint(0,100) for _ in range(10)]

def heap_sort(N):
    m = len(N)
    arr2 = []
    while m > 0:
        arr = bin_heap().buildHeap(N)
        max = arr[0]
        arr[0] = 0
        arr2.append(max)

        m -= 1
    return arr2



print(N)
print(heap_sort(N))
