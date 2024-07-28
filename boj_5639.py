import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(tree):
    if len(tree) == 0:
        return
    root = tree[0]
    treeLeft, treeRight = [], []
    
    for i in range(1, len(tree)):
        if tree[i] > root:
            treeLeft = tree[1:i]
            treeRight = tree[i:]
            break
    if len(treeRight) == 0:
        treeLeft = tree[1:]
    
    DFS(treeLeft)
    DFS(treeRight)
    print(root)

num = []
while True:
    try:
       num.append(int(input()))
    except:
        break

DFS(num)