import sys
sys.stdin = open("사냥군_input.txt","r")
T = int(input())

def solve():
    global ans
    dx = [-1, 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, 1, -1, 1, 1, -1, -1]
    for i in range(len(hunter)):    # 사냥군 명수만큼
        for j in range(8):          # 8방향 검색
            x, y = hunter[i]
            while(1):
                x += dx[j]
                y += dy[j]

                if x < 0 or x >= N or y < 0 or y >= N: break    #벽
                if arr[x][y] == 3 : break                       #바위
                if arr[x][y] == 2 : ans += 1                    #토끼


for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 0:빈공간, 1:사냥군, 2:토끼, 3:바위
    hunter =[]
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                hunter.append((i,j))
    solve()
    print("#{} {}".format(tc+1, ans))