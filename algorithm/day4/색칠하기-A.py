def printArr(a):
    for i in range(N):
        for j in range(N):
            print(a[i][j], end="")
        print()
    print()

import sys
sys.stdin = open("색칠하기_input.txt", "r")
T = int(input())
N = 10
for test_case in range(1, T+1):
    data = [[0] * N for i in range(N)]
    n = int(input())
    cnt = 0
    #색칠하기
    for k in range (n):
        r1,c1,r2,c2,color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                data[i][j] += color
    #printArr(data)
    #겹쳐진 칸수 카운팅
    for i in range(N):
        for j in range(N):
            if(data[i][j] == 3): cnt += 1

    print("#{} {}".format(test_case, cnt))