import sys
from collections import deque
input = sys.stdin.readline

def solution(i, j):
    global check_Chicken
    add_score = 10**9
    
    for x, y in check_Chicken:
        ns = abs(x - i) + abs(y - j)
        if ns < add_score:
            add_score = ns
            
    return add_score

def DFS(s, cnt):
    global visited
    global check_Chicken
    global ans
    
    if cnt == M:
        score = 0
        for i in range(House_Count):
            x, y = House[i]
            score += solution(x, y)
        if score < ans:
            ans = score
    else:
        for i in range(s, Chicken_Count):
            if not visited[i]:
                visited[i] = True
                check_Chicken.append(Chicken[i])
                DFS(i + 1, cnt + 1)
                check_Chicken.pop()
                visited[i] = False

N, M = map(int, input().split())
city = [[0 for _ in range(N)] for _ in range(N)]
Chicken = []
Chicken_Count = 0
House = []
House_Count = 0

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        city[i][j] = data[j]
        if data[j] == 1:
            House.append([i, j])
            House_Count += 1
        elif data[j] == 2:
            Chicken.append([i, j])
            Chicken_Count += 1

ans = 10**9
check_Chicken = deque()
visited = [False for _ in range(Chicken_Count)]
DFS(0, 0)
print(ans)