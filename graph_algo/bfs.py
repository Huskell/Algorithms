from collections import deque

G = {0: [1, 6],
     1: [2, 3],
     2: [1],
     3: [1, 4],
     4: [3, 5],
     5: [4, 6],
     6: [5, 0]
     }

n = len(G.keys())
print(n)

# аглоритм прохода в ширину определяет есть ли из искомой вершины путь к нужной
# и какой путь короче(для невзвешенных графов)
def bfs(v, m):
    search_q = deque()  # двух сторонняя очередь
    search_q += G.get(v) #добавляем стартовую точку
    searched = [] # список для фиксации посещенных
    while search_q: # пока не пусто
        point = search_q.popleft()
        print('piont = ', point)
        if not point in searched: # проверка на посещенность
            if point == m:
                return True
            else:
                search_q += G.get(point)
                searched.append(point)
                print('searched = ', searched)

    return False

print(bfs(0,7))

def bfs_with_dist(start, g):
    distances = [None] * len(G)
    distances[start] = 0
    q = deque([start])
    while q:
        cur_v = q.popleft()
        for i in G[cur_v]:
            if distances[i] is None:
                distances[i] = distances[cur_v] + 1
                q.append(i)
    return distances

print('-----------------')
print(bfs_with_dist(0,G))
