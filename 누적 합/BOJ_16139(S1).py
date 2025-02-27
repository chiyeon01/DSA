import sys # 50점짜리

input = sys.stdin.readline

content = input().rstrip()
q = int(input())
N = len(content)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
S = [{a: 0 for a in alphabet} for _ in range(N+1)]

for i in range(N+1):
    if i == 0:
        continue
    a = content[i-1]
    if i == 1:
        S[i][a] = 1
        continue
    for key in alphabet:
        value = S[i-1][key]
        S[i][key] = value
    S[i][a] = S[i-1][a] + 1

for _ in range(q):
    a, s, e = input().split()
    sys.stdout.write(str(S[int(e)+1][a] - S[int(s)][a])+'\n')