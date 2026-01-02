import sys

def solution(n, arr, S):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        dp[i][i+1] = arr[i] + arr[i+1]
        
    for i in range(n-3, -1, -1): # start
        for j in range(i+2, n): # end
            MIN = 10e9
            for k in range(i, j):
                MIN = min(MIN, dp[i][k] + dp[k+1][j])
            dp[i][j] = MIN + S[j+1] - S[i]
            
    return dp[0][n-1]

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    S = [0]
    for a in arr:
        S.append(S[-1] + a)
    print(solution(N, arr, S))