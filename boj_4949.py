import sys

input = sys.stdin.readline

def IsEmpty(stack):
    if len(stack) == 0:
        return True
    
    return False

def IsBalance(string):
    stack = []
    couple = {')' : '(', ']': '['}
    for x in string:
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')':
            if not IsEmpty(stack) and stack[-1] == couple[x]:
                stack.pop()
            else:
                stack.append(x)
        elif x == ']':
            if not IsEmpty(stack) and stack[-1] == couple[x]:
                stack.pop()
            else:
                stack.append(x)
    if IsEmpty(stack):
        return True
    else:
        return False
    
words = []
while True:
    string = input().rstrip()
    if string == ".":
        break
    words.append(string)
    if IsBalance(string):
        print('yes')
    else:
        print('no')
