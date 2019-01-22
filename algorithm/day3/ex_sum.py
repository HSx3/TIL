import sys
sys.stdin = open("sum_input.txt")
T = 10
sum_max = -987654321

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))

    # 행
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr[i])):
            sum += arr[i][j]
        if sum_max < sum:
            sum_max = sum

    # 열
    for j in range(len(arr[0])):
        sum = 0
        for i in range(len(arr)):
            sum += arr[i][j]
        if sum_max < sum:
            sum_max = sum

    # 대각선
    sum = 0
    for i in range(len(arr)):
        sum += arr[i][i]
    if sum_max < sum:
        sum_max = sum

    # 대각선2
    sum = 0
    for i in range(len(arr)):
        sum += arr[i][len(arr)-i-1]
    if sum_max < sum:
        sum_max = sum
        
    print(f'#{test_case} {sum_max}')
    sum_max = -987654321