import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arrN = {}

for a in sorted(arr):
    if a in arrN:
        arrN[a] += 1
    else:
        arrN[a] = 1
    
stack = []
ans = [-1 for _ in range(N)]

for i in range(N-1, -1, -1):
    if not stack:
        stack.append(arr[i])
        continue
    
    while stack:
        s = stack.pop()
        if arrN[arr[i]] < arrN[s]:
            ans[i] = s
            stack.append(s)
            break
    stack.append(arr[i])

for a in ans:
    print(a, end=' ')