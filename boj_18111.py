import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
board = []
for _ in range(N):
    line = list(map(int, input().split()))
    board.append(line)

height = 0
ans_height = 0
ans_second = 10**9
while height <= 256:
    second = 0
    minus = 0
    plus = 0
    BREAK = False
    for i in range(N):
        for j in range(M):
            if board[i][j] > height:
                second += 2*(board[i][j] - height)
                plus += board[i][j] - height
            elif board[i][j] < height:
                second += height - board[i][j]
                minus += height - board[i][j]
            
            if second > ans_second:
                BREAK = True
                break
        if BREAK:
            break
                
    if ans_second >= second and B + plus - minus >= 0:
        ans_second =  second
        ans_height = height
    height += 1

print(ans_second, ans_height)