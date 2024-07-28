import sys
input = sys.stdin.readline

def check_cant(x, y):
    global Cant
    sx = x
    sy = y
    for i in range(N):
        if i == x:
            continue
        Cant[i][y] += 1
    for i in range(N):
        if i == y:
            continue
        Cant[x][i] += 1
    while 0 <= x and 0 <= y:
        if x == sx and y == sy:
            x -= 1
            y -= 1
            continue
        Cant[x][y] += 1
        x -= 1
        y -= 1
    while sx < N and sy < N:
        Cant[sx][sy] += 1
        sx += 1
        sy += 1

def check_can(x, y):
    global Cant
    sx = x
    sy = y
    for i in range(N):
        if i == x:
            continue
        Cant[i][y] -= 1
    for i in range(N):
        if i == y:
            continue
        Cant[x][i] -= 1
    while 0 <= x and 0 <= y:
        if x == sx and y == sy:
            x -= 1
            y -= 1
            continue
        Cant[x][y] -= 1
        x -= 1
        y -= 1
    while sx < N and sy < N:
        Cant[sx][sy] -= 1
        sx += 1
        sy += 1

def DFS(r, c, cnt):
    global Cant
    global ans
    if cnt == N:
        ans += 1
        return
    for x in range(r, N):
        for y in range(N):
            if x == r and y < c:
                continue
            if Cant[x][y] > 0:
                continue
            else:
                check_cant(x, y)
                DFS(x, y + 1, cnt + 1)
                check_can(x, y)

N = int(input())
Cant = [[0 for _ in range(N)] for _ in range(N)]
ans = 0
DFS(0, 0, 0)
print(ans)