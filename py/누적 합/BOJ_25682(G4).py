import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
board = []
WboardN = [[0 for _ in range(m+1)] for _ in range(n+1)]
BboardN = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    board.append(input().rstrip())
    if i % 2 == 0:
        Wstart = 'W'
        Bstart = 'B'
    else:
        Wstart = 'B'
        Bstart = 'W'

    # Wboard
    for j, b in enumerate(board[i]):
        if b != Wstart:
            WboardN[i+1][j+1] = 1
        if Wstart == 'W':
            Wstart = 'B'
        else:
            Wstart = 'W'
            
        if b != Bstart:
            BboardN[i+1][j+1] = 1
        if Bstart == 'W':
            Bstart = 'B'
        else:
            Bstart = 'W'

for i in range(1, n+1):
    for j in range(1, m+1):
        WboardN[i][j] = WboardN[i-1][j] + WboardN[i][j-1] + WboardN[i][j] - WboardN[i-1][j-1]
        BboardN[i][j] = BboardN[i-1][j] + BboardN[i][j-1] + BboardN[i][j] - BboardN[i-1][j-1]

ans = 10e9
for si in range(1, n - k + 2): # start row
    for sj in range(1, m - k + 2): # start column
        
        ei = si + k - 1 # end row
        ej = sj + k - 1 # end column
        ans = min(WboardN[ei][ej] - WboardN[si-1][ej] - WboardN[ei][sj-1] + WboardN[si-1][sj-1], BboardN[ei][ej] - BboardN[si-1][ej] - BboardN[ei][sj-1] + BboardN[si-1][sj-1], ans)
print(ans)