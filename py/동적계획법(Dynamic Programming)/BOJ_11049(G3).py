import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[[0, arr[i][0], arr[j][1]] for j in range(N)] for i in range(N)]

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        MINCNT = 10e10
        for k in range(i, j):
            MINCNT = min(MINCNT, dp[i][k][0] + dp[k+1][j][0] + (dp[i][k][1] * dp[i][k][2] * dp[k+1][j][2]))
        dp[i][j][0] = MINCNT
        
print(dp[0][N-1][0])

'''
파일 합치기(BOJ_11066)에서 활용한 알고리즘을 이용해 품.
dp의 이차원 배열 활용.
'''