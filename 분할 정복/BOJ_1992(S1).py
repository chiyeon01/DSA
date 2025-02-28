import sys

input = sys.stdin.readline

def solution(r1, c1, r2, c2):
    zero = 0
    one = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if board[i][j] == '0':
                zero += 1
            else:
                one += 1
    
    if zero != 0 and one != 0:
        print('(', end='')
        solution(r1, c1, (r2+r1)//2, (c2+c1)//2)
        solution(r1, (c2+c1)//2 + 1, (r2+r1)//2, c2)
        solution((r2+r1)//2 + 1, c1, r2, (c2+c1)//2)
        solution((r2+r1)//2 + 1, (c2+c1)//2 + 1, r2, c2)
        print(')', end='')
    else:
        if zero != 0:
            print(0, end='')
        else:
            print(1, end='')

N = int(input())
board = []

for _ in range(N):
    board.append(input().rstrip())
    
solution(0, 0, N-1, N-1)