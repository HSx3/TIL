import sys
sys.stdin = open("퍼킷_input.txt")

def DFS(no, sin, ssun):
    global nmin
    if no >= N:
        if sin != 1 and ssun != 0:
            calc = abs(sin - ssun)
            if nmin > calc:
                nmin = calc
        return


    DFS(no+1, sin*Ss[no], ssun+Bs[no])
    DFS(no+1, sin, ssun)


N = int(input())
Ss = []
Bs = []
for i in range(N):
    S, B = map(int, input().split())
    Ss.append(S)
    Bs.append(B)
# print(Ss)
# print(Bs)

rec_S = [0] * N
rec_B = [0] * N
nmin = 987654321

DFS(0, 1, 0)
print(nmin)