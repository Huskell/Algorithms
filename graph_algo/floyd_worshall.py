'''
алгоритм обхода графа. Работает с отрицательными весами
работает с матрицами смежности

может определять наличие отрицательных циклов: если по итогу работы алгоритма
есть d[i][i] < 0 то эта вершина входит в такой цикл
'''


def main():
    inf = float('inf')
    G = [[0,   2,   2,   inf, inf],
         [inf, 0,   inf, 2,   2],
         [inf, 2,   0,   inf, inf],
         [inf, inf, inf, 0,   inf],
         [inf, inf, -1,  2,   0]
         ]
    start = int(input('Введите стартовую вершину: '))
    finish = int(input('Введите конечную вершину: '))
    graph, path_matrix = fw(G)
    path = []
    restore_way(path_matrix, start, finish, path)

    print("Исходная матрица")
    print_matr(G)
    print('----------------')
    print("Матрица весов")
    print_matr(graph)
    print('----------------')
    print("Путь: ")
    print(path)
    print('----------------')

def fw(G):
    if len(G[0]) != len(G):
        print("матрица должна быть NxN")
    n = len(G)
    inf = float('inf')
    p = [[0 for _ in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] != inf:
                p[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if G[k][j] > G[k][i] + G[i][j]:
                    G[k][j] = G[k][i] + G[i][j]
                    p[k][j] = p[k][i]

    return G, p

def restore_way(p, start, finish, path):
    path.append(start)
    point = p[start][finish]
    if point == p[finish][finish]:
        path.append(finish)
        return path
    else:
        return restore_way(p, point, finish, path)

def print_matr(M):
    for i in M:
        print(i)

if __name__ == '__main__':
    main()