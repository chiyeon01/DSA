import sys

input = sys.stdin.readline

def row(r, n):
    for i in range(9):
        if sudoku[r][i] == n:
            return False
    return True

def col(c, n):
    for i in range(9):
        if sudoku[i][c] == n:
            return False
    return True

def square(r, c, n):
    for i in range(3):
        for j in range(3):
            if sudoku[r//3 * 3 + i][c//3 * 3 + j] == n:
                return False
            
    return True

def solution(n):
    if n == len(temp):
        for s in sudoku:
            print(*s)
        exit()
    for i in range(1, 10):
        r = temp[n][0]
        c = temp[n][1]
        if row(r, i) and col(c, i) and square(r, c, i):
            sudoku[r][c] = i
            solution(n+1)
            sudoku[r][c] = 0
    
sudoku = [list(map(int, input().split())) for _ in range(9)]
temp = []

for i, arr in enumerate(sudoku):
    for j, a in enumerate(arr):
        if a == 0:
            temp.append([i, j])

solution(0)