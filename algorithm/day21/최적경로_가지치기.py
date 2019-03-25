import time
import sys
from time import strftime
sys.stdin = open("최적경로_input.txt")
start_time = time.time()

def myprint(n):
    global answer
    distance = 0

    for i in range(1, len(cc)):
        distance += (abs(cc[i-1][0] - cc[i][0]) + abs(cc[i-1][1] - cc[i][1]))
    # ctoc = abs(company[0] - client[0][0]) + abs(company[1] - client[0][1])
    ctoh = abs(cc[-1][0] - house[0]) + abs(cc[-1][1] - house[1])

    distance = (distance + ctoh)
    if answer > distance:
        answer = distance
    # print(distance)
    # total_distance.append(distance)
    # print('distance = {}'.format(distance))


def perm(n, k, checkmin):
    if answer < checkmin:
        return
    if n == k:
        myprint(n)
    else:
        for i in range(k, n):
            cc[i], cc[k] = cc[k], cc[i]
            a = abs(cc[k-1][0] - cc[k][0]) + abs(cc[k-1][1] - cc[k][1])
            perm(n, k+1, checkmin + a)
            cc[i], cc[k] = cc[k], cc[i]

T = 10
for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    for_tuple = []
    count = 0
    answer = 987654321
    for i in range(len(data)):
        if i%2 == 1:
            for_tuple.append((data[i-1], data[i]))

    company = for_tuple[0]
    house = for_tuple[1]
    client = for_tuple[2:]
    cc = [company]+client
    checkmin = 0
    # print(cc)
    perm(len(cc), 1, checkmin)

    # print('total_distance : {}'.format(total_distance))
    # print('min_distance : {}'.format(min(total_distance)))

    print('#{} {}'.format(test_case, answer))
print(time.time() - start_time, 'seconds')