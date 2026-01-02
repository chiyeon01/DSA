import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix1 = []
for _ in range(n):
    matrix1.append(list(map(int, input().split())))
    
m, k = map(int, input().split())
matrix2 = []
for _ in range(m):
    matrix2.append(list(map(int, input().split())))

ans_matrix = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        for kk in range(k):
            ans_matrix[i][kk] += matrix1[i][j] * matrix2[j][kk]

for i in range(n):
    for j in range(k):
        print(ans_matrix[i][j], end=' ')
    print()