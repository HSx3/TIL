def isWall(x, y):
    if x < 0 or x >= N:
        return True
    if y < 0 or y >= N:
        return True
    if data[x][y] == 0 or data[x][y] == 1:
        return True
    return False

def hunting(x, y):
    # 12시부터 시계방향
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    count = 0

    for k in range(8):
        testX = x + dx[k]
        testY = y + dy[k]
        while True:
            if isWall(testX, testY) == True:
                break
            elif isWall(testX, testY) == False:
                if data[testX][testY] == 2:
                    count += 1
                    data[testX][testY] = 9
                    testX += dx[k]
                    testY += dy[k]
                else:
                    testX += dx[k]
                    testY += dy[k]
    return count

import sys
sys.stdin = open("사냥꾼.txt")

N = int(input())
data = [list(map(int, input())) for _ in range(N)]

sum = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            rabbit = hunting(i, j)
            sum += rabbit
print(sum)


