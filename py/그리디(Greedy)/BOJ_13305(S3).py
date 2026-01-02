import sys
input = sys.stdin.readline

n = int(input())
edge = list(map(int, input().split()))
node = list(map(int, input().split()))
ans = 0
price = node[0]

for i in range(n-1):
    if price < node[i+1]:
        ans += price * edge[i]
    else:
        ans += price * edge[i]
        price = node[i+1]
        
print(ans)