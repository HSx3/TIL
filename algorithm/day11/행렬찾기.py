def count_arr_len(start_x, start_y):
    global count_arr
    count_y = 0
    while data[start_x][start_y] != 0:
        temp[start_x][start_y] = 0
        start_y += 1
        count_y += 1

        if data[start_x][start_y] == 0:
            start_y -= 1
            break

    count_x = 0
    while data[start_x][start_y] != 0:
        temp[start_x][start_y] = 0
        start_x += 1
        count_x += 1
        if data[start_x][start_y] == 0:
            start_x -= 1
            break
    # print(count_x, count_y)
    arr_list.append((count_x, count_y))
    count_arr += 1
    # for x in range(abs(start_y - count_y)):
    #     for y in range(abs(start_x - count_x)):
    for x in range(start_x + 1 - count_x, start_x + 1):
        for y in range(start_y + 1 - count_y, start_y + 1):
            temp[x][y] = 0
    # print(arr_list)
    # print(count_arr)
    # print(temp)

import copy
import sys
sys.stdin = open("행렬찾기_input.txt")

# arr_list = []
T = int(input())
for test_case in range(1, T+1):
# for test_case in range(2):
    arr_list = []
    ans = []
    count_arr = 0
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)
    temp = copy.deepcopy(data)

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if temp[i][j] != 0:
                start_x = i
                start_y = j
                count_arr_len(start_x, start_y)
    # print(arr_list)
    # print(count_arr)
    # print(sorted(arr_list))
    # print(sorted(arr_list, key = (lambda x: (x[0]*x[1], x[0]))))
    a = sorted(arr_list, key = (lambda x: (x[0]*x[1], x[0])))
    # print(a)

    for i in a:
        ans.append(i[0])
        ans.append(i[1])
    # print(ans)
    ans_str = ' '.join(str(x) for x in ans)

    print(f'#{test_case} {count_arr} {ans_str}')
