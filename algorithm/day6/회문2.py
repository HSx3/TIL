import sys
sys.stdin =open("회문2_input.txt", "r")
# T = int(input())
# print(T)

def isPalindrome(N, M, data):
    check_Pal = []
    while M > 0:
        inverse = []
        # 가로
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i][j:j+M-1] == data[i][j+M-1:j:-1]:
                    check_Pal.append(data[i][j:j+M])

        # 세로
        for j in range(N):
            check = ''
            for i in range(N):
                check += data[i][j]
            inverse.append(''.join(check))

        for i in range(N):
            for j in range(N):
                if inverse[i][j:j+M-1] == inverse[i][j+M-1:j:-1]:
                    check_Pal.append(inverse[i][j:j+M])

        M -= 1
    answer = []
    for i in check_Pal:
        answer.append(len(i))
    # return check_Pal
    return max(answer)
    # print(check_Pal)
    # answer = max(len())





for test_case in range(10):
# for test_case in range(10):
    T = int(input())
    # print(test_case)
    N, M = 100, 100
    data = [input() for _ in range(N)]
    # data = str(input())
    # print(N, M)
    # print(N)
    # print(M)
    # print(T)
    # print(data)
    print("#{} {}".format(test_case + 1, isPalindrome(N, M, data)))