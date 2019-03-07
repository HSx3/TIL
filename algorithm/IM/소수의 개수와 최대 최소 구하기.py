import sys
sys.stdin = open("소수의 개수와 최대 최소 구하기.txt")

A, B = map(int, input().split())
prime = [0 for i in range(B)]
count = 0

for i in range(A, B):
    if i*i > 100:
        break
    if prime[i]:
        continue
    for j in range(i*2, B, i):
        prime[j] = 1
print(prime)

for i in range(2, len(prime)):
    if prime[i] == 0:
        count += 1

for i in range(1, len(prime)):
    if prime[i] == 0:
        min_prime = i
        break

for i in range(len(prime)-1, 1, -1):
    if prime[i] == 0:
        max_prime = i
        break

print(count)
print(min_prime + max_prime)