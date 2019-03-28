def find(v, G, D):
    stack = list()
    for i in range(1, v + 1):  # 진입차수가 0인 노드 push
        if (D[i] == 0):
            stack.append(i)

    while (len(stack) != 0):    #not Empty
        t = stack.pop()
        print(t, end=' ')
        for i in range(1, v + 1):
            if (G[t][i] == 1):  # 인접노드 i에 대해
                D[i] -= 1         # 진입차수 감소
                if (D[i] == 0):  # 진입차수가 0이면 push
                    stack.append(i)

import sys
sys.stdin = open("(1267)작업순서_input.txt")
T = 10
for tc in range(T):
    V, E = map(int, input().split())  #정점, 간선
    edge = list(map(int, input().split()))
    G = [[0 for _ in range(V + 1)] for _ in range(V + 1)] #인접행렬
    D = [0] * (V + 1)  #진입차수
    for i in range(E):
        n1 = edge[i * 2]
        n2 = edge[i * 2 + 1]
        G[n1][n2] = 1  # 인접 행렬
        G[n2][n1] = 1

        D[edge[i * 2 + 1]] += 1  # 진입차수
    print('#{}'.format(tc+1), end=' ')
    find(V, G, D)
    print()