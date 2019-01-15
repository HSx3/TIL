import sys
sys.stdin = open("flatten_input.txt")
T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    minmax = 0

    for i in range(len(data) - 1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    while N > 0:
        data[0] = data[0]+1
        data[-1] = data[-1]-1
        for i in range(len(data) - 1, 0, -1):
            for j in range(0, i):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        N -= 1
    minmax = data[-1] - data[0]
    print("#{} {}".format(test_case, minmax))


