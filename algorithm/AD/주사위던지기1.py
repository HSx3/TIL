import sys
sys.stdin = open("주사위던지기1_input.txt")


# 중복순열
def dfs1(n):
    if n == N:
        print(*dice)
        return
    for i in range(1, 7):
        dice[n] = i
        dfs1(n + 1)


# 중복조합
def dfs2(n, k):
    if n == N:
        print(*dice)
        return
    for i in range(k, 7):
        dice[n] = i
        dfs2(n + 1, i)


# 순열
def dfs3(n):
    if n == N:
        print(*dice)
        return
    for i in range(1, 7):
        if visit[i]: continue
        dice[n] = i
        visit[i] = 1
        dfs3(n + 1)
        visit[i] = 0


# 조합
def dfs4(n, k):
    if n == N:
        print(*dice)
        return
    for i in range(k, 7):
        dice[n] = i
        dfs4(n + 1, i + 1)


# main
N, M = map(int, input().split())
visit = [0] * 7
dice = [0] * N

if M == 1: dfs1(1)  # 눈의 중복순열 1번 주사위부터 시작
elif M == 2: dfs2(1, 1)   # 눈의 중복조합 : 1번 주사위부터 시작, 1눈부터 시작
elif M == 3: dfs3(1)  # 눈의 중복배제한 순열
elif M == 4: dfs4(1, 1)


