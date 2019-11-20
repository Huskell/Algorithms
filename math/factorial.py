

def facorial(N):
    assert N >= 0, "Факториал отрицательного числа неопределен"
    if N == 0 or N == 1:
        return 1

    return facorial(N-1)*N

print(facorial(-1))