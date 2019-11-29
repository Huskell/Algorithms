import math as m
import matplotlib.pyplot as plt


def haar(signal): # раскладываем сигнал сигнал

    N = len(signal)
    A = {}
    D = {}
    a = st(signal)
    for j in range(a):
        A[j] = []
        D[j] = []
        for i in range(0, N, 2):
            A[j].append((signal[i]+signal[i + 1])/2)
            D[j].append((signal[i]-signal[i + 1])/2)
        N //= 2

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
    direct = 0
    d = len(inv[0])
    for i in range(d):
        direct += (inv[0][i]) ** 2
    direct /= d
    direct = direct ** 1 / 2
    dd = [direct for _ in range(d)]

    return dd

def main():
    d = 256
    n = [i for i in range(d)]
    s = [m.sin(2 * m.pi * 50 + i / 10) for i in range(d)]
    s2 = [2 * m.sin(2 * m.pi * 50 + i / 10) for i in range(d)]
    s3 = s[:128] + s2[128:]
    A, D = haar(s3)
    # print(D)
    for i in range(len(D)):
        print(D[i])
    inv = inverseHaar(A, D)
    direct = dd(inv)

    # plt.plot(n, s)
    # plt.plot(n, s2)
    plt.plot(n, s3)
    plt.plot(n, inv[0])
    plt.plot(n, direct)
    plt.show()

if __name__ == '__main__':
    main()
