def check_row(call):
    global count_call, count_bingo, temp_digonal_1, temp_digonal_2
    for i in range(5):
        for j in range(5):
            if call == temp_row[i][j]:
                temp_row[i][j] = 0
                temp_col[j][i] = 0
                temp_digonal_1[i][j] = 0
                temp_digonal_2[i][j] = 0
                if [0, 0, 0, 0, 0] in temp_row:
                    count_bingo += 1
                    for i in range(len(temp_row)):
                        if temp_row[i] == [0, 0, 0, 0, 0]:
                            temp_row[i] = [99, 99, 99, 99, 99]
                return

def check_col(call):
    global count_call, count_bingo, temp_digonal_1, temp_digonal_2
    for i in range(5):
        for j in range(5):
            if [0, 0, 0, 0, 0] in temp_col:
                count_bingo += 1
                for i in range(len(temp_col)):
                    if temp_col[i] == [0, 0, 0, 0, 0]:
                        temp_col[i] = [99, 99, 99, 99, 99]
            return

def check_digonal_1(call):
    global count_call, count_bingo, count_digonal_1, temp_digonal_1
    if count_digonal_1 < 1 and [[0, 0, 0, 0, 0]] * 5 == temp_digonal_1:
        count_bingo += 1
        count_digonal_1 += 1
    return

def check_digonal_2(call):
    global count_call, count_bingo, count_digonal_2, temp_digonal_2
    if count_digonal_2 < 1 and [[0, 0, 0, 0, 0]] * 5 == temp_digonal_2:
        count_bingo += 1
        count_digonal_2 += 1
    return


import sys
sys.stdin = open("빙고.txt")

numbers = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

temp_row = [[0 for _ in range(5)] for _ in range(5)]
temp_col = [[0 for _ in range(5)] for _ in range(5)]
digonal_1 = []
digonal_2 = []
temp_digonal_1 =[[0 for _ in range(5)] for _ in range(5)]
temp_digonal_2 =[[0 for _ in range(5)] for _ in range(5)]

count_call = 0
count_bingo = 0
count_digonal_1 = 0
count_digonal_2 = 0

# temp_row, temp_col
for i in range(5):
    for j in range(5):
        temp_row[i][j] = numbers[i][j]
        temp_col[j][i] = numbers[i][j]
        if i == j:
            temp_digonal_1[i][j] = numbers[i][j]
        if i+j == 4:
            temp_digonal_2[i][j] = numbers[i][j]
print(temp_row)
print(temp_col)
print(temp_digonal_1)
print(temp_digonal_2)
for i in range(5):
    for j in range(5):
        if temp_digonal_1[i][j] != 0:
            digonal_1.append(temp_digonal_1[i][j])
        if temp_digonal_2[i][j] != 0:
            digonal_2.append(temp_digonal_2[i][j])

flag = False
for i in range(5):
    if flag:
        break
    for j in range(5):
        count_call += 1
        check_row(call[i][j])
        check_col(call[i][j])
        check_digonal_1(call[i][j])
        check_digonal_2(call[i][j])
        if count_bingo >= 3:
            print(count_call)
            flag = True
            break