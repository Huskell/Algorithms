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
    d, p = {}, {} # массив длинн, массив предков
    while search_q: # пока не пусто
        point = search_q.popleft()
        print('piont = ', point)
        if not point in searched: # проверка на посещенность
            if point == m:
                return True
                # print_way(m)
            else:
                search_q += G.get(point)
                searched.append(point)
                print('searched = ', searched)

    return False

def print_way():
    pass # TODO сделать восстановление кратчайшего пути


print(bfs(0,7))