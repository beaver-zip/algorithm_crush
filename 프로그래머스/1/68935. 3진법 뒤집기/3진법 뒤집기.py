def solution(n):
    three = ''
    while n != 0:
        three += str(n % 3)
        n //= 3
    three = three[::-1]
    
    ans = 0
    for i in range(len(three)):
        ans += (3 ** i) * int(three[i])
    return ans