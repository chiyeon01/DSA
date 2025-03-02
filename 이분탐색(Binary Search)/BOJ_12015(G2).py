import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = []

for a in A:
    if not stack or stack[-1] < a:
        stack.append(a)
    else:
        left = 0
        right = len(stack) - 1
        mid = (left + right) // 2
        while left < right:
            mid = (left + right) // 2
            if stack[mid] < a:
                left = mid + 1
            else:
                right = mid
        mid = (left + right) // 2
        stack[mid] = a

print(len(stack))

# BOJ_12738도 똑같이 풀림.