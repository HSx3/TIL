import sys
sys.stdin = open("회문_input.txt")

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    data = [0] * N

    for i in range(N):
         data[i] = list(input())

    print("#{} ".format(t), end="")
    #행방향
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if data[i][j+k] != data[i][j+M-k-1]:
                    flag = 0
                    break
            if flag == 1 :
                for k in range(j, M+j):
                    print("{}".format(data[i][k]), end="")
                print()
    #열방향
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if data[j+k][i] != data[j+M-k-1][i]:
                    flag = 0
                    break
            if flag == 1 :
                for k in range(j, M+j):
                    print("{}".format(data[k][i]), end="")
                print()