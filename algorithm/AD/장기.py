import sys
sys.stdin = open("장기_input.txt")

def bfs():
    que = []
    que.append((R, C, 0))
    data[R][C] = 1

    dr = [-2, -2, -1, 1, 2, 2, 1, -1]
    dc = [-1, 1, 2, 2, 1, -1, -2, -2]

    while que:
        r, c, turn = que.pop(0)

        if r == S and c == K:
            return turn

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if data[nr][nc] == 1:
                continue
            data[nr][nc] = 1
            que.append((nr, nc, turn+1))

N, M = map(int, input().split())
R, C, S, K = map(int, input().split())
R -= 1
C -= 1
S -= 1
K -= 1

data = [[0 for _ in range(M)] for _ in range(N)]
print(bfs())