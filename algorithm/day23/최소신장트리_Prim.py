import sys
sys.stdin = open("최소 신장 트리_input.txt")




def Prim(V, r):
    D = [9876543210] * (V + 1)
    P = [-1] * (V + 1)
    visited = [0] * (V + 1)
    D[r] = 0
    answer = 0
    for _ in range(V + 1):
        minindex = -1
        min = 9876543210

        for i in range(V + 1):
            if not visited[i] and D[i] < min:
                min = D[i]
                minindex = i
        visited[minindex] = 1
        answer += D[minindex]

        for i in range(V + 1):
            if not visited[i] and graph[minindex][i] != 0 and graph[minindex][i] < D[i]:
                D[i] = graph[minindex][i]
                P[i] = minindex
    return answer

T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(E)]  # 시작, 끝, 가중치
    graph = [[0]*(V+1) for i in range(V+1)]

    for i in range(E):
        graph[data[i][0]][data[i][1]] = data[i][2]
        graph[data[i][1]][data[i][0]] = data[i][2]

    print("#{} {}".format(test_case+1, Prim(V, 0)))