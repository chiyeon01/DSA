import sys
from collections import deque
input = sys.stdin.readline

def solution(s):
    global visited
    
    queue = deque()
    queue.append((s, 1))
    cnt = 0
    
    while queue:
        now, level = queue.popleft()
        for x in network[now]:
            if not visited[x]:
                visited[x] = True
                queue.append((x, level + 1))
                cnt += level
    
    return cnt
        
N, M = map(int, input().split())
network = [[]for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

min_num = 10**9
pp = 1
for i in range(1, N + 1):
    visited = [False for _ in range(N + 1)]
    visited[i] = True
    cnt = solution(i)
    if cnt < min_num:
        min_num = cnt
        pp = i
        
print(pp)