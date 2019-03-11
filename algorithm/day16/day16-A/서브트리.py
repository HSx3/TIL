def preorder(n):                                # 전위 순회
    global cnt
    if n != 0:
        cnt += 1                                    # 방문한 노드 개수
        preorder(tree[n][0])
        preorder(tree[n][1])

import sys
sys.stdin = open('서브트리_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())  #간선, 시작정점
    tree = [[0]*3 for i in range(E+2)]
    temp = list(map(int, input().split()))
    cnt = 0

    for i in range(E):                              # E개의 간선을 처리
        p = temp[i * 2]
        c = temp[i * 2 + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:                                           # 이미 자식이 한 개 있는 경우
            tree[p][1] = c

        tree[c][2] = p  # 부모도 저장
    preorder(N)     
    print('#{} {}'.format(tc, cnt))
