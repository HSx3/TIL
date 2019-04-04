import sys
sys.stdin = open("테이프이어붙이기_input.txt")

# def comb(no, count, nsum):
#     global sol
#     if count + (N-no) < N/2:
#         return
#     if count == N // 2:
#         temp = abs(nsum - (total - nsum))  # 이등분한 테이프의 차이
#         if temp < sol:
#             sol = temp
#         return
#
#     if no >= N:
#         # for i in range(N):
#         #     print(rec[i], end=' ')
#         # print(count, nsum)
#
#         # if count == N//2:
#         #     temp = abs(nsum - (total-nsum))    # 이등분한 테이프의 차이
#         #     if temp < sol:
#         #         sol = temp
#         return
#
#     # 현재 no번 테이프를 붙이거나 붙이지 않는 경우 시도
#     rec[no] = data[no]
#     comb(no+1, count+1, nsum + data[no])
#     rec[no] = 0
#     comb(no+1, count, nsum)
#
# N = int(input())
# data = list(map(int, input().split()))
# total = sum(data)
# rec = [0] * N
# sol = 987654321
#
# comb(0, 0, 0)   # 0번째 테이프부터 시작, 고른개수 0개, 테이프길이 합
# print(sol)



def comb(no, count):
    global sums, total
    if no >= N:
        if count == N//2:

            # if sum(b) not in sums:
            #     sums.append((sum(b), total-sum(b)))
            for i in range(N):
                print(b[i], end=' ')
            print()
        return
    b[no] = data[no]
    comb(no+1, count+1, )
    b[no] = 0
    comb(no+1, count)

N = int(input())
data = list(map(int, input().split()))
total = sum(data)
# print(total)
b = [0] * N
sums = []
# check = [0] * N

answer = 987654321

comb(0, 0)
# print(sums)

# for i in range(len(sums)):
#     if answer > abs(sums[i][0] - sums[i][1]):
#         answer = abs(sums[i][0] - sums[i][1])
# print(answer)
