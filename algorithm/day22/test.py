import sys
sys.stdin = open("화물도크_input.txt")


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    visited = [0 for _ in range(25)]

    cnt = 0

    data =[]
    for _ in range(N):
        st, ed = map(int, input().split())

        data.append([st, ed])


    data.sort(key=lambda x:x[1])

    print(data)