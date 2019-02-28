import sys
sys.stdin = open("같은 모양 찾기 simple.txt")

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
print(sol)