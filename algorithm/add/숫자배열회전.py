import sys
sys.stdin = open("숫자배열회전_input.txt")

def turn_90():
    global data, data_90
    data_90 = []
    ans = list(map(list, zip(*data)))
    for i in range(len(data)):
        data_90.append((ans[i])[::-1])

    data = data_90


T = int(input())
for test_case in range(1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)

    # for i in range(N):
    #     for j in range(N):
    #         data[j][N-i-1] = data[i][j]
    # print(data)

    save = []
    # 90도
    turn_90()
    for i in data:
        # print(i)
        save.append(i)
    print(*save)