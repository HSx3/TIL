import sys
sys.stdin = open("재미있는 오셀로 게임_input.txt")

def check(Y, X):
    global N, board

    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(8):
        ny = Y + dy
        nx = X + dx

        if ny < 0 or ny >= N:
            continue
        if nx < 0 or nx >= N:
            continue
        else:
            if board[Y][X] == 'B':
                temp[Y][X] = 'B'
                if board[ny][nx] == 'B':
                    break
                elif board[ny][nx] == 'W':
                    temp[ny][nx] = 'W'
                    Y = ny
                    X = nx
                    continue
                elif board[ny][nx] == 0:
                    continue

T = int(input())
N, M = map(int, input().split())    # N : 보드길이, M : 돌을 놓는 횟수

board = [[0 for _ in range(N)] for _ in range(N)]

board[(N//2) - 1][(N//2) - 1] = 'W'
board[(N//2) - 1][N//2] = 'B'
board[N//2][(N//2) - 1] = 'B'
board[N//2][N//2] = 'W'
print(board)

temp = [[0 for _ in range(N)] for _ in range(N)]
temp[(N//2) - 1][(N//2) - 1] = 'W'
temp[(N//2) - 1][N//2] = 'B'
temp[N//2][(N//2) - 1] = 'B'
temp[N//2][N//2] = 'W'

for i in range(len(board)):
    x, y, c = map(int, input().split())
    X = x-1
    Y = y-1
    if c == 1:
        board[Y][X] = 'B'
    elif c == 2:
        board[Y][X] = 'W'
    check(Y, X)