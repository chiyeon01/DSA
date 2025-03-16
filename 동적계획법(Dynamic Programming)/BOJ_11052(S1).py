import sys

input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    dp[1][i] = dp[1][i-1] + card[0]
    
for i in range(1, N):
    cost = card[i]
    for j in range(N):
        if j - i >= 0:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i][(j+1)%(i+1)] + cost*((j+1)//(i+1)))
        else:
            dp[i+1][j+1] = dp[i][j+1]
            
print(dp[N][N])