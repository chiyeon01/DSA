import sys
input = sys.stdin.readline

def solution(x1, y1, x2, y2):
    global cnt_blue
    global cnt_white
    blue = 0
    white = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if board[i][j] == 1:
                blue += 1
            else:
                white += 1
    
    if blue > 0 and white > 0:
        solution(x1, y1, x2 - (x2-x1+1)//2, y2 - (y2-y1+1)//2)
        solution(x1, y1 + (y2-y1+1)//2, x2 - (x2-x1+1)//2, y2)
        solution(x1 + (x2-x1+1)//2, y1, x2, y2 - (y2-y1+1)//2)
        solution(x1 + (x2-x1+1)//2, y1 + (y2-y1+1)//2, x2, y2)
    elif blue > 0:
        cnt_blue += 1
    else:
        cnt_white += 1
 
N = int(input())
cnt_blue = 0
cnt_white = 0
board = [[0 for _ in range(N + 1)]for _ in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    for j in range(1, N + 1):
        board[i][j] = line[j - 1]

solution(1, 1, N, N)
print(cnt_white)
print(cnt_blue)