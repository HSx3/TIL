import sys
sys.stdin = open("자리배정.txt")

def find(startx, starty):
    global X, Y, num
    while K <= X*Y:
        # 오른쪽이동
        for x in range(X):
            startx = startx + 1
            num += 1
            L[starty][startx] = num
            if num == K:
                return startx, starty
        # 아래이동
        Y = Y-1
        for y in range(Y):
            starty = starty + 1
            num += 1
            L[starty][startx] = num
            if num == K:
                return startx, starty
        # 왼쪽이동
        X = X-1
        for x in range(X):
            startx -= 1
            num += 1
            L[starty][startx] = num
            if num == K:
                return startx, starty
        # 위로이동
        Y = Y -1
        for y in range(Y):
            starty = starty - 1
            num += 1
            L[starty][startx] = num
            if num == K:
                return startx, starty

    return 0


Y, X = map(int, input().split())
K = int(input())

L = [[0 for _ in range(X+1)] for _ in range(Y+1)]

startx, starty = 0, 1
num = 0

answer = find(startx, starty)

if answer:
    print(*answer)
else:
    print(0)