import copy
import sys
sys.stdin = open('배열 정리.txt')

Y, X = map(int, input().split())
data = [list(map(int, input().split())) for i in range(Y)]
temp = copy.deepcopy(data)

for i in range(Y):
    for j in range(1, X):
        if data[i][j] == 1:
            temp[i][j] = temp[i][j-1]+1

for i in range(len(temp)):
    print(*temp[i])


'''
R, C = map(int, input().split())
arr = []
for i in range(R):
    arr.append(list(map(int, input().split())))

for i in range(R):
    for j in range(1, C):
    if arr[i][j]==1:
        arr[i][j] += arr[i][j-1]

for i in range(R):
    for j in range(C):
        print(arr[i][j], end=' ')
    print()
'''