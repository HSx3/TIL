import sys
sys.stdin = open("최대상금_input.txt")

def perm(n,k,cnt):
    global N
    if cnt == 0 :
        cnt = 0
        # print(dummy)
    else:
        for i in range(k,n):
            dummy[k], dummy[i] = dummy[i], dummy[k]
            perm(n, k+1 , cnt-1)
            dummy[i], dummy[k] = dummy[k], dummy[i]

T = int(input())

for test_case in range(T):
    data, N = map(int, input().split())
    dummy = list(str(data))
    cnt = N+1
    # perm(len(dummy), 0, cnt)

    A = '호성이 바보'
    while True:
        for i in range(len(A)):
            for j in range(len(A)-1, -1, -1):
                print((" "*(j-i),A[j]," "*(j-i))*5,end="")
            print()
