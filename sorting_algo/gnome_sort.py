from random import randint

def gnome_sort(array):
    i = 1
    while i < len(array):
        if array[i-1] <= array[i]:
            i += 1
        else:
            array[i-1], array[i] = array[i], array[i-1]
            if i > 1:
                i -= 1

a = [randint(0, 100) for _ in range(10)]
print(gnome_sort(a))