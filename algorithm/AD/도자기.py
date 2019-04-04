import sys
sys.stdin = open("도자기_input.txt")

def DFS(no, count):
    global answers
    answer = []

    if no >= N:
        if count == M:
        #     print(check)
            for i in range(N):
                if check[i] != 0:
                    answer.append(check[i])
            # print(answer)
            if sorted(answer) not in answers:
                answers.append(sorted(answer))
            # print(answers)
        return

    check[no] = data[no]
    DFS(no+1, count+1)
    check[no] = 0
    DFS(no+1, count)


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    check = [0] * N
    answers = []
    DFS(0, 0)
    print(len(answers))