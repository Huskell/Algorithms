


n = 10
adj_list = [[2, 4, 6],
            [9],
            [0, 3],
            [2, 4],
            [0, 3],
            [],
            [0, 7, 8],
            [6],
            [6],
            [1]]
s = 0 #начало пути

visited = [False] * n  # массив посещенных вершин
# аглоритм прохода в глубину определяет колличество вершин в данном компоненте связности
def dfs(v):
    visited[v] = True
    for w in adj_list[v]:
        if visited[w] == False:  # посещён ли текущий сосед?
            print('w=', w)
            dfs(w)

print(dfs(s))
print(visited)