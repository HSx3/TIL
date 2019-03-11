def postOrder(node):
    global N

    if firstChild[node] == 0 or secondChild[node] == 0:
        return num[node]
    else:
        a = postOrder(firstChild[node])  # 왼쪽 자식으로 이동
        b = postOrder(secondChild[node])  # 오른쪽 자식으로 이동
        num[node] = calc(oper[node], a, b)
        return num[node]  # 노드에 저장된 값을 반환

def calc(op, left, right):
    if op == '+':
        result = left + right
    elif op == '-':
        result = left - right
    elif op == '*':
        result = left * right
    elif op == '/':
        result = left / right

    return result

import sys
sys.stdin = open("(1232)사칙연산_input.txt", "r")
T = 10
for tc in range(T):
    N = int(input())
    stack=[]
    oper = [''] * (N+1)
    firstChild  = [0] * (N+1)
    secondChild = [0] * (N+1)
    num = [0] *(N+1)
    for i in range(N):  # 입력
        temp = list(input().split())
        no = int(temp[0])
        if temp[1] == '+' or temp[1] == '-' or temp[1] == '*' or temp[1] == '/':
            oper[no] = temp[1]
            firstChild[no] = int(temp[2])
            secondChild[no] = int(temp[3])
        else:
            num[no] = int(temp[1])
    ans = postOrder(1)

    print(f"#{tc+1} {int(ans)}")