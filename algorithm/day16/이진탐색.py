




import sys
sys.stdin = open("이진탐색_input.txt")

T = int(input())
for _ in range(T):
    N = int(input())
    tree = [0]*(N+1)
    idx = 1
    for i in range(1, N):
        if i <= N:
            tree[i] = i

