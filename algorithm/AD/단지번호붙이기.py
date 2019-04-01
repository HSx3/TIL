import sys
sys.stdin = open("단지번호붙이기_input.txt")

def bfs():
    que = []
    que.append((sx, sy))
    count = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while que:
        x, y = que.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if data[nx][ny] != 1:
                continue
            data[nx][ny] = 9
            count += 1
            que.append((nx, ny))
    return count


N = int(input())
data = [list(map(int, input())) for _ in range(N)]

block = 0
for_print = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            sx, sy = i, j
            data[sx][sy] = 9
            answer = bfs()
            block += 1
            for_print.append(answer)
for_print.append(block)
print(for_print.pop())
for_print.sort()
for i in range(0, len(for_print)):
    print(for_print[i])