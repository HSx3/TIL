import sys
sys.stdin = open("달팽이사각형.txt")

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
r, c = 0, -1 # 한칸 이전위치에서 시작
num = 0 # 카운팅할 숫자
cnt = N # 루프 회전수
while num < N*N:
    # 오른쪽방향
    for i in range(cnt):
        c += 1 # 열좌표만 증가하면서 오른방향으로
        num += 1
        arr[r][c] = num
    cnt -= 1
    # 아래방향
    for i in range(cnt):
        r += 1 # 행좌표만 증가하면서 아래방향으로
        num += 1
        arr[r][c] = num
    # 왼쪽방향
    for i in range(cnt):
        c -= 1 # 열좌표만 감소하면서 왼쪽방향으로
        num += 1
        arr[r][c] = num
    cnt -= 1
    # 위쪽방향
    for i in range(cnt):
        r -= 1 # 행좌표만 감소하면서 위쪽방향으로
        num += 1
        arr[r][c] = num

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()