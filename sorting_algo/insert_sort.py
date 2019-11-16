from random import randint

N2 = [randint(0,100) for _ in range(15)]

def insert_sort(N):

    for i in range(1, len(N)):
        currentValue = N[i]
        pos = i
        while pos > 0 and N[pos-1] > currentValue:
            N[pos] = N[pos-1]
            pos = pos - 1
        N[pos] = currentValue
    return N

print(N2)
print(insert_sort(N2))

