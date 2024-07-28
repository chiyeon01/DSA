import sys
input = sys.stdin.readline

n = int(input())
stair = [0]
for _ in range(n):
    s = int(input())
    stair.append(s)
    
D = [0 for _ in range(n + 1)]
D[0] = 0
D[1] = stair[1]
ans = stair[1]
for i in range(2, n + 1):
    if i >= 3:
        D[i] = max(stair[i] + D[i - 2], stair[i] + stair[i - 1] + D[i - 3])
    elif i == 2:
        D[i] = stair[1] + stair[2]
print(D[n])