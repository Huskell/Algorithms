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
        #print(min)
        N[i], N[n] = N[n], N[i]
        min = N[n]

    return N

print([72, 24, 41, 14, 31, 3, 67, 8, 29, 47])
print(insert_sort([72, 24, 41, 14, 31, 3, 67, 8, 29, 47]))