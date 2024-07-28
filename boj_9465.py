import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):
    n = int(input())
    sticker = []
    dp = [[0 for _ in range(n)] for _ in range(2)]
    for _ in range(2):
        line = list(map(int, input().split()))
        sticker.append(line)
    for j in range(n): # col
        for i in range(2): # row
            if i == 0:
                if j - 1 >= 0 and j - 2 >= 0:
                    dp[i][j] = max(dp[i + 1][j - 1] + sticker[i][j], dp[i + 1][j - 2] + sticker[i][j])
                elif j - 1 >= 0:
                    dp[i][j] = dp[i + 1][j - 1] + sticker[i][j]
                else:
                    dp[i][j] = sticker[i][j]
            else:
                if j - 1 >= 0 and j - 2 >= 0:
                    dp[i][j] = max(dp[i - 1][j - 1] + sticker[i][j], dp[i - 1][j - 2] + sticker[i][j])
                elif j - 1 >= 0:
                    dp[i][j] = dp[i - 1][j - 1] + sticker[i][j]
                else:
                    dp[i][j] = sticker[i][j]
    print(max(dp[0][n - 1], dp[1][n - 1]))