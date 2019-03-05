import sys
sys.stdin = open("회문1_input.txt")

T = 10
for test_case in range(T):
    length = int(input())
    data = [list(map(str, input())) for _ in range(8)]
    datadata = [[0 for i in range(8)] for j in range(8)]
    count = 0

    # row
    for i in range(8):
        for j in range(8-length+1):
            check = data[i][j:j+length]
            if check == check[::-1]:
                count += 1

    for i in range(8):
        for j in range(8):
            datadata[i][j] = data[j][i]

    # col
    for i in range(8):
        check = ''
        for j in range(8-length+1):
            check = datadata[i][j:j+length]
            # print(check)
            if check == check[::-1]:
                count += 1
    print('#{} {}'.format(test_case + 1, count))