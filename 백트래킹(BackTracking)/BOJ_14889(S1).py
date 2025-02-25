import sys

input = sys.stdin.readline

def solution(S, member, n, cnt):
    global diff
    
    if cnt == N//2:
        OtherSUM = 0
        OtherTeam = []
        for i in range(N):
            if i in member:
                continue
            OtherTeam.append(i)
        for i in range(cnt):
            for j in range(cnt):
                OtherSUM += synergy[OtherTeam[i]][OtherTeam[j]]

        if max(OtherSUM, S) - min(OtherSUM, S) < diff:
            diff = max(OtherSUM, S) - min(OtherSUM, S)
        return
    
    for i in range(n+1, N):
        member.append(i)
        for idx in range(cnt):
            S += synergy[i][member[idx]] + synergy[member[idx]][i]
        solution(S, member, i, cnt+1)
        for idx in range(cnt):
            S -= synergy[i][member[idx]] + synergy[member[idx]][i]
        member.pop()
        
N = int(input())
synergy = []
diff = 10e9
for _ in range(N):
    s = list(map(int, input().split()))
    synergy.append(s)

for i in range(N):
    solution(0, [i], i, 1)
  
print(diff)