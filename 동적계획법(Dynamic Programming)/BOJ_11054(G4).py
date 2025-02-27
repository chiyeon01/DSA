import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [[1, 1] for _ in range(N)] # dp[a][b] : 0 ~ a 인덱스의 범위에서 b(0인 경우 오르는 중, 1인 경우 내리는 중)위치인 상태에서 바이토닉이 가장 큰 길이의 경우

for i, a in enumerate(arr):
    now = arr[i]
    for j in range(i):
        if now > arr[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        elif now < arr[j]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1, dp[j][0] + 1)

ans = 1
for d in dp:
    ans = max(ans, max(d))

print(ans)