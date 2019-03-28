def dfs(s):
    global adj, visited, flag, goal, V  # goal:도착노드, V:정점수
    if s == goal :
        flag = 1
        return
    visited[s] = 1

    for i in range(1, V+1):
        if adj[s][i] == 1 and visited[i] == 0:
            dfs(i)

import sys
sys.stdin = open("그래프경로_input.txt")
T = int(input())

for t in range(1, T+1):
    flag = 0
    V, E = map(int, input().split())  # 정점, 간선
    adj = [[0 for i in range(V+1)] for j in range(V+1)]   # 2차원 초기화
    visited = [0 for i in range(V+1)]                     # 방문처리
    for i in range(E):
        s_node, e_node = map(int, input().split()) #시작노드, 끝노드
        adj[s_node][e_node] = 1       #인접행렬

    start, goal = map(int, input(). split())   #출발노드, 도착노드
    dfs(start)

    print("#{} {}".format(t, flag))