import time
import sys
from time import strftime
sys.stdin = open("최적경로_input.txt")
start_time = time.time()

def myprint(n):
    global total_distance
    distance = 0

    for i in range(len(client)-1):
        distance += (abs(client[i][0] - client[i+1][0]) + abs(client[i][1] - client[i+1][1]))
    ctoc = abs(company[0] - client[0][0]) + abs(company[1] - client[0][1])
    ctoh = abs(client[-1][0] - house[0]) + abs(client[-1][1] - house[1])

    distance = (ctoc + distance + ctoh)
    total_distance.append(distance)
    # print('distance = {}'.format(distance))


def perm(n, k):
    if n == k:
        myprint(n)
    else:
        for i in range(k, n):
            client[i], client[k] = client[k], client[i]
            perm(n, k+1)
            client[i], client[k] = client[k], client[i]

T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    for_tuple = []
    count = 0
    total_distance = []
    for i in range(len(data)):
        if i%2 == 1:
            for_tuple.append((data[i-1], data[i]))

    company = for_tuple[0]
    house = for_tuple[1]
    client = for_tuple[2:]


    perm(len(client), 0)

    # print('total_distance : {}'.format(total_distance))
    # print('min_distance : {}'.format(min(total_distance)))

    print('#{} {}'.format(test_case, min(total_distance)))
print(time.time() - start_time, 'seconds')