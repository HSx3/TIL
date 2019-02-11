import sys
sys.stdin = open("Ladder1_input.txt")

# for test_case in range(10):
for test_case in range(1):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    floor = 98
    print(data)
    # print(data[-1].index(2))
    icecream = data[99].index(2)
    print(icecream)
    left = icecream-1
    right = icecream+1

    while floor > 0:
        if data[floor][left] == 0 and data[floor][right] == 0:
            floor -= 1
        if data[floor][left] == 1 and data[floor][right] == 0:
            data[floor][left] = 0
            left -= 1
        if data[floor][left] == 0 and data[floor][right] == 1:
            data[floor][left] = 0
            right += 1
    # while floor < 0:
    #     if data[floor][icecream-1] == 0 and data[floor][icecream+1] == 0:
    #         floor -= 1
    #     if data[floor][icecream-1] == 1 and data[floor][icecream+1] == 0:
    #         data[floor][icecream-1] = 0
    #         icecream-1 -= 1
    #     if data[floor][icecream-1] == 0 and data[floor][icecream+1] == 1:
    #         data[floor][icecream+1] = 0
    #         icecream+1 += 1
    # answer = data[0][icecream]
    # answer = left
    answer = right
    print(f'#{test_case} {answer}')