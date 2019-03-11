def postOrder(node):           # 후위 순회
    global N
    if node > N:               # 유효한 노드가 아니면 0 반환
        return 0
    else:
        if tree[node] != 0:    # 리프노드인 경우 저장된 값 리턴
            return tree[node]
        else:
            a = postOrder(2 * node)  # 왼쪽 자식으로 이동
            b = postOrder(2 * node + 1)  # 오른쪽 자식으로 이동
            tree[node] = a + b  # 양쪽의 값을 더해서 저장
        return tree[node]       # 노드에 저장된 값을 반환

import sys
sys.stdin = open("노드의합_input.txt", "r")
T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split()) #노드의 수, 리프노드의 수, 값을 출력할 노드번호
    tree = [0 for i in range(N + 1)]    # 트리 생성

    for i in range(M):
        idx, value = map(int, input().split())  # 리프노드 값을 입력받아 저장
        tree[idx] = value
    postOrder(1)
    print('#{} {}'.format(tc, tree[L]))
