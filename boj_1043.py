import sys
input = sys.stdin.readline

def find(i):
    if i == parent[i]:
        return i
    parent[i] = find(parent[i])
    return parent[i]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

N, M = map(int, input().split())
parent = [i for i in range(N + 1)] # parent[i] == 0이면 거짓말을 알고있는 경우
Know_People = list(map(int, input().split()))
Parties = []

for i in range(1, Know_People[0] + 1):
    parent[Know_People[i]] = 0
    
for _ in range(M):
    party = list(map(int, input().split()))
    parent_node = -1
    Parties.append(party)
    
    for i in range(1, party[0] + 1):
        if find(party[i]) == 0: # 거짓말임을 알고있다면 부모노드로 바꿔주기
            parent_node = party[i]
            break
        
    if parent_node == -1:
        parent_node = party[1]
        for i in range(2, party[0] + 1):
            union(parent_node, party[i])
    else:
        for i in range(1, party[0] + 1):
            union(parent_node, party[i])

ans = M
for P in Parties:
    for i, p in enumerate(P):
        if i == 0:
            continue
        if find(p) == 0:
            ans -= 1
            break

print(ans)