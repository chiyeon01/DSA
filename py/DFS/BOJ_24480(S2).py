import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def DFS(node):
    global visited_order, cnt
    
    for n in graph[node]:
        if visited_order[n] == -1:
            visited_order[n] = cnt
            cnt += 1
            DFS(n)
            
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_order = [-1 for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

visited_order[R] = 1
cnt = 2
DFS(R)

for i in range(1, N+1):
    if visited_order[i] == -1:
        print(0)
    else:
        print(visited_order[i])