import sys
input = sys.stdin.readline

def DFS(s):
    global visited
    global standard
    for x in load[s]:
        if not visited[x]:
            visited[x] = True
            ans[standard][x] = 1
            DFS(x)

N = int(input())
load = [[] for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            load[i].append(j)

ans = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    visited = [False for _ in range(N)]
    standard = i
    DFS(i)

for i in range(N):
    for j in range(N):
        print(ans[i][j], end = ' ')
    print()