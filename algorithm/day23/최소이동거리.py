import sys

sys.stdin = open("최소이동거리_input.txt")


def Dijkstra(G, r):
    D = [9876543210] * (N + 1)
    P = [-1] * (N + 1)
    visited = [0] * (N + 1)
    D[r] = 0

    for _ in range(N + 1):
        minindex = -1
        min = 9876543210

        for i in range(N + 1):
            if not visited[i] and D[i] < min:
                min = D[i]
                minindex = i
        visited[minindex] = 1

        for i in range(N + 1):
            if not visited[i] and graph[minindex][i] != 0 and D[minindex] + graph[minindex][i] < D[i]:
                D[i] = D[minindex] + graph[minindex][i]
                P[i] = minindex
    return D[N]



T = int(input())
for test_case in range(T):
    N, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(E):
        graph[data[i][0]][data[i][1]] = data[i][2]
    print("#{} {}".format(test_case+1, Dijkstra(N, 0)))