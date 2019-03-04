def inorder(node):
    if node != 0:
        inorder(firstChild[node])
        print("{}".format(alpha[node]), end="")
        inorder(secondChild[node])

import sys
sys.stdin = open("중위순회_input.txt")

T = 10
for test_case in range(T):
    N = int(input())
    firstChild = [0] * (N+1)
    secondChild = [0] * (N+1)
    alpha = [0] * (N+1)
    for i in range(N):
        temp = list(input().split())
        addr = int(temp[0])
        ch = temp[1]
        alpha[addr] = ch
        if addr * 2 <= N:
            firstChild[addr] = int(temp[2])
            if addr * 2 + 1 <= N:
                secondChild[addr] = int(temp[3])
    #     print(temp)
    # print(firstChild)
    # print(secondChild)
    # print(alpha)

    print("#{}".format(test_case+1), end=" ")
    inorder(1)
    print()