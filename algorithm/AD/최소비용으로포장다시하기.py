import sys
sys.stdin = open("최소비용으로포장다시하기_input.txt")

# main
N = int(input())
arr = list(map(int, input().split()))
answer = 0
# solution - 1
# k 위치에서 2개씩만 정렬
for k in range(N-1):
    for i in range(k, k+2):
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    arr[k + 1] += arr[k]  # k, k+1번째 포장
    answer += arr[k + 1]  # 포장비용누계

# solution - 2 (insert sort)
# arr.sort() # 정렬 먼저
# for k in range(1, N):
#     arr[k] += arr[k-1]  # k, k+1번째 포장
#     answer += arr[k]    # 포장비용누계
#     temp = arr[k]
#     for i in range(k+1, N):
#         if arr[i] < temp:  # 크거나 같을때까지 교환
#             arr[i], arr[i-1] = arr[i-1], arr[i]
#         else:
#             break
print(answer)