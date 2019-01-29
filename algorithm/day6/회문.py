import sys
sys.stdin =open("회문_input.txt", "r")
T = int(input())

def isPalindrome(N, M, data):
    inverse = []
    if N == M:
        # 가로
        for i in data:
            if i[:M] == i[::-1]:
                return i[:M]

        # 세로
        for j in range(N):
            check = ''
            for i in range(N):
                check += data[i][j]
            inverse.append(''.join(check))
        # print(inverse)

        for i in inverse:
            if i[:M] == i[::-1]:
                return i[:M]

    else:
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j:j+M-1] == data[i][j+M-1:j:-1]:
                    return data[i][j:j+M-1]

for test_case in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    # data = str(input())
    # print(N, M)
    # print(N)
    # print(M)
    # print(data)
    print("#{} {}".format(test_case + 1, isPalindrome(N, M, data)))