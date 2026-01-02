import sys

def fibonacci(n):
    global dp
    if n in dp:
        return dp[n]
    dp[n] = fibonacci(n-1) + fibonacci(n-2)
    return dp[n]

input = sys.stdin.readline

n = int(input())

dp = {
    0: 0,
    1: 1,
    2: 1
}

print(fibonacci(n))

'''
간단하게 메모이제이션 기법 연습하기 좋은 문제
'''