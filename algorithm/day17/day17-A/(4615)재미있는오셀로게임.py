def check(a, b, dol):
    for i in range(8):
        x = a
        y = b
        flag = False
        while x + dx[i] > 0 and x + dx[i] <= N and y + dy[i] > 0 and y + dy[i] <= N : # 벽체크
            x += dx[i]
            y += dy[i]
            if pan[x][y] == 0: break
            if pan[x][y] == dol:
                flag = True
                ex = x  #end x
                ey = y  #end y
                break
        if flag:
            x = a
            y = b
            while not(x == ex and y == ey):
                x += dx[i]
                y += dy[i]
                pan[x][y] = dol

def printArr():
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(pan[i][j], end=" ")
        print()
    print()

import sys
sys.stdin = open("(4615)재미있는오셀로게임_input.txt")
dx = [-1, -1, -1, 0, 1, 1,  1,  0]
dy = [-1,  0,  1, 1, 1, 0, -1, -1]

T = int(input())

for tc in range(1, T+1):
    pan = [[0 for _ in range(10)] for _ in range(10)]
    N, M = map(int, input().split())

    mid = N // 2
    # W = 2, B = 1
    pan[mid][mid] = pan[mid+1][mid+1] = 2
    pan[mid][mid+1] = pan[mid+1][mid] = 1
    #printArr()

    for i in range(M):
        a, b, dol = map(int, input().split())
        pan[a][b] = dol
        check(a, b, dol)
        #printArr()

    B = 0
    W = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if pan[i][j] == 1 : B += 1
            if pan[i][j] == 2: W += 1

    print("#{} {} {}".format(tc, B, W))