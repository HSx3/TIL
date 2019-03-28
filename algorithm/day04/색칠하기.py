import sys
sys.stdin = open("색칠하기_input.txt")
T = int(input()) # input line1

for test_case in range(1, T + 1):
    count = 0
    N = int(input()) # 줄 수
    arr = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color
                if arr[i][j] == 3:
                    count += 1
    print(f'#{test_case} {count}')