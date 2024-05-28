import sys
input = sys.stdin.readline

arr = []
for i in range(int(input())):
    x, y = map(int, input().rstrip().split())
    arr.append((x, y))

arr.sort(key = lambda a: a[0])
arr.sort(key = lambda a: a[1])

for a in arr:
    print(*a)