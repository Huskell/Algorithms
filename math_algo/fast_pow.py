

def pow(a, n):
    assert n >= 0, "степень должна быть больше нуля"

    if n == 0:
        return 1
    else:
        return pow(a, n - 1) * a

def fast_pow(a,n):
    assert n >= 0, "степень должна быть больше нуля"

    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_pow(a * a, n/2)
    else:
        return pow(a, n - 1) * a


print(pow(2, 10))
print(fast_pow(2, 10))
