import sys
sys.stdin = open('(5251)최소이동거리_input.txt', 'r')
T = int(input())

def getMinIdx():
    minV = 999999  #
    minIdx = 0
    for i in range(N + 1):  # 방문 안 한 노드 중 D가 최소인 노드 찾기
        if visit[i] == 0 and D[i] < minV:
            minIdx = i
            minV = D[i]
    return minIdx

def dijkstra (goal):
    D[0] = 0  # 출발점의 가중치
    
    for i in range(N+1):
        if adj[0][i]:   # 출발점과 인접한 노드
            D[i] = adj[0][i]  # D 초기화
    visit[0] = 1        # 시작노드

    while True:
        node = getMinIdx()
        visit[node] = 1     # D가 가장 작은 노드 방문처리
        if node == goal:    # 도착지에 도착하면
            return D[goal]

        for x in range(N+1):
            if adj[node][x]:  # minIdx에 인접인 노드에 대해
                if D[x] > (D[node] + adj[node][x]):     # minIdx를 경유하는 비용이 더 작으면
                    D[x] = D[node] + adj[node][x]       # D[x] 갱신

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visit = [0] * (N + 1)  # 방문처리
    D = [99999999] * (N + 1)  # 0번 부터의 거리(가중치)

    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w  # 방향성 있음
    print('#{} {}'.format(tc, dijkstra (N)))
