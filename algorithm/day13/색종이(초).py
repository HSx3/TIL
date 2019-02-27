import sys
sys.stdin = open("색종이(초).txt")

paper = int(input())
XY = [list(map(int, input().split())) for _ in range(paper)]

temp = [[0 for _ in range(100)] for _ in range(100)]
count = 0

for i in XY:
    x = i[0]-1
    y = i[1]-1

    for i in range(x, x+10):
        for j in range(y, y+10):
            temp[i][j] = 1

for i in range(100):
    for j in range(100):
        if temp[i][j] == 1:
            count += 1

print(count)