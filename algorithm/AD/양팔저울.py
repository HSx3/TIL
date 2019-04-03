import sys
sys.stdin = open("양팔저울_input.txt")

def DFS(no, Lsum, Rsum):
    # 현재 추를 사용하거나 (왼쪽, 오른쪽저울에 사용) 사용하지 않기
    # 양쪽저울무게가 같으면 성공
    global sol
    if no >= CN:
        if Lsum == Rsum:
            sol = 1
        return

    DFS(no+1, Lsum+chu[no], Rsum)   # 현재 추를 왼쪽에 올리기
    DFS(no+1, Lsum, Rsum+chu[no])   # 현재 추를 오른쪽에 올리기
    DFS(no+1, Lsum, Rsum)   # 현재 추를 사용하지 않기



# main ----------------------------------------------------
CN = int(input())
chu = list(map(int, input().split()))
BN = int(input())
ball = list(map(int, input().split()))
rec = [0] * CN

for i in range(BN):
    sol = 0
    DFS(0, ball[i], 0)  # 0번추부터 시작, 왼쪽저울무게는 구슬을 초기값으로, 오른저울무게 0
    if sol:
        print('Y')
    else:
        print('N')
