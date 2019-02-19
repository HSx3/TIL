# def isWall(x, y):
#     global arr, N
#     if x < 0 or x >= N:
#         return True
#     if y < 0 or y >= N:
#         return True
#     return False
#
# def calAbs(y, x):
#     if y - x > 0:
#         return y - x
#     else:
#         return x- y
#
# def move(x, y):
#     global arr, sum
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#
#     for i in range(4):
#         testX = x + dx[i]
#         testY = y + dy[i]
#
#         if isWall(testX, testY) == False:
#             sum += calAbs(arr[y][x], arr[testY][testX])



import sys
sys.stdin = open("미로_input.txt")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(arr)

    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                start_x = i
                start_y = j
                x = start_x
                y = start_y
    print(f'#{test_case+1}')