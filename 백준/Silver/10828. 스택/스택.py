import sys
input = sys.stdin.readline

n = int(input())
stack = [None] * n
top = -1

for _ in range(n):
    s = input().strip()
    if s[:4] == 'push':
        top += 1
        stack[top] = int(s[5:])
    elif s == 'pop':
        if top == -1:
            print(-1)
        else:
            data = stack[top]
            stack[top] = None
            top -= 1
            print(data)
    elif s == 'size':
        if top == -1:
            print(0)
        else:
            print(top + 1)
    elif s == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    else:
        if top == -1:
            print(-1)
        else:
            print(stack[top])