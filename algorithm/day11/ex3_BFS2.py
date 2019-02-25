def bfs(v): # 1에서 가장 멀리 있는 정점을 찾으시오.
    global G, V
    queue = []
    queue.append(v)
    visited[v] = 1
    print(v, end=" ")
    while len(queue) != 0:
        t = queue.pop(0)
        for w in range(1, V+1):
            if G[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
                print(w, end=" ")

N = 7
n = N + 1
temp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

G = [[0 for i in range(n)] for j in range(n)]

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1