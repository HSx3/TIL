import copy
import sys
sys.stdin = open("ladder2_input.txt")

def findstart(x, y):
    for x in range(0):
        for y in range(100):
            if data[x][y] == 1:
                sx, sy = x, y

def maze(sx, sy):
    global data
    count = 0
    dx = [0, 0, 1]
    dy = [-1, 1, 0]

    while sx < 100:
        for i in range(3):
            nx = sx + dx[i]
            ny = sy + dy[i]

            if nx < 0 or nx >= 100:
                continue
            if ny < 0 or ny >= 100:
                continue
            if temp[nx][ny] == 1:
                if nx == 99:
                    data[nx][ny] = 9
                    count += 1
                    return count
                else:
                    temp[nx][ny] = 9
                    count += 1
                    sx = nx
                    sy = ny
                    continue



T = 10
for test_case in range(1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    print(data)


    count_list = []
    min = 99999
    # sx, sy = findstart(x, y)
    # 시작점 찾기
    for i in range(100):
        temp = copy.deepcopy(data)
        if data[0][i] == 1:
            sx, sy = 0, i
            # maze(sx, sy)
            count_list.append((i, maze(sx, sy)))
            # if min > maze(sx, sy)
    count_list.sort(key=lambda t: (t[1]))
    print('#{} {}'.format(test_case+1, count_list[0][0]))
    # print('#{}'.format(test_case+1), end=" ")
    # for i in range(len(count_list)):
    #     print(min(count_list[i][1]))
    # print('#{} {}'.format(test_case+1, min(count_list[])))
