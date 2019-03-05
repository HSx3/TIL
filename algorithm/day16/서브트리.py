def preorder(node):
    global count
    if node != 0:
        count += 1
        preorder(tree[node][0])
        preorder(tree[node][1])
    return count


import sys
sys.stdin = open("서브트리_input.txt")

T = int(input())
for test_case in range(T):
    E, N = map(int, input().split())    # E : 간선의 개수, N : 노드
    V = E+1
    tree = [[0 for _ in range(3)] for _ in range(V + 1)]
    temp = list(map(int, input().split()))
    count = 0
    # print(tree)

    for i in range(E):
        n1 = temp[i * 2]
        n2 = temp[i * 2 + 1]
        if not tree[n1][0]:     # 값이 비어있으면 왼쪽에 넣기
            tree[n1][0] = n2
        else:                   # 왼쪽이 채워져있으면 오른쪽에 넣기
            tree[n1][1] = n2
        tree[n2][2] = n1        # 부모값 채우기

    print("#{} {}".format(test_case+1, preorder(N)))