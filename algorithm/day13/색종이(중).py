import sys
sys.stdin = open("색종이(중).txt")

# for i in range(N):
#     r, c = map(int, input().split())
paper = int(input())
XY = [list(map(int, input().split())) for _ in range(paper)]

temp = [[0 for _ in range(101)] for _ in range(101)]
count = 0
for_index_i = []
for_index_j = []

for i in XY:
    x = i[0]-1
    y = i[1]-1

    for i in range(x, x+10):
        for j in range(y, y+10):
            temp[i][j] = 1
            for_index_i.append(i)
            for_index_j.append(j)

ans = 0
for i in range(0, 101):
    for j in range(0, 101):
        if temp[i][j] == 1:
            if temp[i][j] != temp[i-1][j]:
                ans += 1
            if temp[i][j] != temp[i+1][j]:
                ans += 1
            if temp[i][j] != temp[i][j-1]:
                ans += 1
            if temp[i][j] != temp[i][j+1]:
                ans += 1
print(ans)