arr = [-7,-3,-2,5,8]

n = len(arr)

for i in range(1<<n):
    sum = 0
    for j in range(n):
        if i & (1<<j):
            sum += arr[j]
    if sum == 0:
        for j in range(n):
            if i & (1<<j):
                print(arr[j], end= " ")
        print()