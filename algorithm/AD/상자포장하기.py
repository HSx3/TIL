import sys
sys.stdin = open("상자포장하기_input.txt")

def DFS(no, Asum, Bsum, past_A, past_B):
    global result

    if no >= N:
        sums = Asum + Bsum
        if result < sums:
            result = sums
        return

    if boxes[no] < past_A:
        DFS(no+1, Asum + boxes[no], Bsum, boxes[no], past_B)
    if boxes[no] > past_B:
        DFS(no+1, Asum, Bsum + boxes[no], past_A, boxes[no])
    DFS(no+1, Asum, Bsum, past_A, past_B)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))

    result = 0
    DFS(0, 0, 0, 1000, 0)
    print(result)