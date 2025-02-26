import sys

input = sys.stdin.readline

N = int(input())
dp = [[0, 0] for _ in range(N)] #dp[n][m]: n+1번째 포도주를 마실 때 m+1번째 연속
for i in range(N):
    n = int(input())
    if i == 0:
        dp[i][0] = n
        dp[i][1] = 0
        continue
    elif i == 1:
        dp[i][0] = n
        dp[i][1] = dp[i-1][0] + n
        continue
    elif i == 2:
        dp[i][0] = max(dp[i-2][1] + n, dp[i-2][0] + n)
        dp[i][1] = dp[i-1][0] + n
        continue
        
    dp[i][0] = max(dp[i-2][0] + n, dp[i-2][1] + n, dp[i-3][0] + n, dp[i-3][1] + n)
    dp[i][1] = dp[i-1][0] + n

ans = 0
for d in dp:
    ans = max(max(d), ans)

print(ans)