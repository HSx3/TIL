import sys
sys.stdin = open("최소비용_input.txt")


def Find(x, y):
    visited[x][y] = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    Q = [(x, y)]
    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                if data[nx][ny] > data[x][y]:
                    if visited[nx][ny] > visited[x][y] + 1 + (data[nx][ny] - data[x][y]):
                        visited[nx][ny] = visited[x][y] + 1 + (data[nx][ny] - data[x][y])
                        Q.append((nx, ny))
                else:
                    if visited[nx][ny] > visited[x][y] + 1:
                        visited[nx][ny] = visited[x][y] + 1
                        Q.append((nx, ny))

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    Find(0, 0)
    print("#{} {}".format(test_case+1, visited[N - 1][N - 1]))