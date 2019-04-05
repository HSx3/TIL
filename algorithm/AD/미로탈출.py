import sys
sys.stdin = open("미로탈출_input.txt")

# r, c, bomb, distance
def BFS():
    global flag
    que = []
    que.append((sr, sc, 3, 0))
    visited[3][sr][sc] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while que:
        r, c, bomb, distance = que.pop(0)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if visited[bomb][nr][nc]:
                continue
            if arr[nr][nc] == 1:
                continue

            if bomb > 0 and arr[nr][nc] == 2:
                que.append((nr, nc, bomb-1, distance+1))
                visited[bomb-1][nr][nc] = 1

            if arr[nr][nc] == 0:
                que.append((nr, nc, bomb, distance+1))
                visited[bomb][nr][nc] = 1

            if arr[nr][nc] == 4:
                flag = 1
                return distance+1


R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(4)]
flag = 0
for i in range(1, R-1):
    for j in range(1, C-1):
        if arr[i][j] == 3:
            sr, sc = i, j
            answer = BFS()
            break
if flag:
    print(answer)
else:
    print(-1)