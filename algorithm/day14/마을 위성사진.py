import sys
sys.stdin = open("마을 위성사진.txt")

N = int(input())
data = []
for i in range(N):
    data.append(list(map(int, input())))

for h in range(N):
    flag=0
    for i in range(1, N-1):
        for j in range(1, N-1):
            if data[i][j] > h:# 사방이 모두 언덕이면 높이 1 증가
                flag = 1
                if data[i-1][j]>h and data[i+1][j]>h and data[i][j-1]>h and data[i][j+1]>h:
                    data[i][j]+=1
    if flag == 0:   # 더이상 높일 언덕이 없으면 탈출
        break

print(h)