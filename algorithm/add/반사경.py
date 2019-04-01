import sys
sys.stdin = open("반사경_input.txt")

def go(bx, by):
    count = 0
    dx = [0]
    dy = [1]


    while True:
        for i in range(1):
            nx = bx + dx[i]
            ny = by + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                return count

            if data[nx][ny] == 1:
                if bx == nx and by > ny:     # 오른쪽에서 왼쪽
                    data[nx][ny] = 9
                    count += 1
                    dx = [1]
                    dy = [0]
                    bx = nx
                    by = ny
                if bx == nx and by < ny:     # 왼쪽에서 오른쪽
                    data[nx][ny] = 9
                    count += 1
                    dx = [-1]
                    dy = [0]
                    bx = nx
                    by = ny
                if bx > nx and by == ny:     # 아래에서 위
                    data[nx][ny] = 9
                    count += 1
                    dx = [0]
                    dy = [1]
                    bx = nx
                    by = ny
                if bx < nx and by == ny:     # 위에서 아래
                    data[nx][ny] = 9
                    count += 1
                    dx = [0]
                    dy = [-1]
                    bx = nx
                    by = ny

            elif data[nx][ny] == 2:
                if bx == nx and by > ny:     # 오른쪽에서 왼쪽
                    data[nx][ny] = 9
                    count += 1
                    dx = [-1]
                    dy = [0]
                    bx = nx
                    by = ny
                if bx == nx and by < ny:     # 왼쪽에서 오른쪽
                    data[nx][ny] = 9
                    count += 1
                    dx = [1]
                    dy = [0]
                    bx = nx
                    by = ny
                if bx > nx and by == ny:     # 아래에서 위
                    data[nx][ny] = 9
                    count += 1
                    dx = [0]
                    dy = [-1]
                    bx = nx
                    by = ny
                if bx < nx and by == ny:     # 위에서 아래
                    data[nx][ny] = 9
                    count += 1
                    dx = [0]
                    dy = [1]
                    bx = nx
                    by = ny
            elif data[nx][ny] == 0 or data[nx][ny] == 9:
                data[nx][ny] = 9
                bx = nx
                by = ny



T = int(input())
for test_case in range(1, T+1):
     n = int(input())
     data = [list(map(int, input().split())) for _ in range(n)]
     print('#{} {}'.format(test_case, go(0, 0)))