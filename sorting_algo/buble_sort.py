from random import random

N = [ i*random() for i in range(40)]

def buble_sort(N):
    M = len(N)
    for i in range(M-1):
        for j in range(M-i-1):
            if N[j] > N[j+1]:
                N[j], N[j+1] = N[j+1], N[j]
    return N

#print(buble_sort(N))
#=================================================================
#=============with recursion======================================
#=================================================================

def buble_recursion(N,M):

    if M == 1:
        return N
    for j in range(M-1):
        if N[j] > N[j + 1]:
            N[j], N[j + 1] = N[j + 1], N[j]
    return buble_recursion(N,M-1) # отправляя функцию через return в рекурсию мы получим искомый N, а иначе нас ждет None
print(buble_recursion(N,len(N)))