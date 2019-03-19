import copy
import sys
sys.stdin = open("정식이의은행업무_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    data2 = list(input())
    data3 = list(input())
    print(data2, data3)
    for i in range(len(data2)):
        for j in range(len(data3)):
            if data2[i] == '0':
                data2[i] = '1'
                if data3[j] == '0':
                    data3[j] = '1'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))
                    data3[j] = '2'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))
                elif data3[j] == '1':
                    data3[j] = '0'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))
                    data3[j] = '2'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))
                elif data3[j] == '2':
                    data3[j] = '0'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))
                    data3[j] = '1'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))

            elif data2[i] == '1':
                data2[i] = '0'
                if data3[j] == '0':
                    data3[j] = '1'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))
                    data3[j] = '2'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))
                elif data3[j] == '1':
                    data3[j] = '0'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))
                    data3[j] = '2'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))
                elif data3[j] == '2':
                    data3[j] = '0'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))
                    data3[j] = '1'
                    if int(data2, 2) == int(data3, 3):
                        print("#{} {}".format(test_case+1, int(data2, 2)))