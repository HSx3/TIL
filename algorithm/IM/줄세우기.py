import sys
sys.stdin = open("줄세우기.txt")

N = int(input())    # 학생의 수
number = list(map(int, input().split()))
line = []

for i in range(1, len(number)+1):
    pick = number.pop(0)
    if pick:
        line = line[:-pick] + [i] + line[-pick:]
    else:
        line += [i]
print(*line)