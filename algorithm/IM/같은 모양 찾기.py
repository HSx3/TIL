import sys
sys.stdin = open("같은 모양 찾기.txt")

M = int(input())
mArr = [] # 모눈종이
for i in range(M):
    mArr.append(list(map(int, input())))
P = int(input())
pArr = [] # 패턴맵
for i in range(P):
    pArr.append(list(map(int, input())))

cnt, sol = 0, 0
for i in range(M-P+1): # 모눈종이의 시작행 제어
    for j in range(M-P+1): # 모눈종이의 시작열 제어
        for k in range(P): # 패턴행
            for l in range(P): # 패턴열
                if mArr[i+k][j+l] == pArr[k][l]:
                    cnt += 1
        if cnt == P*P:
            sol += 1
        cnt = 0

# 90도 회전
pArr90 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        pArr90[j][P-i-1] = pArr[i][j]

for i in range(M-P+1): # 모눈종이의 시작행 제어
    for j in range(M-P+1): # 모눈종이의 시작열 제어
        for k in range(P): # 패턴행
            for l in range(P): # 패턴열
                if mArr[i+k][j+l] == pArr90[k][l]:
                    cnt += 1
        if cnt == P*P:
            sol += 1
        cnt = 0

# 180도 회전
pArr180 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        pArr180[j][P-i-1] = pArr90[i][j]

for i in range(M-P+1): # 모눈종이의 시작행 제어
    for j in range(M-P+1): # 모눈종이의 시작열 제어
        for k in range(P): # 패턴행
            for l in range(P): # 패턴열
                if mArr[i+k][j+l] == pArr180[k][l]:
                    cnt += 1
        if cnt == P*P:
            sol += 1
        cnt = 0

# 270도 회전
pArr270 = [[0]*P for _ in range(P)]
for i in range(P):
    for j in range(P):
        pArr270[j][P-i-1] = pArr180[i][j]

for i in range(M-P+1): # 모눈종이의 시작행 제어
    for j in range(M-P+1): # 모눈종이의 시작열 제어
        for k in range(P): # 패턴행
            for l in range(P): # 패턴열
                if mArr[i+k][j+l] == pArr270[k][l]:
                    cnt += 1
        if cnt == P*P:
            sol += 1
        cnt = 0

print(sol)