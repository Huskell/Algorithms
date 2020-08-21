

def main():
    v, e = map(int, input('Введите через пробел количество вершин и ребер: ').split())
    A = [[0] * (v) for i in range(v)] # создаем матрицу V на V
    for i in range(e):
        a, b = map(int, input('Введите ребро номер ' + str(i) +' из ' + str(e) + ': ').split())
        A[a][b] = 1
        A[b][a] = 1 # Для создания ориентированного графа закомментировать эту сроку

    for i in A:
        print(i)


if __name__ == '__main__':
    main()
