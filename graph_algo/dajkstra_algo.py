
from collections import deque

def main():
    G = read_graph()
    start = input('start =')
    while start not in G:
        start = input('start =')

    shortest_distances = dijkstra(G, start)
    finish = input('what are way you need?: ')

    shortest_path = reveal_shortest_path(start, finish, shortest_distances)

def read_graph():
    M = int(input())
    G = {}
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
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
    while q:
        v = q.popleft()
        for u in G[v]:
            if (u not in s) or s[v] + G[v][u] < s[u]:
                s[u] = s[v] + G[v][u]
                q.append(u)
    return s











if __name__ == '__main__':
    main()