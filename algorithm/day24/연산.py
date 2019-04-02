import time
from time import strftime
start_time = time.time()

import sys
sys.stdin = open("연산_input.txt")

def BFS():
    global visited

    que = []
    visited[N] = 1
    que.append((N, 0))

    while que:
        n, count = que.pop(0)

        calc = [n+1, n-1, n*2, n-10]

        if n == M:
            return count

        for i in range(4):
            nn = calc[i]
            if nn > 1000000:
                continue
            if nn < 0:
                continue
            if visited[nn] == 0:
                visited[nn] = 1
                que.append((nn, count + 1))



T = int(input())
for test_case in range(1, T+1):
    visited = [0] * 1000001
    N, M = map(int, input().split())
    print('#{} {}'.format(test_case, BFS()))

print(time.time() - start_time, 'seconds')