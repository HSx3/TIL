import sys
sys.stdin = open("예산_input.txt")

# def check(m):
#     # 상한액으로 지방에서 요청액을 배정가능하면 배정하고 아니면 상한액으로 합계 계산
#     total = 0
#     for i in range(N):
#         if arr[i] <= m:
#             total += arr[i]
#         else:
#             total += m
#     # 합계가 총액 이하이면 성공 아니면 실패 리턴
#     if total <= M:
#         return 1
#     else:
#         return 0
#
# N = int(input())
# arr = list(map(int, input().split()))
# M = int(input())
#
# e = max(arr)
# s = 1
# sol = 0
# while s<=e:
#     m=(s+e)//2
#     if check(m):  # 성공하면 상한액 늘리고
#         sol = m
#         s = m+1
#     else:         # 초과하면 상한액 줄임
#         e = m-1
# print(sol)


# 그리디
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr.sort()
sol, total = 0, 0
for i in range(N):
    if total + arr[i]*(N-i) <= M:    # 현재 예산액으로 배정 가능하면
        total += arr[i]
    else:                           # 현재 예산액으로 배정 불가능
        sol = (M-total)//(N-i)
        break
if sol:
    print(sol)
else:
    print(arr[N-1])