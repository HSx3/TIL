# 2차원 배열
arr = [[0,1,2,3],
       [4,5,6,7],
       [8,9,10,11]]
# i : 행의 좌표, n = len(arr)
# j : 열의 좌표, m = len(arr[0])


# 행 우선
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = " ")
    print()
print()


# 열 우선
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j], end = " ")
    print()
print()


# 델타

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# for x in range(len(arr)):
#     for y in range(len(arr[x])):
#         for i in range(4):
#             testX = x + dx[i]
#             testY = y + dy[i]
#             test(arr[testX][testY])