import sys
sys.stdin = open("작업순서_input.txt")

N = 10
for test_case in range(2):
    V, E = map(int, input().split())
    print(V, E)
    V += 1
    temp = list(map(int, input().split()))
    print(temp)

    check = [[0 for i in range(V)] for j in range(V)]  # 2차원 초기화
    visited = [0 for i in range(V)]

    for i in range(0, len(temp), 2):  # 입력
        check[temp[i]][temp[i + 1]] = 1

    for_sum = []
    for i in range(V):  # 입력확인
        for_sum.append(check[i])
    print(for_sum)

    for j in range(len(for_sum[0])):
        for i in range(len(for_sum)):
            print(for_sum[i][j], end=" ")
        print()
    print()
    
    # for i in range(V):  # 입력확인
    #     print("{} {}".format(i, check[i]))

    print(f'#{test_case+1}')


# V, E = 9, 9
# temp = [4, 1, 1, 2, 2, 3, 2, 7, 7, 6, 1, 5, 5, 6, 8, 5, 8, 9]
# print(temp)
# V += 1
#
# check = [[0 for i in range(V)] for j in range(V)]  # 2차원 초기화
# visited = [0 for i in range(V)]
#
# for i in range(0, len(temp), 2):  # 입력
#     check[temp[i]][temp[i + 1]] = 1
#
# for i in range(V):  # 입력확인
#     print("{} {}".format(i, check[i]))
#
# print(f'#{test_case+1}')