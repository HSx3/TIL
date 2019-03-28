import sys
sys.stdin = open("(1259)금속막대_input.txt")
T = int(input())
for tc in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    data= [[0 for _ in range(2)] for _ in range(N)]
    ans= [0] * 2 * N
    pos = 0
    for i in range(N):
        for j in range(2):
            data[i][j] = temp[pos]
            pos += 1

    #시작찾기
    spos = 0
    while(spos < N):
        j = 0
        while(j < N):
            if data[spos][0] == data[j][1]:
                break
            j += 1
        if j == N : break
        spos += 1

    # ans list에 저장하기
    pos = 0
    ans[pos] = data[spos][0]
    pos += 1
    ans[pos] = data[spos][1]
    while(1):
        for i in range(N):
            if ans[pos] == data[i][0]:
                pos += 1
                ans[pos] = data[i][0]
                pos += 1
                ans[pos] = data[i][1]
        if pos == 2*N-1:
            break
    #출력
    print("#{}".format(tc+1), end=" ")
    for i in ans:
        print(i, end=" ")
    print()


