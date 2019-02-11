def fibonacci(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibonacci(n-1) + fibonacci(n-2))
    return memo[n]

memo = [0, 1]
print(fibonacci(100))

# factorial
# def factorial(n):
#     global memo
#     if n >= 2 and len(memo) <= n:
#         memo.append(n * factorial(n-1))
#     return memo[n]
#
# memo = [1, 1]
#
# print(factorial(5))