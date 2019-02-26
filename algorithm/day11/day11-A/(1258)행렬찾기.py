def selectionSort(arr, cnt):
    for i in range(cnt - 1):
        min = i
        for j in range(i+1, cnt):
            x = arr[min][0] * arr[min][1]
            y = arr[j][0] * arr[j][1]
            if x > y:
                min = j
            elif x == y and arr[min][0] > arr[j][0]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


def get_submatrix(x, y):
    global submatrix, subcnt
    i = 0
    while data[x+i][y]:
        j = 0
        while data[x+i][y+j]:
            data[x+i][y+j] = 0
            j += 1
        i += 1
    submatrix[subcnt][0] = i
    submatrix[subcnt][1] = j
    subcnt += 1


import sys
sys.stdin = open("(1258)행렬찾기_input.txt","r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    submatrix = [[0 for _ in range(2)] for _ in range(20)]

    subcnt = 0
    for i in range(N):
        for j in range(N):
            if data[i][j]:
                get_submatrix(i, j)

    selectionSort(submatrix, subcnt)

    print(f"#{tc+1} {subcnt}", end=" ")
    for i in range(subcnt):
        print(f"{submatrix[i][0]} {submatrix[i][1]}", end=" ")
    print()
