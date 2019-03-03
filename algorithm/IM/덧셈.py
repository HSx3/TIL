import sys
sys.stdin = open("덧셈.txt")

S, X = map(str, input().split())
# print(S, X)

for_sum = []        # + 함께 출력
for_result = []     # int 변환 후 sum

for i in range(0, len(S)-1):
    check = S[0:i+1] + '+' + S[i+1:]
    for_sum.append(check)
# print(for_sum)

for i in range(len(for_sum)):
    for_int = for_sum[i].split('+')
    SA, SB = map(int, for_int)
    # print(SA)
    # print(SB)
    for_result.append(SA+SB)
    if SA+SB == int(X):
        print(f'{SA}+{SB}={X}')
# print(for_result)

if int(X) not in for_result:
    print('NONE')






