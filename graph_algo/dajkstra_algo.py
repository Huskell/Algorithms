
from collections import deque

def main():
    G = read_graph()
    start = int(input('start vertex = '))
    while start not in G:
        start = input('start vertex = ')

    shortest_distances, parents = dijkstra(G, start)
    print(shortest_distances)
    finish = int(input('finish vertex = '))
    shortest_path = reveal_shortest_path(start, finish, parents)
    print(shortest_path)

def read_graph():
    M = int(input('Сколько ребер в графе?: '))
    G = {}
    print('Введите ребра: \n')
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
        a, b = int(a), int(b)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)
    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

def dijkstra(G, start):
    q = deque()
    s = {}
    s[start] = 0
    q.append(start)
    parents = [None] * len(G)
    while q:
        v = q.popleft()
        for u in G[v]:
            if (u not in s) or s[v] + G[v][u] < s[u]:
                s[u] = s[v] + G[v][u]
                parents[u] = v
                q.append(u)

    return s, parents

def reveal_shortest_path(start, finish, parents):
    path = [finish]
    parent = parents[finish]
    while not parent is start:
        path.append(parent)
        parent = parents[parent]
    path.append(start)
    return path[::-1]

if __name__ == '__main__':
    main()
''' граф. первое число - число ребер
9
0 1 5
0 2 2
1 3 4
1 4 2
2 1 8
2 4 7
3 4 6
3 5 3
4 5 1
'''