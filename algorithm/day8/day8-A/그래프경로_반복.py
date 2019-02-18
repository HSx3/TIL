def dfs(s):
    global adj, visited, flag, goal, V # goal:도착노드, V:정점수
    stack = []
    stack.append(s)  #push

    while len(stack) != 0:
        node = stack.pop()
        if node == goal: #도착점 찾음
            return 1
        if not visited[node]:
            visited[node] = 1
            for w in range(1, V+1):
                if adj[node][w] == 1 and visited[w] == 0:
                    stack.append(w)
    return 0

import sys
sys.stdin = open("그래프경로_input.txt")
T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())  # 정점, 간선
    adj = [[0 for i in range(V+1)] for j in range(V+1)]   # 2차원 초기화
    visited = [0 for i in range(V+1)]                     # 방문처리

    for i in range(E):
        s_node, e_node = map(int, input().split()) #시작노드, 끝노드
        adj[s_node][e_node] = 1       #인접행렬:방향성 있음

    start, goal = map(int, input(). split())   #출발노드, 도착노드

    print("#{} {}".format(t, dfs(start)))