
def fib(n):
    assert n >=0, 'Требуется положительное число n'

    a = 0
    b = 1
    i = 0
    if n <=1:
        return 1
    while i <= n:
        a, b = a + b, a
        i += 1

    return a

print(fib(5))
