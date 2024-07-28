import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for x in range(N):
    for y in range(N):
        if board[x][y] == 1:
            continue
        for k in range(3):
            if k == 0:
                if 0 <= y-1 < N:
                    dp[x][y][k] += dp[x][y-1][0] + dp[x][y-1][2]
            elif k == 1:
                if 0 <= x-1 < N:
                    dp[x][y][k] += dp[x-1][y][1] + dp[x-1][y][2]
            else:
                if 0 <= x-1 < N and 0 <= y-1 < N:
                    if board[x-1][y] == 1 or board[x][y-1] == 1:
                        continue
                    dp[x][y][k] += dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]
ans = sum(dp[N-1][N-1])
print(ans)