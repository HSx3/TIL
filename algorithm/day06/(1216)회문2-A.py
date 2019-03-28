import sys
sys.stdin = open("(1216)회문2_input.txt")
T = 10
SIZE = 100

def rowMax(data, SIZE):  #행방향 체크
    len = SIZE
    while len >= 0:
        for i in range(SIZE):
            for j in range(SIZE - len + 1):
                flag = 1
                for k in range(len//2):
                    if data[i][j + k] != data[i][j + len - 1 - k]: # len-1 : 마지막 인덱스
                        flag = 0
                        break
                if flag : return len
        len += -1

def colMax(data, SIZE): #열방향 체크
    len = SIZE
    while len >= 0:
        for i in range(SIZE):
            for j in range(SIZE - len + 1):
                flag = 1
                for k in range(len//2):
                    if data[j + k][i] != data[j + len - 1 - k][i]:
                        flag = 0
                        break
                if flag : return len
        len += -1

for tc in range(T):
    no = int(input())
    max, rmax, cmax = 0, 0, 0
    data = [0 for _ in range(SIZE)]
    for i in range(SIZE):
        data[i] = list(input())

    rmax = rowMax(data, SIZE)
    cmax = colMax(data, SIZE)
    if rmax > cmax : max = rmax
    else: max = cmax

    print(f"#{tc+1} {max}")
