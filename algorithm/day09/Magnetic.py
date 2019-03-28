import sys
sys.stdin = open("Magnetic_input.txt")

N = 10
for test_case in range(N):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(T)]
    # print(data)

    count = 0
    for j in range(len(data)):
        stack = []
        for i in range(len(data)):
            if data[i][j] == 1 or data[i][j] == 2:
                stack.append(data[i][j])

        for i in range(len(stack)):
            if stack[0] == 2:
                stack.pop(0)
            if stack[-1] == 1:
                stack.pop()

        for i in range(len(stack)-1):
            if stack[i] == 1 and stack[i+1] != 1:
                count += 1

    print(f'#{test_case+1} {count}')