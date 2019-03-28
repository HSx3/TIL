import sys

sys.stdin = open("Ladder1_input.txt")

for test_case in range(10):
    # for test_case in range(1):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    floor = 99
    # print(data)
    # print(data[-1].index(2))
    icecream = data[99].index(2)
    # print(icecream)

    while floor > 0:

        if icecream != 0 and icecream != 99:
            if data[floor][icecream - 1] == 0 and data[floor][icecream + 1] == 0:
                floor -= 1

            if data[floor][icecream - 1] == 1 and data[floor][icecream + 1] == 0:
                data[floor][icecream] = 0
                icecream -= 1

            if data[floor][icecream - 1] == 0 and data[floor][icecream + 1] == 1:
                data[floor][icecream] = 0
                icecream += 1

        if icecream == 0 and data[floor][icecream + 1] == 0:
            floor -= 1

        if icecream == 0 and data[floor][icecream + 1] == 1:
            data[floor][icecream] = 0
            icecream += 1

        if icecream == 99 and data[floor][icecream - 1] == 0:
            floor -= 1

        if icecream == 99 and data[floor][icecream - 1] == 1:
            data[floor][icecream] = 0
            icecream -= 1

    answer = icecream
    print(f'#{test_case + 1} {answer}')