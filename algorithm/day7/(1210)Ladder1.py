
def check(data, x, y):
    global SIZE
    if x < 0 or x >= SIZE : return False
    if y < 0 or y >= SIZE : return False
    if data[x][y] == 0 : return False
    if data[x][y] == 9 : return False #방문표시
    return True

def solve(data):
    global SIZE
    x, y, newX, newY = 0, 0, 0, 0
    dx = [0, 0, -1]  # 좌우를 먼저 해야 함
    dy = [-1, 1, 0]

    for i in range(SIZE): # 시작점 좌표 값 설정
        if data[SIZE-1][i] == 2:
            x = SIZE -1
            y = i
            break

    while True:
        if x == 0 : return y
        for i in range(3):
            newX = x + dx[i]
            newY = y + dy[i]
            if check(data, newX, newY):
                x = newX
                y = newY
                data[x][y] = 9 #방문표시

import sys
sys.stdin = open("(1210)Ladder1_input.txt")
T = 10
SIZE = 100
for tc in range(T):
    no = int(input())
    data = [[0 for _ in range(SIZE)]for _ in range(SIZE)]
    for i in range(SIZE):
        data[i] = list(map(int, input().split()))
    print(f"#{no} {solve(data)}")