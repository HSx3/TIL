import sys
sys.stdin = open("최소신장트리_input.txt")

T = int(input())

def findSet2(n):
    while p[n] != n:
        n = p[n]
    return n

def findSet(x):
    if x == p[x]:
        return x
    else:
        return findSet(p[x])

def mst():
    global V
    c = 0                                   # 간선개수
    s = 0                                   # 가중치의 합
    i = 0                                   # 제어변수
    while c < V:                            # MST 구성을 위해 V개의 간선을 선택
        p1 = findSet(edge[i][0])
        p2 = findSet(edge[i][1])
        if p1 != p2:                        # 사이클이 생성되지 않으면
            s += edge[i][2]                 # MST에 포함되므로 가중치 추가
            c += 1                          # 간선 개수 증가
            p[p2] = p1                      # 대표 원소 관리(union)
        i += 1                              # MST 완성 후 가중치 합 변환
    return s

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    edge = [list(map(int, input().split())) for _ in range(E)]      # 시작, 끝, 가중치
    # for i in range(len(edge)):
    #     adj[edge[0]][edge[1]] = edge[2]
    #     adj[edge[1]][edge[0]] = edge[2]

    # print(adj)
    # print(edge)
    edge.sort(key=lambda x : x[2])                                  # 간선을 가중치 기준으로 정렬
    p = list(range(V+1))                                            # 대표원소 초기화(make set)
    print('#{} {}'.format(test_case, mst()))