import sys
sys.stdin = open("로봇_input.txt")

def BFS():
    dr = (0, 0, 0, 1, -1)
    dc = (0, 1, -1, 0, 0)
    turn = [(0, 0), (4, 3), (3, 4), (1, 2), (2, 1)] # 동서남북 1234별 왼쪽턴 0열, 오른쪽턴 1열
    que = [(sr, sc, sdir, 0)]   # 행, 열, 방향, 명령횟수
    chk[sdir][sr][sc] = 1

    while que:
        r, c, dir, cnt = que.pop(0)     # 현재위치
        if r == er and c == ec and dir == edir:
            return cnt
        
        for i in range(1, 4):   # go 1, 2, 3
            nr = r + dr[dir] * i
            nc = c + dc[dir] * i
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                break
            if arr[nr][nc] == 1:    # 벽이면 break
                break
            if chk[dir][nr][nc]:    # 길이지만 방문했다면 스킵
                continue
            que.append((nr, nc, dir, cnt+1))

        for i in range(2):  # 왼쪽턴 0열, 오른쪽턴 1열
            ndir = turn[dir][i]
            if chk[ndir][r][c]:
                continue
            que.append((r, c, ndir, cnt+1))
            chk[ndir][r][c] = 1


R, C = map(int, input().split())
chk = [[[0]*C for i in range(R)] for j in range(5)]
arr = [list(map(int, input().split())) for _ in range(R)]
sr, sc, sdir = map(int, input().split())
er, ec, edir = map(int, input().split())
sr, sc = sr-1, sc-1
er, ec = er-1, ec-1
sol = BFS()
print(sol)