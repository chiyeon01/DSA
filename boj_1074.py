import sys
input = sys.stdin.readline

def solution(x1, y1, x2, y2, start_num):
    global r
    global c
    diff = x2 - x1 + 1
    if diff == 1:
        return start_num
    if x1 + diff//2 > r:
        if y1 + diff//2 > c:    
            return solution(x1, y1, x2 - diff//2, y2 - diff//2, start_num) # 1사분면
        else:
            return solution(x1, y1 + diff//2, x2 - diff//2, y2, start_num + ((diff**2)//4)) # 2사분면
    else:
        if y1 + diff//2 > c:
            return solution(x1 + diff//2, y1, x2, y2 - diff//2, start_num + 2*((diff**2)//4)) # 3사분면
        else:
            return solution(x1 + diff//2, y1 + diff//2, x2, y2, start_num + 3*((diff**2)//4)) # 4사분면

N, r, c = map(int, input().split())
print(solution(0, 0, 2**N - 1, 2**N - 1, 0))