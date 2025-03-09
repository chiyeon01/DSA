import sys

input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
dp = [[0 for _ in range(40001)] for _ in range(n)]
dp[0][0] = 1 # 초기화
dp[0][w[0]] = 1
S = w[0]

for i in range(1, n):
    S += w[i]
    for j in range(S+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][abs(w[i] - j)], dp[i-1][w[i] + j])
        
m = int(input())
ball = list(map(int, input().split()))
for b in ball:
    if dp[n-1][b] == 1:
        print('Y', end=' ')
    else:
        print('N', end=' ')
        
'''
양팔저울의 양 끝에 더하는 지 아니면 빼는 지 혹은 넣지 않는 지 확인하는 dp문제.
2차원 dp활용.
'''