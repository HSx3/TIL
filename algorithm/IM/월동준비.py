import sys
sys.stdin = open("월동준비.txt")

N = int(input())
acorn = list(map(int, input().split()))

# print(N)
# print(acorn)

genius = 0
idiot = 0

max_genius = 0
max_idiot = 0
max = 0

# max_idiot
for i in acorn:
    max_idiot += i
    if max < max_idiot:
        max = max_idiot
# print(max)

# max_genius
for_genius = sorted(acorn)[::-1]
for i in for_genius:
    if for_genius[0] < 0:
        max_genius = for_genius[0]
        break
    else:
        if i >= 0:
            max_genius += i
# print(max_genius)

print(f'{max} {max_genius}')