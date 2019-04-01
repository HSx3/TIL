import sys
sys.stdin = open("퍼킷_input.txt")

def DFS(no):
    global total_S, total_B
    total_Ss = 1
    total_Bb = 0
    if no >= N:
        for i in range(N):
            if S_b[i] != 0:
                total_Ss *= S_b[i]
            if B_b[i] != 0:
                total_Bb += B_b[i]

        total_S.append(total_Ss)
        total_B.append(total_Bb)
        return

    S_b[no] = Ss[no]
    B_b[no] = Bb[no]
    DFS(no+1)

    S_b[no] = 0
    B_b[no] = 0
    DFS(no+1)


N = int(input())
Ss = []
Bb = []
total_S = []
total_B = []
for i in range(N):
    S, B = map(int, input().split())
    Ss.append(S)
    Bb.append(B)
S_b = [0]*N
B_b = [0]*N
DFS(0)

answer = 987654321
for i in range(len(total_S)-1):
    if answer > abs(total_S[i] - total_B[i]):
        answer = abs(total_S[i] - total_B[i])
print(answer)