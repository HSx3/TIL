import sys
sys.stdin = open("구슬 굴리기.txt")

def isWall(x, y):
    if x < 0 or x > c-1:
        return True
    if y < 0 or y > r-1:
        return True
    return False


def roll(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    k = 0
    count = 1
    while k < len(navi):
        testX = x + dx[navi[k]-1]
        testY = y + dy[navi[k]-1]

        if isWall(testX, testY) == False:
            if data[testX][testY] == 0 or data[testX][testY] == 2:
                data[testX][testY] = 3
                count += 1
                x = testX
                y = testY
            elif data[testX][testY] == 3:
                x = testX
                y = testY
            else:
                k += 1
        else:
            k += 1
    return count


r, c = map(int, input().split())
data = [list(map(int, input())) for _ in range(c)]
N = int(input())
navi = list(map(int, input().split()))
# print(info)
# print(data)

for i in range(c):
    for j in range(r):
        if data[i][j] == 2:
            data[i][j] = 3
            answer = roll(i, j)
print(answer)



