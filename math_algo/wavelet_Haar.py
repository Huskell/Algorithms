import math as m
import matplotlib.pyplot as plt

class window:
    def __init__(self):
        self.queue = [0 for _ in range(64)]

    def push(self, element):
        self.queue.pop(0)
        self.queue.append(element)

    def get(self):
        return self.queue


def haar(signal): # раскладываем сигнал сигнал

    N = len(signal)
    A = {}
    D = {}
    a = st(signal)
    for j in range(a):
        A[j] = []
        D[j] = []
        for i in range(0, N, 2):
            A[j].append((signal[i] + signal[i + 1])/2)
            D[j].append((signal[i] - signal[i + 1])/2)
        N = N >> 1

    return A, D

def inverseHaar(A, D): # восстанавливаем сигнал

    n = len(A)-1
    A_invers = {}
    D_invers = {}
    for i in range(n, -1, -1):
        A_invers[i] = []
        D_invers[i] = []
        for j in range(len(A[i])):
            A_invers[i].append(A[i][j] + 0)
            A_invers[i].append(A[i][j] - 0)
    return A_invers



def st(number): # вычисляем степень 2
    num = len(number)
    count = 1
    while num/2 != 1:
        if num % 2 != 0:
            break
        num //= 2
        count +=1
    return count

def dd(inv):  # вычисляем действующее значение тока
    win = window()
    # inv = inv[0]
    direct = 0
    dd = []
    period = 64
    d = len(inv)
    for i in range(len(inv)):
        win.push(inv[i])
        for j in range(period):
            direct += (win.get()[j]) ** 2
        direct = (direct / period) ** (1 / 2)
        dd.append(direct)

    return dd

def main():
    d = 128
    n = [i for i in range(d)]
    s = [m.sin((2 * m.pi / 64) * i) for i in range(d)]
    s2 = [2 * m.sin((2 * m.pi / 64) * i) for i in range(d)]
    # s2 = [2 * m.sin(2 * m.pi * 50 + i / 10) for i in range(d)]
    # s3 = s[:128] + s2[128:]
    A, D = haar(s)
    # print(D)
    for i in range(len(D)):
        print(A[i])
    inv = inverseHaar(A, D)
    # direct = dd(inv)
    direct = dd(s)

    # plt.plot(n, s)
    # plt.plot(n, s2)
    plt.plot(n, s)

    # plt.plot(n, inv[0])
    plt.plot(n, direct)
    plt.show()

    n = [i for i in range(d//2)]
    plt.plot(n, A[0])
    plt.show()
    n = [i for i in range(d//4)]
    plt.plot(n, A[1])
    plt.show()
    n = [i for i in range(d//8)]
    plt.plot(n, A[2])
    plt.show()
    n = [i for i in range(d//16)]
    plt.plot(n, A[3])
    plt.show()
    n = [i for i in range(d//32)]
    plt.plot(n, A[4])
    plt.show()
    n = [i for i in range(d//64)]
    plt.plot(n, A[5])
    plt.show()
    n = [i for i in range(2)]
    plt.plot(n, A[6])
    plt.show()
if __name__ == '__main__':
    main()


