def checkparen(data):
    paren = []
    for i in data:
        if i == '(' or i == ')' or i == '{' or i == '}':
            paren.append(i)

    if len(paren) % 2 != 0:
        return 0

    if paren[0] == '(' and paren[-1] == ')':
        for i in range(len(paren) - 1):
            if paren[i] == '(' and paren[i + 1] == '}':
                return 0
            if paren[i] == '{' and paren[i + 1] == ')':
                return 0
        else:
            return 1

    if paren[0] == '{' and paren[-1] == '}':
        for i in range(len(paren) - 1):
            if paren[i] == '(' and paren[i + 1] == '}':
                return 0
            if paren[i] == '{' and paren[i + 1] == ')':
                return 0
        else:
            return 1

    else:
        return 1


import sys
sys.stdin = open("괄호검사_input.txt")

N = int(input())
for test_case in range(N):
    data = list(input())
    # print(data)

    print(f'#{test_case + 1} {checkparen(data)}')