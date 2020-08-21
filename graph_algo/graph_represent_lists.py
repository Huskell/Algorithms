


def main():
    v, e = map(int, input('Введите через пробел количество вершин и ребер: ').split()) # вводим кол-во вершин и ребер
    graph = {i: set() for i in range(v)} # создаем пустой массив графа
    for i in range(e):
         v1, v2 = map(int, input('Введите ребро номер ' + str(i + 1) +' из ' + str(e) + ': ').split())
         graph[v1].add(v2) # если использовать две строки то получим неориентированный граф
         graph[v2].add(v1) # с одной строкой - ориентированный

    for i in graph.keys():
        print(i, ':', graph[i])


if __name__ == '__main__':
    main()
