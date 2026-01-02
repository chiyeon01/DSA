import sys

input = sys.stdin.readline

N = int(input())
stack = []
ans = 0

for i in range(N):
    num = int(input())
    cnt = 0
    if not stack:
        stack.append([num, cnt])
        continue
    
    if stack[-1][0] > num: # 바로 자기보다 큰 값을 만나면 +1 해줘야함.
        ans += 1
        stack.append([num, cnt])
        continue
    
    while stack and stack[-1][0] <= num:
        n, c = stack.pop()
        ans += 1 + c
        if n == num: # 자기와 같은 경우 cnt를 체크.
            cnt += c + 1
            
    if stack: # 이전에 자기보다 큰 값을 만나서 끝난 경우 그 값까지 +1 해줘야 함.
        ans += 1
        
    stack.append([num, cnt])
    
print(ans)


'''
반례 체크
4
4
3
2
1

ans: 3

4
1
2
3
4

ans: 3

4
1
2
3
2

ans: 3

4
2
2
2
2

ans: 6
'''