import numpy as np
from numpy import linalg



def fib(n):
    assert n >=0, 'Требуется положительное число n'

    a = 0
    b = 1
    i = 0
    if n <=1:
        return 1
    while i <= n-1:
        a, b = a + b, a
        i += 1
    return a

def fib_list(n):

    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    return f

def fib_rec(n):

    if n < 2:
        return n

    return fib_rec(n - 1) + fib_rec(n - 2)

def fib_matrix(n):

    mat = np.array([[1, 1], [1, 0]], dtype=object)
    number = linalg.matrix_power(mat,n-1)

    return number[0, 0]



print(fib(41))
print(fib_list(41))
print(fib_rec(41))
print(fib_matrix(41))
