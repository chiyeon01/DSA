import sys

input = sys.stdin.readline
N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))

ans = []
for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    ans.append(rank)
    
for x in ans:
    print(x, end=' ')