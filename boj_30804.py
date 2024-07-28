import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
t_num = [0 for _ in range(10)]
ans = 0
t_num[S[0]] += 1

def solution(start, end, prev_num, kind):
    global N
    global ans
    if end >= N:
        return ans
    if kind > 2:
        t_num[S[start]] -= 1
        if t_num[S[start]] == 0:
            kind -= 1
        prev_num -= 1
        start += 1
    else:
        end += 1
        if end < N:
            t_num[S[end]] += 1
            if t_num[S[end]] == 1:
                kind += 1
            prev_num += 1
    
    if kind <= 2:
        ans = max(ans, prev_num)
        
    return solution(start, end, prev_num, kind)

print(solution(0, 0, 1, 1))