import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
string = input().rstrip()
start = 0
count = 0
ans = 0

while start < M:
    if string[start: start + 3] == 'IOI':
        start += 2
        count += 1
        if count == N:
            ans += 1
            count -= 1
    else:
        count = 0
        start += 1
print(ans)