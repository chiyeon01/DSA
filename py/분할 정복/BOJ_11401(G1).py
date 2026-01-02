import sys
# 핵심은 페르마의 소수정리

input = sys.stdin.readline

def divide_for_square(a, p):
    if p <= 1:
        return a
    if p % 2 == 0:
        return (divide_for_square(a, p//2)**2) % 1000000007
    else:
        return (a * divide_for_square(a, p//2)**2) % 1000000007
    

n, k = map(int, input().split())
n_factorial = 1
n_k_factorial = 1
k_factorial = 1

for i in range(1, n+1):
    n_factorial = (n_factorial * i) % 1000000007

for i_k in range(1, n-k+1):
    n_k_factorial = (n_k_factorial * i_k) % 1000000007
    
for k in range(1, k+1):
    k_factorial = (k_factorial * k) % 1000000007

bottom = divide_for_square((n_k_factorial * k_factorial)%1000000007, 1000000005)

print((n_factorial * bottom) % 1000000007)