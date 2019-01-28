import sys
sys.stdin = open("GNS_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    check = [0] * 10
    # print(test_case)
    temp = input() # dummy
    data = list(map(str, input().split()))
    # print(temp)
    # print(data)
    # print(len(data))
    checklist = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in data:
        if i == 'ZRO':
            check[0] += 1
        if i == 'ONE':
            check[1] += 1
        if i == 'TWO':
            check[2] += 1
        if i == 'THR':
            check[3] += 1
        if i == 'FOR':
            check[4] += 1
        if i == 'FIV':
            check[5] += 1
        if i == 'SIX':
            check[6] += 1
        if i == 'SVN':
            check[7] += 1
        if i == 'EGT':
            check[8] += 1
        if i == 'NIN':
            check[9] += 1

    print("#{}".format(test_case))
    for i in range(len(check)):
        count = check[i]
        while count > 0:
            print(checklist[i], end = " ")
            count -= 1