import sys
sys.stdin = open("(1974)스도쿠검증_input.txt","r")
T = int(input())
SIZE = 9
for tc in range(T):
    flag = 1
    arr = [list(map(int, input().split())) for _ in range(SIZE)]

    for i in range(SIZE):
        visit = [0] * (SIZE + 1)
        for j in range(SIZE):
            visit[arr[i][j]] += 1
            if visit[arr[i][j]] > 1 :
                flag = 0
                break

    for i in range(SIZE):
        visit = [0] * (SIZE + 1)
        for j in range(SIZE):
            visit[arr[j][i]] += 1
            if visit[arr[j][i]] > 1 :
                flag = 0
                break

    for i in range(0, SIZE, 3):
        for j in range(0, SIZE,3):
            visit = [0] * (SIZE + 1)
            for x in range(3):
                for y in range(3):
                    visit[arr[i+x][j+y]] += 1
                    if visit[arr[j][i]] > 1:
                        flag = 0
                        break
    print("#{} {}".format(tc+1, flag))