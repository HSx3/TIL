import sys
sys.stdin = open("토마토(고)_input.txt")

def BFS():
    que = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    zero = 0    # 0의 개수

    for i in range(R):
        for j in range(C):
            if data[i][j] == 1:
                que.append((i, j, 0))
            elif data[i][j] == 0:
                zero += 1
    if zero == 0:
        return 0

    while que:
        r, c, days = que.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if data[nr][nc] == 0:
                data[nr][nc] = 1
                que.append((nr, nc, days+1))
                zero -= 1
    if zero:
        return -1
    else:
        return days



C, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(R)]
print(BFS())