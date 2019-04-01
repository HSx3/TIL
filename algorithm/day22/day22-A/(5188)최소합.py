import time
from time import strftime
start_time = time.time()
import sys
sys.stdin = open("(5188)최소합_input.txt", "r")
T = int(input())

def solve(r, c, sum):
    global ans
    ############################
    #if ans <= sum:                            # 목적지 도착전에 이미 다른 경로의 최소값 이상인 경우
    #   return                                     # 이동을 중단하고 다른 경로로 가면 시간을 줄일 수 있다.
    ############################

    if r == N-1 and c == N-1:                   # 목적지 도착
        if ans > sum :
            ans = sum
    else:
        if r+1 < N:                                   # 아래로 이동 가능한지 확인
            solve(r+1, c, sum+arr[r+1][c])
        if c+1 < N:                                   # 오른쪽으로 이동 가능한지 확인
            solve(r, c+1, sum+arr[r][c+1])

for tc in range(1, T+1):
    N = int(input())                   
    arr = [list(map(int,input().split())) for i in range(N)]
    ans = 987654321                       # 최소값 초기화
    solve(0, 0, arr[0][0])
    print('#{} {}'.format(tc, ans))
print(time.time() - start_time, 'seconds')