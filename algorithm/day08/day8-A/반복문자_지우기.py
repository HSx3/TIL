import sys
sys.stdin = open("반복문자_지우기_input.txt")
T = int(input())

for t in range(1, T+1):
    stack=[]
    str = input()

    for i in range(len(str)):
        if len(stack) == 0:         # 스택이 비어 있으면
            stack.append(str[i])
        else:
            if stack[len(stack)-1] == str[i] : # 스택의 맨위 숫자와 비교
                stack.pop()
            else:
                stack.append(str[i])

    print("#{} {}".format(t, len(stack)))

