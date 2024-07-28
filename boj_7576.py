import sys
from collections import deque
input = sys.stdin.readline

def BFS(fresh_position):
    global No_Fresh_Num
    global visited
    global day
    dm = [0, 1, 0, -1]
    dn = [-1, 0, 1, 0]
    queue = deque()
    for m, n in fresh_position:
        queue.append([m, n, 0])
        
    while queue:
        m, n, lv = queue.popleft()
        for k in range(4):
            nm = m + dm[k]
            nn = n + dn[k]
            if 0 <= nm < M and 0 <= nn < N:
                if not visited[nn][nm] and apple_box[nn][nm] == 0:
                    visited[nn][nm] = True
                    apple_box[nn][nm] = 1
                    No_Fresh_Num -= 1
                    queue.append([nm, nn, lv + 1])
                    day = lv + 1

M, N = map(int, input().split())
apple_box = []
Fresh_Position = []
visited = [[False for _ in range(M)] for _ in range(N)]
No_Fresh_Num = 0
day = 0

for n in range(N):
    apple = list(map(int, input().split()))
    apple_box.append(apple)
    for m, a in enumerate(apple):
        if a == 1:
            Fresh_Position.append([m, n])
        elif a == 0:
            No_Fresh_Num += 1

BFS(Fresh_Position)
if No_Fresh_Num > 0:
    print(-1)
else:
    print(day)