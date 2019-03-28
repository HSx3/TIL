'''
memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다
memo[0]을 0으로 memo[1]는 1로 초기화 한다
'''

def fibo(n) :
    # global memo
    if n >= 2 and len(memo) <= n :
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]
print(fibo(1000))