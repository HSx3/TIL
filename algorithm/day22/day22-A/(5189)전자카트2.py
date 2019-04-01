import sys
sys.stdin = open('(5189)전자카트_input.txt', 'r')
T = int(input())

def calc(n, r, cursum):
    global ans
    cursum += dist[0][t[1]]  # cursum  1-> 2, 2-> 0 까지만 포함됨
    if ans > cursum: ans = cursum

def perm(n, r, cursum):
    if ans < cursum: return

    if r == 0:
       calc(n, r, cursum)
    else:
        for i in range(n, 0, -1):  # 0번째 사용 안 함으로 n으로 수정
            arr[n], arr[i] = arr[i], arr[n]
            t[r] = arr[n]
            perm(n-1, r-1, cursum + dist[t[r]][t[r+1]])  # 2->0, 1->2, ... 으로 저장됨
            arr[n], arr[i] = arr[i], arr[n]

for tc in range(T):
    ans = 987654321
    N = int(input())
    arr = [0] * N           # 0번째 사용안함
    for i in range(N):
        arr[i] = i
    t = [0] * N  + [0]      # 앞뒤에 0 추가  [0, 1, 2, 0]
    dist = [list(map(int,input().split())) for _ in range (N)]

    perm(N-1, N-1, 0)
    print('#{} {}'.format(tc+1, ans))