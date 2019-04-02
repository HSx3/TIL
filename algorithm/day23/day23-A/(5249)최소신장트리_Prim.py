import sys
sys.stdin = open('(5249)최소신장트리_input.txt', 'r')
T = int(input())

def mst():
    global V
    total = 0
    u = 0
    D[u] = 0
    PI[u] = 0

    for i in range(V+1):    # 가중치 최소값 찾기
        min = 0x7fffffff
        for v in range(V+1):
            if visit[v] == 0 and min > D[v]:
                min = D[v]
                u = v

        visit[u] = 1
        total += adj[PI[u]][u]

        for v in range(V+1):    # 인접한 정점 업데이트
            if adj[u][v] != 0 and visit[v] == 0 and adj[u][v] < D[v]:
                D[v] = adj[u][v]
                PI[v] = u

    return total

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    D = [987654321]*(V+1)
    PI = list(range(V+1))
    visit = [0] * (V+1)
    for i in range(E):
        edge = list(map(int, input().split()))
        for j in range(len(edge)):
            adj[edge[0]][edge[1]] = edge[2]
            adj[edge[1]][edge[0]] = edge[2]
    print('#{} {}'.format(tc, mst()))