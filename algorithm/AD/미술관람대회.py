import sys
sys.stdin = open("미술관람대회_input.txt")

def bfs(sx, sy):
    global check, sector
    que = []
    data[sx][sy] = sector
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
            data[nx][ny] = sector
            que.append((nx, ny))
    return sector

def bfs2(sx, sy):
    global check, sector2
    que = []
    data[sx][sy] = sector
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
            data[nx][ny] = sector
            que.append((nx, ny))
    return sector


N = int(input())
data = [list(map(str, input())) for _ in range(N)]
temp = data
print(data)
sector = 1
sector2 = 1
check_number = list(range(1, 61))
for_check = []
for i in range(N):
    for j in range(N):
        if data[i][j] not in check_number:
            check = data[i][j]
            sx, sy = i, j
            answer = bfs(sx, sy)
            # answer2 = bfs2(sx, sy)
            sector += 1
print(answer)
print(data)