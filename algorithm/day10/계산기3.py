# 계산기3.py

import sys
sys.stdin = open("계산기3_input.txt")

T = 10
for test_case in range(T):
    length = int(input())
    data = input()  # type : str
    print(data)

    token = []
    stack = []

    for i in range(len(data)):
        if data[i].isdigit():
            stack.append(data[i])
        else:

            if data[i] != ')' and data[i] == '*' and token[-1] == '*':
                stack.append(token.pop())
                token.append(data[i])

            if data[i] != ')' and data[i] == '+' and token[-1] == '+':
                stack.append(token.pop())
                token.append(data[i])


            if data[i] != ')' and data[i] != '/':
                token.append(data[i])
            if data[i] == ')' and i != len(data) - 1:
                # print(data.index(data[i]))
                stack.append(token.pop())
                token.pop()

                # while token[-1] != '(':
                #     if token[-1] != '(':
                #         stack.append(token.pop())
                #     else:
                #         token.pop()
                #         break
            if data[i] == ')' and i == len(data) - 1:
                while len(token) > 0:
                    if token.pop() != '(':
                        stack.append(token.pop())

    print(stack)
    print(token)