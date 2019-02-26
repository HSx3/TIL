def bfs(v):  # 1에서 가장 멀리 있는 정점을 찾으시오.
    global data, V, G
    queue=[]

    queue.append(v)  #enQueue하면서 방문처리
    visited[v] = 1
    while len(queue) != 0:
        t = queue.pop(0)
        for w in range(1, V+1):
            if data[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
        if t == G:
            print(visited[w])
            break

import sys
sys.stdin = open("노드의거리_input.txt")

T = int(input())
for test_case in range(1):
    V, E = map(int, input().split())
    # print(f'V는 {V}, E는 {E}')
    V += 1

    temp = []
    for _ in range(E):
        node, route = map(int, input().split())
        # print(f'노드는 {node}, 루트는 {route}')
        temp.append(node)
        temp.append(route)
    # print(temp)
    S, G = map(int, input().split())
    print(f'S는 {S}, G는 {G}')

    data = [[0 for i in range(V + 1)] for j in range(V + 1)]  # 2차원 초기화
    # print(G)
    for i in range(0, len(temp), 2):  # 입력
        data[temp[i]][temp[i + 1]] = 1
        data[temp[i + 1]][temp[i]] = 1

    visited = [0 for _ in range(V + 1)]
    # for i in range(V + 1):  # 입력확인
    #     print("{} {}".format(i, data[i]))

    bfs(S)