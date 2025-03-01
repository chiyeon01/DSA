
import sys

input = sys.stdin.readline

def binary_search(house, start, end):
    
    while start <= end:
        node = house[0]
        count = 1
        mid = (start + end) // 2
        for i in range(1, len(house)):
            if node + mid <= house[i]:
                count += 1
                node = house[i]
        
        if count >= c:
            global ans
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

n, c = map(int, input().split())
house = []
ans = 1
for _ in range(n):
    house.append(int(input()))
    
house.sort()

binary_search(house, 1, house[-1] - house[0])
print(ans)