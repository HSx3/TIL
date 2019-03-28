import sys
sys.stdin = open("피보나치수열_input.txt")

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

def mfibo(n):
    global fib
    if n >= 2 and len(fib) <= n:
        fib.append(mfibo(n-2) + mfibo(n-1))
        print(n, fib)
    return fib[n]

N = int(input())
fib = [0, 1]
# print(fibo(N))
print(mfibo(N))