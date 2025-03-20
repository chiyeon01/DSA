import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_order = [-1 for _ in range(N+1)]
queue = deque()

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
for i in range(1, N+1):
    graph[i].sort(reverse=True)
    
queue.append(R)
visited_order[R] = 1
cnt = 2
while queue:
    q = queue.popleft()
    for n in graph[q]:
        if visited_order[n] == -1:
            visited_order[n] = cnt
            cnt += 1
            queue.append(n)

for i in range(1, N+1):
    if visited_order[i] == -1:
        print(0)
    else:
        print(visited_order[i])