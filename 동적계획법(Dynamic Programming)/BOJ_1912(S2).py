import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
for i, a in enumerate(arr):
    if i == 0:
        continue
    arr[i] = max(arr[i], arr[i-1]+arr[i])

print(max(arr))