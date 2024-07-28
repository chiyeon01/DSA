import sys
from collections import deque
input = sys.stdin.readline

def solution(fresh_position):
    global visited
    global No_Fresh_Num
    global day
    queue = deque()
    dm = [0, 1, 0, -1, 0, 0]
    dn = [-1, 0, 1, 0, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]
    
    for m, n, h in fresh_position:
        queue.append([m, n, h, 0])
    
    while queue:
        m, n, h, lv = queue.popleft()
        for k in range(6):
            nm = m + dm[k]
            nn = n + dn[k]
            nh = h + dh[k]
            if 0 <= nm < M and 0 <= nn < N and 0 <= nh < H:
                if not visited[nh][nn][nm] and apple_box[nh][nn][nm] == 0:
                    apple_box[nh][nn][nm] = 1
                    visited[nh][nn][nm] = True
                    queue.append([nm, nn, nh, lv + 1])
                    No_Fresh_Num -= 1
                    day = lv + 1

M, N, H = map(int, input().split())
No_Fresh_Num = 0
Fresh_Position = []
apple_box =[[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
day = 0

for h in range(H):
    for n in range(N):
        apple = list(map(int, input().split()))
        for idx, a in enumerate(apple):
            apple_box[h][n][idx] = a
            if a == 0:
                No_Fresh_Num += 1
            elif a == 1:
                Fresh_Position.append([idx, n, h])

solution(Fresh_Position)
if No_Fresh_Num > 0:
    print(-1)
else:
    print(day)