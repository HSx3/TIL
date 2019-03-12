import sys
sys.stdin = open('배열최소합.txt')

def minsum(k):
    global min, sum, N

    if k == N:
        if min > sum:
            min = sum

    for i in range(N):
        if visit[i] == 0:
            if sum > min:
                continue
            else:
                visit[i] = 1
                sum += num[i][k]
                minsum(k+1)
                visit[i] = 0
                sum -= num[i][k]

for tc in range(int(input())):
    min = 987654321
    sum = 0
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N

    minsum(0)

    print('#{} {}'.format(tc+1, min))



