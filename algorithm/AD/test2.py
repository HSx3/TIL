import sys
sys.stdin = open("input.txt")

def DFS(x, y):
    global flag

    if flag:
        return

    data[x][y] = 9
    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    if x == 0:
        flag = y
        return

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= 100 or ny < 0 or ny >= 100:
            continue
        if data[nx][ny] == 0:
            continue
        if data[nx][ny] == 9:
            continue

        if data[nx][ny] == 1:
            data[nx][ny] = 9
            DFS(nx, ny)

T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    # print(data)
    flag = 0
    for i in range(100):
        if data[99][i] == 2:
            sx, sy = 99, i
            DFS(sx, sy)
            print('#{} {}'.format(test_case, flag))