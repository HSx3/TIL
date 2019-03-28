import sys
sys.stdin = open("저글링방사능오염_input.txt")

def BFS():
    que = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    que.append((sr, sc, 3))
    data[sr][sc] = 0
    while que:
        r, c, time = que.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if data[nr][nc] == 1:
                data[nr][nc] = 0
                que.append((nr, nc, time+1))
    return time # 큐가 빈상태(더이상 없앨 저글링이 없는 경우)


C, R = map(int, input().split())
data = [list(map(int, input())) for _ in range(R)]

sc, sr = map(int, input().split())
sc -= 1
sr -= 1
print(BFS())
count = 0
for i in range(R):
    for j in range(C):
        if data[i][j] == 1:
            count += 1
print(count)