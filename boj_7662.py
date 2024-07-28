import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    t = int(input())
    check = [1 for _ in range(t)]
    min_heap = []
    max_heap = []
    
    for i in range(t):
        command, num = input().split()
        num = int(num)
        if command == 'I':
            heapq.heappush(min_heap, [num, i])
            heapq.heappush(max_heap, [-num, i])
        elif command == 'D':
            if num == -1 and min_heap:
                check[heapq.heappop(min_heap)[1]] = 0
            elif num == 1 and max_heap:
                check[heapq.heappop(max_heap)[1]] = 0
        
        while min_heap and check[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
        while max_heap and check[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)
    
    if min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')