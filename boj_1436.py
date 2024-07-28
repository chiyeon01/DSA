import sys

input = sys.stdin.readline
N = int(input())
rank = 1
ans = 666
while N!=rank:
    ans += 1
    if '666' in str(ans):
        rank += 1
print(ans)