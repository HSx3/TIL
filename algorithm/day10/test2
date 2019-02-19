def process_solution(a, k):
    global min
    sum = 0
    for i in range(1, k+1):
        sum += arr[i-1][data[a[i]]]
    if sum < min:
        min = sum


def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k) #답이면 원하는 작업을 한다.
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)

import sys
sys.stdin = open('배열최소.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for s in range(len(arr)):
        arr[s] = list(map(int, input().split()))

    data = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        data[i] = i-1 # 0부터 1,2,
    print(data)
    sum = []
    min = 1000000000



    MAXCANDIDATES = N+1
    NMAX = N+1

    a = [0] * NMAX
    backtrack(a, 0, N)
    print(min)