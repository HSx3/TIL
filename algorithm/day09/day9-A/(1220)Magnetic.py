def solve(data, size):
    cnt = 0
    for x in range(size):       #열우선 순회
        flag = 0
        for y in range(size):
            value = data[y][x]
            if flag == 0 and value == 1:    # N극을 찾음
                flag = 1
            elif flag == 1 and value == 2:  # S극을 찾음
                cnt += 1
                flag = 0
    return cnt


import sys
sys.stdin = open("(1220)Magnetic_input.txt")
T = 10
for tc in range(T):
    N = int(input())
    data = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))

    print(f"#{tc+1} {solve(data, N)}")