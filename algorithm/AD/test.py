import sys
sys.stdin = open("장군.txt")

def bfs():
    que = []
    data[r1][c1] = 1
    que.append((r1, c1, 0))

    dr = [-3, -3, -2, 2, 3, 3, 2, -2]
    dc = [-2, 2, 3, 3, 2, -2, -3, -3]
    wall = [[[-1,0], [-2,-1]], [[-1,0], [-2,1]], [[0,1], [-1,2]], [[0,1], [1,2]],
            [[1,0], [2,1]], [[1,0], [2,-1]], [[0,-1], [1,-2]], [[0,-1], [-1,-2]]]
    while que:
        r, c, turn = que.pop(0)

        if r == r2 and c == c2:
            # print('A')
            return turn

        for i in range(8):
            flag = 0
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= 10 or nc < 0 or nc >= 9:
                continue

            # for j in wall[i]:
            #     if r2 == r + j[0] and c2 == c + j[1]:
            #         flag = 1
            # if flag == 0:
            data[nr][nc] = 1
            que.append((nr, nc, turn + 1))

            # # if data[nr][nc] == 0:
            # data[nr][nc] = 1
            # que.append((nr, nc, turn+1))




T = int(input())
for test_case in range(1, T+1):
    r1, c1 = map(int, input().split())  # 상 위치
    r2, c2 = map(int, input().split())  # 왕 위치
    # print(r1, c1)
    # print(r2, c2)
    data = [[0 for _ in range(9)] for _ in range(10)]
    data[r2][c2] = 9
    print(bfs())
