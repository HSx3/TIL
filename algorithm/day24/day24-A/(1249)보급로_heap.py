import time
from time import strftime

start_time = time.time()

import sys
import heapq
sys.stdin = open('(1249)보급로_input.txt', 'r')
T = int(input())
def minDistacne():
    minV = 987654321
    mx, my = -1, -1
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and dist[i][j] < minV:
                minV = dist[i][j]
                mx, my = i, j
    return mx, my

def check(x, y):
    if x < 0 or y < 0 or x > N-1 or y > N-1: return False
    if visit[x][y] : return False
    return True

def dijkstra(x,y):
    dx = [0, 0 ,1, -1]
    dy = [1, -1, 0, 0]

    dist[x][y] = 0
    heapq.heappush(heap,(dist[x][y], x, y))  # 가중치, x, y

    while True:
        # x, y = minDistacne()
        d, x, y = heapq.heappop(heap)
        if x == N-1 and y == N-1 : return
        visit[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny) and dist[nx][ny] > dist[x][y] + arr[nx][ny]:
                dist[nx][ny] = dist[x][y] + arr[nx][ny]
                heapq.heappush(heap, (dist[nx][ny], nx, ny))

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dist = [[987654321] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    heap = []

    dijkstra(0,0)
    print("#{} {}".format(tc+1, dist[N-1][N-1]))
print(time.time() - start_time, 'seconds')