import sys
sys.stdin = open("로봇과자먹기_input.txt")

def perm(n, k, sums):
    global result
    if sums > result:
        return

    if k >= n and result > sums:
        result = sums

    for i in range(n):
        if not check[i]:
            check[i] = k+1
            perm(n, k+1, sums + table[k][i])
            check[i] = 0

for test_case in range(T):
    N = int(input())
    raw_cookie = list(map(int, input().split()))
    raw_robots = list(map(int, input().split()))
    table = [[0] * 100 for _ in range(100)]
    cookie = [(raw_cookie[_], raw_cookie[_ + 1]) for _ in range(0, 2 * N, 2)]
    robots = [(raw_robots[_], raw_robots[_ + 1]) for _ in range(0, 2 * N, 2)]

    for i in range(N):
        for j in range(N):
            table[i][j] = abs(cookie[i][0] - robots[j][0]) + abs(cookie[i][1] - robots[j][1])
    check = [0 for _ in range(N)]
    result = float('inf')
    perm(N, 0, 0)
    print(result)