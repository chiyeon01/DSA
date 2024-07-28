import sys
input = sys.stdin.readline

n = int(input())
INF = 10**9
dp = [INF for _ in range(500000)]
for i in range(1, int(n**0.5) + 1):
    dp[i**2] = 1

for i in range(1, n + 1):
    if dp[i] == 1:
        continue
    j = 1
    while j**2 <= i:
        dp[i] = min(dp[i], dp[i - j**2] + dp[j**2])
        j += 1
print(dp[n])