import sys
sys.stdin = open("최소합_input.txt")

def dfs(x, y, sum):
    global min
    if x == N-1 and y == N-1:
        if min > sum:
            min = sum
        return

    else:
        dx = [1, 0]
        dy = [0, 1]

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < N and ny < N:
                dfs(nx, ny, sum+data[nx][ny])

T = int(input())
for tese_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)

    min = 987654321
    dfs(0, 0, data[0][0])    # x, y, sum

    print(min)