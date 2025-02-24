import sys

input = sys.stdin.readline

def solution(n, result, method):
    global ansMin, ansMax
    if n == N:
        ansMin = min(result, ansMin)
        ansMax = max(result, ansMax)
        return
    now = num[n]
    for i, m in enumerate(method):
        if m <= 0:
            continue
        if i == 0: # +
            result += now
            method[i] -= 1
            solution(n+1, result, method)
            result -= now
            method[i] += 1
        elif i == 1: # -
            result -= now
            method[i] -= 1
            solution(n+1, result, method)
            result += now
            method[i] += 1
        elif i == 2: # x
            result *= now
            method[i] -= 1
            solution(n+1, result, method)
            result //= now
            method[i] += 1
        else: # /
            r = result
            if result < 0:
                result = (-1) * (abs(result) // now)
            else:
                result //= now
            method[i] -= 1
            solution(n+1, result, method)
            result = r
            method[i] += 1
            
N = int(input())
num = list(map(int, input().split()))
method = list(map(int, input().split()))
ansMin = 10e9
ansMax = -10e9
solution(1, num[0], method)
print(ansMax)
print(ansMin)