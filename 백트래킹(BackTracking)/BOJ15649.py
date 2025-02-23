import sys

input = sys.stdin.readline

def DFS(N, M, cnt, seq):
    global Visited
    if cnt == M:
        print(' '.join(seq))
        return
    for n in range(1, N+1):
        if Visited[n]:
            continue
        Visited[n] = True
        seq.append(str(n))
        DFS(N, M, cnt+1, seq)
        Visited[n] = False
        seq.pop()
        
N, M = map(int, input().split())
Visited = [False for _ in range(N+1)]
for n in range(1, N+1):
    seq = [str(n)]
    Visited[n] = True
    DFS(N, M, 1, seq)
    Visited[n] = False