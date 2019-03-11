def inorder(node):
    global idx, N
    if node <= N:
        inorder(node * 2)       # 왼쪽 서브트리 방문
        tree[node] = idx        # 중위 순회로 현재 노드값 저장
        idx += 1
        inorder(node*2 + 1)     # 오른쪽 서브트리 방문




import sys
sys.stdin = open("이진탐색_input.txt")

T = int(input())
for _ in range(T):
    N = int(input())    # 정점의 수
    tree = [0]*(N+1)
    idx = 1
    for i in range(1, N):   # 리스트를 이용한 완전 이진트리 저장
        if i <= N:
            tree[i] = i

