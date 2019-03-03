import sys
sys.stdin = open("투표.txt")

data = []
N = int(input())    # 학생의 수
for i in range(N):
    data.append(list(map(int, input().split())))
# print(data)

candidate = [[0]*4 for _ in range(3)]

for j in range(3):
    for i in range(len(data)):
        if data[i][j] == 1:
            candidate[j][0] += 1
            candidate[j][1] += 1
        elif data[i][j] == 2:
            candidate[j][0] += 2
            candidate[j][2] += 1
        elif data[i][j] == 3:
            candidate[j][0] += 3
            candidate[j][3] += 1
# print(candidate)

ans = sorted(candidate)[::-1]
# print(ans)
for i, vote in enumerate(candidate):
    if ans[0] == vote:
        if ans[0] == ans[1] == ans[2] or ans[0] == ans[1]:
            print(f'{0} {candidate[i][0]}')
            break
        else:
            print(f'{i+1} {candidate[i][0]}')
            break

if ans[0] not in candidate:
    print(f'{0} {candidate[i][0]}')