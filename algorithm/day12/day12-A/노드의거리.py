def bfs(v):
    global goal
    Q = []
    Q.append(v)
    visited[v] = 1
    while len(Q) != 0:
        t = Q.pop(0)
        if t == goal:
            return visited[t] - 1  # 출발지가 1부터 시작하므로 1을 빼줌

        for w in range(1, V + 1):
            if adj[t][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[t] + 1 # 거리 누적

    return 0  # 경로가 없는 경우

import sys
sys.stdin = open('노드의거리_input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # 정점, 간선
    adj = [[0 for i in range(V + 1)] for j in range(V + 1)]  # 2차원 초기화
    visited = [0 for i in range(V + 1)]  # 방문처리
    for i in range(E):
        s_node, e_node = map(int, input().split())  # 시작노드, 끝노드
        adj[s_node][e_node] = 1  # 인접행렬
        adj[e_node][s_node] = 1  # 방향성이 없음

    start, goal = map(int, input().split())  # 출발노드, 도착노드

    print("#{} {}".format(tc, bfs(start)))
