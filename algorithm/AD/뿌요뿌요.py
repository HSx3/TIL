import sys
sys.stdin = open("뿌요뿌요_input.txt")

def


T = int(input())
for i in range(1, T+1):
    data = [list(input()) for _ in range(12)]
    print(data)

    for i in range(11, -1, -1):
        for j in range(0, 6):
            BFS()
