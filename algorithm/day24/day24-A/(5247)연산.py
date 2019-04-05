# 큐를 C처럼 사용
import time
from time import strftime
start_time = time.time()
import sys
sys.stdin = open('(5247)연산_input.txt', 'r')
T = int(input())

def bfs(n, m):
    f = r = -1
    visit[n] = 1  # 방문 기록
    r += 1
    Q[r] = n  # 큐에 시작 노드 인큐
    while f != r:  # 큐가 비어있지 않으면
        f += 1
        n = Q[f]  # 다음 노드를 꺼내
        t = [n + 1, n - 1, n * 2, n - 10]  # 인접 노드번호 계산
        for i in range(4):
            if t[i] == m:  # 찾는 노드인 경우 거리 리턴
                return visit[n]
            if t[i] > 0 and t[i] <= 1000000:  # 유효한 노드 번호이므로
                if visit[t[i]] == 0:  # 아직 방문하지 않은 노드면
                    visit[t[i]] = visit[n] + 1  # 거리를 기록하고
                    # q.append(t[i])  # 큐에 추가
                    r += 1
                    Q[r] = t[i]


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Q = [0]*(1000000)

    visit = [0 for _ in range(1000000+1)]
    print('#{} {}'.format(tc, bfs(N, M)))

print(time.time() - start_time, 'seconds')