def solution(a, b, n):
    z = n # z = 20
    result = 0
    while z >= a: # 20 >= 3
        x = z - (z % a) # x = 20 - (20 % 3) = 18 / x = 14 - (14 % 3) = 12
        y = x / a * b # y = 18 / 3 * 2 = 12 / y = 8
        z = z - x + y # z = 20 - 18 + 12 = 14 / z = 14 - 12 + 8 = 10
        result += y # 14
    return result

# 줌 / 받음 / 남음
# 20   0    20
# 18   12    (20-18) + 12 = 14
# 12   8    (14-12) + 8 = 10
# ....
# x = 20 - (20%3) = 18 / y = (18/3*2) / z = (z - x) + y, num += z