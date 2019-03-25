import sys
sys.stdin = open("정곤이의단조증가하는수_input.txt")

def check(data):
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            return -1
    return 1

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    check_ij = []
    print('#{}'.format(test_case), end=' ')
    if check(data) == -1:
        print(-1)
    elif check(data) == 1:
        for i in range(N):
            for j in range(i+1, len(data)):
                ij = data[i]*data[j]
                if len(str(ij)) == 1:
                    check_ij.append(ij)
                elif len(str(ij)) > 1:
                    if check(str(ij)) == 1:
                        check_ij.append(ij)
    print(max(check_ij))