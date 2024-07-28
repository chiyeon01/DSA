import sys
input = sys.stdin.readline

n = int(input())
D = []
for i in range(1, n + 1):
    if i==1:
        D.append(1)
    else:
        D.append(3)

for i in range(3, n + 1):
    D[i - 1] = D[i - 3] * 2 + D[i - 2]
print(D[n - 1]%10007)