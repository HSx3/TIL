def SearchParent(n):
    if tree[n][2] != 0:
        L.append(tree[n][2])
        SearchParent(tree[n][2])
    return L

def Search(L1, L2):
    for i in L2:
        if i in L1:
            return i

def preorder(node):
    global count
    if node != 0:
        count += 1
        preorder(tree[node][0])
        preorder(tree[node][1])
    return count


import sys
sys.stdin = open("공통조상_input.txt")

T = int(input())

for test_case in range(T):
    V, E, node1, node2 = map(int, input().split())
    tree = [[0 for _ in range(3)] for _ in range(V + 1)]
    temp = list(map(int, input().split()))
    count = 0

    for i in range(E):
        n1 = temp[i * 2]
        n2 = temp[i * 2 + 1]
        if not tree[n1][0]:     # 값이 비어있으면 왼쪽에 넣기
            tree[n1][0] = n2
        else:                   # 왼쪽이 채워져있으면 오른쪽에 넣기
            tree[n1][1] = n2
        tree[n2][2] = n1        # 부모값 채우기

    L = []
    Parent_node1 = SearchParent(node1)
    L = []
    Parent_node2 = SearchParent(node2)
    n = Search(Parent_node1, Parent_node2)
    print("#{} {} {}".format(test_case + 1, n, preorder(n)))