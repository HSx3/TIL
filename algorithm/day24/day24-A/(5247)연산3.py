#시간초과 : Q 라이브러리 시간 더 걸림
import time
from time import strftime

start_time = time.time()
import sys
import queue
q = queue.Queue()   # 큐 생성

sys.stdin = open('(5247)연산_input.txt', 'r')
T = int(input())

def bfs(n, m):
    visit[n] = 1  # 방문 기록
    q.put(n)  # 큐에 시작 노드 인큐
    while not q.empty():  # 큐가 비어있지 않으면
        n = q.get()  # 다음 노드를 꺼내
        t = [n + 1, n - 1, n * 2, n - 10]  # 인접 노드번호 계산
        for i in range(4):
            if t[i] == m:  # 찾는 노드인 경우 거리 리턴
                return visit[n]
            if t[i] > 0 and t[i] <= 1000000:  # 유효한 노드 번호이므로
                if visit[t[i]] == 0:  # 아직 방문하지 않은 노드면
                    visit[t[i]] = visit[n] + 1  # 거리를 기록하고
                    q.put(t[i])  # 큐에 추가


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visit = [0 for _ in range(1000000+1)]
    print('#{} {}'.format(tc, bfs(N, M)))
print(time.time() - start_time, 'seconds')