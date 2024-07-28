import sys

input = sys.stdin.readline
N = int(input())
board = []

for _ in range(N):
    x, y = map(int, input().split())
    board.append([x, y])
    
board = sorted(board, key = lambda x : (x[1], x[0]))
for x in board:
    print(x[0], x[1])