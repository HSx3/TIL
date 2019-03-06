import sys
sys.stdin = open("자리배정.txt")

C, R = map(int, input().split())
K = int(input())
seat = [[0 for _ in range(C)] for _ in range(R)]

r, c = R, 0
num = 0
count_C = C
count_R = R

if K <= C*R:
    while num < C*R:
        # 위쪽
        for i in range(count_R):
            r -= 1
            num += 1
            seat[r][c] = num
            if seat[r][c] == K:
                print('{} {}'.format(c + 1, R - r))
        count_C -= 1
        # 오른쪽
        for i in range(count_C):
            c += 1
            num += 1
            seat[r][c] = num
            if seat[r][c] == K:
                print('{} {}'.format(c + 1, R - r))
        count_R -= 1
        # 아래쪽
        for i in range(count_R):
            r += 1
            num += 1
            seat[r][c] = num
            if seat[r][c] == K:
                print('{} {}'.format(c + 1, R - r))
        count_C -= 1
        # 왼쪽
        for i in range(count_C):
            c -= 1
            num += 1
            seat[r][c] = num
            if seat[r][c] == K:
                print('{} {}'.format(c + 1, R - r))
        count_R -= 1
else:
    print('0')