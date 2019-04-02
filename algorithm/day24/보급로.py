import sys
sys.stdin = open("보급로_input.txt")

def bfs():
    que = []
    que.append((0, 0))
    visited[0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while que:
        x, y = que.pop(0)

        # if x == N-1 and y == N-1:
        #     return time

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] > visited[x][y] + data[x][y]:
                visited[nx][ny] = visited[x][y] + data[x][y]
                # que.append((nx, ny, visited[x][y] + data[x][y]))
                que.append((nx, ny))

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    visited = [[0xffffff]*N for _ in range(N)]
    # print(visited)
    total = []
    bfs()
    print('#{} {}'.format(test_case, visited[N-1][N-1]-1))