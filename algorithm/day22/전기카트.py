import sys
sys.stdin = open("전기카트_input.txt")

def myprint(n):
    global route, answer
    office = [1]
    real_route = office + route + office
    e = 0

    for i in range(len(real_route)-1):
        e += data[real_route[i]-1][real_route[i+1]-1]
    answer.append(e)

def perm(n, k):
    if n == k:
        myprint(n)
    else:
        for i in range(k, n):
            route[i], route[k] = route[k], route[i]
            perm(n, k+1)
            route[i], route[k] = route[k], route[i]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    answer = []
    office = [1]
    route = list(range(2, N+1))
    perm(len(route), 0)

    print('#{} {}'.format(test_case, min(answer)))
