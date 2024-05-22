def facto(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
n, k = map(int, input().split())
print(facto(n) // (facto(k) * facto(n-k)))