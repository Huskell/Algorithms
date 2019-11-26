
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

s = 0 #начало пути

visited = [False] * n  # массив посещенных вершин
# аглоритм прохода в глубину определяет колличество вершин в данном компоненте связности
def dfs(v):
    visited[v] = True
    print('visit = ', v)
    print('G = ', G.get(v))
    for w in G.get(v):
        print('w = ', w)
        if visited[w] == False:  # посещён ли текущий сосед?
            print('w=', w)
            dfs(w)

print(dfs(s))
print(visited)