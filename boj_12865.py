import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = []
dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

for _ in range(N):
    W, V = map(int, input().split())
    bag.append([W, V])

for i in range(1, K + 1):
    for j in range(N):
        w = bag[j][0]
        v = bag[j][1]
        if i - w >= 0:
            dp[i][j] = max(dp[i - w][j - 1] + v, dp[i][j - 1])
        else:
            dp[i][j] = dp[i][j - 1]
    
print(dp[K][N - 1])