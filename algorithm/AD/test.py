import sys
sys.stdin = open("로봇과자먹기_input.txt")


def perm(n, k):



T = int(input())
for tc in range(T):
    N = int(input())
    cookie = list(map(int, input().split()))
    robot = list(map(int, input().split()))


    data = [[0]*N for _ in range(N)]
    # print(data)


    for i in range(0, len(robot)//2):
        rx = robot[2*i]
        ry = robot[2*i +1]
        for j in range(0, len(cookie)//2):
            cx = cookie[2*j]
            cy = cookie[2*j +1]

            data[i][j] = abs(rx - cx) + abs(ry-cy)
    print(data)

    perm(N, 0)