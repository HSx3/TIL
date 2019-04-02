import sys
sys.stdin = open('(5249)최소신장트리_input.txt', 'r')
T = int(input())

def mst():
    global V
    c = 0   #간선갯수
    s = 0   #가중치의 합
    i = 0   #제어변수
    while c < V:                        # MST 구성을 위해 V개의 간선을 선택
        p1 = findSet(edge[i][0])            # 두 노드의 대표원소 알아내기
        p2 = findSet(edge[i][1])
        if p1 != p2:                # 사이클이 생성되지 않으면
            s += edge[i][2]         # MST에 포함되므로 가중치 추가
            c += 1                      # 간선 개수 증가
            p[p2] = p1                  # 대표 원소 관리
        i += 1                          # 저장된 다음 간선으로 이동
    return s                        # MST 완성 후 가중치 합 반환

def findSet(n):                         # 대표원소 검색
    while p[n]!=n:
        n = p[n]
    return n

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for i in range(E)]
    edge.sort(key=lambda x : x[2])                  # 간선을 가중치 기준으로 정렬
    p = list(range(V+1))                        # 대표원소 초기화
    print('#{} {}'.format(tc, mst()))
