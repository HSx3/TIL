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

# max_idiot
data_sum = acorn[0]
max_idiot = acorn[0]

for i in range(1, len(acorn)):
    data_sum = max(data_sum + acorn[i], acorn[i])
    max_idiot = max(data_sum, max_idiot)

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

print('{} {}'.format(max_idiot, max_genius))