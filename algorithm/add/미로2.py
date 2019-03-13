import sys
sys.stdin = open("미로2_input.txt")

def maze(sx, sy):
    global SIZE, visited
    nx, ny = 0, 0
    q = []
    q.append((sx, sy))
    visited[sx][sy] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while len(q) != 0:
        sx, sy = q.pop(0)

        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]

            # if nx < 0 or nx >= SIZE:
            #     continue
            # if ny < 0 or ny >= SIZE:
            #     continue
            # if data[nx][ny] == 1:
            #     continue
            if visited[nx][ny] == 1:
                continue
            if data[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
            if data[nx][ny] == 3:
                return 1
    return 0

T = 10
for test_case in range(1, T+1):
    N = int(input())
    SIZE = 100
    data = [list(map(int, input())) for _ in range(SIZE)]
    visited = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

    sx, sy = 0, 0
    for i in range(SIZE):
        for j in range(SIZE):
            if data[i][j] == 2:
                sx, sy = i, j
                break
    # maze(sx, sy)
    print('#{} {}'.format(test_case, maze(sx, sy)))