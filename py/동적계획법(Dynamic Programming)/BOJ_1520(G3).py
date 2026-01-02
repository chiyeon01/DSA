import sys
import heapq

input = sys.stdin.readline

m, n = map(int, input().split())
board = []
dp = [[0 for _ in range(n)] for _ in range(m)]
dp[0][0] = 1 # dp[r][c] : r,c까지 가는 경우의 수
visited = [[False for _ in range(n)] for _ in range(m)]
visited[0][0] = True

for i in range(m):
    board.append(list(map(int, input().split())))

queue = []
heapq.heappush(queue, [-1 * board[0][0], 0, 0]) # value, x, y
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    value, x, y = heapq.heappop(queue)
    value = -1 * value
    for k in range(4):
        nx = x + dx[k] # 행
        ny = y + dy[k] # 열
        
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        
        if value > board[nx][ny]:
            dp[nx][ny] += dp[x][y]
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            heapq.heappush(queue, [-1 * board[nx][ny], nx, ny])
            
print(dp[m-1][n-1])