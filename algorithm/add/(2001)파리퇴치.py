import sys
sys.stdin = open("(2001)파리퇴치_input.txt")
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))

    max = 0  #최대값
    min = 987654321
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0 #파리채에 죽은 파리의 수
            for x in range(M):
                for y in range(M):
                   sum += data[i+x][j+y]
            if max < sum: max = sum
            if min > sum: min = sum
    print("#%d %d" % (tc + 1, max))







