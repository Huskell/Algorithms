from random import randint


N = [randint(0, 100) for _ in range(10)]

def merge_sort(N):
    if len(N) > 1:
        mid = len(N)//2 # определяем середину листа
        right = N[mid:] # разрезаем на половины
        left = N[:mid]

        merge_sort(right)   # рекурсивно продолжаем разбивать до Len(list) = 1
        merge_sort(left)

        i, j, k = 0, 0, 0
        while i < len(right) and j < len(left):  # начинаем объединять половины в один лист
            if left[j] > right[i]:
                N[k] = right[i]
                i += 1
            else:
                N[k] = left[j]
                j += 1
            k += 1

        while i < len(right): # добавляем остатки листа в конец списка
            N[k] = right[i]
            i += 1
            k += 1

        while j < len(left): # добавляем остатки листа в конец списка
            N[k] = left[j]
            j += 1
            k += 1

    return N

print(N)
print(merge_sort(N))
