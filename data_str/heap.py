

class bin_heap:
    def __init__(self):
        self.heapsize = 0
        self.heaplist = [0]

    def heapify(self, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < self.heapsize and self.heaplist[l] > self.heaplist[i]:
            largest = l
        if r < self.heapsize and self.heaplist[r] > self.heaplist[largest]:
            largest = r
        if largest != i:
            self.heaplist[i], self.heaplist[largest] = self.heaplist[largest], self.heaplist[i]
            self.heapify(largest)

    def buildHeap(self, list):
        self.heaplist = list
        self.heapsize = len(list)
        # Индексы  c середины и до нуля включительно
        for i in range(len(list) // 2, -1, -1):
            self.heapify(i)

        return self.heaplist
