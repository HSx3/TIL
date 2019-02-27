def root_calc(num):
    while True:
        total = 0
        while num:
            total += num%10
            num //= 10
        if total < 10:
            return total
        num = total

import sys
sys.stdin = open("숫자근.txt")

N = int(input())
data = list(int(input()) for _ in range(N))

check = []
max = 0
ans = 0
for i in range(N):
    root = root_calc(data[i])
    check.append(root)
    for j in range(len(check)):
        if max < check[j]:
            max = check[j]
            ans = data[j]
        if max == check[j]:
            if ans > data[j]:
                ans = data[j]
print(ans)