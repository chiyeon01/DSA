import sys

input = sys.stdin.readline

# nCr = n! / (r!(n-r)!)
# n! = n x (n-1) x ... x 1

def factorial(a):
    f = 1
    for i in range(2, a+1):
        f *= i
    return f

def Combination(n, r):
    if r == 0:
        return 1
    return (factorial(n) // (factorial(r) * factorial(n-r))) % 1000000007

N, K = map(int, input().split())
binary_search = list(map(int, input().split()))
arr = [0 for _ in range(N)]

start = 0
end = N-1
for i in range(K):
    mid = (start+end) // 2
    arr[mid] = binary_search[i]
    if i == K-1:
        continue
    if binary_search[i] < binary_search[i+1]:
        start = mid + 1
    else:
        end = mid - 1

ans = 1
r = 0
startNum = 0
List = []
for i in range(N):
    if arr[i] == 0:
        r += 1
        if i == N-1:
           List.append(Combination(100 - startNum, r)) 
    else:
        List.append(Combination(arr[i] - startNum - 1, r))
        startNum = arr[i]
        r = 0

for s in List:
    ans *= s

print(ans % 1000000007)