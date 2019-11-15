from random import randint

N= [randint(0, 100) for _ in range(10)]

def insert_sort(N):
    min = N[0]
    for i in range(len(N)):
        # определение минимального элемента последовательности
        for j in range(i, len(N)):
            if N[j] < min:
                min = N[j]
                n = j
        N[i], N[n] = N[n], N[i]
        min = N[n]
    return N

print('N=',N)
print('N=', insert_sort(N))

N = [randint(0, 100) for _ in range(10)]
#======================================================
#=========with recursion===============================
#======================================================
def insert_sort(N, M = 0):
    min = N[M]
    n = M
    if len(N) - M == 1:
        return N
    # for i in range(M,len(N)):
    #     # определение минимального элемента последовательности
    for j in range(M, len(N)):
        if N[j] < min:
            min = N[j]
            n = j
    N[M], N[n] = N[n], N[M]
    min = N[n]
    #print(N)
    return insert_sort(N,M+1)

print('N2=',N)
print('N2=',insert_sort(N))