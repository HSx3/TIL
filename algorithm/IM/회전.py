def turn_90(n):
    global data, data_90
    data_90 = []
    ans = list(map(list, zip(*data)))
    for i in range(len(data)):
        data_90.append((ans[i])[::-1])

    data = data_90

import sys
sys.stdin = open("회전.txt")

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

turn = int(input())
while True:
    if turn == 90:
        turn_90(n)
        for i in data:
            print(*i)

    elif turn == 180:
        turn_90(n)
        turn_90(n)
        for i in data:
            print(*i)

    elif turn == 270:
        turn_90(n)
        turn_90(n)
        turn_90(n)
        for i in data:
            print(*i)

    elif turn == 360:
        for i in data:
            print(*i)

    turn = int(input())
    if turn == 0:
        break


        # for i in range(len(ans)):
        #     print(*(ans[i])[::-1])