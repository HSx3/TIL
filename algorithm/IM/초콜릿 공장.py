import sys
sys.stdin = open("초콜릿 공장.txt")

count = 0
N = int(input())
for i in range(N):
    L, H = map(str, input().split())

    chocolate_L = list(L)
    chocolate_H = list(H)

    if len(set(chocolate_L) | set(chocolate_H)) >= len(chocolate_L) + len(chocolate_H) - 2:
        count += 1
print(count)

# a = [1, 2]
# c = [3, 4]
#
# b = a | c
# print(b)
