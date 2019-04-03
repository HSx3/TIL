a = [1,2,3] # 구슬
b = [0, 0, 0] # 구슬을 담을 상자
N = 3

def DFS(no): # a[no]번째 구슬을 상자에 담거나 담지 않는 모든 경우
# 1] 리턴조건 : N번째이면 인쇄후 리턴
    if no >= N:
        for i in range(N): print(b[i], end=' ')
        print()
        return
# 2] 현재 구슬을 고르기(b배열에 담기)
    b[no] = a[no]
    DFS(no+1)
# 3] 현재 구슬을 고르지 않기(b배열에 담지 않기)
    b[no] = 0
    DFS(no+1)

def DFS2(no, cnt):  # N개 중 M개를 고르는 조합
    if no >= N:
        if cnt == 2:
            for i in range(N): print(b[i], end=' ')
            print()
        return
    b[no] = a[no]
    DFS2(no+1, cnt+1)
    b[no] = 0
    DFS2(no+1, cnt)

def DFS3(no, start):
    for i in range(N):
        print(b[i], end=' ')
    print()
    if no >= N or start >= N:
        return

    for i in range(start, N):   # a[i]
        b[no] = a[i]
        DFS3(no+1, i+1)
        b[no] = 0

# main ============================
# DFS(0) # a[0]요소 구슬부터 시작
# print()
# DFS2(0, 0)
DFS3(0, 0)  # b[0] 담기 시작, a[0] 구슬부터 시작