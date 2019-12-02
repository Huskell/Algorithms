from random import randint, choice

N = [i for i in range(10)]

def simple_bt(arr):

    largest = i
    l = 2*i + 1
    r = 2*i + 2
        # print('larg = ', largest, self.heaplist[largest])
        # print('l = ', l, self.heaplist[l])
        # print('r = ', r, self.heaplist[r])
    if l < heapsize and self.heaplist[l] > self.heaplist[i]:
        largest = l
    if r < heapsize and heaplist[r] > heaplist[largest]:
        largest = r
    if largest != i:
        heaplist[i], heaplist[largest] = heaplist[largest], heaplist[i]





print(N)
print(simple_bt(N))
