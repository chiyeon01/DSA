import sys
from collections import deque
input = sys.stdin.readline

def BFS(s):
    queue = deque()
    queue.append([s, 0])
    while queue:
        now, lv = queue.popleft()
        if graph[now]:
            for n in graph[now]:
                if lv < dp[n]:
                    dp[n] = lv
                    queue.append([n, lv])
        else:
            for k in range(1, 7):
                if now + k < 101:
                    if lv + 1 < dp[now + k]:
                        dp[now + k] = lv + 1
                        queue.append([now + k, lv + 1])
                

N, M = map(int, input().split())
graph = [[]for _ in range(101)]
INF = 10**9
dp = [INF for _ in range(101)]
dp[1] = 0

for _ in range(N + M):
    s, e = map(int, input().split())
    graph[s].append(e)
BFS(1)
print(dp[100])