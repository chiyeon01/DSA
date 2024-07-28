import sys
input = sys.stdin.readline
N, K = map(int, input().split())
end = 0
start = 1
l = []

for _ in range(N):
    n = int(input())
    l.append(n)
    if end < n:
        end = n

while start <= end:
    mid = (start + end) // 2 
    cnt = 0
    for x in l:
        cnt += x//mid
    if cnt >= K:
        start = mid + 1
    else:
        end = mid - 1
        
cnt = 0
for x in l:
    cnt += x // start
    
if cnt >= K:
    print(start)
else:
    print(start-1)