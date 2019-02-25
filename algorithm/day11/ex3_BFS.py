def BFS(G, v):
    global n
    visited = [0]*n
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            print(t, end = ' ')
        for i in range(len(G[t])):
            if G[t][i] == 1 and visited[i] == 0:
                queue.append(i)
        # print(queue)

N = 7
n = N + 1
temp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

G = [[0 for i in range(n)] for j in range(n)]

for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

BFS(G, 1)

#################################
# import sys
# sys.stdin = open("ex3_input.txt")
#
# V, E = map(int, input().split())
# V += 1
# temp = list(map(int, input().split()))
#
# G = [[0 for i in range(V)] for j in range(V)] # 2차원 초기화
# visited = [0 for i in range(V)]
#
# for i in range(0, len(temp), 2): # 입력
#     G[temp[i]][temp[i+1]] = 1
#     G[temp[i+1]][temp[i]] = 1
#
# for i in range(V): # 입력확인
#     print("{} {}".format(i, G[i]))
#
# def bfs(v):
#     global G, V
#     visited = [0] * (V+1)
#     queue = []
#     queue.append(v)
#     while len(queue) != 0:
#         v = queue.pop(0)
#         if not visited[v]:
#             visited[v] = 1
#             print(v, end=" ")
#             for w in range(V+1):
#                 if G[v][w] == 1 and visited[w] == 0:
#                     queue.append(w)
#
# bfs(1)