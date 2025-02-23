import sys

input = sys.stdin.readline

def Queen(r, c, cnt):
    global QueenW, QueenH, QueenLD, QueenRD, ans, N
    if cnt == N:
        ans += 1
        return
    for c in range(1, N + 1):
        LD = LDdia(N, r + 1, c)
        RD = RDdia(N, r + 1, c)
        if QueenH[c] or QueenLD[LD] or QueenRD[RD]:
            continue
        QueenW[r + 1] = True
        QueenH[c] = True
        QueenLD[LD] = True
        QueenRD[RD] = True
        Queen(r + 1, c, cnt + 1)
        QueenW[r + 1] = False
        QueenH[c] = False
        QueenLD[LD] = False
        QueenRD[RD] = False
            
# LD번째 구하는 함수 
def LDdia(N, R, C):
    return N + R - C

# RD번째 구하는 함수
def RDdia(N, R, C):
    return R + C -1

N = int(input())
QueenW = [False for _ in range(N+1)]
QueenH = [False for _ in range(N+1)]
QueenLD = [False for _ in range(2 * N)]
QueenRD = [False for _ in range(2 * N)]
ans = 0

for c in range(1, N + 1):
    LD = LDdia(N, 1, c)
    RD = RDdia(N, 1, c)
    QueenW[1] = True
    QueenH[c] = True
    QueenLD[LD] = True
    QueenRD[RD] = True
    Queen(1, c, 1)
    QueenW[1] = False
    QueenH[c] = False
    QueenLD[LD] = False
    QueenRD[RD] = False
        
print(ans)


### 행 번호와 열 번호의 차이로 대각선을 구하면 더 빠름