import sys
from collections import deque
input = sys.stdin.readline

def BFS(x, y):
    global ans
    global visited
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append([x, y, 0])
    while queue:
        now_x, now_y, lv = queue.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append([nx, ny, lv + 1])
                ans[nx][ny] = lv + 1
    
    for i in range(N):
        for j in range(M):
            if ans[i][j] == INF and board[i][j] != 0:
                ans[i][j] = -1
            elif board[i][j] == 0:
                ans[i][j] = 0
             
N, M = map(int, input().split())
board = []
visited = [[False for _ in range(M)] for _ in range(N)]
goal_x = 0
goal_y = 0
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for j, x in enumerate(line):
        if x == 2:
            goal_x = i
            goal_y = j

INF = 10**9
ans = [[INF for _ in range(M)] for _ in range(N)]
ans[goal_x][goal_y] = 0
visited[goal_x][goal_y] = True
BFS(goal_x, goal_y)

for i in range(N):
    for j in range(M):
        print(ans[i][j], end=' ')
    print()