def calc(n, k, cursum):
    global ans
    if ans > cursum : ans = cursum

def perm(n, k, cursum):
    global ans, N
    if ans < cursum: return
    if k == n:
        calc(n, k, cursum)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, cursum + data[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]

import sys
sys.stdin = open('배열최소합_input.txt', 'r')
T = int(input())

for tc in range(T):
    ans = 987654321
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = i
    data = [list(map(int,input().split())) for x in range (N)]

    perm(N, 0, 0)
    print('#{} {}'.format(tc+1, ans))