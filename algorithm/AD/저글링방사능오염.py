import sys
sys.stdin = open("저글링방사능오염_input.txt")

def BFS():
    global time
    que = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    que.append((sr, sc, 0))
    data[sr][sc] = 9
    while que:

        # if r = er and c = ec:
        #     return time
        r, c, time = que.pop(0)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= r or nc < 0 or nc >= c:
                continue
            if data[nr][nc] != 1:
                continue
            data[nr][nc] = 9
            que.append((nr, nc, time+1))
    return


c, r = map(int, input().split())
data = [list(map(int, input())) for _ in range(r)]

sc, sr = map(int, input().split())
sc -= 1
sr -= 1
# time = 0
print(BFS())
# print(time)