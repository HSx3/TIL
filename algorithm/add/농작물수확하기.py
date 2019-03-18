import sys
sys.stdin = open("농작물수확하기_input.txt")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    total = 0
    j = 0
    for i in range(0, (N//2)+1):
        for j in range((N//2)-i, (N//2)+i+1):
            total += data[i][j]
    k = 1
    for i in range((N//2)+1, N):
        for j in range(N+k-3, 0-k+1, -1):
            total += data[i][j]
        k -= 1

    print('#{} {}'.format(test_case, total))


'''
    mid = N//2
    start = mid
    end = mid
    sum = 0
    for i in range(N):
        for j in range(start, end+1, 1):
            sum += data[i][j]
        if i < mid:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print("#{} {}".format(test_case, sum))
'''