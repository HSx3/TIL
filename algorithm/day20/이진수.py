import sys
sys.stdin = open('이진수_input.txt')

asc = [[0, 0, 0, 0],  # 0
       [0, 0, 0, 1],  # 1
       [0, 0, 1, 0],  # 2
       [0, 0, 1, 1],  # 3
       [0, 1, 0, 0],  # 4
       [0, 1, 0, 1],  # 5
       [0, 1, 1, 0],  # 6
       [0, 1, 1, 1],  # 7
       [1, 0, 0, 0],  # 8
       [1, 0, 0, 1],  # 9
       [1, 0, 1, 0],  # A
       [1, 0, 1, 1],  # B
       [1, 1, 0, 0],  # C
       [1, 1, 0, 1],  # D
       [1, 1, 1, 0],  # E
       [1, 1, 1, 1]]  # F

def aToh(c):
    if c <= '9': return ord(c) - ord('0')
    else: return ord(c) - ord('A') + 10

def makeT(x):
    global pos
    for i in range(4):
        t.append(asc[x][i])

T = int(input())
for test_case in range(1, T+1):
    N, hex = map(str, input().split())
    N = int(N)

    t = []
    arr = hex
    for i in range(len(arr)):
        makeT(aToh(arr[i]))

    print('#{}'.format(test_case), end=" ")
    for i in range(len(t)):
       print(t[i], end='')
    print()

    # n = 0
    # for i in range(len(t)):
    #     n = n * 2 + t[i]
    #     if i % 7 == 6:
    #         print(n, end=", ")
    #         n = 0
    # if i % 7 != 6:
    #     print(n)

