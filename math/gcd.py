

def simple_gcd(a, b):

    if a == b:
        return a
    if a > b:
        return simple_gcd(a -b , b)
    if a < b:
        return simple_gcd(a, b - a)

def gcd(a, b):

    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(simple_gcd(400, 72))
print(gcd(400, 72))

