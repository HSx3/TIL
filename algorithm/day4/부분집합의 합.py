import sys
sys.stdin = open("부분집합의 합_input.txt")
T = int(input()) # input line1
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(A)

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    for i in range(1, 1 << n):
        count_N = 0
        count_K = 0
        sum = 0
        for j in range(n):
            if i & (1 << j):
                sum += A[j]
                count_N += 1
            if count_N == N and sum == K:
                count_K += 1

    print(f'#{test_case} {count_K}')