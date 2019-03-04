def bfs(v):
    global G, visited, V
    queue=[]

    queue.append(v)
    visited[v] = 1

    while len(queue) != 0:
        v = queue.pop(0)
        for w in range(V+1):
            if G[v][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[v] + 1

import sys
sys.stdin = open("(1238)Contact_input.txt")
T = 10
V = 100
for tc in range(T):
    E, start = map(int, input().split())
    temp = list(map(int, input().split()))

    G = [[0 for i in range(V+1)] for j in range(V+1)]   #2차원 초기화
    visited = [0 for i in range(V+1)]

    for i in range(0, len(temp), 2):  #입력
        G[temp[i]][temp[i+1]] = 1

    # for i in range(V+1):  #입력확인
    #     print("{} {}".format(i, G[i]))

    bfs(start)
    maxI = 0
    for i in range(V+1):
        if visited[maxI] <= visited[i]:
            maxI = i
    print(f"#{tc+1} {maxI}")

