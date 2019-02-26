import sys
sys.stdin = open("미로의거리_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [[x for x in range(N)] for _ in range(N)]
    print(maze)


