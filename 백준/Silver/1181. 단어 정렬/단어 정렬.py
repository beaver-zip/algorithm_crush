import sys
n = int(input())
arr = [i.strip() for i in sys.stdin.readlines()]
arr = list(set(arr))
arr.sort()
arr.sort(key = lambda x: len(x))
for a in arr:
    print(a)