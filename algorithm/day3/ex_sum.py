import sys
sys.stdin = open("sum_input.txt")
T = 10

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))

# 행 우선
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = " ")
    print()
print()