import sys
sys.stdin = open("자외선피해가기_input.txt")

def BFS():
    que = []
    que.append((0, 0))
    rec[0][0] = arr[0][0]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while que:
        r, c = que.pop(0)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 가 볼 위치의 이전의 해 > 현재진행경로의 해 비교하여 최소이면
            if rec[nr][nc] > rec[r][c] + arr[nr][nc]:
                rec[nr][nc] = rec[r][c] + arr[nr][nc]
                que.append((nr, nc))
    return rec[N-1][N-1]
N = int(input())
arr = []
rec = [[1000000]*N for _ in range(N)]   # 자외선 합 기록
for i in range(N):
    arr.append(list(map(int, input())))

sol = 10 * 100 * 100
rec[0][0] = 0   # 시작점 값 기록
# DFS(0, 0)
sol = BFS()
print(sol)