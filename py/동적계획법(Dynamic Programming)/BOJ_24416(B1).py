import sys

input = sys.stdin.readline

def fibonacci_recursion(n):
    global recursion_O
    recursion_O += 1
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_dynamic(n):
    global dynamic_O
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        dynamic_O += 1
        f[i] = f[i-1] + f[i-2]
        
N = int(input())
recursion_O = 0
dynamic_O = 0
f = [1 for _ in range(N+1)]
fibonacci_recursion(N)
fibonacci_dynamic(N)
print(recursion_O//2 + 1, dynamic_O)