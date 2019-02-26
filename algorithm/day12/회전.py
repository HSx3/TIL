import sys
sys.stdin = open("회전_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # data = input()
    data = list(map(int, input().split()))
    # print(N, M)
    # print(data)

    count = M % N
    # print(count)
    ans = data[count]
    print(f'#{test_case} {ans}')