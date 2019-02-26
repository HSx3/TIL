def total(i, j):
    global N, M, data
    for_sum = []
    for x in range(i, i+M):
        for y in range(j, j+M):
            for_sum.append(data[x][y])
    a = sum(for_sum)
    return total_sum.append(a)

import sys
sys.stdin = open("파리퇴치_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    total_sum = []
    # print(N, M)
    # print(data)

    for i in range(N-M+1):
        for j in range(N-M+1):
            total(i, j)
    print(f'#{test_case} {max(total_sum)}')


