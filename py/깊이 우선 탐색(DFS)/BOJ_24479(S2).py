import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(node):
    global Visited
    global ans, cnt
    for n in graph[node]:
        if Visited[n]:
            continue
        else:
            ans[n] = cnt
            cnt += 1
            Visited[n] = True
            DFS(n)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

ans = [-1 for _ in range(N+1)]
Visited = [False for _ in range(N+1)]
Visited[R] = True
ans[R] = 1
cnt = 2   
DFS(R)
for i in range(1, N+1):
    if ans[i] == -1:
        print(0)
    else:
        print(ans[i])