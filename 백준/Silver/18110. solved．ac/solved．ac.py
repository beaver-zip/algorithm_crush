import sys
input = sys.stdin.readline

def round2(num):
    return int(num) + (1 if num-int(num)>=0.5 else 0)

n = int(input())
if n == 0:
    print(0)
else:
    arr = [0] * n
    for i in range(n):
        arr[i] = int(input())
    arr.sort()

    rid = round2(n * 0.15)
    arr = arr[rid:n-rid]
    print(round2(sum(arr)/len(arr)))