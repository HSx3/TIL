import sys
sys.stdin = open("금속막대_input.txt")

T = int(input()) # input line1
for test_case in range(1, T + 1):
    N = int(input()) # 줄 수
    data = list(map(int, input().split()))

    front = []
    back = []
    result = []

    for i in range(len(data)):
        if not i % 2:
            front.append(data[i])
        else:
            back.append(data[i])

    for i in range(N):
        if front[i] not in back:
            result.append(front[i])
            result.append(back[i])
   
    count = 0
    while count < N-1:
        count += 1
        for i in range(N):
            if front[i] == result[-1]:
                result.append(front[i])
                result.append(back[i])

    result = ' '.join(str(i) for i in result)

    print(f'#{test_case} {result}')