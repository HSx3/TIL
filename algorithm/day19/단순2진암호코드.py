import sys
sys.stdin = open("단순2진암호코드_input.txt")

T = int(input())

code = [[0, 0, 0, 1, 1, 0, 1],  # 0
        [0, 0, 1, 1, 0, 0, 1],  # 1
        [0, 0, 1, 0, 0, 1, 1],  # 2
        [0, 1, 1, 1, 1, 0, 1],  # 3
        [0, 1, 0, 0, 0, 1, 1],  # 4
        [0, 1, 1, 0, 0, 0, 1],  # 5
        [0, 1, 0, 1, 1, 1, 1],  # 6
        [0, 1, 1, 1, 0, 1, 1],  # 7
        [0, 1, 1, 0, 1, 1, 1],  # 8
        [0, 0, 0, 1, 0, 1, 1]]  # 9

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(N)]
    # print(data)

    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                sx = i
                sy = j
                break

    result = []
    k = len(data[sx])-1
    while k >= 6:
        if data[sx][k] == 1:
            if data[sx][k-6 : k+1] in code:
                result.append(code.index(data[sx][k-6:k+1]))
                k -= 5
        k -= 1

    result.reverse()
    if ((result[0] + result[2] + result[4] + result[6])*3 + result[1] + result[3] + result[5] + result[7]) % 10 == 0:
        print('#{} {}'.format(test_case, sum(result)))
    else:
        print('#{} {}'.format(test_case, 0))