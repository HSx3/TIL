import sys
sys.stdin = open("로봇과자먹기_input.txt")

# def myprint(n):
#     for i in range(n):
#         print(data[i], end=' ')
#     print()
#
# def perm(n, k):
#     if n == k:
#         myprint(n)
#     else:
#         for i in range(k, n):
#             data[i], data[k] = data[k], data[i]
#             perm(n, k+1)
#             data[i], data[k] = data[k], data[i]

def perm(no, nsum):
    global nmin

    if nsum > nmin:
        return

    if no >= N:
        # for i in range(N):
        #     print(data[i])
        #     print(check[i], end=' ')
        # print(nsum)
        if nsum < nmin:
            nmin = nsum
        return
    for i in range(N):
        if check[i]:
            continue
        check[i] = 1
        visited[no] = data[no][i]
        perm(no+1, nsum+data[no][i])
        check[i] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    cookie = list(map(int, input().split()))
    robot = list(map(int, input().split()))

    visited = [0] * N
    check = [0] * N

    data = [[0]*N for _ in range(N)]
    # print(data)


    for i in range(0, len(robot)//2):
        rx = robot[2*i]
        ry = robot[2*i +1]
        for j in range(0, len(cookie)//2):
            cx = cookie[2*j]
            cy = cookie[2*j +1]

            data[i][j] = abs(rx - cx) + abs(ry-cy)
    # print(data)
    nmin = 987654321
    perm(0, 0)
    print(nmin)






'''
def perm(n, k, distance):
    global min_distance, distances

    if distance > min_distance:
        return

    if n == k:
        distance = 0
        for i in range(len(cookies_tuple)):
            distance += (abs(cookies_tuple[i][0] - robots_tuple[i][0]) + abs(cookies_tuple[i][1] - robots_tuple[i][1]))
        if min_distance > distance:
            min_distance = distance
    else:
        for i in range(k, n):
            cookies_tuple[i], cookies_tuple[k] = cookies_tuple[k], cookies_tuple[i]
            perm(n, k+1, distance)
            cookies_tuple[i], cookies_tuple[k] = cookies_tuple[k], cookies_tuple[i]


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cookies = list(map(int, input().split()))
    robots = list(map(int, input().split()))

    min_distance = 987654321
    distances = 0
    cookies_tuple = []
    robots_tuple = []
    for i in range(len(cookies)):
        if i % 2 == 0:
            cookies_tuple.append((cookies[i], cookies[i+1]))
            robots_tuple.append((robots[i], robots[i+1]))

    perm(len(cookies_tuple), 0, 0)
    print(min_distance)
'''
