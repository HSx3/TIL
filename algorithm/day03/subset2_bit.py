arr = [1,2,3]

n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (i<<j):
            print(arr[j], end=' ')
    print()
# print()