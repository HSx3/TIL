import sys
sys.stdin =open("글자수_input.txt", "r")
T = int(input())

for test_case in range(T):
    str1 = str(input())
    str2 = str(input())
    # print(str1)
    # print(str2)

    check = {}
    for i in str2:
        check[i] = 0
    # print(check)

    for i in str2:
        if i in str1:
            check[i] += 1
    # print(check)
    # print(list(check.values()))
    # print(max(list(check.values())))

    print("#{} {}".format(test_case + 1, max(list(check.values()))))
