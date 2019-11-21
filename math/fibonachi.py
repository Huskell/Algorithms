
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


print(fib(8))
print(fib_list(8))
