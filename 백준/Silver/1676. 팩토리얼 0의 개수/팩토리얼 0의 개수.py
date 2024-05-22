def Factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
num = Factorial(int(input()))
cnt = 0
for i in str(num)[::-1]:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)