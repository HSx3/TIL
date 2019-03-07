import sys
sys.stdin = open("과수원.txt")

def farm(x, y):
    sum = []
    count = 0

    for i in range(x+1):
        for j in range(y+1):
            if data[i][j] == 1:
                count += 1
    sum.append(count)

    count = 0
    for i in range(x+1):
        for j in range(y+1, N):
            if data[i][j] == 1:
                count += 1
    sum.append(count)

    count = 0
    for i in range(x+1, N):
        for j in range(y+1):
            if data[i][j] == 1:
                count += 1
    sum.append(count)

    count = 0
    for i in range(x+1, N):
        for j in range(y+1, N):
            if data[i][j] == 1:
                count += 1
    sum.append(count)

    for i in range(len(sum)):
        if sum[i] != sum[0]:
            return 0
    return 1

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(N):
        result += farm(i, j)

if result == 0:
    print(-1)
else:
    print(result)