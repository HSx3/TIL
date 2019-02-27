def check_type(temp):
    global length, check_width, check_height, width, height
    length_check = 0
    Sw = sorted(check_width)
    Sh = sorted(check_height)
    a = Sw[-1] - Sw[0] + 1
    b = Sh[-1] - Sh[0] + 1

    if a != width or b != height:
        if a < width or b < height:
            for i in range(len(temp)):
                for j in range(len(temp)):
                    if temp[i][j] > n:
                        return 3
            else:
                return 2
        else:
            return 4
    else:
        return 1


import sys
sys.stdin = open("색종이 배치.txt")

temp = [[0 for _ in range(102)] for _ in range(102)]
paper = 2
length = 0
check_width = []
check_height = []
width = 0
height = 0
for n in range(1, paper+1):
    r, c, x, y = map(int, input().split())
    length += x
    length += y
    width += x
    height += y

    # 색종이 배치
    for i in range(r, r+x):
        for j in range(c, c+y):
            if temp[i][j] == 0:
                temp[i][j] = n
                check_width.append(i)
                check_height.append(j)
            else:
                temp[i][j] += n

print(check_type(temp))

# print(width)
# print(height)
# print(length)
# print(check_width)
# print(check_height)
# print(check_width[-1]-check_width[0]+1)

