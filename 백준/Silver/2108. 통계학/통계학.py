from collections import Counter
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
arr = list(map(int, data[1:n+1]))
arr.sort()

print(round(sum(arr)/n))
print(arr[n//2])

common = Counter(arr).most_common()
if len(common) == 1:
    print(common[0][0])
elif common[0][1] == common[1][1]:
    print(common[1][0])
else:
    print(common[0][0])

print(arr[-1]-arr[0])