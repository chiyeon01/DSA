import sys

input = sys.stdin.readline

def solution(start, end):
    global arr
    if start == end:
        return arr[start]
    
    mid = (start + end) // 2
    left_ex = solution(start, mid)
    right_ex = solution(mid+1, end)
    
    
    left = mid
    right = mid + 1
    h = min(arr[mid:mid+2])
    mid_ex = h * 2
    while start < left or end > right:
        if start == left:
            right += 1
            h = min(h, arr[right])
        elif end == right:
            left -= 1
            h = min(h, arr[left])
        elif arr[left - 1] > arr[right + 1]:
            left -= 1
            h = min(h, arr[left])
        else:
            right += 1
            h = min(h, arr[right])
        mid_ex = max(mid_ex, h*(right-left+1))
        
    return max(right_ex, mid_ex, left_ex)
    

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    print(solution(1, len(arr)-1))