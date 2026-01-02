import sys

input = sys.stdin.readline

N = int(input())
arr = []
dp = [1 for _ in range(N)]

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort()

for i in range(N):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(N - max(dp))