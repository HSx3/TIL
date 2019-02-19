def Forth(data):
    for i in range(len(data)):
        if data[i] not in operator and data[i] != '.':
            stack.append(data[i])

        if data[i] in operator:
            if len(stack) < 2:
                return "error"

            if data[i] == '+':
                stack[-2] = int(stack[-2]) + int(stack[-1])
                stack.pop()

            if data[i] == '-':
                stack[-2] = int(stack[-2]) - int(stack[-1])
                stack.pop()

            if data[i] == '*':
                stack[-2] = int(stack[-2]) * int(stack[-1])
                stack.pop()

            if data[i] == '/':
                stack[-2] = int(stack[-2]) // int(stack[-1])
                stack.pop()

        if data[i] == '.':
            if len(stack) > 1:
                return "error"
            else:
                return stack[0]


import sys
sys.stdin = open("Forth_input.txt")

T = int(input())
for test_case in range(T):
    data = input().split()
    print(data)

    operator = ['+', '-', '*', '/']
    stack = []
    print(f'#{test_case + 1} {Forth(data)}')