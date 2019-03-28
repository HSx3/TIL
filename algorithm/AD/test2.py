
import sys
sys.stdin = open('test.txt')

def isWall(x, y):
    if x < 0 or x > N-1: return True
    if y < 0 or y > M-1: return True
    return False

def BFS(x, y):
    global ans, ex, ey
    # 8방향 좌표
    dx = [-3, -3, -2, 2, 3, 3, 2, -2]
    dy = [-2, 2, 3, 3, 2, -2, -3, -2]

    # 상하좌우 방향구현
    direct = [[(-2, -1), (-1, 0)], [(-2, 1), (-1, 0)], [(-1, 2), (0, 1)], [(1, 2), (0, 1)],
              [(2, 1), (1, 0)], [(2, -1), (1, 0)], [(1, -2), (0, -1)], [(-1, -2), (0, -1)]]
    Q = [(x, y, 0)]

    while Q:
        x, y, cnt = Q.pop(0)

        if x == ex and y == ey:
            ans = cnt
            return 1

        for i in range(8):
            rex = x + dx[i]
            rey = y + dy[i]

            chk = 0
            if not isWall(rex, rey):
                for j in range(2):
                    if data[x + direct[i][j][0]][y + direct[i][j][1]] == 1:
                        chk = 1

                if chk == 0:
                    Q.append((rex, rey, cnt + 1))

N, M = 10, 9
data = [[0]*M for _ in range(N)]

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

data[ex][ey] = 1
ans = 0

if BFS(sx, sy):
    print(ans)
else:
    print(-1)