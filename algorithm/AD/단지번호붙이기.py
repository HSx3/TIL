import sys
sys.stdin = open("단지번호붙이기_input.txt")

def DFS():


N = int(input())
data = [list(map(int, input())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if data[i][j] ==1:
            i = sx
            j = sy
            DFS()