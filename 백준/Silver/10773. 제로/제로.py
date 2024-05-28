import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())):
    i = int(input())
    if i != 0:
        arr.append(i)
    elif i == 0 and arr:
        arr.pop()
print(sum(arr))