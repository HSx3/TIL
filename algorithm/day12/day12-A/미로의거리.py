def bfs(x, y):
    global N, maze, visited
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []
    q.append((x, y))            #리스트로 큐 구현, 좌표는 튜플로 저장
    visited[x][y] = 1           #방문 표시
    while len(q) != 0:
        x, y = q.pop(0)         #deQ
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny == N: continue
            if nx < 0 or nx == N: continue
            if maze[nx][ny] == 3 :                  # 출구인 경우 지나온 칸 반환
                return visited[x][y] - 1      # 출발지는 칸 수에서 제외
            elif maze[nx][ny] == 0 and visited[nx][ny] == 0: # 갈수 있는 곳 저장
                q.append([nx, ny]) # enQ
                visited[nx][ny] = visited[x][y] + 1
    return 0  # 출구에 가지 못하고 모든 칸 방문

import sys
sys.stdin = open("미로의거리_input.txt","r")
T = int(input())
for tc in range(T):
    N = int(input())
    maze = [[int(x) for x in input()]for i in range(N)] # 미로를 중첩리스트로 저장
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):  #출발점 찾기
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j
    print('#{} {}'.format(tc+1, bfs(x, y)))