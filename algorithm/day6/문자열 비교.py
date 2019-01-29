import sys
sys.stdin =open("문자열 비교_input.txt", "r")
T = int(input())

def bruteForce(str2, str1):
    i, j =0, 0
    while j < len(str1) and i < len(str2):
        if str2[i] != str1[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(str1):
        return 1
    else:
        return 0


for test_case in range(T):
    str1 = str(input())
    str2 = str(input())
    print("#{} {}".format(test_case+1, bruteForce(str2, str1)))


