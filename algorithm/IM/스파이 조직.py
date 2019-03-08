import sys
sys.stdin = open("스파이 조직.txt")

N, S = map(str, input().split())
N = int(N)
S = list(S)
print(S)

spy_N = []
# print(type(spy))

spy_number = []
for i in range(len(S)):
    if S[i].isdigit():
        S[i] = int(S[i])
        spy_number.append(S[i])
        print(S[i])
print(spy_number)

level = 0


