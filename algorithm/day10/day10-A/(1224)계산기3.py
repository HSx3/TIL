def priority(c):
    if c == '(': return 0
    elif c == '+' or c == '-': return 1
    elif c == '*' or c == '/': return 2

def infix_to_postfix(infix_str):
    postfix_str = []
    for i in range(len(infix_str)):
        if infix_str[i] >= '0' and infix_str[i] <= '9':
            postfix_str.append(infix_str[i])
        else:
            if infix_str[i] == '(': #왼쪽괄호이면 무조건 push
                c_stack.append(infix_str[i])
            elif infix_str[i] == ')': #오른쪽 괄호는 왼쪽괄호가 나올 때까지 pop
                while c_stack[-1] != '(':
                    postfix_str.append(c_stack.pop())
                c_stack.pop()  # 오른쪽 괄호 제거
            else:
                if len(c_stack) != 0:
                    while priority(infix_str[i]) <= priority(c_stack[-1]): #스택안의 값이 우선순위가 높으면
                        postfix_str.append(c_stack.pop())   #스택에서 pop해서 결과 문자열에 넣기
                        if len(c_stack) == 0 : break
                c_stack.append(infix_str[i]) # 이후에 push
    while len(c_stack) != 0 :
        postfix_str.append(c_stack.pop())

    #print(postfix_str) # 후위표기법 확인하기
    return "".join(postfix_str)

#후위표기법을 스택을 이용하여 계산하기
def calc_postfix(postfix_str):
    for i in range(len(postfix_str)):
        if postfix_str[i] >= '0' and postfix_str[i] <= '9': #숫자는 스택에 push
            i_stack.append(int(postfix_str[i]))
        elif postfix_str[i] == '+':
            x = i_stack.pop()
            y = i_stack.pop()
            i_stack.append(y + x)
        elif postfix_str[i] == '-':
            x = i_stack.pop()
            y = i_stack.pop()
            i_stack.append(y - x)
        elif postfix_str[i] == '*':
            x = i_stack.pop()
            y = i_stack.pop()
            i_stack.append(y * x)
        elif postfix_str[i] == '/':
            x = i_stack.pop()
            y = i_stack.pop()
            i_stack.append(y / x)

import sys
sys.stdin = open("(1224)계산기3_input.txt", "r")
T = 10
for tc in range(T):
    c_stack = []
    i_stack = []
    length = int(input())
    infix_str = input()
    postfix_str = infix_to_postfix(infix_str)
    calc_postfix(postfix_str)
    print(f"#{tc+1} {int(i_stack.pop())}")

