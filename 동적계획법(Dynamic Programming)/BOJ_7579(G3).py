import sys

input = sys.stdin.readline

n, m = map(int, input().split())
M = list(map(int, input().split()))
C = list(map(int, input().split()))
arr = []

for i in range(n):
    arr.append([C[i], M[i]])
    
dp = [[0 for _ in range(10001)] for _ in range(n)]
S = 0

for i in range(n):
    S += arr[i][0]
    if i == 0:
        dp[i][arr[i][0]] = arr[i][1]
        continue
    
    for w in range(S+1):
        if w - arr[i][0] < 0:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - arr[i][0]] + arr[i][1])
            
for i in range(10001):
    if dp[n-1][i] >= m:
        print(i)
        break