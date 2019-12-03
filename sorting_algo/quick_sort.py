from random import randint, choice

# N = [randint(0, 100) for i in range(10)]

def quick_sort(N):

    if len(N) <= 1:
        return N

    q = choice(N)
    left, mid, right = [], [], []

    for n in N:
        if n > q:
            right.append(n)
        elif n < q:
            left.append(n)
        else:
            mid.append(n)
    return quick_sort(left) + mid + quick_sort(right)

# print(N)
# print(quick_sort(N))

