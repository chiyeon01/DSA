import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(x, y):
    global ans
    global visited
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and campus[nx][ny] != 'X':
            if visited[nx][ny]:
               continue
            else:
                visited[nx][ny] = True
                if campus[nx][ny] == 'P':
                    ans += 1
                DFS(nx, ny)

N, M = map(int, input().split())
campus = [[0 for _ in range(M)]for _ in range(N)]
x = 0
y = 0

for i in range(N):
    line = input().rstrip()
    for j in range(M):
        campus[i][j] = line[j]
        if line[j] == 'I':
            x = i
            y = j

ans = 0
visited = [[False for _ in range(M)] for _ in range(N)]
DFS(x, y)
if ans == 0:
    print('TT')
else:
    print(ans)