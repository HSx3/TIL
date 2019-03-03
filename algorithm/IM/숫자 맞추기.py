import sys
sys.stdin = open("숫자 맞추기.txt")

N = int(input())    # player 수
number = []
round1 = []
round2 = []
round3 = []
score = [0] * N
for i in range(N):
    number += [input().split()]
# print(number)

for j in range(len(number)):
    for i in range(len(number)):
        if j == 0:
            round1.append(number[i][j])
        elif j == 1:
            round2.append(number[i][j])
        elif j == 2:
            round3.append(number[i][j])
# print(f'round1: {round1}')
# print(f'round2: {round2}')
# print(f'round3: {round3}')

for i, num in enumerate(round1):
    if round1[i] not in round1[:i] and round1[i] not in round1[i+1:]:
        score[i] += int(num)
# print(score)

for i, num in enumerate(round2):
    if round2[i] not in round2[:i] and round2[i] not in round2[i+1:]:
        score[i] += int(num)
# print(score)

for i, num in enumerate(round3):
    if round3[i] not in round3[:i] and round3[i] not in round3[i+1:]:
        score[i] += int(num)
# print(score)

for i in score:
    print(i)