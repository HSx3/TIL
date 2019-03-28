import sys
sys.stdin = open("주사위던지기2_input.txt")

def DFS(no):
    if no>N:
        for i in range(1, N+1):
            print(rec[i], end=' ')
        print()
        return
    for i in range(1, 7):
        rec[no] = i
        DFS(no+1)

# 눈의 중복을 배제한 순열
def DFS2(no):
    if no>N:
        for i in range(1, N+1):
            print(rec[i], end=' ')
        print()
        return
    for i in range(1, 7):
        if chk[i]:
            continue
        rec[no] = i
        DFS2(no+1)
        chk[i] = 0

# 눈의 합이 M인 경우만 출력
def DFS3(no, nsum):
    if no>N:
        if nsum==M:
            for i in range(1, N+1):
                print(rec[i], end=' ')
            print()
        return
    for i in range(1, 7):
        rec[no] = i
        DFS3(no+1, nsum+i)
        chk[i] = 0


# main
N, M = map(int, input().split())
rec = [0]*8 # 주사위별 눈 기록배열
chk = [0]*7 # 눈 사용여부 체크배열
# DFS(1)
# DFS2(1)
DFS3(1, 0)   # 1번 주사위부터 시작, 합계는 0