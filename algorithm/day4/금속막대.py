import sys
sys.stdin = open("금속막대_input.txt")

T = int(input()) # input line1
# for test_case in range(1, T + 1):
for test_case in range(1, T + 1):
    N = int(input())  # 줄 수
    data = list(map(int, input().split()))
    print(data)

    # line = []
    # line += str(data[0]) + str(data[1])
    # print(line)


    line = []
    # front = ''
    # front_line = ''
    line += str(data[0]) + str(data[1])
    for i in range(2, len(data)):
        if i % 2 == 0:
            if data[i] == line[-1]:
                line += str(data[i]) + str(data[i+1])
            elif data[i+1] == line[0]:
                line = data[i] + data[i+1]
            # else:
            #     front += str(data[i]) + str(data[i+1])

    print(line)



    #
    # line = []
    # # front = ''
    # # front_line = ''
    # line += str(data[0]) + str(data[1])
    # for i in range(2, len(data)):
    #     if i % 2 == 0:
    #         if str(data[i]) == line[-1]:
    #             line += str(data[i]) + str(data[i+1])
    #         elif str(data[i+1]) == line[0]:
    #             line = str(data[i]) + str(data[i+1])
    #         # else:
    #         #     front += str(data[i]) + str(data[i+1])
    #
    # print(line)


    # print(front + line)

            # for j in data:
            #     if j not in
            #     line[0] = j
            # print(line[0])

        # if i % 2 == 0:

            # line += str(data[i]) + ' ' + str(data[i+1]) + ' '
    # print(line)









    # print(f'#{test_case} {select(data)}')