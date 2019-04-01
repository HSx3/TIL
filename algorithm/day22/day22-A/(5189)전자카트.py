import sys
sys.stdin = open('(5189)전자카트_input.txt', 'r')
T = int(input())

def calc(n, k, cursum):
    global ans
    cursum += dist[arr[N-1]][arr[N]]  # cursum  0 -> 1 -> 2 까지만 포함됨
    if ans > cursum: ans = cursum

def perm(n, k, cursum):
    if ans < cursum: return

    if n == k:
        calc(n, k, cursum)
    else:
        for i in range(k, n):  # 0번째 사용 안 함으로 1씩 더해야
            arr[i + 1], arr[k + 1] = arr[k + 1], arr[i + 1]
            perm(n, k+1, cursum + dist[arr[k]][arr[k+1]])  #
            arr[i + 1], arr[k + 1] = arr[k + 1], arr[i + 1]

for tc in range(T):
    ans = 987654321
    N = int(input())
    arr = [0] * N + [0]
    for i in range(N):
        arr[i] = i
    dist = [list(map(int,input().split())) for _ in range (N)]

    perm(N-1, 0, 0)
    print('#{} {}'.format(tc+1, ans))