def RPS(a, b):
    global g_1, g_2
    if a == 1 and b == 1:
        print(a)
        # return a
    if a == 1 and b == 2:
        print(b)
        # return b
    if a == 1 and b == 3:
        print(a)
        # return a

    if a == 2 and b == 1:
        print(a)
        # return a
    if a == 2 and b == 2:
        print(a)
        # return a
    if a == 2 and b == 3:
        print(b)
        # return b

    if a == 3 and b == 1:
        print(b)
        # return b
    if a == 3 and b == 2:
        print(a)
        # return a
    if a == 3 and b == 3:
        print(a)
        # return a


import sys
sys.stdin = open("토너먼트카드게임_input.txt")

T = int(input())
for test_case in range(T):
    N = int(input())
    # data = input().split()                      # ['1', '3', '2', '1']
    data = list(map(int, input().split()))      # [1, 3, 2, 1]
    # data = ' '.join(input().split())            # 1 3 2 1
    print(data)

    g_1 = []
    g_2 = []

    for i in range(len(data)):
        if i <= (len(data)-1)//2:
            g_1.append(data[i])
        else:
            g_2.append(data[i])

    print(g_1)
    print(g_2)
    for i in range(len(g_1)):
        if i % 2 == 0:
            a = g_1[i]
        if i % 2 != 0:
            b = g_1[i]
    RPS(a, b)

