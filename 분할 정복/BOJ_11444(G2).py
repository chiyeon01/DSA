import sys

input = sys.stdin.readline

def fibonacci(n):
    global m
    if n in m:
        return m[n]
    else:
        if n % 2 == 0:
            m[n] = (fibonacci(n//2) * (fibonacci(n//2 + 1) + fibonacci(n//2 - 1))) % 1000000007
            return m[n]
        else:
            m[n] = (fibonacci((n+1)//2)**2 + fibonacci((n+1)//2 - 1)**2) % 1000000007
            return m[n]

n = int(input())
m = {0:0,
     1:1,
     2:1}

print(fibonacci(n))