def dfs(S):
    global check, visited, V, E, G
    visited[S] = 1
    # print(visited)
    # print(v, end=" ")

    for w in range(V):
        if check[S][w] == 1 and visited[w] == 0:
            dfs(w)

    if visited[G] == 1:
        return 1
    else:
        return 0

import sys
sys.stdin = open("그래프경로_input.txt")

N = int(input())
for test_case in range(N):
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
    # print(f'S는 {S}, G는 {G}')

    check = [[0 for i in range(V)] for j in range(V)]  # 2차원 초기화
    visited = [0 for i in range(V)]

    for i in range(0, len(temp), 2):  # 입력
        check[temp[i]][temp[i + 1]] = 1

    # print(check)


    print(f'#{test_case+1} {dfs(S)}')
    # for i in range(V):  # 입력확인
    #     print("{} {}".format(i, check[i]))


# dfs(S)

# print(f'#{test_case} {dfs(1)}')
    # answer = 0
    # print(f'{test_case} {answer}')