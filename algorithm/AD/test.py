import sys
sys.stdin = open("장군_input.txt")

def bfs():
    global r2, c2

    que = []
    dx = [-3, -3, -2, 2, 3, 3, 2, -2]
    dy = [-2, 2, 3, 3, 2, -2, -3, -3]

    que.append((r1, c1, 0))
    map[r1][r2] = 1
    while que:
        x, y, count = que.pop(0)

        if x == r2 and y == c2:
            return count

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx)
            # print(ny)

            if nx < 0 or nx >= 10 or ny < 0 or ny >= 9:
                continue
            # if map[nx][ny] == 9:
            #     continue
            map[nx][ny] = 1
            que.append((nx, ny, count+1))
    return -1


r1, c1 = map(int, input().split())  # 상 위치
r2, c2 = map(int, input().split())  # 왕 위치
map = [[0 for _ in range(9)] for _ in range(10)]
map[r2][c2] = 9
print(map)

print(bfs())

# print(map)