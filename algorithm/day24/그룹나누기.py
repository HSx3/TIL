import sys
sys.stdin = open("그룹나누기_input.txt")


def findSet(x):
    if x == p[x]:
        return x
    else:
        return findSet(p[x])


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    p = list(range(N+1))
    edge = []

    for i in range(len(data)):
        if i % 2 == 0:
            p[findSet(data[i+1])] = findSet(data[i])

    count = 0
    for i in range(1, len(p)):
        if i == p[i]:
            count += 1
    print('#{} {}'.format(test_case, count))




'''
def findSet(x):
    if x == p[x]:
        return x
    else:
        return findSet(p[x])

def mst():
    global N, data
    i = 0

    while i < M:
        p1 = findSet(edge[i][0])
        p2 = findSet(edge[i][1])
        if p1 != p2:
            p[p2] = p1
        i += 1
    return p


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # print(data)
    edge = []
    for i in range(len(data)):
        if i % 2 == 0:
            edge.append((data[i], data[i+1]))
    # print(edge)

    adj = [[0]*(2+1) for _ in range(N+1)]
    p = list(range(N+1))

    # print(p)
    for_answer = mst()
    # print(for_answer)
    count = 0
    for i in range(1, len(for_answer)):
        if i == for_answer[i]:
            count += 1
    print('#{} {}'.format(test_case, count))

'''
