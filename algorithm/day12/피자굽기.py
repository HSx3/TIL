import sys
sys.stdin = open("피자굽기_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    # print(N, M)
    # print(Ci)

    Q = [0] * N
    i = 0

    while i < M:
        Q[0] = [Ci[i], i]
        Q.append(Q.pop(0))
        i += 1

        while 0 not in Q:
            if 0 not in Q:
                Q[0][0] = Q[0][0] // 2
                if Q[0][0] == 0:
                    break
                Q.append(Q.pop(0))

    while len(Q) >= 1:
        if len(Q) == 1:
            print(f'#{test_case} {Q[-1][1] + 1}')
            break
        if Q[0][0] == 0:
            Q.pop(0)
        else:
            Q[0][0] = Q[0][0] // 2
            if Q[0][0] == 0:
                Q.pop(0)
            else:
                Q.append(Q.pop(0))