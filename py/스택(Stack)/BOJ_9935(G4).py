import sys

input = sys.stdin.readline

arr = input().rstrip()
gang = input().rstrip()
arr_num = len(arr)
gang_num = len(gang)
stack = []

for i in range(arr_num-1, -1, -1):
    stack.append(arr[i])
    cnt = 0
    gang_start = 0
    stack_start = -1
    stack_num = len(stack)
    
    while -1 * stack_start <= stack_num  and gang[gang_start] == stack[stack_start]:
        if gang_start == gang_num - 1:
            cnt += 1
            gang_start = 0 # gang_start 초기화
            stack_start -= 1
            continue
        gang_start += 1
        stack_start -= 1
                
    for _ in range(gang_num * cnt):
        stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack[::-1]))