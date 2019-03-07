import sys
sys.stdin = open("원안의 마을.txt")

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
# print(data)

# def calc_d

# 1 : 마을 // 2 : 기지국
x1, y1, x2, y2 = 0, 0, 0, 0
D = (x2-x1)**2 + (y2-y1)**2
max_d = 0

# 기지국 찾기
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            x1, y1 = i, j
            break

# 반경 계산
for k in range(N):
    for l in range(N):
        if data[k][l] == 1:
            # calc_d(i,j)
            x2, y2 = k, l
            D = (x2 - x1) ** 2 + (y2 - y1) ** 2
            # print(D)
            if max_d < D:
                max_d = D
# print(max_d)
# print(max_d**0.5)

if max_d**0.5 > round(max_d**0.5):
    ans = round(max_d**0.5)+1
    print(ans)
else:
    ans = round(max_d**0.5)
    print(ans)