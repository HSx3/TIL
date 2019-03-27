import sys
sys.stdin = open("사냥꾼_input.txt")

def hunting(x, y):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    count = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        while True:
            if nx < 0 or nx >= N:
                break
            if ny < 0 or ny >= N:
                break
            if data[nx][ny] == 3:
                break
            if data[nx][ny] == 1:
                break
            if data[nx][ny] == 0:
                nx += dx[i]
                ny += dy[i]
                continue
            if data[nx][ny] == 2:
                count += 1
                nx += dx[i]
                ny += dy[i]
    return count

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)
    rabbit = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                rabbit += hunting(i, j)
    print('#{} {}'.format(test_case, rabbit))