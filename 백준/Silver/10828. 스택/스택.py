import sys
input = sys.stdin.readline

def isEmpty():
    global stack, top
    if top == -1:
        return True
    return False

n = int(input())
stack = [None] * n
top = -1

for _ in range(n):
    s = input().strip()
    if s[:4] == 'push':
        top += 1
        stack[top] = int(s[5:])
    elif s == 'pop':
        if isEmpty():
            print(-1)
        else:
            data = stack[top]
            stack[top] = None
            top -= 1
            print(data)
    elif s == 'size':
        if isEmpty():
            print(0)
        else:
            print(top+1)
    elif s == 'empty':
        if isEmpty():
            print(1)
        else:
            print(0)
    else:
        if isEmpty():
            print(-1)
        else:
            print(stack[top])