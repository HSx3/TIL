def turn_90():
    for i in range(n):
        for j in range(n):
            data[i][j] =


import sys
sys.stdin = open("회전.txt")

n = int(input())
data = [list(map(int, input().split())) for _ in range(5)]
print(data)
print(list(zip(data)))
print(list(zip(data))[0][0])  # [3, 4, 1, 2, 3]
print(list(zip(data))[1][0])  # [2, 3, 4, 5, 6]

while True:
    turn = int(input())
    if turn == 0:
        break
    else:
        if turn == 90:
            ans = list(zip(data))
            for i in range(len(ans)):
                print(*ans[i][0])
        # elif turn == 180:
        #     ans = list(zip(data))

