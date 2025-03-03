import sys

input = sys.stdin.readline

M, N = map(int, input().split())
board = []
dp = [[0 for _ in range(N)] for _ in range(M)]
dp[0][0] = 1

for _ in range(M):
    board.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
for r in range(M):
    for c in range(N):
        current = board[r][c]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= M or nc < 0 or nc >= N:
                continue
            if board[nr][nc] < current:
                dp[nr][nc] += dp[r][c]
                
for r in range(M):
    for c in range(N):
        current = board[r][c]
        s = 0
        if r == c == 0:
            continue
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= M or nc < 0 or nc >= N:
                continue
            if board[nr][nc] > current:
                s += dp[nr][nc]
        dp[r][c] = s
                
print(dp[M-1][N-1])