import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(T):
    I = int(input())
    board = [[-1 for _ in range(I)] for _ in range(I)]
    sr, sc = map(int, input().split())
    gr, gc = map(int, input().split())
    queue = deque()
    queue.append([sr, sc, 0])
    
    while queue:
        r, c, cnt = queue.popleft()
        if r == gr and c == gc:
            print(cnt)
            break
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr < 0 or nr >= I or nc < 0 or nc >= I:
                continue
            if board[nr][nc] == -1:
                board[nr][nc] = cnt + 1
                queue.append([nr, nc, cnt+1])
        
        cnt += 1