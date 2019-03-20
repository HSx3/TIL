import sys
sys.stdin = open("스도쿠검증_input.txt")

T = int(input())

for test_case in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(9)]

    print('#{}'.format(test_case), end=' ')

    check = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    ans = []
    # 가로
    for i in range(9):
        check_row = []
        for j in range(9):
            check_row.append(data[i][j])
        x = set(check_row)
        if x != check:
            ans.append(0)
            # break

    # 세로
    for i in range(9):
        check_col = []
        for j in range(9):
            check_col.append(data[j][i])
        x = set(check_col)
        if x != check:
            ans.append(0)
            # break

    # for * 4
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check_grid = []
            for k in range(3):
                for l in range(3):
                    check_grid.append(data[k][l])
            x = set(check_grid)
            if x != check:
                ans.append(0)



    # 격자
    # check_grid = []
    # for i in range(0, 3):
    #     for j in range(0, 3):
    #         check_grid.append(data[i][j])
    # x = set(check_grid)
    # if x != check:
    #     ans.append(0)
    #
    # check_grid = []
    # for i in range(3, 6):
    #     for j in range(0, 3):
    #         check_grid.append(data[i][j])
    # x = set(check_grid)
    # if x != check:
    #     ans.append(0)
    #
    # check_grid = []
    # for i in range(6, 9):
    #     for j in range(0, 3):
    #         check_grid.append(data[i][j])
    # x = set(check_grid)
    # if x != check:
    #     ans.append(0)
    #
    # check_grid = []
    # for i in range(0, 3):
    #     for j in range(3, 6):
    #         check_grid.append(data[i][j])
    # x = set(check_grid)
    # if x != check:
    #     ans.append(0)
    #
    # check_grid = []
    # for i in range(3, 6):
    #     for j in range(3, 6):
    #         check_grid.append(data[i][j])
    # x = set(check_grid)
    # if x != check:
    #     ans.append(0)
    #
    # check_grid = []
    # for i in range(6, 9):
    #     for j in range(3, 6):
    #         check_grid.append(data[i][j])
    # x = set(check_grid)
    # if x != check:
    #     ans.append(0)
    #
    # check_grid = []
    # for i in range(0, 3):
    #     for j in range(6, 9):
    #         check_grid.append(data[i][j])
    # x = set(check_grid)
    # if x != check:
    #     ans.append(0)
    #
    # check_grid = []
    # for i in range(3, 6):
    #     for j in range(6, 9):
    #         check_grid.append(data[i][j])
    # x = set(check_grid)
    # if x != check:
    #     ans.append(0)
    #
    # check_grid = []
    # for i in range(6, 9):
    #     for j in range(6, 9):
    #         check_grid.append(data[i][j])
    # x = set(check_grid)
    # if x != check:
    #     ans.append(0)

    if 0 in ans:
        print(0)
    if 0 not in ans:
        print(1)