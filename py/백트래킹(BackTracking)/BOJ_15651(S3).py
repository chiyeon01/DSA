import sys

input = sys.stdin.readline

def DFS(N, M, cnt, seq):
    if cnt == M:
        print(' '.join(seq))
        return
    for n in range(1, N+1):
        seq.append(str(n))
        DFS(N, M, cnt+1, seq)
        seq.pop()
        
N, M = map(int, input().split())

for n in range(1, N+1):
    seq = [str(n)]
    DFS(N, M, 1, seq)