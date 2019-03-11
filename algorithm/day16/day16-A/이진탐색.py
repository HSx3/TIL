def inorder(node):
    global idx, N
    if node <= N:
        inorder(node * 2)       # 왼쪽 서브트리 방문
        tree[node] = idx        # 중위 순회로 현재 노드값 저장
        idx += 1
        inorder(node * 2 + 1)   # 오른쪽 서브트리 방문

import sys
sys.stdin = open("이진탐색_input.txt", "r")
T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 정점의 수
    idx = 1
    tree = [0 for i in range(N + 1)]  # 리스트를 이용한 완전 이진 트리 저장
    inorder(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))
