import sys
sys.stdin = open("책꽂이_input.txt")

def DFS(no):
    global answers, B

    if no >= N:
        total = 0
        for i in range(N):
            total += b[i]
        if total >= B:
            answers.append(total)
        return
    b[no] = cows[no]
    DFS(no+1)

    b[no] = 0
    DFS(no+1)


T = int(input())
for test_case in range(T):
    N, B = map(int, input().split())
    cows = []
    b = [0]*N
    answers = []
    for i in range(N):
        H_i = int(input())
        cows.append(H_i)

    DFS(0)
    answers.sort()
    print(answers[0]-B)