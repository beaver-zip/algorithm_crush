import sys
input = sys.stdin.readline

arr = []
for i in range(int(input())):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key = lambda a: (a[1], a[0]))
for a in arr:
    print(*a)