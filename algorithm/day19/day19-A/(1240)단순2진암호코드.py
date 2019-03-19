import sys
sys.stdin=open("(1240)단순2진암호코드_input.txt", "r")
code = [[[[[[[0 for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(2)]for _ in range(2)]
code[0][0][0][1][1][0][1] = 0 # 0
code[0][0][1][1][0][0][1] = 1 # 1
code[0][0][1][0][0][1][1] = 2 # 2
code[0][1][1][1][1][0][1] = 3 # 3
code[0][1][0][0][0][1][1] = 4 # 4
code[0][1][1][0][0][0][1] = 5 # 5
code[0][1][0][1][1][1][1] = 6 # 6
code[0][1][1][1][0][1][1] = 7 # 7
code[0][1][1][0][1][1][1] = 8 # 8
code[0][0][0][1][0][1][1] = 9 # 9
T =int(input())

def findPos(arr): #뒤에서 1찾기
    for i in range(len(arr)):
        for j in range(len(arr[i])-1, -1, -1):
            if arr[i][j] ==  1:
                return (i, j)

for tc in range(T):
    r, c = map(int, input().split())
    arr = [list(map(int, input())) for i in range(r)]
    a_code = []  # 암호코드
    a_value = 0  # 암호_검증
    sx, sy = findPos(arr)

    for i in range(8): #시작위치로 가기
        sy -= 7
    sy += 1

    for i in range(8):
        a_code.append(code[arr[sx][sy]][arr[sx][sy+1]][arr[sx][sy+2]][arr[sx][sy+3]][arr[sx][sy+4]][arr[sx][sy+5]][arr[sx][sy+6]])
        sy += 7

    a_value = (a_code[0] + a_code[2] + a_code[4] + a_code[6])*3 + a_code[1] + a_code[3] + a_code[5] + a_code[7]
    if a_value % 10 == 0:
        print("#{} {}".format(tc+1, sum(a_code)))
    else:
        print("#{} {}".format(tc+1, 0))
