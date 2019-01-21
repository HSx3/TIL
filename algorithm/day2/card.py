import sys
sys.stdin = open("card_input.txt")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input()))
    count_num = []
    max_idx = 0
    for i in range(0, 10):
        data.count(i)
        count = data.count(i)
        count_num.append(count)
        for idx, number in enumerate(count_num):
            if number == max(count_num):
                max_idx = idx
    print("#{} {} {}".format(test_case, max_idx, max(count_num)))





# import sys
# sys.stdin = open("card_input.txt")
# T = int(input())
# for test_case in range(1, T + 1):
#     C = [0] * 10
#     N = int(input())
#     data = list(map(int, input()))
#
#     for i in range(N):
#         C[int(data[i])] += 1
#
#     maxIndex = 0
#     maxValue = C[0]
#     for i in range(1, 10):
#         if maxValue <= C[i]:
#             maxValue = C[i]
#             maxIndex = i
#
#     print("#{0} {1} {2}".format(test_case, maxindex, maxvalue)