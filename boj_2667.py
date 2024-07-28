import sys
input = sys.stdin.readline

N = int(input())
land = []
visited = [[False for _ in range(N)]for _ in range(N)]
cnt = 0
ans = []

for _ in range(N):
    line = input().rstrip()
    land.append(line)

def DFS(r, c):
    global N
    global cnt
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for k in range(4):
        nx = r + dx[k]
        ny = c + dy[k]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and land[nx][ny] == '1':
            visited[nx][ny] = True
            cnt += 1
            DFS(nx, ny)
    
for r in range(N):
    for c in range(N):
        if visited[r][c] or land[r][c] == '0':
            continue
        cnt = 1
        visited[r][c] = True
        DFS(r, c)
        ans.append(cnt)

print(len(ans))
ans.sort()
for a in ans:
    print(a)