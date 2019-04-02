import sys
sys.stdin = open("로봇과자먹기_input.txt")

def perm(n, k):
    global min_distance, distances
    if n == k:
        distance = 0
        for i in range(len(cookies_tuple)):
            distance += (abs(cookies_tuple[i][0] - robots_tuple[i][0]) + abs(cookies_tuple[i][1] - robots_tuple[i][1]))
        if min_distance > distance:
            min_distance = distance
    else:
        for i in range(k, n):
            cookies_tuple[i], cookies_tuple[k] = cookies_tuple[k], cookies_tuple[i]
            perm(n, k+1)
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

    perm(len(cookies_tuple), 0)
    print(min_distance)