import sys
input = sys.stdin.readline

def IsRate(A, B):
    for i in range(N):
        for j in range(N):
            if A[i] > A[j] and B[i] > B[j]:
                continue
            elif A[i] == A[j] and B[i] == B[j]:
                continue
            elif A[i] < A[j] and B[i] < B[j]:
                continue
            else:
                return False
    return True

M, N = map(int, input().split())
Planet = []
for _ in range(M):
    Planet.append(list(map(int, input().split())))
cnt = 0
for A in range(M):
    for B in range(A + 1, M):
        if IsRate(Planet[A], Planet[B]):
            cnt += 1

print(cnt)