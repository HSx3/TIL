import sys
sys.stdin = open("미술관람대회.txt")

def bfs(sx, sy):
    global check, sector, visited
    que = []
    visited[sx][sy] = sector
    que.append((sx, sy))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while que:
        x, y = que.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if data[nx][ny] != check:
                continue
            if data[nx][ny] == check and visited[nx][ny] == 0:
                visited[nx][ny] = sector
                que.append((nx, ny))
    return sector


N = int(input())
data = [list(map(str, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
sector = 1
check_number = list(range(1, 61))
for i in range(N):
    for j in range(N):
        if visited[i][j] not in check_number:
            check = data[i][j]
            sx, sy = i, j
            answer = bfs(sx, sy)
            sector += 1
print(answer, end=' ')
sector = 1
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if data[i][j] == 'G':
            data[i][j] = 'R'
# print(data)
for i in range(N):
    for j in range(N):
        if visited[i][j] not in check_number:
            check = data[i][j]
            sx, sy = i, j
            answer2 = bfs(sx, sy)
            sector += 1
print(answer2)