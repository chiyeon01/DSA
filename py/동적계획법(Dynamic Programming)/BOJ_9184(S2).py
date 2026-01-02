import sys

input = sys.stdin.readline

dp = [[[1 for _ in range(101)] for _ in range(101)] for _ in range(101)]

for i in range(101):
    for j in range(101):
        for k in range(101):
            if i - 50 <= 0 or j - 50 <= 0 or k - 50 <= 0:
                dp[i][j][k] = 1
            elif i - 50 > 20 or j - 50 > 20 or k - 50 > 20:
                dp[i][j][k] = 1048576
            elif i < j and j < k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
                
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print('w({}, {}, {}) = {}'.format(a, b, c, dp[a+50][b+50][c+50]))
    
# 사실 100까지가 아니라 20까지만 구해도 쉽게 풀 수 있음.
# 하지만, 100까지로 두고 풀어도 충분함.
# 20을 범위로 둘 경우 20x20x20=8000, 100을 범위로 둘 경우 100x100x100=1000000번 돔.