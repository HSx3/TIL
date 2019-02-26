import sys
sys.stdin = open("노드의거리_input.txt")

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    print(f'V는 {V}, E는 {E}')
    V += 1

    temp = []
    for _ in range(E):
        node, route = map(int, input().split())
        print(f'노드는 {node}, 루트는 {route}')
        temp.append(node)
        temp.append(route)
    # print(temp)
    S, G = map(int, input().split())
    print(f'S는 {S}, G는 {G}')

    G = [[0 for i in range(V + 1)] for j in range(V + 1)]  # 2차원 초기화

    for i in range(0, len(temp), 2):  # 입력
        G[temp[i]][temp[i + 1]] = 1
        G[temp[i + 1]][temp[i]] = 1

    visited = [0 for _ in range(V + 1)]