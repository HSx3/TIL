import sys
sys.stdin = open("n까지의합_input.txt")

def s(n):
    if n <= 1:
        return 1
    else:
        return n + s(n-1)

N = int(input())
print(s(N))
