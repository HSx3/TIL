def answer_T(time):
    global count, timecheck, K
    count += 1
    timecheck += int(time)
    K += 1
    if K == 9:
        K = 1;

def answer_X(time):
    global count, timecheck, K
    timecheck += int(time)
    if K == 9:
        K = 1;

import sys
sys.stdin = open("폭탄돌리기.txt")

K = int(input())    # 시작번호
N = int(input())    # 퀴즈의 수
limit = 220

# number = [1, 2, 3, 4, 5, 6, 7, 8]
timecheck = 0
count = 0
for i in range(N):
    time, Z = map(str, input().split())
    print(time, Z)

    if timecheck + int(time) >= 220:
        print(K)
        break
    else:
        if Z == 'T':
            if count == N:
                break
            answer_T(time)
        else:
            if count == N:
                break
            answer_X(time)
