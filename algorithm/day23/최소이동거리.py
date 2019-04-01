import sys

sys.stdin = open("최소이동거리_input.txt")


T = int(input())
for test_case in range(1, T+1):
    N, E = map(int, input().split())
    # data = [list(map(int, input().split())) for _ in range(E)]
    # print(data)

    start = 0
    end = N

    adjacent = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(E):
        u, v, w = map(int, input().split())

        if v in adjacent[u]:
            adjacent[u][v] = min(adjacent[u][v], w)
        else:
            adjacent[u][v] = w
