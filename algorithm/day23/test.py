import sys
import heapq
sys.stdin = open("최소이동거리_input.txt")
INF = sys.maxsize

# 다익스트라 알고리즘
def solve(adjacent, K):
    prev = [-1] * (len(adjacent) + 1)    # predecessor
    dist = [INF] * (len(adjacent) + 1)   # source로부터의 최소 거리 배열
    dist[K] = 0

    priority_queue = []
    heapq.heappush(priority_queue, [0, K])

    while priority_queue:
        # 거리가 제일 작은 노드 선택
        current_dist, here = heapq.heappop(priority_queue)

        # 인접 노드 iteration
        for there, length in adjacent[here].items():
            next_dist = dist[here] + length

            if next_dist < dist[there]:
                dist[there] = next_dist
                prev[there] = here
                heapq.heappush(priority_queue, [next_dist, there])

    return dist, prev

if __name__ == "__main__":
    T = int(input())
    V, E = map(int, input().split())
    # K = int(input())
    adjacent = [{} for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())

        # 만약 동일한 경로의 간선이 주어질 경우 적은 비용의 간선 선택
        if v in adjacent[u]:
            adjacent[u][v] = min(adjacent[u][v], w)
        else:
            adjacent[u][v] = w

    dist, prev = solve(adjacent, 0)
    print(adjacent)

    for d in dist[1:]:
        print(d if d != INF else "INF")