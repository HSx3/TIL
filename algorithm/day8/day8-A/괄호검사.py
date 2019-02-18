def solve(str):
    global flag
    stack = []

    for i in range(len(str)):
        if str[i] == '{' or str[i] == '(':  # 여는 괄호
            stack.append(str[i])
        elif str[i] == '}' or str[i] == ')': # 닫는 괄호
            if len(stack) == 0:  # isEmpty
                flag = 0
                break
            else:
                temp = stack.pop()

            # 같은 쌍인지 확인
            if str[i] == ')':
                if temp != '(':
                    flag = 0
                    break
            elif str[i] == '}':
                if temp != '{':
                    flag = 0
                    break

    if len(stack) != 0:  # 스택이 비어 있지 않으면
        flag = 0

import sys
sys.stdin = open("괄호검사_input.txt")
T = int(input())

for t in range(1, T+1):
    str = input()
    flag = 1
    solve(str)
    print("#{} {}".format(t, flag))